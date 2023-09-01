import cv2                                               #OpenCVをインポート
import matplotlib.pyplot as plt                          #matplotlibをpltという名前でインポート

img_original = cv2.imread('Airplane.jpg')                #画像を読み込み(元の画像表示用)
img_trans = cv2.imread('Airplane.jpg')                   #画像を読み込み(画像変換用)
img_BitwiseNot = cv2.bitwise_not(img_original)           #画像をネガポジ反転

img_trans_blue_val = []                                  #変換後の青(blue)の画素値を格納するためのリストの宣言
img_trans_green_val = []                                 #変換後の緑(green)の画素値を格納するためのリストの宣言
img_trans_red_val = []                                   #変換後の赤(red)の画素値を格納するためのリストの宣言

img_BitwiseNot_blue_val = []                             #ネガポジ反転後の青(blue)の画素値を格納するためのリストの宣言
img_BitwiseNot_green_val = []                            #ネガポジ反転後の緑(green)の画素値を格納するためのリストの宣言
img_BitwiseNot_red_val = []                              #ネガポジ反転後の赤(red)の画素値を格納するためのリストの宣言

for i in range(img_BitwiseNot.shape[0]):                        #画像のy座標iを画像の高さの分img_BitwiseNotの配列の第１引数に入力
	for j in range(img_BitwiseNot.shape[1]):                    #画像のx座標jを画像の幅の分img_BitwiseNotの配列の第2引数に入力
		img_BitwiseNot_blue_val.append(img_BitwiseNot[i,j,0])   #ネガポジ反転後の青(blue)の画素値をimg_BitwiseNot_blue_valというリストに追加
		img_BitwiseNot_green_val.append(img_BitwiseNot[i,j,1])  #ネガポジ反転後の緑(green)の画素値をimg_BitwiseNot_green_valというリストに追加
		img_BitwiseNot_red_val.append(img_BitwiseNot[i,j,2])    #ネガポジ反転後の赤(red)の画素値をimg_BitwiseNot_red_valというリストに追加

for i in range(img_trans.shape[0]):                      #画像のy座標iを画像の高さの分img_transの配列の第１引数に入力
	for j in range(img_trans.shape[1]):                  #画像のx座標jを画像の幅の分img_transの配列の第２引数に入力
		Max = int(max(img_trans[i,j]))                   #BGRのリストの最大値の取得(型変換をしないと255まで行くと0になってしまう)
		Min = int(min(img_trans[i,j]))                   #BGRのリストの最小値の取得(型変換をしないと255まで行くと0になってしまう)
		total = Max+Min                                  #BGR値のリストの最大値とBGR値の最小値の和の計算
		img_trans[i,j,0] = total-img_trans[i,j,0]        #和から青(B)の値を引いてその値を新しい青(B)の値にする
		img_trans[i,j,1] = total-img_trans[i,j,1]        #和から緑(G)の値を引いてその値を新しい緑(G)の値にする
		img_trans[i,j,2] = total-img_trans[i,j,2]        #和から赤(R)の値を引いてその値を新しい赤(R)の値にする
		
		img_trans_blue_val.append(img_trans[i,j,0])      #新しい青(B)の値をimg_trans_blue_valというリストに追加
		img_trans_green_val.append(img_trans[i,j,1])     #新しい緑(G)の値をimg_trans_green_valというリストに追加
		img_trans_red_val.append(img_trans[i,j,2])       #新しい赤(R)の値をimg_trans_red_valというリストに追加

#img_originalの画像に「Original」という文字を描画
img_original = cv2.putText(img_original,text='Original',org=(0,25),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0,0,0),thickness=2,lineType=cv2.LINE_AA)
#img_transの画像に「Trans」という文字を描画
img_trans = cv2.putText(img_trans,text='Trans',org=(0,25),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0,0,0),thickness=2,lineType=cv2.LINE_AA)
#img_BitwiseNotの画像に「Bitwise Not」という文字を描画
img_BitwiseNot = cv2.putText(img_BitwiseNot,text='Bitwise Not',org=(0,25),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)

img_result = cv2.hconcat([img_original,img_trans,img_BitwiseNot])       #元の画像と変換後の画像を横に並べる
cv2.imshow("result",img_result)                                         #横に並べた画像を表示
cv2.imwrite("result.jpg",img_result)
cv2.waitKey()                                                           #window closeボタンが押されるまで待機

plt.hist(img_trans_blue_val,ec='black',label="Trans")                        #変換後の画素値に関するヒストグラムの設定(青(blue)について)
plt.hist(img_BitwiseNot_blue_val,ec='black',alpha=0.5,label="Bitwise Not")   #ネガポジ反転の画素値に関するヒストグラムの設定(青(blue)について)
plt.title('Blue')                                                            #タイトルの表示
plt.legend(loc='center',bbox_to_anchor=(0.8,1.08))                           #凡例の表示(グラフ外)
plt.show()                                                                   #ヒストグラムの表示

plt.hist(img_trans_green_val,ec='black',label="Trans")                       #変換後の画素値に関するヒストグラムの設定(緑(green)について)
plt.hist(img_BitwiseNot_green_val,ec='black',alpha=0.5,label="Bitwise Not")  #ネガポジ反転の画素値に関するヒストグラムの設定(緑(green)について)
plt.title('Green')                                                           #タイトルの表示
plt.legend(loc='center',bbox_to_anchor=(0.8,1.08))                           #凡例の表示(グラフ外)
plt.show()                                                                   #ヒストグラムの表示

plt.hist(img_trans_red_val,ec='black',label="Trans")                         #変換後の画素値に関するヒストグラムの設定(赤(red)について)
plt.hist(img_BitwiseNot_red_val,ec='black',alpha=0.5,label="Bitwise Not")    #ネガポジ反転の画素値に関するヒストグラムの設定(赤(red)について)
plt.title('Red')                                                             #タイトルの表示
plt.legend(loc='center',bbox_to_anchor=(0.8,1.08))                           #凡例の表示(グラフ外)
plt.show()                                                                   #ヒストグラムを表示