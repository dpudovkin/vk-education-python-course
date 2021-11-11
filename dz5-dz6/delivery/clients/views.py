import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from clients.models import Client


@require_http_methods(['GET'])
def clients_list(request):
    resp = []
    for obj in Client.objects.all():
        resp.append(model_to_dict(obj))
    return JsonResponse(resp, safe=False)


@require_http_methods(['POST'])
def new_client(request):
    obj = Client.objects.create(
        status=request.POST.get('status'),
        home_address=request.POST.get('home_address'),
        user_id=request.POST.get('user_id')
    )
    return JsonResponse({'success': True, 'client_id': obj.id}, status=200)


@require_http_methods(['PUT', 'DELETE', 'GET'])
def clients(request, client_id):
    try:
        obj = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return JsonResponse({'success': False, 'error': f"Client with id {client_id} does not exist"},
                            content_type="application/json", status=404)
    else:
        if request.method == 'GET':
            return JsonResponse(model_to_dict(obj), safe=False)
        elif request.method == 'PUT':
            if request.content_type != 'application/json':
                return JsonResponse({'success': False,
                                     'error': f"Bad request. Content type {request.content_type} is not allowed"},
                                    content_type="application/json", status=400)

            req = json.loads(request.body)
            Client.objects.filter(id=client_id).update(
                status=request.POST.get('status'),
                home_address=request.POST.get('home_address'),
                user_id=request.POST.get('user_id')
            )
            return JsonResponse({'success': True, 'client_id': client_id}, status=200)
        elif request.method == 'DELETE':
            obj.delete()
            return JsonResponse({'success': True, 'client_id': client_id}, status=200)
        else:
            return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                                content_type="application/json", status=405)