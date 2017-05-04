
# -*- coding: utf-8 -*-
import random
from light import *
from Reader import *
from Sensor import *

def main():
    data = []#データ配列
    light = []
    sensor = []
    SENSOR_NUM = 97
    LIGHT_NUM = 15
    minlight = [0 for i in range(SENSOR_NUM)]
    minsensor = [0 for i in range(SENSOR_NUM)]
    COUNT = 100000
    Weight = 1
    cd = 1000.0#初期照明光度
    lx = 0.0
    hcd = 50.0
    flag = 0.0
    hlx = 0.0
    g = [0 for i in range(SENSOR_NUM)]
    data = reader()
    tcd = [cd for i in range(SENSOR_NUM)]
    # print data
    # print len(data)

    del data[0:16]
    c=0
    for i in range(SENSOR_NUM):
        c = i * LIGHT_NUM
        # print (data[c])
        del data[c]
    # print data

    #初期値設定
    for num in range(LIGHT_NUM):
        light.append(Light(num,cd,hcd))

    for num in range(SENSOR_NUM):
        sensor.append(Sensor(num,lx,hlx))

    #目標照度設定
    locationa = 9
    locationb = 17
    locationc = 96
    sensor[locationa].set_lx(500);
    sensor[locationb].set_lx(750);
    sensor[locationc].set_lx(800);
    # print light[0].hcd
    # print data[1]

    for i in range(LIGHT_NUM):
        minlight[i] = light[i].cd
    for i in range(SENSOR_NUM):
        minsensor[i] = sensor[i].lx
    #照明の値変更
    # Light.setcd(light[1])
    # print light[1].cd
    min =99999999

    #SHC
    for k in range(COUNT):
        #初期化
        for j in range(SENSOR_NUM):
            sensor[j].lx =0
        P = 0
        s = 0

        for i in range(LIGHT_NUM):
            light[i].cd = minlight[i] * random.uniform(0.92,1.06)
            # print (random.uniform(0.92,1.06))
        #照度，光度変換
        for j in range(SENSOR_NUM):
            if j ==locationa or j == locationb or j == locationc:
                for i in range(LIGHT_NUM):
                    sensor[j].lx += light[i].cd * float(data[i+LIGHT_NUM*j])

        for i in range(SENSOR_NUM):
            if i ==locationa or i == locationb or i == locationc:
                tmp = (sensor[i].lx - sensor[i].hlx)
                if tmp >= 0:
                    g[i] = 0
                else:
                    g[i] =  tmp * tmp
            # print(i)
            # print (g[i])

                for j in range(LIGHT_NUM):
                    P += light[j].cd
                for j in range(SENSOR_NUM):
                    s += g[j]
                f = P + Weight * s

                # print (f)

        if min>f:
            min = f
            for i in range(LIGHT_NUM):
                minlight[i] = light[i].cd
            for i in range(SENSOR_NUM):
                minsensor[i] = sensor[i].lx

    # print (min)

    # 最小値の時のセンサと照明の値
    for i in range(LIGHT_NUM):
        print ('照明{0}：{1}cd'.format(i,minlight[i]))
    for i in range(SENSOR_NUM):
        if i ==locationa or i == locationb or i == locationc:
            print('センサ{0}：照度{1}Lx'.format(i,minsensor[i]))

if __name__=='__main__':
    main()


# print list[1]
# for w in list:
#     print (w)
