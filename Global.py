
# GLOBAL KEYWORD
count = 5       #Global Variable
def some_method():
    global count     #Global Keyword to call Global Variable
    count = count + 1
    local = 10      #Local Variable
    print(count)
    print(local)
some_method()

