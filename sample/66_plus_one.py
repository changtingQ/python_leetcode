def plus_one(ll_1: list):
    if ll_1[-1] < 9:
        ll_1[-1] = ll_1[-1] + 1
    else:
        for i in range(len(ll_1)-1, -1, -1):
            if ll_1[i] == 9:
                ll_1[i] = 0
                if i == 0:
                    ll_1.insert(0, 1)


    return ll_1

result = plus_one([1, 2, 4, 5, 6])
print(result)





















"----------------------answer-----------------------思路1"
def plusOne(digits):
    a = map(str, digits)
    b = int(''.join(a))
    c = str(b + 1)
    d = list(c)
    e = map(int, d)
    f = list(e)
    return f
    # return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))

# result = plusOne([9, 9, 9, 9, 9])
# print(result)
"----------------------answer-----------------------思路2"
def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
        else:
            digits[i] += 1
            break
    return digits

result = plusOne([9, 9, 9, 9, 9])
print(result)