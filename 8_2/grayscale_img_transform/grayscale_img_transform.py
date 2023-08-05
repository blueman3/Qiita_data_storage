import cv2 #OpenCVをインポート
import matplotlib.pyplot as plt #matplotlibをpltという名前でインポート

h = 10**(-4) #中心差分のhの定義
grayscale_val=[] #グレースケールの画素値を格納する配列の定義

img = cv2.imread('lena_std.jpg') #画像の読み込み
img_2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for i in range(img_grayscale.shape[0]): #画像のy座標iを画像の高さの分imgの配列の第１引数に入力
	for j in range(img_grayscale.shape[1]): #画像のx座標jを画像の幅の分imgの配列の第２引数に入力
		img_grayscale[i,j] = ((img_grayscale[i,j]+h)**2-(img_grayscale[i,j]-h)**2)/(2*h) #画像上にあるすべてのグレースケールの画素値に中心差分を施す
		
		grayscale_val.append(img_grayscale[i,j]) #graycale_valに新しくimg[i,j]の計算結果を代入

cv2.imshow("tyuusinsabun",img_grayscale) #処理結果を出力
cv2.waitKey() #window closeボタンが押されるまで待機

plt.hist(grayscale_val,ec='black') #グレースケールのヒストグラムを表示
plt.show()

cv2.imwrite('./grayscale_img_transform.jpg',img_grayscale)