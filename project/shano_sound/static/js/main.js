(function(){

	function poll() {
    setTimeout(function(){
      getMessages(poll)
    }, 2000);
  }

  function getMessages(cb) {
    var rows = "";
    $.getJSON("/chat/get-messages", function (data) {
      $.each(data, function(key, value) {
        rows += makeChatMessage(value.user, value.message);
      })
      $('.message-content').html(rows);
      $(".message-container").scrollTop($(".message-content").height())
      cb();
    });
  }

  function makeChatMessage(user, message) {
    return '<div class="message">'+
      '<div class="sender">' + 
        user + ':' + 
     '</div>' +
      '<div class="content">' +
        message +
      '</div>'+
    '</div>'
  }

  $(document).ready(function() {
    poll();
    $("textarea").keypress(function(e) {
      if(e.which == 13) {
        $("form").submit();    
      }
    });

    $(".message-container").scrollTop($(".message-content").height())
    $("form").submit(function(e) {
      e.preventDefault();
      var csrf = $(this).find("input[name='csrfmiddlewaretoken']").val();
      var message = $(this).find("textarea").val();
      var self = $(this);
      $.ajax({
        url:"/chat/send-message",
        type: "POST",
        data: {"message": message, "csrfmiddlewaretoken": csrf},
        success: function (data) {
          $(".message-content").append(makeChatMessage(data.user, data.message));
          self.find("textarea").val("");
          $(".message-container").scrollTop($(".message-content").height())
        }
      })
    });
  });
})();