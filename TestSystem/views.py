from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
import re
from django.contrib import messages


from .forms import SignUpForm, ChangeForm, UserLoginForm
from .models import SignUp_Model

def demo(request):
    return render(request, 'demo.html')

def index(request):
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)            
        request.session['user_id'] = user.id
        _next = _next or '/'
        if request.user.is_superuser:
            return redirect('/admin_panel/')
        return redirect('/profile/')

    return render(request, 'sign_in.html', {'form': form})

def logout_view(request):
    logout(request)
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'test_id' in request.session:
        del request.session['test_id']
    if 'passed_test_id' in request.session:
        del request.session['passed_test_id']
    if 'attempt_id'  in request.session:
        del request.session['attempt_id']
    return redirect('/')

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser, login_url='/profile/')
def admin_panel(request):
    if request.method == 'POST':
        ans = '0'
        form = SignUpForm(request.POST)
        form1 = ChangeForm(request.POST)
        # Создание пользователя
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=raw_password)
            user.save()

            if username.split('_')[0] == 'stud':
                new_group, created = Group.objects.get_or_create(name='students')
                user.groups.add(Group.objects.get(name='students'))
            elif username.split('_')[0] == 'teacher':
                new_group, created = Group.objects.get_or_create(name='teachers')
                user.groups.add(Group.objects.get(name='teachers'))            

            return redirect('/admin_panel/')

        # Редактирование пользователя
        elif request.POST.get('btn5'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            status = request.POST.get('status_change')
            print(status, type(status))
            status = not(eval(status.capitalize()))
            u = User.objects.get(username=username)
            changed_user = SignUp_Model.objects.get(username=username)
            if password != '':
                u.set_password(password)
            if changed_user.locked != status:
                changed_user.locked = status
                if not status:
                    changed_user.login_attempts=0
            changed_user.save()
            u.save()

            return redirect('/admin_panel/')
        
        # Удаление пользователя
        elif request.POST.get('btn4'):
            username = request.POST.get('username')
            SignUp_Model.objects.filter(username=username).delete()
            u = User.objects.get(username=username)
            u.delete()
            return redirect('/admin_panel/')

        elif request.POST.get('admin_pass'):
            old_pwd = request.POST.get("admin_pwd")
            new_pwd = request.POST.get("new_admin_pwd")
            reg = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@№;%:?*()_+=]).{10,}$'
            qs = User.objects.get(username='admin')
            if check_password(old_pwd, qs.password):
                if re.match(reg, new_pwd) is not None:
                    qs.set_password(new_pwd)
                    qs.save()
                    messages.success(request, "Пароль изменён успешно!")
                else:
                    error = "Пароль не соответсвует требованиям!"
                    messages.error(request, "Пароль не соответсвует требованиям!")
            else:
                error = "Старый пароль не совпадает с существующим!"
                messages.error(request, "Старый пароль не совпадает с существующим!")



            return render(request, 'admin_panel.html', {})

        else:
            return redirect('/admin_panel/')

    else:
        # ans - индекс новой записи для генерации логина
        ans = str(SignUp_Model.objects.order_by('-id').first()).split()[-1][1:-1]
        if ans.isdigit():
            ans = str(int(ans) + 1)
        else:
            ans = 1
        options = SignUp_Model.objects.order_by('username').exclude(username='admin')
        form = SignUpForm()
        form1 = ChangeForm()
    return render(request, 'admin_panel.html', {
        'form': form, 
        'ans': ans,
        'form1': form1,
        'options': options,
        })