def bad_function(x, y):
    z = x + y
    if z > 0:
        return 'positive'
    elif z < 0:
        return 'negative'
    else:
        return 'zero'

def another_bad_function():
    result = []
    for i in range(10):
        result.append(i * i)
    return result