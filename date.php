<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Hello</title>
</head>
<body>
<p>本ページが<?php
date_default_timezone_set('Asia/Tokyo');
$now = date('Y年m月d日H時i分s秒', time());
echo $now;
?>をお知らせします</p>
</body>
</html>

