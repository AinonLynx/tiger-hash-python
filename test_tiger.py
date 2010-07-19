import unittest
import sys
import os
import tiger

    
def round_helper(a, b, c, x, mul, new_a,new_b,new_c):
    ret_values = tiger.tiger_round(a,b,c,x,mul)

    assert ret_values["a"] == new_a, \
       "a failed: " + str(ret_values["a"]) + " != " + str(new_a) + "\n"
    assert ret_values["c"] == new_c, \
        "c failed: " + str(ret_values["c"]) + " != " + str(new_c) + "\n" 
    assert ret_values["b"] == new_b, \
        "b failed: " + str(ret_values["b"]) + " != " + str(new_b) + "\n"

def test_tiger_round():
    round_helper(13065445776871430898,17855811585246249540,518233413090174763, \
        12311797252403697916,7, \
        4821272432160810520,17424479681440429243,12532788606137106391)

def test_tiger_round2():
    round_helper(6280199717849618378, 8343645101657805456, 5997044206234503415, \
        12062177936022666431, 9, \
        11604645957211426640, 3986339792283275959, 17608143266212181064)

def test_tiger_round3():
    round_helper(11604645957211426640, 3986339792283275959, 17608143266212181064, \
        11490956213547313652, 9, \
        6441804261801137295,13333871996800360137,7720474646982516156)


"""
Results from reference:
A: 6280199717849618378
B: 8343645101657805456
C: 5997044206234503415
mul: 9
x0: 12062177936022666431
x1: 11490956213547313652
x2: 16829172008830410301
x3: 11899344311637024046
x4: 3757253942274655973
x5: 17835857420906997132
x6: 10787740079658512390
x7: 17590610739856314589
new A: 1509595445172618351
new B: 206383248218352883
new C: 2725617220977123037

"""
def test_tiger_pass():
    a =  6280199717849618378
    b =  8343645101657805456
    c =  5997044206234503415
    mul = 9
    data = [12062177936022666431, 11490956213547313652, 16829172008830410301, \
        11899344311637024046,  3757253942274655973, 17835857420906997132, \
        10787740079658512390,  17590610739856314589]

    ret_values = tiger.tiger_pass(a,b,c,mul, data)

    assert ret_values["a"] == 1509595445172618351, \
        "a failed, " + str(ret_values["a"]) + " != 1509595445172618351"
    assert ret_values["b"] == 206383248218352883, \
        "b failed, " + str(ret_values["b"]) + " != 206383248218352883"
    assert ret_values["c"] ==  2725617220977123037, \
        "c failed, " + str(ret_values["c"]) + " != 2725617220977123037"


def test_tiger_compress():
    x = [chr(1),chr(0),chr(0),chr(0),chr(0),chr(0),chr(0),chr(0)]
    r1 = 81985529216486895 
    r2 = 18364758544493064720
    r3 = 17336226011405279623

    values = tiger.tiger_compress(x,r1,r2,r3)
    assert values["r1"] == 2661648323708752690, \
        "r1 failed, " + str(values["r1"]) + "!= 2661648323708752690"
    assert values["r2"] == 1591580974389105247, \
        "r2 failed, " + str(values["r2"]) + "!= 1591580974389105247"
    assert values["r3"] == 17542609259623632506, \
        "r3 failed, " + str(values["r3"]) + "!= 17542609259623632506"




      
 
