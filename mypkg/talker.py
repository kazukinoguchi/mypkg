# SPDX-FileCopyRightText: 2023 Kazuki Noguchi
# SPDX-License-Identifire: BSD-3-Clause

import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import String   #通信の型（16ビットの符号付き整数）

class Talker():          #ヘッダの下にTalkerというクラスを作成
    def __init__(self, node):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(String, "Comments", 10)
        #self.n = 0
        node.create_timer(0.01, self.cb)

    def cb(self):              #関数内のnやpubをtalkerのものに変更
        msg = String()
        #msg.data = self.n
        msg.data = input('Comments here: ')
        self.pub.publish(msg)
        self.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)      #オブジェクトを作成（__init__が実行される。）
rclpy.spin(node)            #実行（無限ループ）
