from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import Admission
from .forms import AdmissionForm


@login_required
def admission_list(request):
    if request.user.is_admin_role() or request.user.is_manager():
        admissions = Admission.objects.select_related("student", "batch", "batch__branch", "batch__course").order_by("-created_at")
    elif request.user.is_faculty():
        admissions = Admission.objects.filter(batch__faculty=request.user).select_related("student", "batch", "batch__branch", "batch__course").order_by("-created_at")
    else:
        admissions = Admission.objects.filter(student=request.user).select_related("batch", "batch__branch", "batch__course").order_by("-created_at")
    return render(request, "admissions/admission_list.html", {"admissions": admissions})


@login_required
def admission_apply(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.student = request.user
            admission.save()
            messages.success(request, "Application submitted! Await approval.")
            return redirect("admission_list")
    else:
        form = AdmissionForm()
        if request.user.is_manager():
            form.fields["batch"].queryset = form.fields["batch"].queryset.filter(branch__in=request.user.managed_branches.filter(is_active=True))
        else:
            form.fields["batch"].queryset = form.fields["batch"].queryset.filter(is_active=True)
    return render(request, "admissions/admission_form.html", {"form": form})


@login_required
@user_passes_test(lambda u: u.is_admin_role() or u.is_manager())
def admission_approve(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    admission.status = "approved"
    admission.approval_date = timezone.now().date()
    admission.approved_by = request.user
    admission.save()
    messages.success(request, f"Admission for {admission.student.get_full_name()} approved!")
    return redirect("admission_list")


@login_required
@user_passes_test(lambda u: u.is_admin_role() or u.is_manager())
def admission_reject(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    admission.status = "rejected"
    admission.save()
    messages.warning(request, f"Admission for {admission.student.get_full_name()} rejected.")
    return redirect("admission_list")
