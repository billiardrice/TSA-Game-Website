$(document).ready(function () {
    $('form').on('submit', function (event) {
        $.ajax({
            type: 'POST',
            url: '/auth',
            data: JSON.stringify({
                'email': $('#email').val(),
                'password': $('#password').val()
            }),
            contentType: "application/json; charset=utf-8",
            dataType: "json"
        })
            .done(function (data) {
                if (data.error) {
                    $('#alert').text(data.error).show()
                }
                else {
                    window.location = data.redirect;
                }
            });

        event.preventDefault();

    });
});