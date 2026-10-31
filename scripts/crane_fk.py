from spatialmath import SE3

def calposition(posarray): 
    # 各リンクの長さを変数として定義
 L1 = 0.0454+0.026
 L2 = 0.083
 L3 = 0.0935
 L4 = 0.045

 # 関節角度（例）
 theta1 = posarray[0]
 theta2 = posarray[1]
 theta4 = posarray[2]  #引数は関節情報の順番が一部入れ替わっている
 theta3 = posarray[3]  #引数は関節情報の順番が一部入れ替わっている
 thetah = posarray[4]

 # 各変換行列を作成
 # SE3.Rz(角度) でZ軸周りの回転、SE3(x, y, z) で平行移動（リンクの長さ）を表現
 # SE3.Ry(角度) でy軸周りの回転、SE3.Rx(角度) でx軸周りの回転
 T0_1 = SE3.Rz(theta1) * SE3(0, 0, L1)  # 基準座標から関節1への変換
 T1_2 = SE3.Rx(theta2) * SE3(0, 0, L2)  # 関節1からエンドエフェクタ（リンク2）への変換
 T2_3 = SE3.Rx(theta3) * SE3(0, 0, L3)  # 関節2からエンドエフェクタ（リンク3）への変換
 T3_4 = SE3.Rx(theta4) * SE3(0, 0, L4)  # 関節3からエンドエフェクタ（リンク4）への変換

 # 同次変換行列同士を掛け合わせることで、ベースから見たエンドエフェクタの全体行列を算出
 T_total = T0_1 * T1_2 * T2_3 * T3_4

 # ① 位置 (X, Y, Z) の取得
 position = T_total.t  # 配列 [x, y, z] が返る
 return position

