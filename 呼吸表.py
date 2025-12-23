import math
maxValue=65535/3  #最大亮度降低为65535/3
steps=256
gamma=2.2
print("static const uint16_t breath_table[]={")
for i in range(steps):
    angle=i/steps*math.pi*2-math.pi/2
    sin_value=(math.sin(angle)+1.0)/2.0
    gamaa_value=math.pow(sin_value,gamma)
    final_value=int(gamaa_value*maxValue+0.5)
    print(f"{final_value:3d},",end="")
    if (i+1)%16==0:
        print()
print("};")
    