<?php
	$arrJson = Array();
	$dir = '/home/stratoberry/data/gps/';
	$a = scandir($dir);
	$dir .= end($a)."/";
	$a = scandir($dir);
	array_shift($a);
	array_shift($a);
	foreach($a as $name){
		$path = $dir.$name;	
		$strJson = file_get_contents($path);
		$strJson = str_replace ("NaN" , 0 , $strJson);		
		$_arrJson_= (Array)json_decode($strJson);		
		array_push($arrJson, current($_arrJson_));
	}
	echo json_encode($arrJson);	
?>