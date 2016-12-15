import re

lines = open('input.txt').readlines()
input_pattern = re.compile('(\d+) .* (\d+)')
pass_pattern = re.compile('(\d+) .* (.*?) (\d+) .* (.*?) (\d+)')
bots = {}
passes = {}
outputs = {}
for line in lines:
    if line.startswith('value'):
        match = input_pattern.search(line)
        if match.group(2) in bots:
            bots[match.group(2)].append(match.group(1))
        else:
            bots[match.group(2)] = [match.group(1)]
    else:
        match = pass_pattern.search(line)
        passes[match.group(1)] = (
            match.group(3) if match.group(2) == 'bot' else '-' + match.group(3),
            match.group(5) if match.group(4) == 'bot' else '-' + match.group(5)
        )
print bots
print passes


def sort(bot, result):
    vals = sorted(bots[bot], key=lambda x: int(x))
    bots[bot] = []
    if vals[1] == '61' and vals[0] == '17':
        result.append(bot)
    hands = passes[bot]
    # Low
    if hands[0].startswith('-'):
        outputs[hands[0][1:]] = vals[0]
    elif hands[0] in bots:
        bots[hands[0]].append(vals[0])
    else:
        bots[hands[0]] = [vals[0]]
    # High
    if hands[1].startswith('-'):
        outputs[hands[1][1:]] = vals[1]
    elif hands[1] in bots:
        bots[hands[1]].append(vals[1])
    else:
        bots[hands[1]] = [vals[1]]
    # Recursive sort
    if not hands[0].startswith('-') and len(bots[hands[0]]) > 1:
        sort(hands[0], result)
    if not hands[1].startswith('-') and len(bots[hands[1]]) > 1:
        sort(hands[1], result)

result = []
start_bot = None
for num, vals in bots.iteritems():
    if len(vals) > 1:
        start_bot = num
        break
sort(start_bot, result)
print bots
print result
print int(outputs['0']) * int(outputs['1']) * int(outputs['2'])
