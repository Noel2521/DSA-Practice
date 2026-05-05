# def countdown(n):
#     if n == 0:
#         print("Done!")
#         return
#     print(n)
#     countdown(n-1)
# countdown(3)

def countup(current, max):
    print(current)           # print first
    if current == max:       # then check if we should stop
        print("Done!")
        return
    countup(current + 1, max)

countup(1, 3)