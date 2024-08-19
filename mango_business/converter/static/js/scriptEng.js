
function digits_int(target){
	val = $(target).val().replace(/[^0-9]/g, '');
	val = val.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
	$(target).val(val);
}

function digits_float(target){
	val = $(target).val().replace(/[^0-9.]/g, '');
	if (val.indexOf(".") != '-1') {
		val = val.substring(0, val.indexOf(".") + 2);
	}
	val = val.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
	$(target).val(val);
}





$(function($){
	$('body').on('input', '#qw29', function(e){
		digits_float(this);
	});
	digits_float('#qw29');
});

$(function($){
	$('body').on('input', '#qw28', function(e){
		digits_float(this);
	});
	digits_float('#qw28');
});

$(function($){
	$('body').on('input', '#qw27', function(e){
		digits_float(this);
	});
	digits_float('#qw27');
});

$(function($){
	$('body').on('input', '#qw26', function(e){
		digits_float(this);
	});
	digits_float('#qw26');
});

$(function($){
	$('body').on('input', '#qw25', function(e){
		digits_float(this);
	});
	digits_float('#qw25');
});

$(function($){
	$('body').on('input', '#qw20', function(e){
		digits_float(this);
	});
	digits_float('#qw20');
});

$(function($){
	$('body').on('input', '#qw16', function(e){
		digits_float(this);
	});
	digits_float('#qw16');
});

$(function($){
	$('body').on('input', '#qw18', function(e){
		digits_float(this);
	});
	digits_float('#qw18');
});

$(function($){
	$('body').on('input', '#qw24', function(e){
		digits_float(this);
	});
	digits_float('#qw24');
});


$(function($){
	$('body').on('input', '#qw1', function(e){
		digits_int(this);
	});
	digits_int('#qw1');
});

$(function($){
	$('body').on('input', '#qw2', function(e){
		digits_int(this);
	});
	digits_int('#qw2');
});


$(function($){
	$('body').on('input', '#qw3', function(e){
		digits_int(this);
	});
	digits_int('#qw3');
});


$(function($){
	$('body').on('input', '#qw4', function(e){
		digits_int(this);
	});
	digits_int('#qw4');
});


$(function($){
	$('body').on('input', '#qw5', function(e){
		digits_int(this);
	});
	digits_int('#qw5');
});


$(function($){
	$('body').on('input', '#qw6', function(e){
		digits_int(this);
	});
	digits_int('#qw6');
});


$(function($){
	$('body').on('input', '#qw7', function(e){
		digits_int(this);
	});
	digits_int('#qw7');
});


$(function($){
	$('body').on('input', '#qw8', function(e){
		digits_int(this);
	});
	digits_int('#qw8');
});


$(function($){
	$('body').on('input', '#qw9', function(e){
		digits_int(this);
	});
	digits_int('#qw9');
});


$(function($){
	$('body').on('input', '#qw10', function(e){
		digits_int(this);
	});
	digits_int('#qw10');
});


$(function($){
	$('body').on('input', '#qw11', function(e){
		digits_int(this);
	});
	digits_int('#qw11');
});


$(function($){
	$('body').on('input', '#qw12', function(e){
		digits_int(this);
	});
	digits_int('#qw12');
});


$(function($){
	$('body').on('input', '#qw13', function(e){
		digits_int(this);
	});
	digits_int('#qw13');
});


$(function($){
	$('body').on('input', '#qw14', function(e){
		digits_int(this);
	});
	digits_int('#qw14');
});


$(function($){
	$('body').on('input', '#qw15', function(e){
		digits_int(this);
	});
	digits_int('#qw15');
});

$(function($){
	$('body').on('input', '#qw17', function(e){
		digits_int(this);
	});
	digits_int('#qw17');
});

$(function($){
	$('body').on('input', '#qw19', function(e){
		digits_int(this);
	});
	digits_int('#qw19');
});

$(function($){
	$('body').on('input', '#qw21', function(e){
		digits_int(this);
	});
	digits_int('#qw21');
});


$(function($){
	$('body').on('input', '#qw22', function(e){
		digits_int(this);
	});
	digits_int('#qw22');
});


$(function($){
	$('body').on('input', '#qw23', function(e){
		digits_int(this);
	});
	digits_int('#qw23');
});



