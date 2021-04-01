//$(document).ready(function(){ 
//    $('.toggleMenu1').click(function() { 
//          $('.menuList1').toggleClass('show');
//		  $('.menuList2').removeClass('show');
//	});
//	$('.toggleMenu2').click(function() {
//          $('.menuList2').toggleClass('show');
//		  $('.menuList1').removeClass('show');
//	});
//});


// Fix CSRF token issue 
$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}
		if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
			// Only send the token to relative URLs i.e. locally.
			xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		}
	}
});


