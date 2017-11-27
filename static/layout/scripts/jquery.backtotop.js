jQuery("#backtotop").click(function () {
    jQuery("body,html").animate({
        scrollTop: 0
    }, 600);
});
jQuery(window).scroll(function () {
    if (jQuery(window).scrollTop() > 150) {
        jQuery("#backtotop").addClass("visible");
    } else {
        jQuery("#backtotop").removeClass("visible");
    }
});

var theForm = document.getElementById('theForm');
var theInput = document.getElementById('subj');

theForm.onsubmit = function(e){
    location = "http://localhost:8000/busca/" + encodeURIComponent(theInput.value);
    return false;
};

