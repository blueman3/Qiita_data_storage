#任意の関数の二接線の交点の座標を算出

#ライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt

#微分の定義でのhを定義
h = 10**(-4)

#関数上の任意の二点を定義
a = -2
b = 2

x = np.linspace(-10,10,1001)

#11行目～12行目で接線の交点を求めたい関数の宣言
def func(x):
	return x**2

'''7行目～8行目で定義したa,bでの微分係数の計算
微分係数の計算には中心差分を適用'''
dydx_a = (func(a+h)-func(a-h))/(2*h)
dydx_b = (func(b+h)-func(b-h))/(2*h)

y_a = dydx_a*x-dydx_a*a+func(a)
y_b = dydx_b*x-dydx_b*b+func(b)

'''交点のx座標を計算

          f(b)-f(a)-f'(b)b+f'(a)a
x_交点 =  ----------------------
               f'(a)-f'(b)

'''

x_inter = (func(b)-func(a)-dydx_b*b+dydx_a*a)/(dydx_a-dydx_b)

'''交点のy座標を計算

          (a-b)f'(a)f'(b)+f'(a)f(b)-f'(b)f(a)
y_交点 =  -----------------------------------
                     f'(a)-f'(b)

'''

y_inter = ((a-b)*dydx_a*dydx_b+dydx_a*func(b)-dydx_b*func(a))/(dydx_a-dydx_b)

print("f(a) = {:.3f}".format(func(a))) #コメントアウトを外すとx=aでのy座標が出力される
print("f'(a) = {:.3f}".format(dydx_a)) #コメントアウトを外すとx=aでの微分係数が出力される
print("f(b) = {:.3f}".format(func(b))) #コメントアウトを外すとx=bでのy座標が出力される
print("f'(b) = {:.3f}".format(dydx_b)) #コメントアウトを外すとx=bでの微分係数が出力される
print("x_inter = {:.3f}".format(x_inter)) #コメントアウトを外すと2つの接線の交点のx座標が出力される
print("y_inter = {:.3f}".format(y_inter)) #コメントアウトを外すと2つの接線の交点のy座標が出力される

print("(%f,%f)" % (x_inter,y_inter)) #コメントアウトを外すと2つの接線の交点の座標が出力される

plt.xlim(-10,10)  #x軸の表示範囲を制限
#plt.ylim(0,2) #y軸の表示範囲を制限
plt.plot(x,func(x)) #任意の関数のグラフを描画
plt.plot(x,y_a) #任意の関数のx=aでの接線を描画
plt.plot(x,y_b) #任意の関数のx=bでの接線を描画
plt.scatter(x_inter,y_inter) #2つの接線の交点を描画

#plt.plot(x,np.zeros(len(x))) #コメントアウトを外すとx=0の直線を描画
plt.show() #グラフ表示
