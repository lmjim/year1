def dupCt(s):
	if len(s) != 0:
		prev_char = s[0]
		dup_ct = 1
		high_ct = 1
	else:
		high_ct = 0
	for i in range(1, len(s)):
		if s[i] == prev_char:
			dup_ct += 1
		else:
			prev_char = s[i]
			if dup_ct > high_ct:
				high_ct = dup_ct
			dup_ct = 1
	return high_ct
'''
>>> dupCt('a')
1
>>> dupCt('ababab')
1
>>> dupCt('aabbaabb')
2
>>> dupCt('abcdc')
1
>>> dupCt('abccccccdef')
6
>>> dupCt('abccccc')
1
>>> dupCt('abbbbbbcc')
6
>>> dupCt('aaabbbbccccc')
4
>>> dupCt('aaaabc')
4
>>> dupCt('abc cc')
1
>>> dupCt('aa abc')
2
>>> dupCt(' ')
1
>>> dupCt('')
0
>>> dupCt('aAaA')
1
>>> dupCt('ddaddaddd')
2
>>> dupCt('aaa')
1
>>> dupCt('abbbb')
1
>>> dupCt('aabbbb')
2
>>> dupCt('bbbbbbbbbbb')
1
'''
