//风格图片数组
var imgs = new Array("../static/image/example.jpg","../static/image/style1.jpg","../static/image/style2.jpg","../static/image/style3.jpg");
var i = 0;
//向左滑动一张图片
function leftChange() {
    if(i<imgs.length-1){
        i++;
        Id("style_image").src=imgs[i];
    }
}
//向右滑动一张图片
function rightChange() {
    if(i>0){
        i--;
        Id("style_image").src=imgs[i];
    }
}
//获得文件对象引用
function Id(id){
    return document.getElementById(id);
}

// 上传函数
//选择图片
function upload(){
    upload_form = document.getElementById('upload-file-form');
    upload_form.submit();
    var file = Id("file");
    if(file.value==''){
        //透明度设置为0
        Id("image").style.opacity=0;
    }else{
        preImg("file","image");
        //透明度设置为1
        Id("image").style.opacity=1;
    }



}
//获取input[file]图片的url
function getFileUrl(fileId) {
    var url;
    var file = Id(fileId);
    var agent = navigator.userAgent;
    if (agent.indexOf("MSIE")>=1) {
        url = file.value;
    } else if(agent.indexOf("Firefox")>0) {
        url = window.URL.createObjectURL(file.files.item(0));
    } else if(agent.indexOf("Chrome")>0) {
        url = window.URL.createObjectURL(file.files.item(0));
    }
    console.log(url);
    return url;
}
//读取图片后预览
function preImg(fileId,imgId) {
    var imgPre =Id(imgId);
    imgPre.src = getFileUrl(fileId);
}

//风格转换
function styleChange() {
    var cg_img = Id("change_image")
    var file = Id("file");
    if(file.value==''){
        //透明度设置为0
        Id("change_image").style.opacity=0;
    }else{
        cg_img.src=getFileUrl("file");
        //透明度设置为1
        Id("change_image").style.opacity=1;
    }

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
