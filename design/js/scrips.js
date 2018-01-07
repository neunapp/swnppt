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
});
