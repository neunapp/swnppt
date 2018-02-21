$(function(){
  var toggleIcon = $('#togle-mov-icon');
  var toggleMenu = $('#togle-mov-menu-ul');

  toggleIcon.on('click',function(){
    //primero menu
    if (toggleMenu.attr('class') === 'mov-header-menu') {
      toggleMenu.removeClass('mov-header-menu').addClass('mov-header-menu-disable');
    }
    else {
      toggleMenu.removeClass('mov-header-menu-disable').addClass('mov-header-menu');
    }

  });


  //scrip para scroll en header
  var header_class = $('#main-header');
  var main_header_logo = $('#main-header-logo');
  $(window).scroll(function () {
      if ($(this).scrollTop() > 70) {
        header_class.removeClass('main-header').addClass('main-header-change');
        main_header_logo.removeClass('main-header-logo').addClass('main-header__menu__ul__logo');
      }
      if ($(this).scrollTop() < 70) {
        header_class.removeClass('main-header-change').addClass('main-header');
        main_header_logo.removeClass('main-header__menu__ul__logo').addClass('main-header-logo');
      }
   });
});
