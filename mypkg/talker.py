# SPDX-FileCopyRightText: 2023 Kazuki Noguchi
# SPDX-License-Identifire: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(String, "Comments", 10)
        node.create_timer(0.01, self.cb)

    def cb(self):
        msg = String()
        msg.data = input('Comments here: ')
        self.pub.publish(msg)

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
