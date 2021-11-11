import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods

from orders.models import Order, Address


@require_http_methods(['GET'])
def order_list(request):
    resp = []
    for obj in Order.objects.all():
        resp.append(model_to_dict(obj))
    return JsonResponse(resp, safe=False)


@require_http_methods(['POST'])
def new_order(request):
    created_order = Order.objects.create(
        performer_id=request.POST.get('performer_id'),
        base_award=request.POST.get('base_award'),
        status=request.POST.get('status'),
        comment=request.POST.get('comment'),
        cost=request.POST.get('cost'),
        arriving_address_id=request.POST.get('arriving_address_id'),
        destination_address_id=request.POST.get('destination_address_id'),
        arriving_client_id=request.POST.get('arriving_client_id'),
        destination_client_id=request.POST.get('destination_client_id')
    )
    return JsonResponse({'success': True, 'order_id': created_order.id}, status=200)


@require_http_methods(['PUT', 'DELETE', 'GET'])
def orders(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return JsonResponse({'success': False, 'error': f"Order with id {order_id} does not exist"},
                            content_type="application/json", status=404)
    else:
        if request.method == 'GET':
            return JsonResponse(order, safe=False)
        elif request.method == 'PUT':
            if request.content_type != 'application/json':
                return JsonResponse({'success': False,
                                     'error': f"Bad request. Content type {request.content_type} is not allowed"},
                                    content_type="application/json", status=400)

            req = json.loads(request.body)

            Order.objects.update(id=order_id).update(
                performer_id=req.get('performer_id'),
                base_award=req.get('base_award'),
                status=req.get('status'),
                comment=req.get('comment'),
                cost=req.get('cost'),
                arriving_address_id=req.get('arriving_address_id'),
                destination_address_id=req.get('destination_address_id'),
                arriving_client_id=req.get('arriving_client_id'),
                destination_client_id=req.get('destination_client_id')
            )
        elif request.method == 'DELETE':
            order.delete()
            return JsonResponse({'success': True, 'order_id': order.id}, status=200)
        else:
            return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                                content_type="application/json", status=405)


@require_http_methods(['GET'])
def address_list(request):
    resp = []
    for obj in Address.objects.all():
        resp.append(model_to_dict(obj))
    return JsonResponse(resp, safe=False)


@require_http_methods(['POST'])
def new_address(request):
    created_address = Address.objects.create(
        full_name=request.POST.get('full_name'),
        longitude=request.POST.get('longitude'),
        latitude=request.POST.get('latitude')
    )
    return JsonResponse({'success': True, 'order_id': created_address.id}, status=200)


@require_http_methods(['PUT', 'DELETE', 'GET'])
def addresses(request, address_id):
    try:
        address = Address.objects.get(id=address_id)
    except Address.DoesNotExist:
        return JsonResponse({'success': False, 'error': f"Address with id {address_id} does not exist"},
                            content_type="application/json", status=404)
    else:
        if request.method == 'GET':
            return JsonResponse(model_to_dict(address), safe=False)
        elif request.method == 'PUT':


            if request.content_type != 'application/json':
                return JsonResponse({'success': False,
                                     'error': f"Bad request. Content type {request.content_type} is not allowed"},
                                    content_type="application/json", status=400)

            req = json.loads(request.body)
            Address.objects.filter(id=address_id).update(
                full_name=req.get('full_name'),
                longitude=req.get('longitude'),
                latitude=req.get('latitude')
            )
            return JsonResponse({'success': True, 'address_id': address_id}, status=200)
        elif request.method == 'DELETE':
            address.delete()
            return JsonResponse({'success': True, 'address_id': address_id}, status=200)
        else:
            return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                                content_type="application/json", status=405)
