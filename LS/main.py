from classes import Node,Edge
from solver import Solver

def init_graph():
	"""
	"""
	n = ['u','x','y','v','w','z']
	e = ['uv','uw','vw','vx','ux','wx','xy','wy','wz','yz']
	e_l_node = ['u','u','v','v','u','w','x','w','w','y']
	e_r_node = ['v','w','w','x','x','x','y','y','z','z']
	w = [2,5,3,2,1,3,1,1,5,2]

	nb_node = len(n)
	nb_edge = len(e)

	E = {}
	for i in range(nb_edge):
		assert e[i] not in E.keys(), "{0} is in E".format(e[i])

		E[e[i]] = Edge(e[i], e_l_node[i], e_r_node[i], w[i])

	N = {}
	for i in range(nb_node):
		assert n[i] not in N.keys(), "{0} is in N".format(n[i])

		N[n[i]] = Node(n[i])

	for i in range(nb_edge):
		N[e_l_node[i]].insert_neigbors(e_r_node[i], w[i])
		N[e_r_node[i]].insert_neigbors(e_l_node[i], w[i])

	G = (N, E)
	return G

if __name__ == '__main__':
	G = init_graph()
	mySolver = Solver(G, verbose=True)
	#mySolver.print_graph()
	r_map = mySolver.LS_Routing('u')
	mySolver.print_routing_map(r_map)
