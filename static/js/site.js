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

    $.ajax({
        url: url,
        method: 'post',
        data: data,
        headers: {
            'X-CSRFToken': csrfToken
        },
        dataType: 'html',
        success: function(data) {
            document.getElementById(element_id).innerHTML=data;
        },
        error: function(jqXHR, text_status, error_thrown) {
            console.log('AJAX error; ' + error_thrown);
            document.getElementById(element_id).innerHTML="Ajax error";
        }
    });
}
