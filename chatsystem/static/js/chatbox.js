document.getElementById("chat").style.borderColor = "black";
$(document).on('submit', '#post-form', function(e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/send',
        data: {
            username: $('#username').val(),
            sessionid: $('#sessionid').val(),
            message: $('#message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function(data) {
            console.log(data)
        }
    })
    document.getElementById('message').value = ''
})
$(document).ready(function() {

    setInterval(function() {
        $.ajax({
            type: 'GET',
            url: '/get_message/' + a,
            success: function(response) {
                console.log(response);

                $('#display').empty();

                for (var key in response.messages) {
                    console.log(key)


                    var temp = '<li class="other"><div class="messages"> <p style="font-weight: bold;">' + response.messages[key].user + '</p><p>' + response.messages[key].message + '</p> </div> </li> '
                    $('#display').append(temp)





                }
            }

        })

    }, 1000)

});