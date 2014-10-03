"""
-----------------------------
creates the correct object syntax for a lib2to3 subtree.
-----------------------------

The MIT License (MIT)

Copyright (c) <2014> <alex balzer>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

__author__ = "alex balzer <abalzer22@gmail.com>"

#ignore all '\s' and '\t' and '\n'
CHARS = { # should be able to supprt these dictioanry queries instead of the static `MATCH` string.
'[Wildcard(None,':[')',']'],
'[Wildcard(None,(':[')',')',']'],
}
found_siblings = []
go = 0
w = open('tree_output_file.py','w')
class sib(object):
	_sibs = {'[':']' , '{':'}' , '(':')'}
	def __init__(self,begin,typ):
		self.begin = begin
		self.typ = typ # '[' or '{' or '('
		self.end = None

def loop_chars(c,p,b,xyz,r):
	""" does a lookahead iteration to find if you have a pattern match """
	global go
	MATCH = '[Wildcard(None,('
	END_MATCH = '))]'
	j = 0
	# TODO: fix the issue with this only taking into account 1 of the paranthesis and it is swapping their proper ends
	for i in xrange(xyz[0],xyz[0]+len(MATCH)):#-1):
		print '*',r[i],MATCH[j],
		if r[i] != MATCH[j]:
			print '\n'
			return False
		elif r[i] == '(': # you need to create a new sib() object so that you can locate its sibling so that you can delete all the necessary characters to make the tree be the proper format.
			curr = sib(xyz[0]+j,'(')
			p.append(curr)
			# TODO: there needs to be a cleanup if this function returns False!!!
		j += 1
	go += len(MATCH)
	return True

def _check_char(c,p,b,xyz,r):
	""" c = char , p = paranthesis_stack , b = bracket_stack , <x,y,z> = placement in the file."""
	global found_siblings
	global go
	#<@>print 'p = ',p,'\nb = ',b
	# check to see if it is ok to write
	return_var = False
	if c == '(':
		# XXX: these are being added redundantly since you are appending in `loop_chars()`
		if check_go():
			p.append(c)
		return_var = True
	elif c == '[':
		if loop_chars(c,p,b,xyz,r): # if this returns true then you need to add a special marker to the paranthesis that will point to its opposite paranthesis. this opposite paranthesis will be the one that call the pop fo the method.
			b.append(sib(xyz[0],'['))
		else:
			b.append(c)
		return_var = True
	elif c == ')':
		if isinstance( p[len(p)-1] , sib ):
			#print '\n\n\nsibling\n\n\n'
			p[len(p)-1].end = xyz[0]
			found_siblings.append( p.pop() )
			#go += 1 #'
		else:
			p.pop()
		return_var = True
	elif c == ']':
		if isinstance( b[len(b)-1] , sib ):
			b[len(b)-1].end = xyz[0]
			found_siblings.append( b.pop() )
			#go += 1 #'
		else:
			b.pop()
		return_var = True
	if check_go():
		global w
		w.write(c)
	return return_var

def check_go():
	global go
	if go > 0:
		go -= 1
		return False
	elif go < 0:
		go = 0
	if go == 0:
		return True

def parse(r,return_stack=False,print_chars=False):
	global go
	pstack = []	# paranthesis stack
	bstack = []	# bracket stack
	a,b,c = 0,0,0
	if isinstance(r,list):
		for i in r:
			if isinstance(i,list):
				for j in i:
					for k in j:
						if not _check_char( k, pstack, bstack, (a,b,c), r ):
							if print_chars:
								print k,
						else:
							if print_chars:
								print k,(a,b,c)
						c += 1
					b += 1
			elif isinstance(i,str):
				for j in i:
					if not _check_char( j, pstack, bstack, (a,b,c), r ):
						if print_chars:
							print j,
					else:
						if print_chars:
							print j,(a,b,c)
					b += 1
			a += 1
	elif isinstance(r,str):
		for i in r:
			if not _check_char( i, pstack, bstack, (a,b,c), r ):
				if print_chars:
					print i,
			else:
				if print_chars:
					print i,(a,b,c)
			a += 1
	if return_stack:
		return pstack , bstack


def check_char(c,p,b):
	print 'p = ',p,'\nb = ',b
	if c == '(':
		p.append(c)
		return True
	elif c == '[':
		b.append(c)
		return True
	elif c == ')':
		p.pop()
		return True
	elif c == ']':
		b.pop()
		return True
	return False

if __name__ == "__main__":
	#_r = open('try_tree_flat.py','r').readlines()
	_r = open('try_tree_flat.py','r').read()
	#parse(_r)
	p,b = parse(_r,True)
	print 'p = ',p,'\nb = ',b,'\ngo = ',go,'\n\nsiblings = ' # these should be empty
	for i in found_siblings:
		print ( i.begin + 1 , i.end + 1 )

