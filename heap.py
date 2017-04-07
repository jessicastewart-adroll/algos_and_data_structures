class MinHeap(object):
	def __init__(self):
		self.heap = []

	def __repr__(self):
		return str(self.heap)

	def insert(self, data):
		self.heap.append(data)
		current = len(self.heap)-1
		while current > 0:
			parent = current//2
			if self.heap[current] < self.heap[parent]:
				self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
				current = parent
			else:
				return
	
	def delete_min(self):
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		delete_min = self.heap.pop()

		current = 0
		depth = 0
		while current < len(self.heap)-1:
			left = (depth*current)+1
			right = (depth*current)+2
			if left < len(self.heap) and self.heap[current] > self.heap[left]:
				self.heap[current], self.heap[left] = self.heap[left], self.heap[current]
				current = left
				depth += 1
			elif right < len(self.heap) and self.heap[current] > self.heap[right]:
				self.heap[current], self.heap[right] = self.heap[right], self.heap[current]
				current = right
				depth += 1
			else:
				return delete_min


min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(1)
min_heap.insert(15)
min_heap.insert(5)
min_heap.insert(4)
min_heap.insert(45)
print(min_heap)
min_heap.delete_min()
print(min_heap)
min_heap.delete_min()
print(min_heap)
min_heap.delete_min()
print(min_heap)
min_heap.delete_min()
print(min_heap)
min_heap.delete_min()
print(min_heap)
