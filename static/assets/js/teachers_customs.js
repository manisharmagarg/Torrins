/////////////////////////////////////////////////////////////
//       Script defines js related to teacher portal       // 
/////////////////////////////////////////////////////////////


// append city/districts list in "City/Districts" dropdown
$("#state_change").change(function () {
	var state_id = $(this).val();
	$.ajax({
		type: "POST",
		url: '/teacher/get_district/',
		data: {
			'state_id': state_id
		},
		dataType: 'json',
		success: function (data) {
			var distt_list = data.district
			for (i = 0; i < distt_list.length; i++){
				var all_distt = distt_list[i]
				var div_data="<option value="+all_distt.id+">"+all_distt.name+"</option>";
            	$(div_data).appendTo('#distt_list');
			}
		}
	});
});


// click on Next button
function someFunction21() {
	setTimeout(function () {
		$('#horizontal-stepper').nextStep(formDataTeacher());
	}, 500);
}


//  Click on save changes button
function formDataTeacher() {
	let form = $('form.profile');
	let formElements = $('li.step.active').find("input, select, textarea");

	var serializedData = $(formElements).serializeArray();
	var data = {}
	$(serializedData ).each(function(index, obj){
    	data[obj.name] = obj.value;
	});
	console.log(data);
	$.ajax({
		type: "POST",
		url: '/teacher/profile/update/',
		data: data,
		dataType: 'json',
		success: function (data) {
			toastr.success('Data saved successfully.');
		}
	});
}



$(document).ready(function() {
	var Standards = [];
	$("div.selectStandard a").click(function () {
		var Input = $(this).parent('.selectStandard').parent('.selecttaught').siblings('input');
		Standards = Input.val() ? JSON.parse("[" + Input.val() + "]") : [];
		let Anchor = $(this).attr('value');
		console.log(Anchor);

		if ($(this).hasClass("active")) {
			$(this).removeClass("active");
			Standards = $.grep(Standards, function (value) {
				return value != Anchor;
			});
			Input.val(Standards.toString());
		} else {
			$(this).addClass("active");
			Standards.push($(this).attr('value'));
			Input.val(Standards.toString());
		}
	});
});


// $.when($.ajax(form[0].method,
	// 	$(formElements).serialize(),
	// 	form[0].action
	// // 	)).done(function () {
	// 		// if($('#tform li:last').hasClass('done') && !$('#tform li:last').hasClass('active'))
	// 		// {
	// 				//window.location.href = teacherver; 
	// 		// }
	// 	        // toastr.success('Data saved successfully.');
	// 	    }).fail(function () {
	// 	    	console.log("error");
	// 	    	 // toastr.error('There is some issues, please try after some time!');
	// 	    	});
		

	