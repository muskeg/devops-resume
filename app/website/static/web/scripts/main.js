$(function() {
});

$(window).scroll(function(){
    var scroll_length = $(document).scrollTop();
    var title_margin = $(window).height() * 0.30;
    var header_height = $(window).height() * 0.70;
    if (scroll_length < ($(window).height() * 0.20)) {
      $('#header').css('height', header_height - scroll_length);
      $('#header_title').css('margin-top', title_margin - scroll_length);
      $('#header').css('margin-bottom', header_height * scroll_length * -0.002 );
    }
});

