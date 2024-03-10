def val_tip(tip,s):
        
    assert isinstance(tip,s),"los tipos de datos no son del mismo tipo de variable"
    print("los daos dadon son dle mismo tipo de variable")
    
try:
    tp=10
    val_tip("hola",int)
except AssertionError  as er:
     print(er)