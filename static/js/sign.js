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

    $('.validate-form').on('submit', function () {
        var check = true;


        // Validate
        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) === false) {
                showValidate(input[i]);
                check = false;
            }
        }

        // Sign in
        if (check === true) {
            const username = $('#username-input').val();
            const password = $('#password-input').val();

            var post_data = {
                "username": username,
                "password": password
            };
            $.ajax({
                url: "/signCheck",
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
        }

        return check;
    });



    $('.validate-form .input-content').each(function () {
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