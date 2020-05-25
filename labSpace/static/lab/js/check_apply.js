/**
 * Created by asus on 2020/5/21.
 */
jQuery(document).ready(function() {
    var address_exist = false;

    $("#lab_name").bind("input propertychange",function(){
        if($.trim(this.value) === "" || $.trim(this.value).length > 21){
            var errorMsg = "请输入1—21位的实验室空间名称";
            $(this).parent().find(".msg").remove();
            $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
        } else {
            $(this).parent().find(".msg").remove();
        }
    });

    $("#introduce").bind("input propertychange",function(){
        if($.trim(this.value).length > 999){
            var errorMsg = "输入简介的长度超过了999";
            $(this).parent().find(".msg").remove();
            $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
        }else{
            $(this).parent().find(".msg").remove();
        }
    });

    $("#url_id").bind("input propertychange",function(){
        if($.trim(this.value) === "" || !(/^[0-9a-zA-Z]*$/g.test($.trim(this.value))) ||
        $.trim(this.value).length > 20){
            console.log(111);
            var errorMsg = "专属空间地址应为1-20位字母和数字的组合";
            $(this).parent().find(".msg").remove();
            $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
        }else{
            $(this).parent().find(".msg").remove();
            var lab_add = $.trim($("#url_id")[0].value);
            var request_url = "/lab/get_address/" + lab_add;
            $.ajax({
                dataType: "json",
                url: request_url,
                data: {},
                success: function(data){
                    var status = data.lab.is_exist;
                    if(status){
                        address_exist = true;
                        var errorMsg = "该空间地址已被注册";
                        $("#url_id").parent().find(".msg").remove();
                        $("#url_id").parent().append("<span class='msg onError'>" + errorMsg + "</span>");
                    }else{
                        address_exist = false;
                        $("#url_id").parent().find(".msg").remove();
                    }
                }
            });
        }
    });

    $("form").submit(function(){
        /*第二：判断数据是否合规*/
        if(!($.trim($("#lab_name")[0].value) === "" || $.trim($("#lab_name")[0].value).length > 21)){
            if(!($.trim($("#introduce")[0].value).length > 999)){
                if(!($.trim($("#url_id")[0].value) === "" || !(/^[0-9a-zA-Z]*$/g.test($.trim($("#url_id")[0].value))) ||
                $.trim($("#url_id")[0].value).length > 20)){
                    if(!address_exist){
                       return confirm("确认提交注册空间表单？");
                    }
                }
            }
        }
        alert("表单数据不规范，请核验！");
        return false;
    })
});