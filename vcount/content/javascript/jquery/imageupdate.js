function reloadImage() {
var now = new Date();

var img = document.getElementById('myImage');

if(img!=null)
{
	var source = img.src.substring(0, img.src.indexOf('?'));
	img.src = source + '?' + now.getTime();
}

setTimeout('reloadImage()', 66);
}

setTimeout('reloadImage()', 1000);