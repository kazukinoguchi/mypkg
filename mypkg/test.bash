#!/bin/bash

cd $~/ros2_ws

#ros2 run mypkg listener
ros2 run mypkg talker | echo comment

