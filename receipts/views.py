from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt
from receipts.forms import ReceiptForm


# CATEGORY LIST
@login_required
def category_list(request):
    # get list of receipts that belong to current user
    receipts = Receipt.objects.filter(purchaser=request.user)

    categories = {}
    # iterate over the receipts and count the instances of each category
    for item in receipts:
        categories[item.category] = categories.get(item.category, 0) + 1

    context = {
        "categories": categories,
    }
    return render(request, "categories/list.html", context)


# ACCOUNT LIST
@login_required
def account_list(request):
    # get list of receipts that belong to current user
    receipts = Receipt.objects.filter(purchaser=request.user)

    count = {}
    number = {}
    accounts = []

    # Get a count of each receipt according to their account name
    for item in receipts:
        count[item.account] = count.get(item.account, 0) + 1
        number[item.account] = item.account.number

    # iterate over count and append an array entry
    for key, value in count.items():
        accounts.append([key, number[key], value])

    context = {
        "accounts": accounts,
    }

    return render(request, "accounts/list.html", context)


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
