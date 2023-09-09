import cv2                               #webカメラの幅と高さの取得、webカメラの映像を反転させるためにインポート
import numpy as np                       #γ変換の初期値を設定するためにインポート
import tkinter                           #γ変換をGUIで操作できるようにインポート
import PIL.Image,PIL.ImageTk             #OpenCVで得られた画像をTkinterで扱えるようにインポート

cap = cv2.VideoCapture(0)                #webカメラを設定

app = tkinter.Tk()                       #tkinterのセットアップ
app.title("画像明るさ調整")              #「画像明るさ調整」という名前のウインドウを作成
app.geometry(str(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))+"x"+str(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))                  #Tkinterのウインドウの初期サイズをwebカメラの幅×高さに設定

canvas = tkinter.Canvas(app,width=cap.get(cv2.CAP_PROP_FRAME_WIDTH),height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT))              #webカメラの映像を表示させる範囲の設定(大きさ：webカメラの幅×
                                                                                                                            #高さに設定)

canvas.pack()                                                                                                               #webカメラの映像を表示させる範囲の表示

var_scale = tkinter.DoubleVar()                                                                                          #Double(浮動小数点数(実数)型でスライドバーの値を取得

#最小値1.0、最大値3.0、刻み幅0.01、値がvar_scale、向きが横向き、背景色が青色、文字色が黄色、枠線の色が青色、目盛の間隔が0.1、長さがwebカメラの幅のスライドバーをappの(x=0,y=0)に設置
#夜間にプログラムを走らせ実装したところ3.0以上は必要ないと考えたため最大値3.0とした
scale = tkinter.Scale(app,from_=1.0,to=3.0,resolution=0.01,variable=var_scale,orient=tkinter.HORIZONTAL,bg='blue',fg='yellow',highlightbackground='blue',tickinterval=0.1,length=cap.get(cv2.CAP_PROP_FRAME_WIDTH)).place(x=0,y=0)

def gamma_trans(event=None):                        #Tkinterの関数の定義(関数の定義をすることで再帰的に処理を実行(こうすることでfor文でのループ処理ができるようになる))
	_,img = cap.read()                              #webカメラから1フレーム取得
	img = cv2.flip(img,1)                           #取得したフレームを左右反転
	gamma = var_scale.get()                         #スライドバーで設定した値を取得
	img2gamma = np.zeros((256,1),dtype=np.uint8)    #256行1列の値がすべて0のリストを作成(OpenCVの色空間の値の範囲は0～255の符号なし8bitの数値であるためdtypeにnp.uint8を指定)

	for i in range(256):                            #0～255まで処理を実行
		
		'''
		γ補正の式
		
		γ_new=255×(X/255)^(1/γ)
		
		γ_new:γ補正後の画素値
		X:ガンマ補正前の画素値
		γ:γ補正値
		
		をもとにルックアップテーブル(LUT)を作成
		'''
		
		img2gamma[i][0] = 255 * (float(i)/255) ** (1.0 /gamma)          #img2gammaの先頭の値に255×(iをfloat(浮動小数点数(実数)型に型変換)したもの/255)^(1.0/スライドバーで指定したγの値)
		                                                                #小数部分が切り捨てられた状態(整数)でimg2gammaが取得される(dtypeをnp.uint8にしているため)

	gamma_img = cv2.LUT(img,img2gamma)                                  #webカメラから得られたフレームをimg2gammaをルックアップテーブル(LUT)として画像処理

	app.img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(gamma_img, cv2.COLOR_BGR2RGB)))             #Tkinterのウインドウのwebカメラを表示させる範囲にgamma_imgを設定
	                                                                                                                    #PIL.Image.fromarrayで画像を指定(PillowとOpenCVの色空間が違うので
	                                                                                                                    #変換)
	canvas.create_image(0,0,image=app.img,anchor=tkinter.NW)                                                            #画像の座標を(0,0)(原点は画像の左上端)に表示する画像をapp.imgに
	                                                                                                                    #基準位置を画像の左上に設定
	app.after(1,gamma_trans)                                                                                            #1ms間隔でgamma_transを実行(この処理がないとリアルタイムなので
	                                                                                                                    #処理が重すぎて固まる)

gamma_trans()       #この部分がないとTkinter上にwebカメラからのリアルタイムの映像が表示されない(関数内でTkinterでの画像表示も組み込んでいるため)
app.mainloop()      #GUIの表示(この処理がないと一瞬表示されて消えるので表示されていないように見える)