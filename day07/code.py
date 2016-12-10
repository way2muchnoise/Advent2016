import regex as re

lines = open('input.txt').readlines()
pattern_abba = r'(\w)(\w)\2\1'
pattern_aba = r'(\w)(\w)\1'
supports_TLS = 0
supports_SSL = 0
for line in lines:
    splitted = re.split('[\[\]]', line)
    net = splitted[0::2]
    hypernet = splitted[1::2]
    net_match = None
    i = 0
    while i < len(net) and (not net_match or net_match.group(1) is net_match.group(2)):
        net_match = re.search(pattern_abba, net[i])
        i += 1
    if net_match and net_match.group(1) is net_match.group(2):
        net_match = None
    net_aba = []
    for part in net:
        net_aba.extend(re.findall(pattern_aba, part, overlapped=True))
    hypernet_match = None
    i = 0
    while i < len(hypernet) and (not hypernet_match or hypernet_match.group(1) is hypernet_match.group(2)):
        hypernet_match = re.search(pattern_abba, hypernet[i])
        i += 1
    if hypernet_match and hypernet_match.group(1) is hypernet_match.group(2):
        hypernet_match = None
    hypernet_aba = []
    for part in hypernet:
        hypernet_aba.extend(re.findall(pattern_aba, part, overlapped=True))
    for aba in net_aba:
        if aba[0] is not aba[1] and (aba[1], aba[0]) in hypernet_aba:
            supports_SSL += 1
            break
    if not hypernet_match and net_match:
            supports_TLS += 1
print 'TLS ' + repr(supports_TLS)
print 'SSL ' + repr(supports_SSL)
