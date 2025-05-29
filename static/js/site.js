function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function sendPostRequest(url, data, element_id) {
    const csrfToken = getCookie('csrftoken');

    if (typeof data !== 'string') {
        data = JSON.stringify(data)
    }

    console.log('calling AJAX: ' + url)
    $.ajax({
        url: url,
        type: 'post',
        data: data,
        headers: {
            'X-CSRFToken': csrfToken
        },
        dataType: 'html',
        success: function(data) {
            console.log('AJAX success');
            document.getElementById(element_id).innerHTML="<h1>Ajax:</h1>"+data;
        },
        error: function(error) {
            console.log('AJAX error; ' + error);
        }
    });
}
