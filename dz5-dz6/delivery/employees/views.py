import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from employees.models import Employee


@require_http_methods(['GET'])
def employees_list(request):
    resp = []
    for obj in Employee.objects.all():
        resp.append(model_to_dict(obj))
    return JsonResponse(resp, safe=False)


@require_http_methods(['POST'])
def new_employee(request):
    obj = Employee.objects.create(
        job=request.POST.get('job'),
        status=request.POST.get('status'),
        user_id=request.POST.get('user_id')
    )
    return JsonResponse({'success': True, 'employee_id': obj.id}, status=200)


@require_http_methods(['PUT', 'DELETE', 'GET'])
def employees(request, employee_id):
    try:
        obj = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return JsonResponse({'success': False, 'error': f"Employee with id {employee_id} does not exist"},
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
            Employee.objects.filter(id=employee_id).update(
                job=req.get('job'),
                status=req.get('status'),
                user_id=req.get('user_id')
            )
            return JsonResponse({'success': True, 'employee_id': employee_id}, status=200)
        elif request.method == 'DELETE':
            obj.delete()
            return JsonResponse({'success': True, 'employee_id': employee_id}, status=200)
        else:
            return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                                content_type="application/json", status=405)