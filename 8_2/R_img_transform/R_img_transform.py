import cv2 #OpenCVをインポート
import matplotlib.pyplot as plt #matplotlibをpltという名前でインポート

h = 10**(-4) #中心差分のhの定義
blue_val=[] #青(B)の画素値を格納する配列の定義
green_val=[] #緑(G)の画素値を格納する配列の定義
red_val=[] #赤(R)の画素値を格納する配列の定義

img = cv2.imread('lena_std.jpg') #画像の読み込み

for i in range(img.shape[0]): #画像のy座標iを画像の高さの分imgの配列の第１引数に入力
	for j in range(img.shape[1]): #画像のx座標jを画像の幅の分imgの配列の第２引数に入力
		img[i,j,0]=0 #画像上にあるすべての青(B)の画素値を0にする
		img[i,j,1]=0 #画像上にあるすべての緑(G)の画素値を0にする
		img[i,j,2] = ((img[i,j,2]+h)**2-(img[i,j,2]-h)**2)/(2*h) #画像上にあるすべての赤(R)の画素値に中心差分を施す
		
		blue_val.append(img[i,j,0]) #blue_valに新しく14行目の計算結果を代入
		green_val.append(img[i,j,1]) #green_valに新しく値0を代入
		red_val.append(img[i,j,2]) #red_valに新しく値0を代入

cv2.imshow("tyuusinsabun",img) #処理結果を出力
cv2.waitKey() #window closeボタンが押されるまで待機

plt.figure(tight_layout=True) #ヒストグラムが重ならないように調整

plt.subplot(221,title="Blue") #2×2のグラフ領域の左上に青(B)のヒストグラムを表示
plt.hist(blue_val,ec='black') #青(B)のヒストグラムのグラフの枠線を黒(black)に設定
plt.subplot(222,title="Green") #2×2のグラフ領域の右上に緑(G)のヒストグラムを表示
plt.hist(green_val,ec='black') #緑(G)のヒストグラムのグラフの枠線を黒(black)に設定
plt.subplot(223,title="Red") #2×2のグラフ領域の左下に赤(R)のヒストグラムを表示
plt.hist(red_val,ec='black') #赤(R)のヒストグラムのグラフの枠線を黒(black)に設定
plt.show() #全体のヒストグラムを表示

cv2.imwrite('./R_img_transform.jpg',img) #R変換画像の保存
