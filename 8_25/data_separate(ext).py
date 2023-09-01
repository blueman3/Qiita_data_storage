import glob                                                                                 #正規表現を用いてフォルダにアクセスするためにインポート
import os                                                                                   #ファイル名の取得・ファイルの拡張子名の取得・フォルダの作成・ファイルの移動のためにインポート
from tkinter import filedialog

dir = filedialog.askdirectory()

path_list=glob.glob(dir+'/*_*/*')                                                           #正規表現を用いて各フォルダにアクセス(「文字の真ん中に＿がある」フォルダにアクセス)

for i in path_list:                                                                         #それぞれの「文字の真ん中に＿がある」フォルダについて処理を実行
	file = os.path.basename(i)                                                              #フォルダ内の拡張子ありのファイル名を取得
	name = os.path.splitext(file)                                                           #ファイル名の.について文字を分割(これで拡張子を取得)

	if name[1] == ".JPG" or name[1] == ".jpg" or name[1] == ".png" or name[1]==".mp4":      #拡張子が「.JPG」、「.jpg」、「.png」、「.mp4」の場合に処理を実行
	                                                                                        #(画像ファイルか動画ファイルの場合)
		os.makedirs(os.path.dirname(i)+"/結果・素材",exist_ok=True)                         #拡張子が「.JPG」、「.jpg」、「.png」、「.mp4」であるファイルがあるフォルダ内に
		                                                                                    #「結果・素材」フォルダを(ない場合に)作成
		if(os.path.isfile(i)):                                                              #「文字の真ん中に＿がある」フォルダの直下に拡張子が「.JPG」、「.jpg」、「.png」、「.mp4」
	                                                                                        #であるファイルがある場合に処理を実行
			os.rename(i,os.path.dirname(i)+"/結果・素材/"+file)                             #「文字の真ん中に＿がある」フォルダの直下にある拡張子が「.JPG」、「.jpg」、「.png」、「.mp4」
			                                                                                #であるファイルを「結果・素材」フォルダ内に移動

	if name[1] == ".py":                                                                    #拡張子が「.py」の場合に処理を実行
		os.makedirs(os.path.dirname(i)+"/ソースコード",exist_ok=True)                       #拡張子が「.py」であるファイルがあるフォルダ内に「ソースコード」フォルダを(ない場合に)作成
		if(os.path.isfile(i)):                                                              #「文字の真ん中に＿がある」フォルダの直下に拡張子が「.py」であるファイルがある場合に処理を実行
			os.rename(i,os.path.dirname(i)+"/ソースコード/"+file)                           #「文字の真ん中に＿がある」フォルダの直下にある拡張子が「.py」であるファイルを「ソースコード」
			                                                                                #フォルダ内に移動