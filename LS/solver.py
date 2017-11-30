import csv
import sys

MAX_WEIGHT = 10000
class Solver(object):
	"""
	"""
	def __init__(self, G, verbose=True, save_file="state.csv"):
		"""
		"""
		self.verbose = verbose
		if verbose is True:
			csvFile = open(save_file, 'w', newline='')
			self.writer = csv.writer(csvFile)
		else:
			self.writer = None

		(N, E) = G
		self.N = N
		self.E = E
		self.nb_nodes = len(N)

		self.src_id = None
		self.step = 0
		self.N_ = []
		self.N_l = []
		self.N_l_ = []
		self.D = {}
		self.D_ = {}
		self.P = {}
		self.route_map = {}

	def print_graph(self):
		"""
		"""
		nb_node = len(self.N)
		nb_edge = len(self.E)

		print("N:")
		for n_id in self.N:
			print("id = {0} :".format(self.N[n_id].id))
			for neigbor_id in self.N[n_id].neigbors:
				print("n:  {0}\tw:  {1}".format(neigbor_id, self.N[n_id].neigbors[neigbor_id]))

		print("E:")
		for e_id in self.E:
			print("id = {0}".format(self.E[e_id].id))
			print("l:  {0}\tr:  {1}\tw:  {2}".format(
				self.E[e_id].l_node,self.E[e_id].r_node, self.E[e_id].weight))

	def print_routing_map(self, route_map):
		"""
		"""
		for i in route_map:
			(route, cos) = route_map[i]
			des_id = i

			str0 = "{0}:  ".format(des_id)
			nb_route_map = len(route)
			for i in range(nb_route_map):
				str0 = str0 + route[nb_route_map-i-1]

			print(str0)
			print("cos:  {0}".format(cos))
			print('\n')
			
	def LS_Routing(self, src_id):
		"""
		"""
		self._init_src(src_id)
		self._LS()
		self._routing_map()

		return self.route_map

	def _print_state0(self):
		"""
		"""
		str0 = []
		str0.append('step')
		str0.append("N'")
		for shift in range(len(self.N)-1):
			str0.append("D({0}),p({1})".format(self.N_l_[shift],self.N_l_[shift]))

		self.writer.writerow(str0)

	def _print_state(self):
		"""
		"""
		str0 = []
		str0.append(str(self.step))
		str0.append("".join(self.N_))
		for shift in range(len(self.N)-1):
			if(self.N_l_[shift] in self.N_l):
				if self.D[self.N_l_[shift]] == MAX_WEIGHT:
					str0.append("-")
				else:
					str0.append("{0},{1}".format(self.D[self.N_l_[shift]], self.P[self.N_l_[shift]]))
			else:
				str0.append("")

		self.writer.writerow(str0)

	def _init_src(self, src_id):
		"""
		"""
		self.src_id = src_id
		self.step = 0
		self.N_ = [src_id]
		self.N_l = [i for i in self.N.keys() if i != src_id]
		self.N_l_ = [i for i in self.N.keys() if i != src_id]
		self.D = {}
		self.D_ = {}
		self.P = {}
		self.route_map = {}
		for n in self.N_l:
			if n in self.N[src_id].neigbors.keys():
				self.D[n] = self.N[src_id].neigbors[n]
				self.D_[n] = self.N[src_id].neigbors[n]
				self.P[n] = src_id
			else:
				self.D[n] = MAX_WEIGHT
				self.D_[n] = MAX_WEIGHT
				self.P[n] = ""

		if self.verbose is True:
			self._print_state0()
			self._print_state()

	def _LS(self):
		"""
		"""
		while len(self.N_l) > 0:
			self.step += 1

			min_id = min(self.D_, key=self.D_.get)			
			self.N_.append(min_id)
			self.N_l.remove(min_id)

			for cur_id in self.N_l:
				if min_id in self.N[cur_id].neigbors.keys() and self.D[cur_id] > self.D[min_id]+self.N[cur_id].neigbors[min_id]:
					self.D[cur_id] =  self.D[min_id]+self.N[cur_id].neigbors[min_id]
					self.D_[cur_id] =  self.D_[min_id]+self.N[cur_id].neigbors[min_id]
					self.P[cur_id] = min_id

			self.D_[min_id] = MAX_WEIGHT
			if self.verbose is True:
				self._print_state()
			
	def _routing_map(self):
		"""
		"""
		for i in self.N_l_:
			cos = self.D[i]
			
			route = []
			cur_node = i
			while cur_node != self.src_id:
				route.append(cur_node)
				cur_node = self.P[cur_node]
			route.append(self.src_id)

			self.route_map[i] = (route, cos)







