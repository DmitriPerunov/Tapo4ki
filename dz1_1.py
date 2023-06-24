def func(c):
    if c == c[::-1]:
        return True
    else:
        return False
    
print(func("helloworld"))