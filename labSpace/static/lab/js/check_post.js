/**
 * Created by asus on 2020/5/23.
 */
jQuery(document).ready(function() {

    $("#title").bind("input propertychange",function(){
        if($.trim(this.value) === "" || $.trim(this.value).length > 20){
            var errorMsg = "请输入1—20位的博客题目";
            $(this).parent().find(".msg").remove();
            $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
        }else{
            $(this).parent().find(".msg").remove();
        }
    });

    $("#link").bind("input propertychange",function(){
        if($.trim(this.value).length > 5000){
            var errorMsg = "博客链接长度大于5000";
            $(this).parent().find(".msg").remove();
            $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
        }else{
            $(this).parent().find(".msg").remove();
        }
    });

    $("form").submit(function(){
        /*第二：判断数据是否合规*/
        if(!($.trim($("#title")[0].value) === "" || $.trim($("#title")[0].value).length > 20)){
            if(!($.trim($("#link")[0].value).length > 5000)){
                return confirm("是否确定提交博客？");
            }
        }
        alert("表单数据不规范，请核验！");
        return false;
    });
});