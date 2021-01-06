$(document).ready(function(){
    function scrollMenu(){
       let navmenu = $('.nav-menu');
           if($(window).scrollTop () >50){
               navmenu.addClass('nav-open');
           }
           else{
               navmenu.removeClass('nav-open');
           }
    }
scrollMenu();
$(window).on('scroll',scrollMenu);

});
    let navcollapse = $('#menucollapse');
      navcollapse.on('show.bs.collapse', function(){
          $(this).parents('.nav-menu').addClass('nav-open');
      });

      navcollapse.on('hide.bs.collapse', function(){
        $(this).parents('.nav-menu').removeClass('nav-open');
     });

// $(Window).on('scroll',function(){
//     console.log($(window).scrollTop());
// })

let gallery = $('.img-gallery');
if(gallery.length && $.fn.owlCarousel){
    gallery.owlCarousel({
        rtl:true,
        nav:false,
        items:3,
        dots:true,
        center:true,
        autoplay:true,
        loop:true,
        responsive:{
            0 :{
                items:1
            },
            768 :{
                items:3
            }
        }
    });
}
