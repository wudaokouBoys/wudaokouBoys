$('#ModifyInfo').click(function(){
	window.location.assign('/modifyInfo');
})

$('#ModifyPassword').click(function(){
	window.location.assign('/modifyPassword');
})

$('#VerifyUser').click(function(){
	window.location.assign('/manageUser');
})

$('#VerifyVideo').click(function(){
	window.location.assign('/manageVideo');
})

$('#UploadHistory').click(function(){
	window.location.assign('/uploadHistory');
})

$('#WatchHistory').click(function(){
	window.location.assign('/viewHistory');
})

$('#Search').click(function(){
	content = $('#searchBar').val()
	if (content != '')
		window.location.assign("/searchResult?condition=keyword; content=" + content);
})

$('#LogIn').click(function(){
	javascript:window.location.assign('/login')
})

$('#SignUp').click(function(){
	javascript:window.location.assign('/register')
})

$('#UploadVideo').click(function(){
	window.location.assign('/upload')
})

$('#LogOut').click(function(){
	document.cookie = 'id=0; path=/';
	window.location.assign('/')
})


$('#nav_bar').children().children().click(function(){
	if (this.id != 0){
		window.location.assign("/searchResult?condition=type; content=" + this.id);
	}else{
		window.location.assign('/')
	}
})

function imageError(e){
	$(e).attr('src', '/static/video_default.png')
}

pos = document.cookie.search('id=')
id = -1
if (pos != -1)
	id = parseInt(document.cookie.substring(pos+3).split(';')[0])
if (id <= 0){
	$('#user-option').css('display', 'none');
	$('#LogIn').css('display', 'block');
	$('#SignUp').css('display', 'block');
}else{
	$('#user-option').css('display', 'block');
	$('#LogIn').css('display', 'none');
	$('#SignUp').css('display', 'none');
	pos = document.cookie.search('name=');
	name = document.cookie.substring(pos+5).split(';')[0];
	pos = document.cookie.search('admin=');
	admin = parseInt(document.cookie.substring(pos+6).split(';')[0]);
	
	$('#UserName').text(decodeURI(name));
	$('#UserID').text('ID: ' + id);
	
	if (admin == 1){
		$('#VerifyUser').css('display', '');
		$('#VerifyVideo').css('display', '');
		$('#administrator').css('display', '');
	}else{
		$('#VerifyUser').css('display', 'none');
		$('#VerifyVideo').css('display', 'none');
		$('#Administrator').css('display', 'none');
	}
}
