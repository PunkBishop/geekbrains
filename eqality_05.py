src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
results = [src[i] for i in range(len(src)) if src[i] not in src[i + 1:] and src[i] not in src[:i]]
print(results)