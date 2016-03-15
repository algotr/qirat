/**
 * Created by ali on 24/12/15.
 */

$(function () {
    delete_post();
});

function delete_post( ) {
    $('a.delete-post').click(function(){
        $(this).preventDefault = true;
        var clicked_item = $(this);

        var csrfmiddlewaretoken = $(this).parent().find('input[name="csrfmiddlewaretoken"]').val();
        var post_id = $(this).attr('data-postid');

        if (confirm("هل انت متأكد من عملية الحذف؟")) {
            $.ajax({
                type: "POST",
                url: "/delete/",
                data: {
                    "id": post_id,
                    "csrfmiddlewaretoken": csrfmiddlewaretoken,
                }
            }).success(function(data){
                if(data=="success"){
                    clicked_item.parents(".panel.panel-default").remove();
                }
            });
        }
    });
}