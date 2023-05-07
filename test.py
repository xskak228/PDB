page = 1
elements = 13
max = elements / 10
print(max)
if max > round(max):
    max = round(max) + 1
else:
    max = round(max)
elem = min(elements - (page - 1) * 10, 10)
print(page)
print(max)
print(elem)