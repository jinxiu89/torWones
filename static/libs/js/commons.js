/**
 * create by Administrator on 16-7-16
 * 处理 Post数据
* 提交form表单数据
* #button_add :提交按钮的ID
* #form-data:提交表单的form ID
* 利用serializeArray
* 组装数组用each方法
* */
$("#button_add").click(function () {
    var data = $("#form-data").serializeArray();
    /***
     * 修正日期：2016-09-08
     * 修正人：袁普照
     * 解决数组的问题
     */
    var postData={};
    $(data).each(function(){
        if(postData[this.name]){
            if($.isArray(postData[this.name])){
                postData[this.name].push(this.value);
            }else{
                postData[this.name]=[postData[this.name],this.value];
            }
        }else{
            postData[this.name]=this.value;
        }
    });

    //console.log(postData);
    //SCOPE是在模板文件的script block中写的
    var url=SCOPE.save_url;
    //noinspection JSUnresolvedFunction
    $.post(url,postData,function (result) {
        //r如果返回结果是0 表示失败了
        if(result.status === 0){
            dialog.error(result.message);
        }
        // 如果返回结果为1 则表示成功
        if(result.status === 1){
            dialog.success(result.message,result.jump_url);
        }
    },'JSON');
});


//获取cookie
function get_cookie(name) {
    var cookies;
    cookies = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return cookies[1];
}
