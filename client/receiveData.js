pos = {
    x: 0,
    y: 0
}	

indx = 0;
var makeRequest = function(){
	var ajaxFunction = function(){
	    if(ajaxRequest.readyState == 4){
			var pointsStr = ajaxRequest.responseText.split("C"); //The co-ordinates are received in this form: "pointCpointCpointCpoint...pointCindex"
			indx = parseInt(pointsStr[pointsStr.length - 1]);
			
			var resultingPoints = new Array();
			for (i = 0; i < pointsStr.length - 1; i++) {
				if(pointsStr[i] != ""){
					var points = pointsStr[i].split(",");
					var point = pos;
					point.x = parseInt(points[0]);
					point.y = parseInt(points[1]);
					resultingPoints.push(point);
					postMessage(point);
				}
			}
	    } 
	}
	console.log("Requesting data.");
    var ajaxRequest = new XMLHttpRequest();
	ajaxRequest.onreadystatechange = ajaxFunction;
    ajaxRequest.open("GET", "http://127.0.0.1:800/receiveData/0=" + indx, true);
	ajaxRequest.send();
}

setInterval(function(){ 
				makeRequest();
			}, 100);