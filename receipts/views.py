from django.shortcuts import render
from receipts.models import Receipt


# LIST_RECEIPTS
def home(request):
    receipt_list = Receipt.objects.all()

    context = {"receipt_list_object": receipt_list}

    return render(request, "receipts/list.html", context)

    # todo_list = TodoList.objects.all()

    # context = {"todo_list_object": todo_list}

    # return render(request, "todos/list.html", context)
