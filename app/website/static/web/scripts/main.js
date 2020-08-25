$(function() {

});

$(window).on('beforeunload', function() {
    $(window).scrollTop(0);
});

/*
$(window).scroll(function(){
    var scroll_length = $(document).scrollTop();
    $( "#header_title" ).animate({
      fontSize: "3vw"
      }, 500, "linear", function() {
      $('#header_nav').fadeIn(200);
    });

    var title_margin = $(window).height() * 0.30;
    var title_size = $(window).width() * 0.16;
    var header_height = $(window).height() * 0.70;
    var content_topmargin = $(window).height() - title_margin;
   // console.log(scroll_length);
    //if (scroll_length > ($(window).height() * 0.75)) {
    //  $('#header_subtitle').fadeOut(100, function() {
    //    $( "#header_title" ).animate({
    //      fontSize: "3vw"
    //    }, 500, "linear", function() {
     //     $('#header_nav').fadeIn(200);
     //   });
    //  });
    //}
    //else if (scroll_length < ($(window).height() * 0.5)) {
    //  $( "#header_title" ).animate({
    //    fontSize: "16vw"
    //  }, 500, "linear", function() {
    //    $('#header_nav').fadeOut(100);
    //    $('#header_subtitle').fadeIn(200);
    //  });
      
      //$('#header').css('height', header_height - scroll_length);
      //$('#content').css('margin-top', content_topmargin - scroll_length);
    }
});
*/
