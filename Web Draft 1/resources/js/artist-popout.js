// function ShowDiv() {
//     document.getElementById("artist-popout").style.display = "";
// }

// $( "#artist-popout" ).click(function() {
//     document.getElementById("artist-popout").style.display="visible";
//   });

$(document).ready(function() {
    $(".arkhum").click(function() {
    $("#artist-popout").show();
    });

    $(".close").click(function() {
    $("#artist-popout").hide();
    });

    $(".banewreaker").click(function() {
    $("#banewreaker").show();
    });

    $("#banewreaker .close").click(function() {
    $("#banewreaker").hide();
    });
});

