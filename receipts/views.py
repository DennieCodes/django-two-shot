from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt


# LIST_RECEIPTS
@login_required
def home(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)

    context = {"receipt_list_object": receipt_list}

    return render(request, "receipts/list.html", context)
