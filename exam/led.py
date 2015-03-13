# -*- coding:utf-8 -*-
# author zhuhp158101@gmail.com 2013.4.16
# use Tab indent 用TAB 缩进
''' print numbers like LED do'''

LED_CODE = {
	'1': '15',
	'2': '23457',
	'3': '23467',
	'4': '1346',
	'5': '12467',
	'6': '124567',
	'7': '236',
	'8': '1234567',
	'9': '123467',
	'0': '123567'
	}

PARTS = ['top', 'up', 'mid', 'down', 'bottom']

def num2code(strn):
	led_codes = [ LED_CODE[n] for n in strn ]
	print led_codes
	return led_codes

def print_top(codes, s):
	tops = []
	ch = ''
	for code in codes:
		if '2' in code:
			ch = '-' * s
		else:
			ch = ' ' * s
		ch = ''.join([' ', ch, ' '])
		tops.append(ch)
	tops.append('\n')

	return tops

def print_mid(codes, s):
	mids = []
	ch = ''
	for code in codes:
		if '4' in code:
			ch = '-' * s
		else:
			ch = ' ' * s
		ch = ''.join([' ', ch, ' '])
		mids.append(ch)
	mids.append('\n')

	return mids

def print_bottom(codes, s):
	bottoms = []
	ch = ''
	for code in codes:
		if '7' in code:
			ch = '-' * s
		else:
			ch = ' ' * s
		ch = ''.join([' ', ch, ' '])
		bottoms.append(ch)
	bottoms.append('\n')

	return bottoms

def print_up(codes, s):
	ups = []
	ch = ''
	for code in codes:
		if '1' in code:
			ch = '|' + s * ' '
		else:
			ch = ' ' * (s + 1)
		if '3' in code:
			ch += '|'
		else:
			ch += ' '
		ups.append(ch)
	ups.append('\n')

	return ups

def print_down(codes, s):
	downs = []
	ch = ''
	for code in codes:
		if '5' in code:
			ch = '|' + s * ' '
		else:
			ch = ' ' * (s + 1)
		if '6' in code:
			ch += '|'
		else:
			ch += ' '
		downs.append(ch)
	downs.append('\n')

	return downs

def translate(strn, s=4):
	codes = num2code(strn)
	top = ' '.join(print_top(codes, s))
	up = ' '.join(print_up(codes, s))
	mid = ' '.join(print_mid(codes, s))
	down = ' '.join(print_down(codes, s))
	bottom = ' '.join(print_bottom(codes, s))
	print ''.join([top, up*s, mid, down*s, bottom])

if __name__ == '__main__':
	import sys
	num = sys.argv[1]
	translate(num)

