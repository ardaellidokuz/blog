$(document).ready(function(){
    $("#owl-one").owlCarousel({items:1,autoplayTimeout:5000,
      autoplayHoverPause:true,
        loop:true,
        autoplay:true,nav:false,
        dots: false
    });
  });
  AOS.init();
  var scroll = new SmoothScroll('a[href*="#"]', {
	speed: 1000
});
$(document).ready(function(){
  $("#owl-two").owlCarousel({
      loop:true,
      autoplay:true,nav:false,
      dots: false,margin:400,autoplayTimeout:7000,
      autoplayHoverPause:true,
  });
});