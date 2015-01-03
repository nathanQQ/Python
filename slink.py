class Node(object):
	def __init__(self, val = 0xFF):
		self.val = val
		self.next = None

class Slink(object):
	def __init__(self, inits = []):
		self.head = Node(0xFF)
		for each in inits:
			self.pushTail(each)
	
	## for non-cyclic list, the empty condition is .next == None
	def isempty(self):
		if self.head.next == None:
			return True
		else:
			return False
	def len(self):
		num = 0
		node = self.head.next
		if self.isempty():
			return 0
		while node != None:
			node = node.next
			num += 1
		return num
	
	def pushTail(self, val):  # o(n)
		node = self.head
		while node.next != None:
			node = node.next
		else:
			node.next = Node(val)

	def popTail(self):  # o(n)
		node = self.head
		if self.isempty():
			print "Cannot remove tail node in an empty list"
			return
		# find the last but 1 node
		while node.next.next != None:
			node = node.next
		else:
			node_ret = node.next
			node.next = None
			return node_ret

	def push(self, val):  # o(1)
		node = Node(val) 
		node.next = self.head.next
		self.head.next = node
	
	def pop(self):  # o(1)
		if self.isempty():
			print "Cannot remove head node in an empty list"
			return
		node = self.head.next
		node_ret = node
		self.head.next = node.next
		return node_ret

	# delete all nodes with val
	def deleteVal(self, val):
		node = self.head.next
		if self.isempty():
			print "Cannot delete node in an empty list"
			return
		while node != None:
			if node.val == val:
				if node.next == None:
					self.popTail()
				else:
					node.val = node.next.val
					node.next = node.next.next
					self.deleteVal(val)
			node = node.next
		else:
			return

	def reverse(self):
		if self.isempty():
			print "Cannot reverse an empty list"
			return		
		next_node = None
		prev_node = None
		node = self.head.next
		while node != None:
			next_node = node.next
			node.next = prev_node
			prev_node = node
			node = next_node
		else:
			self.head.next = prev_node

	def sort(self):
		pass

	def traverse(self):
		if self.isempty():
			print "Cannot travers an empty list"
			return
		node = self.head.next
		while node != None:
			print node.val,
			node = node.next
		print




init_nodes = [2,4,6,8,10,12,14,16,18,20]
slink = Slink(init_nodes)
slink.traverse()
print
#slink.traverse()
slink.reverse()
slink.traverse()



