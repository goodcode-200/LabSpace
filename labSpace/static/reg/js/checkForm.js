/**
 * Created by asus on 2020/5/19.
 */
/*页面调度完之后加载*/
jQuery(document).ready(function() {
    var user_exist = false;
  //为表单的必填文本框添加提示信息（选择form中的所有后代input元素）
  $("#nickname").bind("input propertychange",function(){
      if($.trim(this.value) === "" || $.trim(this.value).length > 6){
          var errorMsg = " 请输入1-6位的昵称！";
          //class='msg onError' 中间的空格是层叠样式的格式
          $(this).parent().find(".msg ").remove();
          $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
      }
      else{
          $(this).parent().find(".msg ").remove();
          var user_add = $.trim($("#nickname")[0].value);
          var request_url = "/user/get_nickname/" + user_add;
          $.ajax({
              dataType:"json",
              url: request_url,
              data:{},
              success:function(data){
                  var status = data.user.is_exist;
                  if(status) {
                      user_exist  = true;
                      var errorMsg = "该昵称已经被使用";
                      $("#nickname").parent().find(".msg ").remove();
                      $("#nickname").parent().append("<span class='msg onError'>" + errorMsg + "</span>");
                  }else{
                      user_exist = false;
                      $("#nickname").parent().find(".msg ").remove();
                  }
              }
          });

      }
  });

  $("#email").bind("input propertychange",function(){
      if($.trim(this.value) === "" ||
          (($.trim(this.value) !== "" && !/.+@.+\.[a-zA-Z]{2,4}$/.test($.trim(this.value))))){
          var errorMsg = "请输入正确的邮箱地址";
          //class='msg onError' 中间的空格是层叠样式的格式
          $(this).parent().find(".msg ").remove();
          $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
      }else{
          $(this).parent().find(".msg ").remove();
      }
  });

  $("#confi_pass").bind("input propertychange",function(){
      if(this.value === $("#pass")[0].value){
          $(this).parent().find(".msg ").remove();
      }
      else{
          var errorMsg = "两次输入密码不一致";
          //class='msg onError' 中间的空格是层叠样式的格式
          $(this).parent().find(".msg ").remove();
          $(this).parent().append("<span class='msg onError'>" + errorMsg + "</span>");
      }
  });

  $("form").submit(function(){
      if(!($.trim($("#nickname")[0].value) === "" || $.trim($("#nickname")[0].value).length > 6)){
          if(!($.trim($("#email")[0].value) === "" ||
          (($.trim($("#email")[0].value) !== "" && !/.+@.+\.[a-zA-Z]{2,4}$/.test($.trim($("#email")[0].value)))))){
              if($("#confi_pass")[0].value === $("#pass")[0].value){
                  if(!user_exist){
                      return confirm("确认提交注册表单？");
                  }
              }
          }
      }
      alert("表单数据不规范，请核验！");
      return false;
  });
});