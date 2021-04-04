logs_tuple = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as log:
    for line in log:
        line = line.split()
        logs_tuple.append((line[0], line[5].strip('"'), line[6]))
print(logs_tuple)
