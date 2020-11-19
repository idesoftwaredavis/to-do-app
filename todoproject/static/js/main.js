$(document).ready(function(){
    $('#btnRecord').click(function(){
        let task = $('#task').val()
        let csrf_token = $("input[name=csrfmiddlewaretoken]").val()
        $.ajax({
          url: "/app/views/home/",
          type: "POST",
          data:{
            tarea:task,
            csrfmiddlewaretoken:csrf_token
          },
          success: function(response){
            html = "<li>" + response.data + "</li>";
            $("#tasks").append(html);
          }
        })
        return false;
    });
});
