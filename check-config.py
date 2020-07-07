import re

def check_config(brand):
    keypair_list = prepare_keypairs(brand)
    print('list:', keypair_list)

    ##create file obj and read config file.
    foo = open('./config.device', 'r')
    #text = foo.read().strip().split('\n')
    text = foo.read().strip()
    print('###############################')

    ##check each interface.
    a_str = '^\/configure service.*%s.*ingress qos %s' % (keypair_list[0][0], keypair_list[0][1])
    print('checking ingress:', a_str)
    match_ingress = re.search(a_str, text)
    if match_ingress:
        print('ingress found')
    else:
        print('ingress not found')

    b_str = 'egress qos %s' % (keypair_list[1][1])
    print('checking egress:', b_str)
    match_egress = re.search(b_str, text)
    if match_egress:
        print('egress found', match_egress.group())
    else:
        print('egress not foud')

    return None

def prepare_keypairs(brand):
    key_pairs = []
    print('do checking config for device:', brand)
    f = open('./keys-mapped.txt', 'rU')
    for line in f:
        if not line.strip().startswith('#'):
            myline_list = line.strip().split(':')
            interface = myline_list[0]
            tmp = []
            if brand == 'nokia':
                key_value = myline_list[1]
                tmp.append(interface)
                tmp.append(key_value)
            if brand == 'cisco':
                key_value = myline_list[2]
                tmp.append(interface)
                tmp.append(key_value)
            key_pairs.append(tmp)
    f.close()
    return key_pairs

#print prepare_keypairs('cisco')
check_config('cisco')
