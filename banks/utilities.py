import decimal

COEFFICIENT_OF_PRIORITY = 0.99
COEFFICIENT_OF_MINORITY = 0.01
COEFFICIENTS_FL = [-0.017675449, 0.380927295, 0.060369258,
                   0.15752668, 0.013691087, 0.135376218, 0.07876334,
                   0.079822131, 0.035988685, 0.039859856]

COEFFICIENTS_UL = [-0.022547089, 0.092361457, 0.065928087,
                   0.231038908, 0.552716109, 0.03540835]


def parse_for_checked(request):
    checked = {}

    for k, v in request.POST.items():
        if k != 'csrfmiddlewaretoken':
            checked[k] = v

    checked.pop('action')
    return [int(x) for x in checked.keys()]


def apply_priorities(vals_list, checked, type_of_client):
    list_of_lists = [list(lst) for lst in vals_list]
    checked_shifted = [x+3 for x in checked]
    for lst in list_of_lists:
        for elem in range(len(lst)):
            if type(lst[elem]) != str:
                if elem in checked_shifted:
                    lst[elem] *= decimal.Decimal(COEFFICIENT_OF_PRIORITY)
                else:
                    lst[elem] *= decimal.Decimal(COEFFICIENT_OF_MINORITY)

    if type_of_client:
        for x in range(10):
            for lst in list_of_lists:
                lst[x+3] *= decimal.Decimal(COEFFICIENTS_FL[x])
    else:
        for x in range(6):
            for lst in list_of_lists:
                lst[x+3] *= decimal.Decimal(COEFFICIENTS_UL[x])

    return list_of_lists


def form_result(prioritised_vals_list):

    final_list_of_lists = []

    for lst in prioritised_vals_list:
        final_coef = sum(lst[3:])
        bank_info = (final_coef, lst[1], lst[2])
        final_list_of_lists.append(bank_info)

    final_list_of_lists.sort(key=lambda x: x[0], reverse=True)

    return final_list_of_lists
