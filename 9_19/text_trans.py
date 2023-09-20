import tkinter as tk
import re
import datetime

now = datetime.datetime.now()                                                           #テキストファイル生成時の日付を取得

path = './変換後文章'+'('+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+')'+'.txt'  #テキスト形式の指定


root = tk.Tk()                                                      #tkinterの初期化
root.geometry('300x300')                                            #tkinterで作ったGUI(rootの画面のサイズ指定)
root.title('test')                                                  #GUIのタイトルの設定

def func(event):                                                    #GUIの関数定義
	text = entry.get("1.0","end")                                   #テキストボックスからの文字列の取得(第1引数は何文字目から開始するか(今回は、1文字目からなので"1.0"と指定)第2引数は
	                                                                #何文字目まで取得するか(今回は、最後までなので"end"と指定))
	text_trans = re.sub(r"<\w*>|</\w*>|<\w*\s\w*=\"\w*\">",'',text) #正規表現で文字列から<>で囲まれた文字列と</>が含まれている文字列を削除(第1引数で正規表現で指定、第2引数で置き換える文字列、第3引数で対象の文字列を指定)
	with open(path,mode='w') as file:                               #fileという名前で書き込みモード('w')のpath('./text.txt')を開く
		file.write(text_trans.rstrip())                                      #text_transの文字列をpathのファイル(text.txt)に書き込む
	print("変換後:",text_trans)                                     #動作確認用(text_transの文字列をコマンドプロンプト上に出力)

entry = tk.Text()                                                   #テキストボックスの設定
entry.place(x=0,y=0,width=300,height=300)                           #テキストボックスをどの位置にどのくらいの大きさで表示するかを設定(第1引数にx座標(今回は、一番上なので0を指定)、
                                                                    #第2引数にy座標(今回は、一番上なので0を指定)、第3引数に幅(今回は、画面いっぱいに表示させたいのでgeometryで設定した値と
                                                                    #同値)、第4引数に高さ(今回は、画面いっぱいに表示させたいのでgeometryで設定した値と同値)

entry.bind('<Return>',func)                                         #エンターキーが押される(キーイベントが'<Return>'となる)と処理(funcの中身)を実行

root.mainloop()                                                     #GUIの表示(この処理がないと一瞬表示されて消えるので表示されていないように見える)