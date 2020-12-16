#!/usr/bin/env python3


sections = open('input.txt').read().split('\n\n')

def make_range(expr):
	(l, h) = [int(n) for n in expr.split('-')]
	return range(l, h+1)

property_map = {}
rules = []
for r in [[i.strip() for i in r.split(':')] for r in sections[0].split('\n')]:
	ranges = r[1].replace('or', '').replace('  ', ' ').split(' ')
	rules.append([r[0], make_range(ranges[0]), make_range(ranges[1])])
	
tickets = [[int(n) for n in s.split(',')] for s in sections[2].split('\n')[1:]]
valid_tickets = list(filter(lambda t: all([any([num in r[1] or num in r[2] for r in rules]) for num in t]), tickets))

my_card = [int(num) for num in sections[1].split('\n')[1].split(',')]

i = 0
s = 1
matching = {}
while (len(property_map.keys()) < len(rules)):
	pi = [t[i] for t in valid_tickets]
	if matching.get(i) is None:
		matching[i] = list(filter(lambda rule: all([(p in rule[1] or p in rule[2]) for p in pi]), rules))
	matching[i] = list(filter(lambda m: m[0] not in property_map.keys(), matching[i]))
	if len(matching[i]) == 1:
		name = matching[i][0][0]
		property_map[name] = i
		if name.startswith('departure'):
			s *= my_card[i]
	i = (i + 1) % len(valid_tickets[0])
print(s)