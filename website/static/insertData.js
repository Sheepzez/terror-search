
function insertDataData(dataMain) {
	var temp="";
	for (var key in dataMain) {
		temp = "<div id='"+key+"' class='small-10 columns'>"+dataMain[key]+"</div>";
		$("#col2").append(temp);
	}
	$("#col2").hide();
	}


function insertDataKeys(dataMain) {
	var temp="";
	var tick=0;
	for (var key in dataMain) {
		temp = "<button onclick='showDiv('"+key+"');' class='button'>" + key + "</button> <br>";
		if (tick==0) {
			document.getElementById("col0").innerHTML += temp;
			console.log(dataMain[key])
			tick=1; }
		else {
			document.getElementById("col1").innerHTML += temp;
			tick=0;
			}
		}
	}

function showDiv(key) { 
	$("#"+key).show();
}
