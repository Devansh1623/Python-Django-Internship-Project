from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Course
from .forms import CourseForm


def course_list(request):
    courses = Course.objects.filter(is_active=True)
    dance_style = request.GET.get("style")
    if dance_style:
        courses = courses.filter(dance_style=dance_style)
    return render(request, "courses/course_list.html", {"courses": courses})


@login_required
@user_passes_test(lambda u: u.is_admin_role())
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, f"Course '{course.name}' created!")
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "courses/course_form.html", {"form": form, "action": "Create"})


@login_required
@user_passes_test(lambda u: u.is_admin_role())
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f"Course '{course.name}' updated!")
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "courses/course_form.html", {"form": form, "action": "Edit"})


@login_required
@user_passes_test(lambda u: u.is_admin_role())
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.is_active = False
    course.save()
    messages.success(request, f"Course '{course.name}' deactivated.")
    return redirect("course_list")
