#!/bin/bash

if [[ -n $5 ]];
then
	echo "cmd = $1"
	echo "container = $2"
	echo "DISPLAY = DISPLAY=:$3"
	echo "USB CAMERA = /dev/video$4"
	echo "option paramters = $5"
	echo 

elif [[ -n $4 ]];
then
	echo "cmd = $1"
	echo "container = $2"
	echo "DISPLAY = DISPLAY=:$3"
	echo "USB CAMERA = /dev/video$4"
	echo 
	
else
	echo "1st run, build, or echo"
	echo "2nd and container name"
	echo "3rd params for -e DISPLAY=:<?>" 
	echo "4th -device /dev/video<?>"
	echo "5th option parameter"
	exit 1
fi

run="run"
echo="echo"
build="build"

cmd="docker run -it --rm --gpus all -e DISPLAY=:$1 -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/argus_socket:/tmp/argus_socket --device /dev/video$2:/dev/video0 --network host $4 $3"

if [[ "$1" == "$echo" ]]; 
then
	echo "$cmd" 
	#"docker run -it --rm --gpus all -e DISPLAY=:$1 -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/argus_socket:/tmp/argus_socket --device /dev/video$2:/dev/video0 --network host $4 $3"

elif [[ "$1" == "$run" ]]; 
then
	$cmd
	#docker run -it --rm --gpus all -e DISPLAY=:"$1" -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/argus_socket:/tmp/argus_socket --device /dev/video"$2":/dev/video0 --network host "$4" "$3"

elif [[ "$1" == "$build" ]]; 
then
	echo "option is not yet ready for exec"

else
	echo "$1 not correct"

fi
