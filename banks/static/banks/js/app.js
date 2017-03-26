$(document).ready(function () {
    $('.button-collapse').sideNav();
    $('select').material_select();
    $('.collapsible').collapsible();
});

$(document).ready(function ($) {
    $(window).load(function () {
        setTimeout(function(){
            $('#preloader').fadeOut('slow', function () {
            });
        },1000);

    });  
});
