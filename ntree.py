"""
-----------------------------
A basic n-tree implementation
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

class ntree(object):
	def __init__(self,root):
		self.root = root
		self.search_node = None

	def walk(self,cnode,do_print=True):
		if do_print:
			print str('  '*cnode.indent)+str(cnode.val)+' ->> '+str(hex(id(cnode)))
		if not cnode.children:
			return
		for i in cnode.children:
			self.walk(i)

	def search(self,cnode,val):
		q = [cnode]
		while q:
			curr = q.pop(0)
			print str('  '*curr.indent)+str(curr.val)+' ->> '+str(hex(id(curr)))
			if curr.val == val:
				return curr
			for i in curr.children:
				q.append(i)
		return None 

	def dsearch(self,cnode,val):
		print str('  '*cnode.indent)+str(cnode.val)+' ->> '+str(hex(id(cnode)))
		if cnode.val == val:
			return cnode
		if cnode.children:
			for i in cnode.children:
				self.dsearch(i,val)
		return None

	def insert(self,tnode,cnode,place=None):
		if place == None:
			cnode.children.append(tnode)
		elif isinstance(place,int):
			cnode.children.insert(place,tnode)

	def insert_v(self,tnode,cnode):
		if tnode.val <= cnode.val:
			if not cnode.children:
				cnode.children = [tnode]
				return
			for i in cnode.children:
				self.insert_v(tnode,i)

	def remove(self,cnode,val):
		if cnode.children:
			for i in xrange(len(cnode.children)):
				if cnode.children[i].val == val:
					cnode.children.pop(i)
					return True
			for i in cnode.children:
				self.remove(i,val)

	def update_nodes(self,cnode):
		if not cnode.children:
			return
		for i in cnode.children:
			i.parent = cnode
			i.indent = cnode.indent+1
			self.update_nodes(i)

class node(object):
	def __init__(self,val,children=[],parent=None,indent=0,siblings=[]):
		self.val = val
		self.parent = parent
		self.indent = indent
		self.children = children
		self.siblings = siblings

	def append_child(self,child):
		self.children.append(child)

	def insert_child(self,n,child):
		self.children.insert(n,child)

if __name__ == "__main__":
  # create root node
	root_node = node(45,[])
	# create n-tree
	tree = ntree(root_node)
	g = node(8,[node(12,[node(34,[]),node(46,[node(78,[])])]),node(15,[]),node(32,[node(88,[]),node(89,[])]),node(33,[]),node(34,[node(168,[]),node(99,[])])]) # get used to this syntax...
	# add a sub tree to the root node
	root_node.append_child(g)
	tree.walk(root_node)
	# add proper class info to all new nodes added to the root
	tree.update_nodes(root_node)
	print '-='*32
	# depth-first-search
	tree.walk(root_node)
	print '-='*32
	# breadth-first-search
	search_node = tree.search(root_node,78)
	print search_node
	g1 = node(865,[node(12345,[node(3465,[]),node(4996,[node(758,[])])]),node(1565,[]),node(3732,[node(8878,[]),node(8349,[])]),node(3223,[node(1,[]),node(2,[]),node(3,[node(4,[node(5,[node(6,[node(7,[node(8,[node(9,[])])])])])])])]),node(3114,[node(1658,[]),node(92349,[])])]) # get used to this syntax...
	search_node.append_child(g1)
	tree.update_nodes(root_node)
	tree.walk(root_node)
	print '-='*32
	tree.search(root_node,457982)
	print '-='*32
	print '\n\ndsearch\n\n'
	tree.dsearch(root_node,4537987)
	print '-='*32
	tree.remove(root_node,78)
	tree.walk(root_node)
#	print '-='*32
#	print '\n\ndsearch\n\n'
#	tree.dsearch(root_node,78)
