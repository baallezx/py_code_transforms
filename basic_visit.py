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

import ast
from _ast import *

class checker(ast.NodeVisitor):
	def __init__(self,edit_file):
		self.edit_file = edit_file

	def visit_Assert(self,node):	#0
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Assign(self,node):	#1
		node_stack.append(node)
		super(Visitor,self).generic_visit(node)	# walk tree
		return node

	def visit_Attribute(self,node):	#2
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_AugAssign(self,node):	#3
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_BinOp(self,node):	#4
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_BoolOp(self,node):	#5
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Break(self,node):	#6
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Bytes(self,node):	#7
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Call(self,node):	#8
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_ClassDef(self,node):	#9
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Compare(self,node):	#10
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Continue(self,node):	#11
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Delete(self,node):	#12
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Dict(self,node):	#13
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_DictComp(self,node):	#14
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Ellipsis(self,node):	#15
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Eq(self,node):	#62
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_ExceptHandler(self,node):	#16
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Exec(self,node):	#17
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Expr(self,node):	#18
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_ExtSlice(self,node):	#19
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_For(self,node):	#20
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_FunctionDef(self,node):	#21
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_GeneratorExp(self,node):	#22
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Global(self,node):	#23
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_If(self,node):	#24
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_IfExp(self,node):	#25
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Import(self,node):	#26
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_ImportFrom(self,node):	#27
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Index(self,node):	#28
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Lambda(self,node):	#29
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_List(self,node):	#30
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_ListComp(self,node):	#31
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Load(self,node):	#32
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Module(self,node):	#33
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Name(self,node):	#34
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Nonlocal(self,node):	#35
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Num(self,node):	#36
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Pass(self,node):	#37
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Print(self,node):	#38
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Raise(self,node):	#39
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Repr(self,node):	#40
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Return(self,node):	#41
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Set(self,node):	#42
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_SetComp(self,node):	#43
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Slice(self,node):	#44
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Starred(self,node):	#45
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Store(self,node):	#46
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Str(self,node):	#47
		node_stack.append(node)
		if node.s.strip().startswith('${') and node.s.strip().endswith('}'):
			for i in special_chars:
				if i in node.s.strip():
					return node
			found_import_string = False
			for i in dont_change:
				if i in node.s.strip():
					return node
			#<,.,>
			found_import_string = False
			for i in self.dma_edit.inputs:
				print '\n\ni = ',repr(i),'\nnode.s = ',repr(node.s)
				if i.lower().replace('${','').replace('}','').strip() == node.s.lower().replace('${','').replace('}','').strip():
					print 'found a non input node in the file ',this_curr_file,'\n\nsource = ',codegen.to_source(node)
					node.s = i
					found_import_string = True
			if not found_import_string:
				print '\n(\n',ast.dump(node),'\n)\n'
				node.s = ''
				return node
			#<,.,>
			print node.s.strip()
			dict_name = node.s.strip()
			for i in ['$','{','}']:
				dict_name = dict_name.replace(i,'')
			dict_name = dict_name.strip()
			temp_node = Subscript(value=Name(id='io_params',ctx=Load()),slice=Index(value=Str(s=dict_name)),ctx=Load())
			add_to_transform_dictionary( node , temp_node )
                elif '${' in node.s.strip() and '}' in node.s.strip():
			print node.s.strip()
                        a = node.s.index('${')
                        b = node.s.index('}')
                        if a < b:       # if '}' comes after '${' , there are special cases this does not account for.
                                print node.s
                                self.handle_report('a')
			userin = ''
			if not no_userin:
				userin = raw_input('\n\n\nPress any key to continue or type \'skip\' to avoid these notifactions:')
			if userin == 'skip':
				no_userin = True
			self.dma_edit.bad_files.append([self.dma_edit.filename,node.s,node.lineno,node.col_offset])
		super(Visitor, self).generic_visit(node)
		if temp_node != None:
			return temp_node
		else:
			return node

	def visit_Subscript(self,node):	#48
		node_stack.append(node)
		if found_Assign:
			curr_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Try(self,node):	#49
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_TryExcept(self,node):	#50
		node_stack.append(node)
		if found_If:
			curr_If_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_TryFinally(self,node):	#51
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Tuple(self,node):	#52
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_UnaryOp(self,node):	#53
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_While(self,node):	#54
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_With(self,node):	#55
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_Yield(self,node):	#56
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_YieldFrom(self,node):	#57
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_alias(self,node):	#58
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_arg(self,node):	#59
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_comprehension(self,node):	#60
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_stmt(self,node):	#Null
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_expr(self,node):
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_excepthandler(self,node):
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node

	def visit_withitem(self,node):	#61
		node_stack.append(node)
		super(Visitor, self).generic_visit(node)
		return node
