def add_sub():
    def add(a, b):
        print ("add:", a + b)
    def sub(a, b):
        print ("sub:", a - b)
    
    a = int(input())
    b = int(input())
    
    add(a, b)
    sub(a, b)