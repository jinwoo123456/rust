print("hihihi")


x= 1.0
y= 10

print(str(x) + str(y))


THRESHOLD = 10

def is_big(n:int) -> bool:
    return n > THRESHOLD

if __name__ == '__main__':
    print(THRESHOLD)
    print(is_big(THRESHOLD))
    THRESHOLD = 5