#!/bin/bash
# SPDX-FileCopyRightText: 2023 Kazuki Noguchi
# SPDX-License-Identifire: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '0h 0m 9s'
