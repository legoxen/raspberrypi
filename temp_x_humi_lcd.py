#-*- coding:utf-8 -*-
"""
Raspberry PiからDHT11センサーから’温度’、’気温’を取得して
Adafruit Char LCDパッケージを利用して16x2LCDに表示する
"""
import Adafruit_CharLCD as LCD
import Adafruit_DHT as DHT
from time import sleep
import os

# LCDと紐づいているGPIO番号で初期化する
lcd = LCD.Adafruit_CharLCD(
        26, # RS
        19, # E
        12, # D4
        25, # D5
        24, # 6
        23, # 7
        16, # LCDの列数
        2,  # LCDの行数
        2   # Backlight
        )

while True:
    try:
        # LCDをクリアしておく
        lcd.clear()
        # LCDの行を1行目に設定
        lcd.set_cursor(0, 0)
        # GPIOの4番からDHT11センサーの情報を取得
        humidity, temperature = DHT.read_retry(11, 4)
        # LCDの１行目に現在の気温を表示する
        lcd.message("Temp : %d C" % temperature)
        # LCDの行を２行目に設定
        lcd.set_cursor(0, 1)
        # 現在の2行目に現在の湿度を表示する
        lcd.message("Humi : %d %%" % humidity)
        # スリップ
        sleep(1)
    except KeyboardInterrupt:
        print("\nprocess close!")

        break

lcd.clear()
