def f1():
    return 10
def aseg(f,b):
    assert f==b,"el valor de la funcion no es el esperado"
    print("el valor fue el esperado")
try:
    aseg(f1(),0)
except AssertionError  as er:
    print(er)