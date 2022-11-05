function checkParams() {
    var full_name = $('#full_name').val();
     
    if(full_name.length != 0 && ($('input[name="user_type"]').is(':checked'))) {
        $('#btn1').removeAttr('disabled');
        $('#btn2').removeAttr('disabled');
    } else {
        $('#btn1').attr('disabled', 'disabled');
        $('#btn2').attr('disabled', 'disabled');
    }
}

function LoginGeneration() {
    var full_name = document.getElementById('full_name').value;
    var ans = document.getElementById('ans').value;
    var user_type = document.querySelector('input[name="user_type"]:checked').value;
    var transliterate = function(text) {

        text = text
            .replace(/\u0401/g, 'YO')
            .replace(/\u0419/g, 'I')
            .replace(/\u0426/g, 'TS')
            .replace(/\u0423/g, 'U')
            .replace(/\u041A/g, 'K')
            .replace(/\u0415/g, 'E')
            .replace(/\u041D/g, 'N')
            .replace(/\u0413/g, 'G')
            .replace(/\u0428/g, 'SH')
            .replace(/\u0429/g, 'SCH')
            .replace(/\u0417/g, 'Z')
            .replace(/\u0425/g, 'H')
            .replace(/\u042A/g, '')
            .replace(/\u0451/g, 'yo')
            .replace(/\u0439/g, 'i')
            .replace(/\u0446/g, 'ts')
            .replace(/\u0443/g, 'u')
            .replace(/\u043A/g, 'k')
            .replace(/\u0435/g, 'e')
            .replace(/\u043D/g, 'n')
            .replace(/\u0433/g, 'g')
            .replace(/\u0448/g, 'sh')
            .replace(/\u0449/g, 'sch')
            .replace(/\u0437/g, 'z')
            .replace(/\u0445/g, 'h')
            .replace(/\u044A/g, "'")
            .replace(/\u0424/g, 'F')
            .replace(/\u042B/g, 'I')
            .replace(/\u0412/g, 'V')
            .replace(/\u0410/g, 'a')
            .replace(/\u041F/g, 'P')
            .replace(/\u0420/g, 'R')
            .replace(/\u041E/g, 'O')
            .replace(/\u041B/g, 'L')
            .replace(/\u0414/g, 'D')
            .replace(/\u0416/g, 'ZH')
            .replace(/\u042D/g, 'E')
            .replace(/\u0444/g, 'f')
            .replace(/\u044B/g, 'i')
            .replace(/\u0432/g, 'v')
            .replace(/\u0430/g, 'a')
            .replace(/\u043F/g, 'p')
            .replace(/\u0440/g, 'r')
            .replace(/\u043E/g, 'o')
            .replace(/\u043B/g, 'l')
            .replace(/\u0434/g, 'd')
            .replace(/\u0436/g, 'zh')
            .replace(/\u044D/g, 'e')
            .replace(/\u042F/g, 'Ya')
            .replace(/\u0427/g, 'CH')
            .replace(/\u0421/g, 'S')
            .replace(/\u041C/g, 'M')
            .replace(/\u0418/g, 'I')
            .replace(/\u0422/g, 'T')
            .replace(/\u042C/g, "'")
            .replace(/\u0411/g, 'B')
            .replace(/\u042E/g, 'YU')
            .replace(/\u044F/g, 'ya')
            .replace(/\u0447/g, 'ch')
            .replace(/\u0441/g, 's')
            .replace(/\u043C/g, 'm')
            .replace(/\u0438/g, 'i')
            .replace(/\u0442/g, 't')
            .replace(/\u044C/g, "'")
            .replace(/\u0431/g, 'b')
            .replace(/\u044E/g, 'yu');
    
        return text;
    };

    last_name = full_name.split(' ')[0];
    document.getElementById('usr').value = user_type + '_' + transliterate(last_name) + '_' + ans
}

function PwdGeneration(elem_id){
    var re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@№;%:?*()_+=]).{10,}$/;
    var password;
    do {
        password = "";
        var symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@№;%:?*()_+=";
        for (var i = 0; i < 10; i++){
            password += symbols.charAt(Math.floor(Math.random() * symbols.length));     
        }
    } while (re.exec(password) == null)
    
    document.getElementById(elem_id).value = password;
}

function SwitchChange(choosen_value) {
    var status = choosen_value.split('+')[0];
    var name = choosen_value.split('+')[1];
    if (status == "--Выберите имя пользователя--") {
        $('#btn3').attr('disabled', 'disabled');
        $('#btn4').attr('disabled', 'disabled');
        $('#btn5').attr('disabled', 'disabled');
        $('#stackedCheck1').bootstrapToggle('off');
        $('#stackedCheck1').attr('disabled', 'disabled');
    }
    else { 
        $('#btn3').removeAttr('disabled');
        $('#btn4').removeAttr('disabled');
        $('#btn5').removeAttr('disabled');
        $('#stackedCheck1').removeAttr('disabled');
        document.getElementById('cngUsrName').value = name
    }
    if (status == "True") {
        $('#stackedCheck1').bootstrapToggle('off');
    }
    if (status == "False") {
        $('#stackedCheck1').bootstrapToggle('on');
    }


    if (status == 'True') {
        document.getElementById('status_change').value = false
    }
    else {
        document.getElementById('status_change').value = true
    }

}

function DeleteConfirm(e) {
    if(!confirm('Вы уверены, что хотите удалить пользователя?')) {
        //prevent sending the request when user clicked 'Cancel'
        e.preventDefault();
    }
}

function changed_status() {
    document.getElementById('status_change').value = $('#stackedCheck1').prop('checked')
    // $('input[name="user_type"]').is(':checked')
    // document.getElementById('status_change').value = status
}
