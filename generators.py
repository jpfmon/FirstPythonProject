
def gen(n):
    for x in range(n):
        z = yield x**2

g = gen(3)
print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except:
    print("no more")
print("***************")

for x in gen(3):
    print(x)

print(list(gen(3)))

text = "hola"
# next(text) # this doesn't work
text_iterable = iter(text)
next(text_iterable)
