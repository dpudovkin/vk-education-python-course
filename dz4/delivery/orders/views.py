from django.http import JsonResponse, Http404


def order_list(request):
    if request.method == 'GET':
        # get data from databases
        orderList = (
            {'OrderID': '12', 'Total payment': 2100, 'isPaid': True, 'UserId': 1},
            {'OrderID': '13', 'Total payment': 2600, 'isPaid': True, 'UserId': 2},
            {'OrderID': '14', 'Total payment': 3500, 'isPaid': False, 'UserId': 2}
        )
        return JsonResponse(orderList, safe=False)
    else:
        raise Http404(f'Method {request.method} not allowed')


def order_info(request, order_id):
    if request.method == 'GET':
        # get data from databases by order id
        order = {'OrderID': order_id, 'Total payment': 2100, 'isPaid': True, 'UserId': 1}
        return JsonResponse(order, safe=False)
    else:
        raise Http404(f'Method {request.method} not allowed')
    pass


def create_order(request):
    if request.method == 'POST':
        # get params from post request body
        createdOrder = {'OrderID': 12, 'Total payment': 2100, 'isPaid': True, 'UserId': 1}
        return JsonResponse(createdOrder, safe=False)
    else:
        raise Http404(f'Method {request.method} not allowed')
