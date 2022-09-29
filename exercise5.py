#Input px
px = int(input("Enter the point px: "))

#Input py
py = int(input("Enter the point py: "))

#Input qx
qx = int(input("Enter the point qx: "))

#Input qy
qy = int(input("Enter the point qy: "))

#formula for rx and ry
rx = (qx - px) + qx
ry = (qy - py) +qy

#print output
print(f"r = ({rx}), ({ry}) ")