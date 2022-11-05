from django.shortcuts import render
from django.shortcuts import redirect
from django.forms import Form
from django.contrib.auth.decorators import login_required

from WebTesting.models import StudTests, Attempts, StudAnswers
from TestSystem.models import SignUp_Model
from TestCreation.models import TeacherTests, Questions


@login_required(login_url='/')
def profile(request):

    ##################################################
    # Изменить, указав соответствующие request
    # request.session['user_id'] = '1'
    ##################################################
    reg_user = SignUp_Model.objects.get(pk=request.session['user_id'])
    if reg_user.user_type == 'teacher':

        if request.method == 'POST':
            if request.POST.get('test'):
                return redirect('/create_test/')
            
            elif request.POST.get("action", "") == "info":
                request.session['test_id'] = request.POST.get("more_info")
                return redirect('/test_result/')
            
            # Удаление теста 
            elif request.POST.get("action", "") == "delete":
                test_id = request.POST.get("test_id", None)
                if test_id is not None:
                    tmp_test = TeacherTests.objects.get(pk=test_id)
                    tmp_test.delete()
                    return redirect('.')
            
            #  Редактирование теста
            elif request.POST.get("action", "") == "edit":
                test_id = request.POST.get("test_id", None)
                if test_id is not None:
                    request.session['test_id'] = test_id
                    # tmp_test = TeacherTests.objects.get(pk=test_id)
                    # test = TeacherTests.objects.get(pk=request.session['test_id'])
                    return redirect('/create_test/')


        query_user = SignUp_Model.objects.get(pk=request.session['user_id'])
        query_tests = TeacherTests.objects.filter(user_id_id=request.session['user_id'])

        return render(request, 'teacher_profile.html', {
            'reg_user': query_user, # Инфа о тичере
            'tests': query_tests, # Инфа о тестах этого тичера  
        })

    else:

        if request.method == 'POST':
            if request.POST.get('test'):
                test_id = int(request.POST.get("test_id"))
                if not TeacherTests.objects.filter(pk=test_id).exists():
                    query_user = SignUp_Model.objects.get(pk=request.session['user_id'])
                    query_tests = StudTests.objects.filter(user_id=request.session['user_id'], attempts_count__gt=0)
                    test_info = []
                    attempt_info = []
                    for test in query_tests:
                        test_info.append(TeacherTests.objects.get(pk=test.test_id))
                        attempt_info.append(Attempts.objects.filter(passed_test_id=test.id).order_by('date').last())
                    return render(request, 'stud_profile.html', {
                        'error': "Нет такого теста!",
                        'reg_user': query_user, # Инфа о студенте
                        'tests': zip(query_tests, test_info, attempt_info), # Инфа о тестах студента
                        })
                elif TeacherTests.objects.get(pk=test_id).question_count == 0:
                    query_user = SignUp_Model.objects.get(pk=request.session['user_id'])
                    query_tests = StudTests.objects.filter(user_id=request.session['user_id'], attempts_count__gt=0)
                    test_info = []
                    attempt_info = []
                    for test in query_tests:
                        test_info.append(TeacherTests.objects.get(pk=test.test_id))
                        attempt_info.append(Attempts.objects.filter(passed_test_id=test.id).order_by('date').last())
                    if 'attempt_id' in request.session:
                        del request.session['attempt_id']
                    return render(request, 'stud_profile.html', {
                        'error': "Вам повезло! В тесте нет вопросов!",
                        'reg_user': query_user,  # Инфа о студенте
                        'tests': zip(query_tests, test_info, attempt_info),  # Инфа о тестах студента
                    })
                test_attempts = TeacherTests.objects.get(pk=test_id).attempt_count
                # passed_test = StudTests.objects.filter(test_id=test_id, user_id=request.session['user_id']).first()
                if not StudTests.objects.filter(test_id=test_id, user_id=request.session['user_id']).exists():
                    new_test = StudTests()
                    new_test.test_id = test_id
                    new_test.user_id = request.session['user_id']
                    new_test.save()
                passed_test = StudTests.objects.filter(test_id=test_id, user_id=request.session['user_id']).first()
                
                if passed_test.attempts_count >= test_attempts:
                    error = "Все попытки исчерпаны" # Сделать вывод ошибок!

                    query_user = SignUp_Model.objects.get(pk=request.session['user_id'])
                    query_tests = StudTests.objects.filter(user_id=request.session['user_id'], attempts_count__gt=0)
                    test_info = []
                    attempt_info = []
                    for test in query_tests:
                        test_info.append(TeacherTests.objects.get(pk=test.test_id))
                        attempt_info.append(Attempts.objects.filter(passed_test_id=test.id).order_by('date').last())

                    return render(request, 'stud_profile.html', {
                        'reg_user': query_user, # Инфа о студенте
                        'tests': zip(query_tests, test_info, attempt_info), # Инфа о тестах студента
                        'error': error,

                    })
            
                else:
                    if 'attempt_id' not in request.session:
                        passed_test.attempts_count += 1
                        passed_test.save()
                        new_attempt = Attempts()
                        new_attempt.attempt_number = passed_test.attempts_count
                        new_attempt.passed_test_id = passed_test.id
                        new_attempt.save()
                        request.session['test_id'] = test_id
                        request.session['passed_test_id'] = passed_test.id
                        request.session['attempt_id'] = new_attempt.id
                        return redirect('/web_testing/')
                    else:
                        error = "Завершите предыдущий тест!!!" # Сделать вывод ошибок!
                        query_user = SignUp_Model.objects.get(pk=request.session['user_id'])
                        query_tests = StudTests.objects.filter(user_id=request.session['user_id'], attempts_count__gt=0)
                        test_info = []
                        attempt_info = []
                        for test in query_tests:
                            test_info.append(TeacherTests.objects.get(pk=test.test_id))
                            attempt_info.append(Attempts.objects.filter(passed_test_id=test.id).order_by('date').last())

                        return render(request, 'stud_profile.html', {
                            'reg_user': query_user, # Инфа о студенте
                            'tests': zip(query_tests, test_info, attempt_info), # Инфа о тестах студента
                            'error': error,
                        })

            if request.POST.get("action", "") == "info":
                request.session['test_id'] = request.POST.get("more_info")
                request.session['student'] = reg_user.id
                return redirect('/student_result/')

        query_user = SignUp_Model.objects.get(pk=request.session['user_id'])
        query_tests = StudTests.objects.filter(user_id=request.session['user_id'], attempts_count__gt=0)
        test_info = []
        attempt_info = []
        for test in query_tests:
            test_info.append(TeacherTests.objects.get(pk=test.test_id))
            attempt_info.append(Attempts.objects.filter(passed_test_id=test.id).order_by('date').last())
        
        return render(request, 'stud_profile.html', {
            'reg_user': query_user, # Инфа о студенте
            'tests': zip(query_tests, test_info, attempt_info), # Инфа о тестах студента

        })