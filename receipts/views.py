from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt
from receipts.forms import ReceiptForm


# CREATE_RECEIPT
@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")

    else:
        form = ReceiptForm()

    context = {"form": form}

    return render(request, "receipts/create.html", context)


# LIST_RECEIPTS
@login_required
def home(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)

    context = {"receipt_list_object": receipt_list}

    return render(request, "receipts/list.html", context)
