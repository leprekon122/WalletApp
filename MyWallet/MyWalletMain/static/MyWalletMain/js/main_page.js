function delete_btn(){
    // function for warning pop-up when try delete article
    $('#confirm_modal').modal('show');
    let btn_dlt = document.getElementById('delete_article');
    let confirm_btn = document.getElementById('yes');

    confirm_btn.onclick = function() {
        btn_dlt.type = "submit"
        btn_dlt.click()
        $('#confirm_modal').modal('hide');
    };
    }
