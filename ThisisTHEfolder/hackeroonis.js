function nanidaphuc() {
	var x = document.getElementsByClassName('paragraph');
	for(var i=0; i<x.length; i++){
		x[0].innerText = 'This line should not be here';
	}
}
