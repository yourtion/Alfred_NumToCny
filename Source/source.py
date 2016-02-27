#encoding: utf-8

import NumToCny

def callback(strs):
	print('<?xml version="1.0"?>')
	print('<items>')
	print("  <item uid=\"octal\" valid=\"yes\" arg=\""+strs+"\">")
	print("    <title>"+strs+"</title>")
	print('    <subtitle>Copy to clipboard</subtitle>')
	print('    <icon>icon.png</icon>')
	print('  </item>')
	print('</items>')

callback(NumToCny.to_rmb_upper({query}))