function page_choosing() {
    // Исчезает предыдущий
    var active_page = $('.search:visible').attr('id');
    if (active_page) {
        active_lbl = '#' + $('.search:visible').attr('name') + '_label'
        $(active_lbl).removeClass('active')
        $(active_lbl).removeClass('btn-secondary').addClass('btn-primary')
        document.getElementById(active_page).style.display = 'none';
    }
    // Появляется нужный вопрос
    var quest = $("input[type='radio'][name='btn_quest_nums']:checked").val();
    document.getElementById(quest).style.display = 'block';
    active_lbl = '#' + quest.substring(0, quest.length - 6) + '_label'
    $(active_lbl).removeClass('btn-primary').addClass('btn-secondary')
}

function navigation(page) {
    if (page == "prev") {
        var prev_page = $('.search:visible').attr('name') - 1;
        var active_page = $('.search:visible').attr('id');
        if (active_page) {
            active_lbl = '#' + $('.search:visible').attr('name') + '_label'
            document.getElementById(active_page).style.display = 'none';
            $(active_lbl).removeClass('active')
            lbl = '#' + (prev_page + 1) + '_label'
            $(lbl).removeClass('btn-secondary').addClass('btn-primary')
        }
        if (prev_page >= 1) {
            document.getElementById(prev_page + "_quest").style.display = 'block';
            lbl = '#' + prev_page + '_label'
            $(lbl).removeClass('btn-primary').addClass('btn btn-secondary')
        }
        else {
            document.getElementById(active_page).style.display = 'block';
            lbl = '#' + (prev_page + 1) + '_label'
            $(lbl).removeClass('btn-primary').addClass('btn btn-secondary')
        }
    }
    if (page == "next") {
        var next_page = parseInt($('.search:visible').attr('name')) + 1;
        var active_page = $('.search:visible').attr('id');
        if (active_page) {
            active_lbl = '#' + $('.search:visible').attr('name') + '_label'
            document.getElementById(active_page).style.display = 'none';
            $(active_lbl).removeClass('active')
            lbl = '#' + (next_page - 1) + '_label'
            $(lbl).removeClass('btn-secondary').addClass('btn-primary')
        }
        if (next_page <= parseInt(document.getElementById('quest_count').value)) {
            document.getElementById(next_page + "_quest").style.display = 'block';
            lbl = '#' + next_page + '_label'
            $(lbl).removeClass('btn-primary').addClass('btn btn-secondary')
        }
        else {
            document.getElementById(active_page).style.display = 'block';
            lbl = '#' + (next_page - 1) + '_label'
            $(lbl).removeClass('btn-primary').addClass('btn btn-secondary')
        }
    }
    if (page == "first") {
        var active_page = $('.search:visible').attr('id');
        active_lbl = '#' + $('.search:visible').attr('name') + '_label'
        if (active_page) {
            $(active_lbl).removeClass('btn-secondary').addClass('btn-primary')
            $(active_lbl).removeClass('active')
            document.getElementById(active_page).style.display = 'none';
        }
        document.getElementById("1_quest").style.display = 'block';
        $('#1_label').removeClass('btn-primary').addClass('btn btn-secondary')
    }
    if (page == "last") {
        active_lbl = '#' + $('.search:visible').attr('name') + '_label'
        active_page = $('.search:visible').attr('id');
        if (active_page) {
            $(active_lbl).removeClass('btn-secondary').addClass('btn-primary')
            $(active_lbl).removeClass('active')
            document.getElementById(active_page).style.display = 'none';
        }
        last = document.getElementById('quest_count').value
        document.getElementById(last + "_quest").style.display = 'block';
        $('#' + last + '_label').removeClass('btn-primary').addClass('btn btn-secondary')
    }
}

function page_scroll(page) {
    if (parseInt(document.getElementById('quest_count').value) > 10) {
        if (page == "prev_list") {
            first_page = $('.pages:visible').attr('id')
            first_page = parseInt(first_page.substring(0, first_page.length - 6));
            if (first_page != 1) {
                first_page = first_page - 1

                first_lbl = '#' + first_page + '_label'
                last_lbl = '#' + (first_page + 10) + '_label'
                $(last_lbl).attr('hidden', 'hidden')

                $(first_lbl).removeAttr('hidden')
            }
        }
        if (page == "next_list") {
            first_page = $('.pages:visible').attr('id')
            first_page = parseInt(first_page.substring(0, first_page.length - 6));
            last_page = first_page + 9
            if (last_page != parseInt(document.getElementById('quest_count').value)) {
                last_page = last_page + 1

                last_lbl = '#' + last_page + '_label'
                first_lbl = '#' + first_page + '_label'
                $(first_lbl).attr('hidden', 'hidden')

                $(last_lbl).removeAttr('hidden')
            }
        }
        if (page == "last") {
            if (parseInt(document.getElementById('quest_count').value) > 10) {
                last_page = parseInt(document.getElementById('quest_count').value)
                first_page = last_page - 9
                for (var i = first_page; i <= last_page; i++) {
                    lbl = '#' + i + '_label'
                    $(lbl).removeAttr('hidden')
                }
                for (i = 1; i < first_page; i++) {
                    lbl = '#' + i + '_label'
                    $(lbl).attr('hidden', 'hidden')
                }
            }
        }
        if (page == "first") {
            page_num = parseInt(document.getElementById('quest_count').value)
            if (page_num > 10) {
                last_page = 10
                first_page = 1
                for (var i = first_page; i <= last_page; i++) {
                    lbl = '#' + i + '_label'
                    $(lbl).removeAttr('hidden')
                }
                for (i = last_page + 1; i <= page_num; i++) {
                    lbl = '#' + i + '_label'
                    $(lbl).attr('hidden', 'hidden')
                }
            }
        }
        if (page == "prev") {
            first_page = $('.pages:visible').attr('id')
            first_page = parseInt(first_page.substring(0, first_page.length - 6));
            active_page = $('.search:visible').attr('id');
            active_page = parseInt(active_page.substring(0, active_page.length - 6));
            if (active_page <= first_page) page_scroll("prev_list")
        }
        if (page == "next") {
            first_page = $('.pages:visible').attr('id')
            first_page = parseInt(first_page.substring(0, first_page.length - 6));
            last_page = first_page + 9
            active_page = $('.search:visible').attr('id');
            active_page = parseInt(active_page.substring(0, active_page.length - 6));
            if (active_page >= last_page) {

                page_scroll("next_list")
            }
        }
    }
}

function show_prompt() {
    active_page = $('.search:visible').attr('id');
    active_page = parseInt(active_page.substring(0, active_page.length - 6));
    document.getElementById(active_page + "_prompt").style.display = 'block';
}

function change_opts() {
    page_count = parseInt(document.getElementById('quest_count').value)
    for (i=1; i<=page_count; i++) {
        ispos = document.getElementById(i + '_ispos').value.split('_')[0]
        
        function shuffle(array) {
            array.sort(() => Math.random() - 0.5);
        }
          
        let arr = ['c1', 'c2', 'c3', 'c4'];
        if (ispos == "True") {
            c1 = document.getElementById('' + i+'_opt1').innerHTML
            c2 = document.getElementById('' + i+'_opt2').innerHTML
            c3 = document.getElementById('' + i+'_opt3').innerHTML
            c4 = document.getElementById('' + i+'_opt4').innerHTML
            dict = {'c1': c1, 'c2': c2, 'c3': c3, 'c4': c4}
            shuffle(arr)
            document.getElementById('' + i+'_opt1').innerHTML = dict[arr[0]]
            document.getElementById('' + i+'_opt2').innerHTML = dict[arr[1]]
            document.getElementById('' + i+'_opt3').innerHTML = dict[arr[2]]
            document.getElementById('' + i+'_opt4').innerHTML = dict[arr[3]]
        }
        else {
            c1 = document.getElementById('' + i+'_opt11').innerHTML
            c2 = document.getElementById('' + i+'_opt12').innerHTML
            c3 = document.getElementById('' + i+'_opt13').innerHTML
            c4 = document.getElementById('' + i+'_opt14').innerHTML
            dict = {'c1': c1, 'c2': c2, 'c3': c3, 'c4': c4}
            shuffle(arr)
            document.getElementById('' + i+'_opt11').innerHTML = dict[arr[0]]
            document.getElementById('' + i+'_opt12').innerHTML = dict[arr[1]]
            document.getElementById('' + i+'_opt13').innerHTML = dict[arr[2]]
            document.getElementById('' + i+'_opt14').innerHTML = dict[arr[3]]
        }

    }
}

document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        change_opts()
        now = new Date().getTime();
        var countDownDate = new Date(now + parseInt(document.getElementById('end_time').value) * 60000);
        // Update the count down every 1 second
        var x = setInterval(function () {
            var now = new Date().getTime();
            var distance = countDownDate - now;

            // Time calculations for days, hours, minutes and seconds
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the element with id="demo"
            document.getElementById("timer").innerHTML = "До автоматического завершения теста осталось: " 
                + hours + ":" + minutes + ":" + seconds;

            // If the count down is finished, write some text
            if (distance < 0) {
                clearInterval(x);
                document.getElementById("timer").innerHTML = "EXPIRED";
                document.getElementById("finish").click()
                
            }
        }, 500);
    }
}

function save_questions() {
    active_page = $('.search:visible').attr('id');
    active_page = parseInt(active_page.substring(0, active_page.length - 6));
    ispossible = document.getElementById('' + active_page + '_ispos').value;
    quest_id = ispossible.split('_')[1]
    ispossible = ispossible.split('_')[0]
    // for_cookie = '' + quest_id + '='
    if (ispossible == "True") {
        for_cookie = ''
        var opt1 = document.getElementById(quest_id + '_answer1').checked;
        var opt2 = document.getElementById(quest_id + '_answer2').checked;
        var opt3 = document.getElementById(quest_id + '_answer3').checked;
        var opt4 = document.getElementById(quest_id + '_answer4').checked;
        if (opt1 || opt2 || opt3 || opt4) {
            if (opt1) {for_cookie += '1';} else {for_cookie += '0'}
            if (opt2) {for_cookie += '1';} else {for_cookie += '0'}
            if (opt3) {for_cookie += '1';} else {for_cookie += '0'}
            if (opt4) {for_cookie += '1';} else {for_cookie += '0'}
            // document.cookie = for_cookie
            sessionStorage.setItem(quest_id, for_cookie)
            document.getElementById(active_page + '_label').style.border = '2px solid #000000';
        }
        else {
            alert("Не выбран ни один ответ!")
        }
    }
    else {
        name_radio = quest_id + '_radio'
        opt = $('input[name="' + name_radio + '"]:checked').val()
        if (opt) {
            // for_cookie += opt
            sessionStorage.setItem(quest_id, opt)
            document.getElementById(active_page + '_label').style.border = '2px solid #000000';
        }
        else {
            alert("Не выбран ни один ответ!")
        }
    }
}

function finish_button(e) {
    if (document.getElementById("timer").innerHTML == "EXPIRED"){
        send_answers();
        return 0;
    }
    else {
        page_count = parseInt(document.getElementById('quest_count').value)
        for (i=1; i <= page_count; i++) {
            checked_el = document.getElementById(i + '_label').style.border
            if (!checked_el) {
                if(!confirm('Не все ответы сохранены! Вы уверены в совершаемом действии?')){
                    //prevent sending the request when user clicked 'Cancel'
                    e.preventDefault();
                    return 0;
                }
                else {
                    send_answers();
                    return 0;
                }
            }
        }
    }
    send_answers();
}

function send_answers() {
    keys = Object.keys(sessionStorage);
    i = 0;
    archive = [];
    // if (sessionStorage) {
    //    archive = [];
    // }
    // else {
    //
    // }
    for (; key = keys[i]; i++) {
        archive.push( key + '=' + sessionStorage.getItem(key));
    }
    document.getElementById('answer_to_send').value = archive
    document.getElementById('finish_time').value = document.getElementById("timer").innerHTML
    sessionStorage.clear();
}

