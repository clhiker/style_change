(function ($) {
    "use strict";


    /*==================================================================
   [ Focus input ]*/
    $('.input-content').each(function () {
        $(this).on('blur', function () {
            if ($(this).val().trim() !== "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        })
    });


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input-content');

    $('.validate-register-form').on('submit', function () {
        var check = true;

        // Validate
        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) === false) {
                showValidate(input[i]);
                check = false;
            }
        }

        return check;
    });


    $('.validate-register-form .input-content').each(function () {
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

    /*==================================================================
    [ Get Verify Code ]*/
    $('.get-verify-code-btn').click(function () {
        var countdown = 0;

        if (countdown === 0) {
            $(this).removeAttr("disabled");
            $(this).value = "点击获取";
            countdown = 60;
            var telephone = $('#telephone-input').val();
            $.post("/register/", {
                phone: telephone
            }, function (data) {
                /** @namespace data.messages */
                if (data.messages !== null && data.messages[0].code === '1000') {
                    window.location.href = "home";
                } else {
                    alert(data.messages[0].message);
                }
            });
        } else {
            $(this).setAttribute("disabled", true);
            $(this).value = "重新发送(" + countdown + ")";
            $(this).border = "1px solid black";
            countdown--;
            if (countdown > 1) {
                setTimeout(function () {
                    setTime(button)
                }, 1000);
            }
        }
    })

})(jQuery);
