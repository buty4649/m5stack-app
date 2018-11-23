# m5stack-app
M5Stackで遊ぶ
便利そうなのでMicro Pythonを使って遊んでいく

## ファームウェア

ファームウェアは以下にある。
https://github.com/m5stack/M5Cloud/tree/master/firmwares

ここにあるファームウェアはオンライン対応でm5cloudに接続するのを前提としてる。
逆にいうとオンラインではないと開発できない。
オフライン版は以下にある。
https://github.com/m5stack/M5Cloud/tree/master/firmwares/OFF-LINE

m5stackで始まるファイルがオフラインで、m5cloudがオンライン版

### psram

psramと名前についているファームウェアがある。
psramはRAM拡張版のM5Stack用のファームウェアらしい。
M5Stack FIREなんかがpsram対応している。
https://www.switch-science.com/catalog/3953/

### 書き込み

書き込みはesptoolを使う

```
$ pip install esptool

# flashの削除
$ esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

# ファームウェアの書き込み
$ esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash --flash_mode dio -z 0x1000 ~/Downloads/m5stack-20180516-v0.4.0.bin
```

## ソースコードの書き込み

M5StackをPCをにさすとUSBシリアルが生える。
そのUSBシリアルに対して接続を行なうとpythonインタープリタが立ち上がる。

```
$ screen /dev/ttyUSB0 115200
FreeRTOS running on BOTH CORES, MicroPython task started on App Core (1).

 Reset reason: Power on reset
    uPY stack: 19456 bytes
     uPY heap: 80000/10992/69008 bytes

MicroPython ESP32_LoBo_v3.2.16 - 2018-05-15 on M5Stack with ESP32
Type "help()" for more information.
>>>
```

この状態で `CTRL-E` を入力するとペーストモードになり貼り付けを行なうとmain.pyに書き込まれる。
ペーストモードから抜ける場合は `CTRL-D` を押す。

インタープリタモードで `CTRL-D` を押すとリセットがかかる。

### CLIを使ってソースを書き込みする

さすがに毎度USBシリアルを使って書き込むのは手間である。
CLIから書き込む場合は **adafruit-ampy(ampy)** を使うと便利。
なお、ampyというパッケージをインストールしようとすると全然別のパッケージがインストールされるので注意。

```
$ pip install adafruit-ampy
```

ampyではポートを `--port` で指定する必要があるが、`$AMPY_PORT`を設定すれば --portオプションは不要である。

```
$ export AMPY_PORT=/dev/ttyUSB0
```

