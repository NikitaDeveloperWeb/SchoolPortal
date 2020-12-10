function mode() {
    $.ajax({
        url: 'chat.html',
        success: function(data) {
            $('#Chat_setinterval').html(data);
        }
    });
};
setInterval(mode, 10000);