(function ($) {
    "use strict";


    /*==================================================================
   [ Focus input ]*/
    $('.input100').each(function () {
        $(this).on('blur', function () {
            if ($(this).val().trim() !== "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        })
    })


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit', function () {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) === false) {
                showValidate(input[i]);
                check = false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') === 'email' || $(input).attr('name') === 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        } else {
            if ($(input).val().trim() === '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

})(jQuery);


// 隐藏按钮图片
function signIn() {
    // var是局部变量
    let submit = document.getElementsByClassName("sign-submit");
    if (submit.value === "登录"){
        submit.value = "登录中..."
    }

    // 拿到Input-text的对象
    let username_input = document.getElementsByClassName("username-input");
    let username = username_input.value;

    let password_input = document.getElementsByClassName("password-input");
    let password = password_input.value;

    alert(username);
    alert(password);
    var post_data = {
        "username" : username,
        "password" : password
    };
    $.ajax({
        url : "/signCheck",
        contentType: 'application/json',
        type: 'POST',
        data: JSON.stringify(post_data),
        success: function (result) {
            console.log('成功');
        },
        fail: function (result) {
          console.log('失败');
        }
    });
    // POST("/user/sign", {
    //     name: username,
    //     password: password
    // }, function (data) {
    //     saveUser(data[0]);
    //     window.location.href = "sign.html";
    // }, function (data) {
    //     alert(data);
    // });
}