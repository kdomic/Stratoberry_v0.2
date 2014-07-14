  <?php
	$arrJson = Array();
	$dir = '/home/stratoberry/data/temp/';
	$a = scandir($dir);	
	array_shift($a);
	array_shift($a);
	
	foreach($a as $name){
		$path = $dir.$name;
		//echo $path."</br>";
		$strJson = file_get_contents($path);
		$_arrJson_ = json_decode($strJson);		
		//array_push($arrJson, (string)$name => current($_arrJson_));		
		$n = substr($name,8,6);
		$arrJson[$n[0].$n[1].":".$n[2].$n[3].":".$n[4].$n[5]] = current($_arrJson_);
	}
		
  ?>  
<html>
  <head>

	
	
	
	<title>Temp</title>
	<!-- /home/kdomic/stratoberry/Adafruit_Python_BMP/examples/temp.json -->
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
	<div id="chart_div2" style="width: 900px; height: 500px;"></div>
	<div id="chart_div3" style="width: 900px; height: 500px;"></div>
  </body>
</html>

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Time', 'Temp'],
		  <?php $first = true; foreach($arrJson as $key => $val){ if(!$first) echo ","; echo "['".$key."',".$val[0]."]"; $first=false;} ?>
        ]);
        var options = {
          title: 'Temp'
        };
        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
		
		
		var data = google.visualization.arrayToDataTable([
          ['Time', 'Pressure', 'Sealevel Pressure'],
		  <?php $first = true; foreach($arrJson as $key => $val){ if(!$first) echo ","; echo "['".$key."',".$val[1].",".$val[3]."]"; $first=false;} ?>
        ]);
		
		var options = {
          title: 'Pressure'
        };
        var chart = new google.visualization.LineChart(document.getElementById('chart_div2'));
        chart.draw(data, options);
		
		
		
		
		var data = google.visualization.arrayToDataTable([
          ['Time', 'Altitude'],
		  <?php $first = true; foreach($arrJson as $key => $val){ if(!$first) echo ","; echo "['".$key."',".$val[2]."]"; $first=false;} ?>
        ]);
		
		var options = {
          title: 'Altitude'
        };
        var chart = new google.visualization.LineChart(document.getElementById('chart_div3'));
        chart.draw(data, options);
		
      }
    </script>