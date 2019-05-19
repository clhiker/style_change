
// 隐藏按钮图片
function registerFunction() {
    // var是局部变量
    var submit = document.getElementById("register-submit");
    if (submit.value === "注册"){
        submit.value = "注册中..."
    }

    // 判断密码是否相同
    var password_input = document.getElementById("password-input");
    var password = password_input.value;

    var password_again_input = document.getElementById("password-input");
    var password_again = password_again_input.value;

    if (password !== password_again){
        // 拿到Input-text的对象
        return;
    }
    var username_input = document.getElementById("username-input");
    var username = username_input.value;

    // 拿到电话号码
    var telephone_input = document.getElementById("telephone-input");
    var telephone = telephone_input.value;

    var verifyCode = $("#verificationCode-input").val();

    POST("user/register", {
        name: username,
        phone: telephone,
        password: password,
        verifyCode: verifyCode
    }, function (data) {
        /** @namespace data.messages */
        if (data.messages !== null && data.messages[0].code === '1000' ){
            window.location.href = "home";
        } else {
            alert(data.messages[0].message);
        }
    }, function (data) {
        alert(data);
    });
}

var countdown=0;
function setTime(button) {
    // 发送一个验证码
    if (countdown === 0) {
        button.removeAttribute("disabled");
        button.value="点击获取";
        countdown = 60;
        var telephone_input = document.getElementById("telephone-input");
        var telephone = telephone_input.value;
        POST("../user/sendMessage", {
            phone: telephone
        }, function (data) {
            /** @namespace data.messages */
            if (data.messages !== null && data.messages[0].code === '1000' ){
                window.location.href = "home";
            } else {
                alert(data.messages[0].message);
            }
        }, function (data) {
            alert(data);
        });
    } else {
        button.setAttribute("disabled", true);
        button.value="重新发送(" + countdown + ")";
        button.border = "1px solid black";
        countdown--;
        if (countdown > 1){
            setTimeout(function() {
                setTime(button)
            },1000);
        }
    }
}

