#!/usr/bin/perl
use strict;
use warnings;

my ( $s, $m, $h, $dt, $mo, $yr ) = localtime();
$yr += 1900;
$mo += 1;
my $now = sprintf(
	'%04d年%02d月%02d日%02d時%02d分%02d秒',
	$yr, $mo, $dt, $h, $m, $s
);

print "Content-Type: text/html; charset=UTF-8\n\n";
print <<"EOF";
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Hello</title>
</head>
<body>
<p>本ページが$nowをお知らせします</p>
</body>
</html>

EOF
