#!/usr/bin/python3
# SPDX-FileCopyRightText: 2023 Kazuki Noguchi
# SPDX-License-Identifire: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("%dh %dm %ds" % (msg.data/3600, (msg.data%3600)/60, (msg.data%3600)%60))

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "CountUp", cb, 10)
rclpy.spin(node)
