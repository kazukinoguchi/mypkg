# mypkg
このレポジトリは、Talkerを起動してから経過した時間ををListenerで受信し、表示するものです。

[![test](https://github.com/kazukinoguchi/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kazukinoguchi/mypkg/actions/workflows/test.yml)

## 必要なソフトウェア
* Python
 * テスト済み: 3.7 ~ 3.10
* ROS2

## テスト環境
Ubuntu-20.04

## インストール方法
**このレポジトリを使用するには、ROS2をインストールしていることが前提となっています。あらかじめ確認をお願いいたします。**
1. 各自のROS2ワークスペースに移動します。
1. 以下のコマンドで、このパッケージをダウンロードします。  
`git clone https://github.com/kazukinoguchi/mypkg`

## 実行方法
1. 各自のROS2ワークスペースに移動します。
1. コマンドを打ち込み実行します。
   * Talkerの実行コマンド  
   `ros2 run mypkg talker`  
   * Listenerの実行コマンド  
   `ros2 run mypkg listener`  
   * TalkerとListenerを同時に実行するコマンド  
   `ros2 launch mypkg talk_listen.launch.py`  
1. Ctrl + Cでプログラムを終了させます。

## 実行例
* Talker  
Talkerは起動しても何も表示されません。  
* Listener  
```
[INFO] [1703394981.576107110] [listener]: 0h 0m 1s
[INFO] [1703394982.567102112] [listener]: 0h 0m 2s
[INFO] [1703394983.567053465] [listener]: 0h 0m 3s
```
* TalkerとListenerを同時に実行
## 著作権・ライセンス表示
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージは，Ryuichi Ueda由来のコード（© 2022 Ryuichi Ueda）を利用しています．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身が編集し、自身の著作としたものです．
    * https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/
    * https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/
    * https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/
    * https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/
* © 2023 Kazuki Noguchi
