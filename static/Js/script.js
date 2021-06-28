$(document).ready(function(){
$('form').on('submit' , function(e){
    e.preventDefault();
     if($('input[name="radiob"]:checked').val() == undefined){
        $('.warn').html('اختار راي الاول');
     }else{
        $.ajax({
                type: 'POST',
                url: '/data',
                data: JSON.stringify({'state' : $('input[name="radiob"]:checked').val()}),
                contentType: 'application/json;charset=UTF-8',
                success : function(data){
                    $('.warn').html('');
                    $('.VoteBtn').prop('disabled' , true)
                    $('VoteBtn').css({'background-color' : 'red'})
                    $('#d').html(data['disagree'])
                    $('#a').html(data['agree'])
                }
                });
     }
})
})