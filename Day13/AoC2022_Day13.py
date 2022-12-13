with open('input.txt') as f:
    packets = f.read()[:-1].split('\n\n')


def parse_packet_pair(packet_pair):
    left, right = packet_pair.split('\n')
    left, right = eval(left), eval(right)
    return left, right


def compare_packets(left, right):

    if type(left) != type(right):
        if type(left) == int:
            return compare_packets([left], right)
        elif type(right) == int:
            return compare_packets(left, [right])

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left == right:
            return None
        if left > right:
            return False

    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            try:
                if left[i] != right[i]:
                    if compare_packets(left[i], right[i]) is None:
                        continue
                    else:
                        return compare_packets(left[i], right[i])
            except IndexError:
                return False
        if len(left) < len(right):
            return True
    return False


index_sum = 0

for j, packet_pair in enumerate(packets):
    packet_1, packet_2 = parse_packet_pair(packet_pair)
    if compare_packets(packet_1, packet_2):
        index_sum += j + 1

print(f'The sum of the indices of pairs of packets which are already in the right order: {index_sum}.')

# Part 2

divider_packets='''[[2]]
[[6]]'''.split('\n')

packetlist = []

for packet_pair in packets:
    packet_1, packet_2 = parse_packet_pair(packet_pair)
    packetlist.append(packet_1)
    packetlist.append(packet_2)

for divider_packet in divider_packets:
    packetlist.append(eval(divider_packet))

for i in range(len(packetlist)):
    for j in range(len(packetlist)-i-1):
        if not compare_packets(packetlist[j], packetlist[j+1]):
            packetlist[j], packetlist[j+1] = packetlist[j+1], packetlist[j]


decoder_key = 1
for divider_packet in divider_packets:
    decoder_key *= packetlist.index(eval(divider_packet))+1

print(f'The decoder key for the distress signal is {decoder_key}.')

#%%
