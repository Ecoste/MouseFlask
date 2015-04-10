//http://127.0.0.1:8000/testing.html

pos = {
    x: 0,
    y: 0
}	

var sendWorker = new Worker("http://127.0.0.1:8000/sendData.js");

mouseRecording = new Array();
document.addEventListener('mousemove', function(e){ 
	var p = pos;
	p.x = e.clientX || e.pageX; 
	p.y = e.clientY || e.pageY;
	//mouseRecording.push(p);
	//console.log("" + p.x + "," + p.y);
	sendWorker.postMessage("" + p.x + "," + p.y);
}, false);

