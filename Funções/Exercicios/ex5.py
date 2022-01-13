'''
V=(4*π*(r**3))/3
'''


def volume(raio):
    v = (4*3.14*(raio**3))/3
    print('Volume: ', v)


r = volume(float(input("Raio: ")))
