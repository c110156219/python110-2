#座標及距離
x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
if x==0 and y==0:
    print("該點位於原點")
elif x==0 and y!=0:
    print("該點位於Y軸,離原點距離為根:",x**2+y**2)
elif x!=0 and y==0:
    print("該點位於X軸,離原點距離為根號",x**2+y**2)
elif x>0 and y>0:
    print("該點位於第一象限,離原點距離為根號",x**2+y**2)
elif x<0 and y>0:
    print("該點位於第二象限,離原點距離為根號",x**2+y**2)
elif x<0 and y<0:
    print("該點位於第三象限,離原點距離為根號",x**2+y**2)
elif x>0 and y<0:
    print("該點位於第四象限,離原點距離為根號",x**2+y**2)