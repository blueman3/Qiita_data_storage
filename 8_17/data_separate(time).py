import os                                                                                             #ファイル操作のためにインポート
import datetime                                                                                       #ファイルの更新月日を取得するためにインポート
from tkinter import *                                                                                 #tkinterライブラリのすべてのモジュールをインポート
from tkcalendar import DateEntry                                                                      #tkcalendarの入力を取得するためにインポート

dir = "./python"                                                                                      #フォルダの指定

root=Tk()                                                                                             #tkinterのセットアップ
root.title("カレンダー")                                                                              #「カレンダー」という名前のウインドウを作成

date_form = DateEntry(locale='ja_JP')                                                                 #tkcalendarをデータ取得用のカレンダー形式の要素(ウィジェット)を作成(locale='ja_JP'と指定することで日本語形式で設定)

def func(event):                                                                                      #tkinterの処理関数を定義
	date_get = date_form.get_date()                                                                   #tkcalendarから日付を取得
	month = date_get.month                                                                            #date_get中の月(month)の部分を取得
	day = date_get.day                                                                                #date_get中の日(day)の部分を取得
	files=os.listdir(dir)                                                                             #「python」フォルダの中のすべてのファイル一覧を取得
	for file in files:                                                                                #すべてのファイルについて処理を実行
		date = datetime.datetime.fromtimestamp(os.path.getmtime(dir+"/"+file))                        #最終更新日時をタイムスタンプ形式で取得
		if ((date.month == month-1 and date.day > day) or (date.month == month and date.day <= day)):
			'''
			date中の月(date.month)がdate_get中の月(month)-1でありdate中の日(date.day)がdate_get中の日(day)より大きいか、date中の月(date.month)がdate_get中の月(month)であり
			date中の日(date.day)がdate_get中の日(day)以下である場合
			ex)
			「8」月「2」日と入力された場合 → 「7」月「3」日以降から「8」月「2」日まで
			※この処理だと順番に日付を指定しないとすべてのデータが指定した日付のフォルダに格納されてしまうという問題が発生する
			'''
			os.makedirs(dir+"/"+str(month)+"_"+str(day),exist_ok=True)                                #フォルダが存在しない場合には、指定した日付のフォルダを「python」フォルダの下に配置
			if(os.path.isfile(dir+"/"+file)):                                                         #上のフォルダがある場合に処理を実行
				os.rename(dir+"/"+file,dir+"/"+str(month)+"_"+str(day)+"/"+file)                      #条件に一致したファイル(指定した日付までのファイル)を作成したフォルダ
				                                                                                      #(指定した日付のフォルダ)の配下に移動させる

date_form.bind("<<DateEntrySelected>>",func)                                                          #tkcalendarでのカレンダーで任意の日付が押されたときに処理関数(func)を実行

date_form.pack()                                                                                      #カレンダー形式で作成したウィジェット(date_form)を画面上に配置

root.mainloop()                                                                                       #GUIの表示(この処理がないと一瞬表示されて消えるので表示されていないように見える)