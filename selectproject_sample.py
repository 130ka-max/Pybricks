# -*- coding: utf-8 -*-
# プロジェクト選択システム - タッチセンサー版
# 左右ボタンでプロジェクトを選択し、Cポートのタッチセンサーで実行する

# 必要なライブラリのインポート
from pybricks.hubs import PrimeHub         # SPIKE Prime本体を制御するためのクラス
from pybricks.parameters import Button, Port  # ボタンとポート定数
from pybricks.pupdevices import TouchSensor   # タッチセンサーを制御するためのクラス
from pybricks.tools import wait              # 待機処理を行うための関数

# ハードウェア機器のインスタンス作成
# SPIKE Prime本体のインスタンス形成
hub = PrimeHub()

# Cポートに接続されたタッチセンサーのインスタンス作成
# このタッチセンサーを押すことで選択されたプロジェクトが実行される
touch_sensor = TouchSensor(Port.C)

# プロジェクトの識別名
# 選択可能なプロジェクトの一覧（新しいプロジェクトを追加する場合はここに名前を追加）
projects = ["A", "B", "C"]
# プロジェクト選択インデックス（現在選択されているプロジェクトの番号）
index = 0

# 画面の更新関数
# 選択中のプロジェクトを画面に表示する
def screenUpdate(index):
    hub.display.clear()  # 画面をクリア
    hub.display.text("SELECT:")  # 選択中であることを表示
    wait(500)  # 表示切り替えのため少し待つ
    hub.display.text(projects[index])  # 現在選択されているプロジェクト名を表示

# 各プロジェクトの関数定義
# 実際のプロジェクトの処理内容をここに記述する
def A():
    hub.display.clear()  # 画面をクリア
    hub.display.text("Running A")  # プロジェクトA実行中を表示
    wait(1000)  # デモ用に1秒待機（実際の処理に置き換える）

def B():
    hub.display.clear()  # 画面をクリア
    hub.display.text("Running B")  # プロジェクトB実行中を表示
    wait(1000)  # デモ用に1秒待機（実際の処理に置き換える）

def C():
    hub.display.clear()  # 画面をクリア
    hub.display.text("Running C")  # プロジェクトC実行中を表示
    wait(1000)  # デモ用に1秒待機（実際の処理に置き換える）

# プロジェクト実行関数
# 現在選択されているプロジェクトに対応する関数を実行する
def projectExecute(index):
    if projects[index] == "A":
        A()  # プロジェクトAの関数を実行
    elif projects[index] == "B":
        B()  # プロジェクトBの関数を実行
    elif projects[index] == "C":
        C()  # プロジェクトCの関数を実行
    # 新しいプロジェクトを追加する場合は以下のように記述
    # elif projects[index] == "D":
    #    D()  # プロジェクトDの関数を実行
    # ...

# 初期画面表示
# プログラム開始時に現在選択されているプロジェクトを表示
screenUpdate(index)

# メインループ
# ユーザーの入力を常に監視し、適切な処理を実行
while True:
    # ボタン入力を検出
    buttons = hub.buttons.pressed()

    if Button.LEFT in buttons:
        # 左ボタンが押されたら前のプロジェクトに移動
        index = (index - 1) % len(projects)  # リストの最初に戻る（循環）
        screenUpdate(index)  # 画面を更新
        wait(300)  # 連続押しを防ぐための待機時間

    elif Button.RIGHT in buttons:
        # 右ボタンが押されたら次のプロジェクトに移動
        index = (index + 1) % len(projects)  # リストの最後から最初に戻る（循環）
        screenUpdate(index)  # 画面を更新
        wait(300)  # 連続押しを防ぐための待機時間

    elif touch_sensor.pressed():
        # タッチセンサーが押されたら、現在選択されているプロジェクトを実行
        projectExecute(index)
        screenUpdate(index)  # プロジェクト実行後に選択画面に戻す
        wait(300)  # 連続押しを防ぐための待機時間

    wait(50)  # メインループの処理間隔を調整（CPUの負荷を軽減）
