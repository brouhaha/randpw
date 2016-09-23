#!/usr/bin/python3

import itertools
import random
import re

if True:
    # https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
    with open('eff_large_wordlist.txt', 'r') as f:
        lines = f.readlines()
        words = [l.split()[1] for l in lines]
else:
    with open('/usr/share/dict/words', 'r') as f:
        words = f.readlines()

if False:
    re_alpha = re.compile('^[a-z]+$')
    words = [w for w in words if re_alpha.match(w)]
         
print("%d words" % len(words))

punct = [chr(n) for n in itertools.chain(range(33, 65), range(91, 97), range(123, 127))]

w1 = random.choice(words)
p1 = random.choice(punct)
w2 = random.choice(words)

print('%s%s%s' % (w1, p1, w2))
