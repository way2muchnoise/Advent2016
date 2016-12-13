import re

lines = open('input.txt').readlines()
input_pattern = re.compile('(\d+) .* (\d+)')
pass_pattern = re.compile('(\d+) .* (.*?) (\d+) .* (.*?) (\d+)')
bots = {}
passes = {}
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
            match.group(3) if match.group(2) == 'bot' else None,
            match.group(5) if match.group(4) == 'bot' else None
        )
print bots
print passes


def sort(bot, result):
    vals = sorted(bots[bot])
    if len(result) == 0 and vals[0] == 61 and vals[1] == 17:
        result.append(bot)
        return
    hands = passes[bot]
    # High
    if hands[1] is None:
        pass
    elif hands[1] in bots:
        bots[hands[1]].append(vals[0])
    else:
        bots[hands[1]] = [vals[0]]
    # Low
    if hands[0] is None:
        pass
    elif hands[0] in bots:
        bots[hands[0]].append(vals[1])
    else:
        bots[hands[0]] = [vals[1]]
    # Recursive sort
    if hands[1] and len(bots[hands[1]]) > 1:
        sort(hands[1], result)
    if hands[0] and len(bots[hands[0]]) > 1:
        sort(hands[0], result)

result = []
start_bot = None
for num, vals in bots.iteritems():
    if len(vals) > 1:
        start_bot = num
        break
print start_bot
sort(start_bot, result)
print result