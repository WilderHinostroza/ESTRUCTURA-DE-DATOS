def contwh(b):
    cont=0
    while cont<b:
        cont+=1
    assert cont>0,"el ciclo while no se ejecuto ni una vez"
    print("el ciclo while se ejecuto al menos una vez")
       
try:
       contwh(1)
except AssertionError  as er:
    print(er)