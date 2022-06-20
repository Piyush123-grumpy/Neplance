$(document).ready(function(){
	$('.form-input').on('keyup, paste, cut, focusout', function(){
		var $parent = $(this).parents('.form-line');
		var input_value = $.trim($(this).val());
		var required = $(this).is(':required');

		if (input_value.length > 0) {
			$parent.find('label').addClass('top');

			$parent
				.removeClass('error')
				.addClass('success');
		}	else {
			$parent.find('label').removeClass('top');
			$parent.removeClass('success')

			if (required) {
				$parent.addClass('error');
			}
		}
	});
});