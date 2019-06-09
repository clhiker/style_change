//风格图片数组
var imgs = new Array("../static/image/example.jpg","../static/image/style1.jpg","../static/image/style2.jpg","../static/image/style3.jpg")
var i = 0;

function leftChange() {
    if(i<imgs.length-1){
        i++;
        Id("style_image").src=imgs[i];
    }
}

function rightChange() {
    if(i>0){
        i--;
        Id("style_image").src=imgs[i];
    }
}
//在风格图片数组中选择风格图片
function selectStyle() {
    var temp = Id("style_image");
    Id("image2").src = temp.src;
}

function Id(id){
    return document.getElementById(id);
}
//选择原图
function changeImage(){
    uploadFile('upload-content-form');
    var img = Id("image1");
    var file = Id("file1");
    if(file.value===''){
        //设置默认图片
        img.src='../static/image/upload1.png';
    }else{
        preImg("file1","image1");
    }
}
//选择自定义风格图片
function changeStyle() {
    uploadFile('upload-style-form');
    var img = Id("image2");
    var file = Id("file2");
    if (file.value === '') {
        //设置默认图片
        img.src = '../static/image/upload1.png';
    } else {
        preImg("file2", "image2");
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
    return url;
}
//读取图片后预览
function preImg(fileId,imgId) {
    var imgPre =Id(imgId);
    imgPre.src = getFileUrl(fileId);
}

//风格转换
function styleChange() {
    var cg_img = Id("change_image");
    var file1 = Id("file1");
    var file2 = Id("file2");
    console.log(file1.value);
    console.log(file2.value);
    if(file1.value===''||file2.value===''){
        // //设置默认图片
        cg_img.src='../static/image/upload1.png';
    }else{
        //风格转换后的图片
        // cg_img.src=getFileUrl("file1");
        cg_img.src='../static/image/loading.gif';
        // Id("change_image").style.opacity=1;
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

function uploadFile(form_id) {
    upload_form = document.getElementById(form_id);
    upload_form.submit();
}


setInterval(function () {
    $.ajax({
        url : "/askForFinish",
        contentType: 'application/json',
        type: 'POST',
        data: 'begin_change',
        success: function (result) {
            console.log(result['status'])
            if (result['status'] == '200'){
                var cg_img = Id("change_image");
                // cg_img.src='../static/image/' + result['file_path'];
                console.log(result['file_path']);
                cg_img.src=result['file_path'];
            }
            console.log('成功');
        },
        fail: function (result) {
          console.log('失败');
        }
    });
}, 10 * 1000);