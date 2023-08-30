from django.shortcuts import render
from receipts.models import Receipt


# LIST_RECEIPTS
def home(request):
    receipt_list = Receipt.objects.all()

    context = {"receipt_list_object": receipt_list}

    return render(request, "receipts/list.html", context)
