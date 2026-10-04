from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from .models import User
from branches.models import Branch
from courses.models import Course
from batches.models import Batch
from admissions.models import Admission


def home(request):
    branches = Branch.objects.filter(is_active=True)[:6]
    courses = Course.objects.filter(is_active=True)[:6]
    context = {"branches": branches, "courses": courses}
    return render(request, "home.html", context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def user_register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data.get("role", "student")
            user.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("dashboard")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")


@login_required
@user_passes_test(lambda u: True, redirect_field_name=None)
def dashboard(request):
    user = request.user
    context = {}

    # Always pass branches & active batches for all authenticated users
    all_branches = Branch.objects.filter(is_active=True).prefetch_related("batches")
    active_batches = Batch.objects.filter(is_active=True).select_related("branch", "course")

    context["all_branches"] = all_branches
    context["active_batches"] = active_batches[:8]

    if user.is_super_admin() or user.is_admin_role():
        context["total_branches"] = Branch.objects.filter(is_active=True).count()
        context["total_courses"] = Course.objects.filter(is_active=True).count()
        context["total_batches"] = Batch.objects.filter(is_active=True).count()
        context["total_students"] = User.objects.filter(role="student").count()
        context["total_admissions"] = Admission.objects.count()
        context["recent_admissions"] = Admission.objects.select_related(
            "student", "batch", "batch__branch", "batch__course"
        ).order_by("-created_at")[:6]
        context["branches"] = all_branches

    elif user.is_manager():
        managed_branches = user.managed_branches.filter(is_active=True)
        context["branches"] = managed_branches
        context["total_branches"] = managed_branches.count()
        context["total_batches"] = Batch.objects.filter(branch__in=managed_branches, is_active=True).count()
        context["total_students"] = Admission.objects.filter(
            batch__branch__in=managed_branches, status="active"
        ).count()
        context["recent_admissions"] = Admission.objects.filter(
            batch__branch__in=managed_branches
        ).select_related("student", "batch").order_by("-created_at")[:6]

    elif user.is_faculty():
        faculty_batches = Batch.objects.filter(faculty=user, is_active=True).select_related("branch", "course")
        context["faculty_batches"] = faculty_batches
        context["total_batches"] = faculty_batches.count()
        context["total_students"] = Admission.objects.filter(
            batch__in=faculty_batches, status="active"
        ).count()

    else:
        # Student view
        context["my_admissions"] = Admission.objects.filter(student=user).select_related(
            "batch", "batch__branch", "batch__course"
        ).order_by("-created_at")
        context["total_branches"] = Branch.objects.filter(is_active=True).count()
        context["total_batches"] = Batch.objects.filter(is_active=True).count()

    return render(request, "dashboard.html", context)


@login_required
def profile(request):
    return render(request, "accounts/profile.html")
