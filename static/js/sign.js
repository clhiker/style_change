
// 隐藏按钮图片
function signFunction() {
    // var是局部变量
    let submit = document.getElementById("sign-submit");
    if (submit.value === "登录"){
        submit.value = "登录中..."
    }

    // 拿到Input-text的对象
    let username_input = document.getElementById("username-input");
    let username = username_input.value;

    let password_input = document.getElementById("password-input");
    let password = password_input.value;

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
