$(document).ready(function(){
    $.ajax({
        url: '/test',
        type: 'POST',
        dataType: 'json',
        success:function(data){
            var converter = new Markdown.Converter();
            var htm = converter.makeHtml(data);
            $('#test').html(htm);
        }
    });
});
