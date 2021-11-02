from django.http import JsonResponse


def order_list(request):
    if request.method == 'GET':
        # get data from databases
        orderlist = (
            {'OrderID': '12', 'Total payment': 2100, 'isPaid': True, 'UserId': 1},
            {'OrderID': '13', 'Total payment': 2600, 'isPaid': True, 'UserId': 2},
            {'OrderID': '14', 'Total payment': 3500, 'isPaid': False, 'UserId': 2}
        )
        return JsonResponse(orderlist, safe=False)

    return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                        content_type="application/json", status=405)


def order_info(request, order_id):
    if request.method == 'GET':
        # get data from databases by order id
        order = {'OrderID': order_id, 'Total payment': 2100, 'isPaid': True, 'UserId': 1}
        return JsonResponse(order, safe=False)

    return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                        content_type="application/json", status=405)


def create_order(request):
    if request.method == 'POST':
        created_order = {'OrderID': request.POST.get('id'),
                         'Total payment': request.POST.get('total'),
                         'isPaid': request.POST.get('is_paid'),
                         'UserId': request.POST.get('user_id')}
        # insert into database
        return JsonResponse(created_order, safe=False)

    return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                        content_type="application/json", status=405)
