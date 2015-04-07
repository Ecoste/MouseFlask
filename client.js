	var mouseX = 0
	var mouseY = 0
	
	// create an new instance of a pixi stage
	var stage = new PIXI.Stage(0x000000);

	// create a renderer instance
	var renderer = new PIXI.WebGLRenderer(1600, 900);

	// add the renderer view element to the DOM
	document.body.appendChild(renderer.view);

        
	
	requestAnimFrame(animate);
	function animate() {
	    requestAnimFrame(animate);
	    renderer.render(stage);
	}
	
	indx = 0;
	
	var makeRequest = function(){
	   var ajaxFunction = function(){
	      if(ajaxRequest.readyState == 4){
			var pointsStr = ajaxRequest.responseText.split("C");
			indx = parseInt(pointsStr[pointsStr.length - 1]); //Why not indx += pointStr.length? Packets arrive at different time and indx went overboard.
			for (i = 0; i < pointsStr.length - 1; i++) {
				if(pointsStr[i] != ""){
					var points = pointsStr[i].split(",");
					
					mouseX = parseInt(points[0]);
					mouseY = parseInt(points[1]);
					
                                        var graphics = new PIXI.Graphics(); //Why create new graphics every time? PixiJS bugs out if I don't.
                                        graphics.lineStyle(1, 0xFFFFFF);
                                        stage.addChild(graphics);
					graphics.drawRect(mouseX,mouseY,1,1);
				}
			}
	      } 
	   }
	   
           var ajaxRequest = new XMLHttpRequest();
	   ajaxRequest.onreadystatechange = ajaxFunction;
           ajaxRequest.open("GET", "http://109.255.170.73/mouseCoord/" + indx, true);
	   ajaxRequest.send();
	}
	
	var interval = setInterval(function(){
	    makeRequest();
	}, 5);