$(function() {
	// $('.menu  li a').on('click', function(e) {
	//     $('.menu  li a').removeClass('active');
	//     $(this).addClass('active');
	// });
    
 //    $('a[href="' + this.location.pathname + '"]').parent().addClass('active');
	
    $(".dropdown").mouseenter(function(){
      	$(this).addClass('open');
      });
    $(".dropdown").mouseleave(function(){
      	$(this).removeClass('open');
      });

    $('.flexslider').flexslider({
		    animation: "fade",
		    animationSpeed: 1700
		});
	// 
});