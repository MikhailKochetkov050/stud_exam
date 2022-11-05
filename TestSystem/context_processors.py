def user_information(request):
    from .models import SignUp_Model
    if 'user_id' in  request.session:
        user_info = SignUp_Model.objects.get(pk=request.session['user_id'])
    else:
        user_info = None

    return {
        'user_info': user_info,  # Add 'user_info' to the context
    }