var header = document.querySelectorAll(".navbar");

var navbarHeight = header.offsetHeight;
var lastScrollTop = 0;

window.onscroll = function() {scrollHide()};

function scrollHide() {
  var st = window.pageYOffset || document.documentElement.scrollTop;
  console.log(st);
  if (st > lastScrollTop) {
    header.classList.add('hide');
  } else {
    header.classList.remove('hide');
  }
  lastScrollTop = st <= 0 ? 0 : st;
}