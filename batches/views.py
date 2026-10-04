from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Batch
from .forms import BatchForm
from branches.models import Branch


def batch_list(request):
    batches = Batch.objects.filter(is_active=True).select_related("branch", "course", "faculty")
    branch_id = request.GET.get("branch")
    if branch_id:
        batches = batches.filter(branch_id=branch_id)
    context = {"batches": batches, "branches": Branch.objects.filter(is_active=True)}
    return render(request, "batches/batch_list.html", context)


@login_required
@user_passes_test(lambda u: u.is_admin_role() or u.is_manager())
def batch_create(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            batch = form.save(commit=False)
            batch.save()
            messages.success(request, f"Batch '{batch.name}' created!")
            return redirect("batch_list")
    else:
        form = BatchForm()
        if request.user.is_manager():
            form.fields["branch"].queryset = request.user.managed_branches.filter(is_active=True)
        else:
            form.fields["branch"].queryset = Branch.objects.filter(is_active=True)
    return render(request, "batches/batch_form.html", {"form": form, "action": "Create"})


@login_required
@user_passes_test(lambda u: u.is_admin_role() or u.is_manager())
def batch_edit(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == "POST":
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            messages.success(request, f"Batch '{batch.name}' updated!")
            return redirect("batch_list")
    else:
        form = BatchForm(instance=batch)
        if request.user.is_manager():
            form.fields["branch"].queryset = request.user.managed_branches.filter(is_active=True)
        else:
            form.fields["branch"].queryset = Branch.objects.filter(is_active=True)
    return render(request, "batches/batch_form.html", {"form": form, "action": "Edit"})


@login_required
@user_passes_test(lambda u: u.is_admin_role() or u.is_manager())
def batch_delete(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    batch.is_active = False
    batch.save()
    messages.success(request, f"Batch '{batch.name}' deactivated.")
    return redirect("batch_list")
