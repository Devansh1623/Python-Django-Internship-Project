from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Branch
from .forms import BranchForm


def branch_list(request):
    branches = Branch.objects.filter(is_active=True)
    return render(request, "branches/branch_list.html", {"branches": branches})


@login_required
@user_passes_test(lambda u: u.is_admin_role())
def branch_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save()
            messages.success(request, f"Branch '{branch.name}' created successfully!")
            return redirect("branch_list")
    else:
        form = BranchForm()
    return render(request, "branches/branch_form.html", {"form": form, "action": "Create"})


@login_required
@user_passes_test(lambda u: u.is_admin_role())
def branch_edit(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            messages.success(request, f"Branch '{branch.name}' updated successfully!")
            return redirect("branch_list")
    else:
        form = BranchForm(instance=branch)
    return render(request, "branches/branch_form.html", {"form": form, "action": "Edit"})


@login_required
@user_passes_test(lambda u: u.is_admin_role())
def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    branch.is_active = False
    branch.save()
    messages.success(request, f"Branch '{branch.name}' deactivated.")
    return redirect("branch_list")
