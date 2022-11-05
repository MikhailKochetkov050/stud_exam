function DeleteConfirm(e) {
    if(!confirm('Вы уверены, что хотите удалить тест?')){
        //prevent sending the request when user clicked 'Cancel'
        e.preventDefault();
    }
}

function hide_it() {
    let form = document.createElement('form');
    form.action = '/profile/';
    document.body.append(form);
    form.method = 'GET';
    form.submit();
}
