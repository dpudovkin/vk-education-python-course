from django.http import JsonResponse, Http404


def user_list(request):
    if request.method == 'GET':
        # get data from databases
        userList = (
            {'Name': 'Nina', 'Age': '18', 'Date of birth': '04.11.2001', 'ID': 1},
            {'Name': 'Dima', 'Age': '19', 'Date of birth': '04.11.2001', 'ID': 2},
            {'Name': 'Sergey', 'Age': '20', 'Date of birth': '04.11.2001', 'ID': 3}
        )
        return JsonResponse(userList, safe=False)
    else:
        raise Http404(f'Method {request.method} not allowed')


def user_info(request, user_id):
    if request.method == 'GET':
        # get data from database by user_id
        user = {'Name': 'Sergey', 'Age': '20', 'Date of birth': '04.11.2001', 'ID': user_id}
        return JsonResponse(user, safe=False)
    else:
        raise Http404(f'Method {request.method} not allowed')


def create_user(request):
    if request.method == 'POST':
        # get params from post request body
        # parse request.body
        createdUser = {'Name': 'Sergey', 'Age': '20', 'Date of birth': '04.11.2001', 'ID': 1}

        return JsonResponse(createdUser, safe=False)
    else:
        raise Http404(f'Method {request.method} not allowed')
