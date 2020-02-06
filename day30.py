def ips_between(start, end):
    diff = [int(b) - int(a) for a,b in zip(start.split('.'), end.split('.'))]
    ip_sum = 0
    for i in diff:
        ip_sum *= 256
        ip_sum += i
    ip_sum += 1
    return ip_sum-1

# One line solution

from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))
