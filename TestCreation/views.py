from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from .forms import TeacherTestsForm, QuestionsForm
from .models import Questions, SignUp_Model, TeacherTests

@login_required(login_url='/')
@user_passes_test(lambda u: u.groups.filter(name='teachers').exists(), login_url='/profile/')
def create_test(request):   
    try:

        # Создание теста, когда тичер ввел основные данные
        if request.POST.get('save_btn'):
            print('Save_Btn')
            form = TeacherTestsForm(request.POST)
            isnew = False

            if form.is_valid():
                tmp_test = form.save(commit=False)
                tmp_test.user_id_id = request.session['user_id']
                tmp_test.save()
                request.session['test_id'] = tmp_test.id
                query_results = Questions.objects.filter(test_id_id=request.session['test_id']).all()
            form1 = QuestionsForm()
            test = TeacherTests.objects.get(pk=request.session['test_id'])
            form = TeacherTestsForm(instance=test)

        # Кнопка Назад (удаление созданного теста)
        elif request.POST.get("back"):
            print("Back")
            if 'edit' in request.session:
                del request.session['test_id']
                del request.session['edit']
            elif 'test_id' in request.session:
                test = TeacherTests.objects.get(pk=request.session['test_id'])
                test.delete()
                del request.session['test_id']
            return redirect('/profile/')

        # Сохранение вопроса
        elif request.POST.get('save_qst'):  
            print('Save_Qst') 
            form1 = QuestionsForm(request.POST, request.FILES)   

            if form1.is_valid():
                
                tmp_quest = form1.save(commit=False)
                tmp_quest.test_id_id = request.session['test_id']
                tmp_quest.save()
                query_results = Questions.objects.filter(test_id_id=request.session['test_id']).all()
                isnew = False
                test = TeacherTests.objects.get(pk=request.session['test_id'])
                test.question_count = F('question_count') + 1
                test.save()
                form = TeacherTestsForm(instance=test)
                form1 = QuestionsForm()

        # Редактирование вопроса
        elif request.POST.get('edit_qst'):
            print('Edit question')
            form1 = QuestionsForm(request.POST, request.FILES)
            if form1.is_valid():
                quest_id = request.POST.get("edit_quest_id", None)
                if quest_id is not None:
                    tmp_quest = Questions.objects.get(pk=quest_id)
                    tmp_quest.question = request.POST.get('question')
                    tmp_quest.answer1 = request.POST.get('answer1')
                    tmp_quest.answer2 = request.POST.get('answer2')
                    tmp_quest.answer3 = request.POST.get('answer3')
                    tmp_quest.answer4 = request.POST.get('answer4')
                    tmp_quest.prompt = request.POST.get('prompt')
                    tmp_quest.manychoises = True if request.POST.get('manychoises') == 'on' else False
                    tmp_quest.isright1 = True if request.POST.get('isright1') == 'on' else False
                    tmp_quest.isright2 = True if request.POST.get('isright2') == 'on' else False
                    tmp_quest.isright3 = True if request.POST.get('isright3') == 'on' else False
                    tmp_quest.isright4 = True if request.POST.get('isright4') == 'on' else False
                    try:
                        tmp_quest.image = form1.cleaned_data['image']
                    except:
                        pass
                    tmp_quest.save()
                test = TeacherTests.objects.get(pk=request.session['test_id'])
                form = TeacherTestsForm(instance=test)
                form1 = QuestionsForm()
                query_results = Questions.objects.filter(test_id_id=request.session['test_id']).all()
                isnew = False
                    

        # Сохранение теста, удаление сессионных значений теста
        elif request.POST.get('save_test_btn'): 
            print('Save_test_btn')
            form = TeacherTestsForm(request.POST) 
            test = TeacherTests.objects.get(pk=request.session['test_id'])
            test.test_name = request.POST.get('test_name')
            test.attempt_count = request.POST.get('attempt_count')
            test.time = request.POST.get('time')
            test.save()
            del request.session['test_id']
            return redirect('/profile/')

        # Удаление вопроса 
        elif request.POST.get("action", "") == "delete":
            print('Delete')
            quest_id = request.POST.get("quest_id", None)
            if quest_id is not None:
                tmp_quest = Questions.objects.get(pk=quest_id)
                tmp_quest.delete()
                test = TeacherTests.objects.get(pk=request.session['test_id'])
                test.question_count = F('question_count') - 1
                test.save()
                query_results = Questions.objects.filter(test_id_id=request.session['test_id']).all()
                isnew = False
                form = TeacherTestsForm(instance=test)
                form1 = QuestionsForm()

        #  Передача формы в модальное окно редактирования
        elif request.POST.get("action", "") == "edit":
            print('Edit')
            quest_id = request.POST.get("quest_id", None)
            if quest_id is not None:
                tmp_quest = Questions.objects.get(pk=quest_id)
                test = TeacherTests.objects.get(pk=request.session['test_id'])
                query_results = Questions.objects.filter(test_id_id=request.session['test_id']).all()
                isnew = False
                form = TeacherTestsForm(instance=test)
                form1 = QuestionsForm(instance=tmp_quest)
                return render(request, 'create_test.html', {
                    'form': form,
                    'form1': form1,
                    'queries': query_results,
                    'isnew': isnew,
                    'edit': True,
                    'quest_id': quest_id,
                })

        elif 'test_id' in request.session:
            request.session['edit'] = True
            test = TeacherTests.objects.get(pk=request.session['test_id'])
            form = TeacherTestsForm(instance=test)
            form1 = QuestionsForm()
            query_results = Questions.objects.filter(test_id_id=request.session['test_id']).all()
            isnew = False
        else:
            print('Nothing')
            form = TeacherTestsForm()
            form1 = QuestionsForm()
            query_results = None
            isnew = True

        return render(request, 'create_test.html', {
            'form': form,
            'form1': form1,
            'queries': query_results,
            'isnew': isnew,
        })
    except KeyError:
        return redirect('/profile/')