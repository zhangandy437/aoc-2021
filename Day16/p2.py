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

def literal(typeid, vals):
    if typeid == 0:
        return sum(vals)
    if typeid == 1:
        ans = 1
        for num in vals: ans *= num
        return ans
    if typeid == 2:
        return min(vals)
    if typeid == 3:
        return max(vals)
    if typeid == 5:
        return int(vals[0] > vals[1])
    if typeid == 6:
        return int(vals[1] > vals[0])
    else:
        return int(vals[0] == vals[1])
    

def packetize(code):
    code = code[3:]
    typeid = int(code[:3], 2)
    code = code[3:]
    
    k = 0
    if typeid != 4:
        ltid = code[0]
        code = code[1:]
        vals = []
        if ltid == '1':
            num_packets = int(code[:11], 2)
            code = code[11:]
            for _ in range(num_packets):
                code, v = packetize(code)
                vals.append(v)
        else:
            length = int(code[:15], 2)
            code = code[15:]
            subpackets = code[:length]
            while subpackets:
                subpackets, v = packetize(subpackets)
                vals.append(v)
            code = code[length:]
        k = literal(typeid, vals)
    else:
        b = ''
        while code[0] == '1':
            b += code[1:5]
            code = code[5:]
        b += code[1:5]
        code = code[5:]
        k = int(b, 2)
    
    return code, k

print(packetize(packets))