from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .models import StudTests, Attempts, StudAnswers
from TestSystem.models import SignUp_Model
from TestCreation.models import TeacherTests, Questions

@login_required(login_url='/')
@user_passes_test(lambda u: u.groups.filter(name='students').exists(), login_url='/profile/')
def web_testing(request):
    #try:
    ##################################################
    # Изменить, указав соответствующие request
    # request.session['user_id'] = '2'
    # request.session['test_id'] = '18'
    # request.session['passed_test_id'] = '1'
    # request.session['attempt_id'] = '1'
    ##################################################

    query_test_info = TeacherTests.objects.get(id=request.session['test_id'])
    student = StudTests.objects.filter(test_id=request.session['test_id'], user_id=request.session['user_id']).first()
    show_attempt = query_test_info.attempt_count - student.attempts_count + 1
    query_questions = Questions.objects.filter(test_id_id=request.session['test_id']).all().order_by('?')

    if request.method == 'POST':
        if request.POST.get('start_test'):
            return render(request, 'web_testing.html', {
                    'query': query_questions, # Вопросы
                    'test_info': query_test_info, # Общая информация по тесту
                })

        elif request.POST.get('finish'):
            read_answers = request.POST.get("answer_to_send", None)
            timer = request.POST.get("finish_time", None)
            answers = {}
            right_ans_counter = 0
            if read_answers != None and read_answers != '':
                read_answers = read_answers.split(',')
                for i in read_answers:
                    quest_num, ans = i.split('=')
                    answers[quest_num] = ans
            test = TeacherTests.objects.get(pk=request.session['test_id'])
            for q in query_questions:
                stud = StudAnswers()
                quest_num = str(q.id)
                stud.question_id = quest_num
                stud.attempt_id = request.session['attempt_id']
                if quest_num in answers:
                    if q.manychoises:
                        correct = False
                        anses = list(answers[quest_num])
                        for index, ans in enumerate(answers[quest_num]):
                            anses[index] = False if ans == '0' else True
                        if anses[0] == q.isright1:
                            if anses[1] == q.isright2:
                                if anses[2] == q.isright3:
                                    if anses[3] == q.isright4:
                                        correct = True
                        stud.iscorrect = correct
                        right_ans_counter += 1 if correct else 0
                        stud.choosen_answer1 = anses[0]
                        stud.choosen_answer2 = anses[1]
                        stud.choosen_answer3 = anses[2]
                        stud.choosen_answer4 = anses[3]
                    else:
                        anses = [q.isright1, q.isright2, q.isright3, q.isright4]
                        stud.iscorrect = True if anses[int(answers[quest_num])-1] else False
                        right_ans_counter += 1 if anses[int(answers[quest_num])-1] else 0
                        stud.choosen_answer1 = True if answers[quest_num] == '1' else False
                        stud.choosen_answer2 = True if answers[quest_num] == '2' else False
                        stud.choosen_answer3 = True if answers[quest_num] == '3' else False
                        stud.choosen_answer4 = True if answers[quest_num] == '4' else False

                else:
                    stud.iscorrect = False
                    stud.choosen_answer1 = False
                    stud.choosen_answer2 = False
                    stud.choosen_answer3 = False
                    stud.choosen_answer4 = False

                stud.save()
            attempts = Attempts.objects.get(pk=request.session['attempt_id'])
            if timer != "EXPIRED":
                attempts.time = query_test_info.time - int(timer.split(':')[2])
            else:
                attempts.time = query_test_info.time
            attempts.result = right_ans_counter
            attempts.save()
            update_best = StudTests.objects.filter(pk=request.session['passed_test_id']).first()
            update_best.best_result = max(update_best.best_result, (right_ans_counter / test.question_count * 100))
            update_best.save()

        del request.session['test_id']
        del request.session['passed_test_id']
        del request.session['attempt_id']

        return redirect('/profile/')

    else:
        return render(request, 'start_test.html', {
            'item': query_test_info,
            'student': show_attempt,
            })
