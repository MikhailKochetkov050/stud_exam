function checkParams() {
    var testname = $('#testname').val();
    var attempt_count = document.getElementById('attempt_count').value;
    var time = document.getElementById('time').value;
    
    if(testname.length != 0 && attempt_count != 0 && time != 0) {
        $('#save_btn').removeAttr('disabled');
    } else {
        $('#save_btn').attr('disabled', 'disabled');
    }
}

function SeveralCorrectAns(e) {
    var ispossible = document.getElementById('manychoises');
    var opt1 = document.getElementById('opt1');
    var opt2 = document.getElementById('opt2');
    var opt3 = document.getElementById('opt3');
    var opt4 = document.getElementById('opt4');
    var count = 0;
    if (opt1.checked) {
        count = count + 1;
    }
    if (opt2.checked) {
        count = count + 1;
    }
    if (opt3.checked) {
        count = count + 1;
    }
    if (opt4.checked) {
        count = count + 1;
    }
    if (count == 0) {
        alert('Не выбран ни один параметр!')
        e.preventDefault();
    }
    if (!ispossible.checked && count > 1) {
        alert('Возможен только один верный вариант ответа!')
        e.preventDefault();
    }
}

function DeleteConfirm(e) {
    if(!confirm('Вы уверены, что хотите удалить вопрос?')){
        //prevent sending the request when user clicked 'Cancel'
        e.preventDefault();
    }
}