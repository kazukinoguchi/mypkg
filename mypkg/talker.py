#!/usr/bin/python3
# SPDX-FileCopyRightText: 2023 Kazuki Noguchi
# SPDX-License-Identifire: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "CountUp", 10)
        self.n = 2
        node.create_timer(1.0, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
