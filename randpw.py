#!/usr/bin/env python3

# Random password generator
# Copyright 2016, 2019 Eric Smith <spacewar@gmail.com>
# SPDX-License-Identifier: GPL-3.0

# This program is free software: you can redistribute it and/or modify
# it under the terms of version 3 of the GNU General Public License
# as published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import itertools
import os
import random
import re
import sys

if True:
    # https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
    with open(os.path.join(sys.path[0],'eff_large_wordlist.txt'), 'r') as f:
        lines = f.readlines()
        words = [l.split()[1] for l in lines]
else:
    with open('/usr/share/dict/words', 'r') as f:
        words = f.readlines()

if False:
    re_alpha = re.compile('^[a-z]+$')
    words = [w for w in words if re_alpha.match(w)]
         
if False:
    print("%d words" % len(words))

punct = [chr(n) for n in itertools.chain(range(33, 65), range(91, 97), range(123, 127))]

w1 = random.choice(words)
p1 = random.choice(punct)
w2 = random.choice(words)

print('%s%s%s' % (w1, p1, w2))
