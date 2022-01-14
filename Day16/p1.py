def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

hexbin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111' }
packets = ''.join(hexbin[i] for i in input('Day16/in.txt')[0])

ans = []

def packetize(code):
    version = int(code[:3], 2)
    code = code[3:]
    ans.append(version)
    
    typeid = int(code[:3], 2)
    code = code[3:]
    if typeid != 4:
        ltid = code[0]
        code = code[1:]
        if ltid == '1':
            num_packets = int(code[:11], 2)
            code = code[11:]
            for _ in range(num_packets):
                code = packetize(code)
        else:
            length = int(code[:15], 2)
            code = code[15:]
            subpackets = code[:length]
            while subpackets:
                subpackets = packetize(subpackets)
            code = code[length:]
    else:
        while code[0] == '1':
            code = code[5:]
        code = code[5:]
    
    return code

packetize(packets)
print(ans, sum(ans))