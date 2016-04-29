function showDescription(id){
    $.get("/radio/s#", {id: id})
        .done(function(data){
            $("#id-input").val(data.id);
            $("#name-input").val(data.name);
            $("#sequence-input").val(data.sequence);
            $("#description-input").val(data.description);
            $("#ajax-form").fadeIn();
    });
}
function closePanel() {
    $("#ajax-form").fadeOut();
}