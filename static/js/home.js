// function changepic() {
//     var reads = new FileReader();
//     f = document.getElementById('file').files[0];
//     reads.readAsDataURL(f);
//     reads.onload = function(e) {
//         document.getElementById('img3').src = this.result;
//         $("#img3").css("display", "block");
//     };
// }
//

// 开始转换
function beginChange() {
    $.ajax({
        url : "/beginChange",
        contentType: 'application/json',
        type: 'POST',
        data: 'begin_change',
        success: function (result) {
            console.log('成功');
        },
        fail: function (result) {
          console.log('失败');
        }
    });
}

function uploadFile() {
    
}