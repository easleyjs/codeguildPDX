#Sock Sorter
import random
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_counts = {
                'ankle':0,
                'crew':0,
                'calf':0,
                'thigh':0
}

random_socks = []

for i in range(0,100):
    random_socks.append(random.choice(sock_types))

for i in random_socks:
    sock_counts[i] += 1

for x in sock_counts.keys():
    if sock_counts[x] > 1:
        print("Duplicate sock type - %s [%s]" % (x,sock_counts[x]))
