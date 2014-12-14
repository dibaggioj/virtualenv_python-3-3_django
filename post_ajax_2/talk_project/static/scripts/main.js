$(function() {

// nothing

console.log("document loaded...");

});

/**
* CSRF Protection
*
* Protect against CSRF attacks
* https://gist.github.com/broinjc/db6e0ac214c355c887e5
*/
// This function gets cookie with a given name
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
var csrftoken = getCookie('csrftoken');


/**
* The functions below will create a header with csrftoken
*/
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
 
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
// end protect against CSRF attacks


/**
* create_post
*/
// AJAX for posting
function create_post() {
    console.log("create post is working!")  // sanity check
    $.ajax({
        url : "create_post/",  // the endpoint
        type : "POST",  // http method
        data : { the_post : $('#post-text').val() },  // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val('');  // remove the value from the input
            console.log(json);  // log the returned json to the console
            $('#talk').prepend("<li id='post-"+json.postpk+"'><strong>"+json.text+"</strong> - <em> "+json.author+"</em> - <span> "+json.created+"</span> <a id='delete-post-"+json.postpk+"'>delete me</a></li>");
            console.log("success");  // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");  // add the error to the DOM
            console.log(xhr.status + ": " + xhr.responseText);  // log the response text and status
        }
    });
};
// end posting AJAX

/**
* delete_post
*/
// AJAX for deleting post
function delete_post(post_primary_key) {
	if (confirm('Are you sure you want to remvoe this post?') == true) {
		$.ajax({
			url : "delete_post/",  // the endpoint
			type : "DELETE",  // http method (if DELETE is unsupported, you can utilize POST tunneling as a work around - https://gist.github.com/mjhea0/43d7b4285c59c2083123)
			data : { postpk : post_primary_key },  // data sent with the delete request

			// handle a successful response
			success : function(json) {
				// hide the post
				$('#post-'+post_primary_key).hide();   // hide the post on successful delete request
				console.log("successfully deleted post "+post_primary_key);
			},

			// handle an unsuccessful response
			error : function(xhr, errmsg, err) {
				// show an error
				$('#results').html("<div class='alert-box alert radius' data-alert>"+
					"Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>");  // add error to the DOM
				console.log(xhr.status + ": " + xhr.responseText);  // log the response text and status
			}
		});
	} else {
		return false;
	}
}
// end delete AJAX

/**
* Handling Events
*
* Here, when a user submits the form this function fires, which:
* 1. Prevents the default browser behavior for a form submission,
* 2. Logs “form submitted!” to the console, and
* 3. Calls a function called create_post() where the AJAX code will live.
*
*/
// jQuery - Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});
// end submit post on

// jQuery - Delete post on click
$("#talk").on('click', 'a[id^=delete-post-]', function(){
    var post_primary_key = $(this).attr('id').split('-')[2];
    console.log(post_primary_key) // sanity check
    delete_post(post_primary_key);
});
// end delete post on click

