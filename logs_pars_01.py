import requests

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
r = requests.get(url).text.split('\n')


def pars():
    logs_tuple = []
    for line in r[:-1]:
        remote_addr = line.split(' - - ')[0].split('] "')
        request_type = line.split('] "')[1].split(' ')
        requested_resource = request_type[1].split(' HTTP')
        logs_tuple += [(remote_addr[0], request_type[0], requested_resource[0])]
    return logs_tuple


print((pars()))
