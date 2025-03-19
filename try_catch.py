def m():
    m()
try:
    # 1//0 #ZeroDivisionError
    # a #nameError
    # "Hello "+5 # TypeError
    # val=dict({"a":1,"b":2})
    # val["c"]  #leads to KeyError
    # int("Abs")
    # leads to valueError
    print(list(__builtins__.__dict__.keys()))
    # if we use only class name __builtins__ we get errors
    m()
    # leads to recursionError
except Exception as e:
    print(f"error is belong to {type(e)}")

