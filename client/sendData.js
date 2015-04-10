//Function for sending data.
pos = {
    x: 0,
    y: 0
}	

var sendRequest = function(e){
	//console.log(arr.x);
	//var t = arr.x.toString() + arr.y.toString();
	//console.log(t);
	var ajaxRequest = new XMLHttpRequest();
	ajaxRequest.open("POST", "http://127.0.0.1:800/sendData/" + e, true);
	ajaxRequest.send();
	console.log("Data sent.")
	/*
	var t = ""
	for (var i = 0; i < arr.length; i++) {
		t += arr[i].x.toString() + "," + arr[i].y.toString() + "C";
	}
	t = t.slice(0,-1);
    var ajaxRequest = new XMLHttpRequest();
    ajaxRequest.open("POST", "http://127.0.0.1/sendData/" + t, true);
	ajaxRequest.send();
	console.log("Send.")*/
}


onmessage = function(e) {
  sendRequest(e.data);
}

