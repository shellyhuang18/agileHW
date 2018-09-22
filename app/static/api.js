$(() => {
    $('button').click(() => {
        console.log("did something")
        $.ajax({
            url: '/add',
            data: $('form').serialize(),
            type: 'POST',
            success: (res) => {
                //reload the div with the answer- response from end point
                console.log(res)
                $('#result').html(res)
            },
            error: (res) => {
                console.log(res)
            }
        })
    })
})