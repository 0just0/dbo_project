from django.shortcuts import render

from .models import Bank, Bank_Ul
from .utilities import parse_for_checked, apply_priorities, form_result


def index(request):
    banks = Bank.objects.all()
    return render(request, 'banks/index.html', {'banks': banks})


def search_fl(request):
    if request.method == 'POST':
        type_of_client = True

        checked = parse_for_checked(request)

        objects = Bank.objects.all().values_list()

        prioritised_objects = apply_priorities(objects, checked, type_of_client)

        dcs_banks = form_result(prioritised_objects)

        return render(request, 'banks/results.html', {'dcs_banks': dcs_banks})

    return render(request, 'banks/search.html')


def search_ul(request):
    if request.method == 'POST':
        type_of_client = False

        checked = parse_for_checked(request)

        objects = Bank_Ul.objects.all().values_list()

        prioritised_objects = apply_priorities(objects, checked, type_of_client)

        dcs_banks = form_result(prioritised_objects)

        return render(request, 'banks/results.html', {'dcs_banks': dcs_banks})

    return render(request, 'banks/search_ul.html')
