//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next").click(function(){
	if(animating) return false;
	animating = true;
	
	current_fs = $(this).parent();
	next_fs = $(this).parent().next();
	
	//activate next step on progressbar using the index of next_fs
	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
	
	//show the next fieldset
	next_fs.show(); 
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale current_fs down to 80%
			scale = 1 - (1 - now) * 0.2;
			//2. bring next_fs from the right(50%)
			left = (now * 50)+"%";
			//3. increase opacity of next_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({
        'transform': 'scale('+scale+')',
        'position': 'absolute'
      });
			next_fs.css({'left': left, 'opacity': opacity});
		}, 
		duration: 800, 
		complete: function(){
			current_fs.hide();
			animating = false;
		}, 
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".previous").click(function(){
	if(animating) return false;
	animating = true;
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	
	//de-activate current step on progressbar
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
	
	//show the previous fieldset
	previous_fs.show(); 
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale previous_fs from 80% to 100%
			scale = 0.8 + (1 - now) * 0.2;
			//2. take current_fs to the right(50%) - from 0%
			left = ((1-now) * 50)+"%";
			//3. increase opacity of previous_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'left': left});
			previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
		}, 
		duration: 800, 
		complete: function(){
			current_fs.hide();
			animating = false;
		}, 
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".submit").click(function(){
	return false;
})
/*
function validate(val) {
    v1 = document.getElementById("sub");
    v2 = document.getElementById("msg");
    
    flag = true;
    
    if(val>=1 || val==0) {
    if(v1.value == "") {
    v1.style.borderColor = "red";
    flag = false;
    }
    else {
    v1.style.borderColor = "green";
    flag = true;
    }
    }
    
    if(val>=2 || val==0) {
    if(v2.value == "") {
    v2.style.borderColor = "red";
    flag = false;
    }
    else {
    v2.style.borderColor = "green";
    flag = true;
    }
    }
    
    return flag;
    }
    
    $(document).ready(function(){
    
    var current_fs, next_fs, previous_fs;
    
    $(".next").click(function(){
    
    str1 = "next1";
    str2 = "next2";
    str3 = "next3";
    
    if(!str1.localeCompare($(this).attr('id')) && document.getElementById("customCheck1").checked == 1) {
    val1 = true;
    }
    else {
    val1 = false;
    }
    
    if(!str2.localeCompare($(this).attr('id')) && document.getElementById("sub").value != "") {
    val21 = true;
    }
    else {
    val21 = false;
    }
    
    if(!str2.localeCompare($(this).attr('id')) && document.getElementById("msg").value != "") {
    val22 = true;
    }
    else {
    val22 = false;
    }
    
    if((!str1.localeCompare($(this).attr('id')) && val1 == true) || (!str2.localeCompare($(this).attr('id')) && val21 == true && val22 == true) || !str3.localeCompare($(this).attr('id'))) {
    current_fs = $(this).parent().parent();
    next_fs = $(this).parent().parent().next();
    
    $(current_fs).removeClass("show");
    $(next_fs).addClass("show");
    
    current_fs.animate({}, {
    step: function() {
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    
    next_fs.css({
    'display': 'block'
    });
    }
    });
    }
    });
    
    $(".prev").click(function(){
    
    current_fs = $(this).parent().parent();
    previous_fs = $(this).parent().parent().prev();
    
    $(current_fs).removeClass("show");
    $(previous_fs).addClass("show");
    
    current_fs.animate({}, {
    step: function() {
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    
    previous_fs.css({
    'display': 'block'
    });
    }
    });
    });
    
    });*/