import json

from django.http import JsonResponse, HttpResponse


def user_list(request):
    if request.method == 'GET':
        # get data from databases
        user_list = (
            {'Name': 'Nina', 'Age': '18', 'Date of birth': '04.11.2001', 'ID': 1},
            {'Name': 'Dima', 'Age': '19', 'Date of birth': '04.11.2001', 'ID': 2},
            {'Name': 'Sergey', 'Age': '20', 'Date of birth': '04.11.2001', 'ID': 3}
        )
        return JsonResponse(user_list, safe=False)
    else:
        return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                            content_type="application/json", status=405)


def user_info(request, user_id):
    if request.method == 'GET':
        # get data from database by user_id
        user = {'Name': 'Sergey', 'Age': '20', 'Date of birth': '04.11.2001', 'ID': user_id}
        return JsonResponse(user, safe=False)
    else:
        return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                            content_type="application/json", status=405)


def create_user(request):
    if request.method == 'POST':
        # get params from post request body
        # parse request.body
        created_user = {'Name': request.POST.get('name'),
                        'Age': request.POST.get('age'),
                        'Date of birth': request.POST.get('birth_date'),
                        'ID': request.POST.get('id')}

        return JsonResponse(created_user, safe=False)
    else:
        return JsonResponse({'success': False, 'error': f"Method {request.method} is not allowed"},
                            content_type="application/json", status=405)
