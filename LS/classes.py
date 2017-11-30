class Node(object):
	"""
	"""
	def __init__(self, node_id):
		"""
		"""
		self.id = node_id
		self.neigbors = {}

	def insert_neigbors(self,neigbor_id, weight):
		"""
		"""
		assert neigbor_id not in self.neigbors.keys(),"{0} is in {1}'s neigbors".format(neigbor_id, self.id)
		assert weight >= 0,"{0}'s weight in {1}'s neigbors error".format(neigbor_id, self.id)

		self.neigbors[neigbor_id] = weight


class Edge(object):
	"""
	"""
	def __init__(self, edge_id, l_node, r_node, weight):
		"""
		"""
		self.id = edge_id
		self.l_node = l_node
		self.r_node = r_node

		assert weight > 0,"{0}'s weight error".format(edge_id)

		self.weight = weight
