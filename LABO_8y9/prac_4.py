def val_list(lst):
    assert len(lst) > 0, "La lista esta vacia"
    print("La lista no esta vacia.")

listp = [1,2]
try:
    val_list(listp)
except AssertionError as er:
    print(er)