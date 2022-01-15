window.addEventListener("load" , function (){

    let config_pay_date   = {
        "locale": "ja"
    }
    flatpickr("[name='pay_date']", config_pay_date);


    //DjangoMessageFrameWorkの削除機能
    $(".message_delete").on("click", function(){ $(this).parent(".message").remove(); });



});
