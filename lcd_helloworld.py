# -*- coding:utf-8 -*-
"""
Raspberry Piを利用して16x2のLCDディスプレイに「Hello world!」
文字列を表示する練習コードです。
"""
import time
import Adafruit_CharLCD as LCD

# LCDのPinの名前の変数にGPIO番号を格納する
rs, en, d4, d5, d6, d7 = 26, 19, 12, 25, 24, 23

# LCDの列数
columns = 16

# LCDの行数
rows = 2

# バックライト
backlight = 2

# LCD初期化
lcd = LCD.Adafruit_CharLCD(
        rs,
        en,
        d4,
        d5,
        d6,
        d7,
        columns,
        rows,
        backlight)

# メッセージを表示する
lcd.message('Hello World!')

# 10秒間待ち
time.sleep(10)

# LCDをクリアして終了
lcd.clear()

        
