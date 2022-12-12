
vertices = ["".join(x.split(' ')) for x in open('clustering_big.txt', 'r').read().split('\n')[1:-1]]

def invert(bit):
    if bit != '0' and bit != '1':
        raise ValueError
    return '1' if bit == '0' else '0'

def similar(v):
    out = []
    for i in range(len(v)):
        out.append(v[:i]+invert(v[i]) + v[i+1:])
        for j in range(i+1, len(v)):
            out.append(v[:i]+invert(v[i])+v[i+1:j]+invert(v[j])+v[j+1:])
    return out
 
heads = {}
for v in vertices:
    heads[v] = v
clusters = len(heads) 
#print clusters
for v in vertices:
    v_head = heads[v]
    while heads[v_head] != v_head:
        v_head = heads[v_head]

    for friend in similar(v):
        if heads.get(friend):
            head = heads[friend]
            while heads[head] != head:
                head = heads[head]
            if v_head != head:
                heads[head] = v_head
                clusters -= 1
print(clusters)
#16508



import csv as csv
import heapq as hp

# will find out whether this new edge starts a cluster of its own 
# or rather fuses two clusters or plainly gets added to a new cluster
# might modify the cluster set and thus it is returned
# is there a better data structure? this works but ...
def addNewEdgeToClusterSet(clusters,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	fuse =[]
	notFuse =[]
	
	for cluster in clusters:
		if doesEdgeBelongToCluster(cluster,edge):
			fuse.append(cluster);
		else:
			notFuse.append(cluster);


	if len(fuse)>0:
		clusters = notFuse;
		#merge the dictionaries
		if len(fuse)>1:
			f = {}
			for i in range(len(fuse)):
				f.update(fuse[i])
		else:
			f = fuse[0]
		f = addNodeToGraph(f,distance,n1,n2)
		clusters.append(f);
	else: 
		# edge should be added to a cluster of its own
		# doesn't seem to be in any cluster 
		C = {};
		C = addNodeToGraph(C,distance,n1,n2);
		clusters.append(C);



	return clusters


def doesEdgeBelongToCluster(cluster,edge):
	distance = edge[0];
	n1 = edge[1][0]
	n2 = edge[1][1]
	if(cluster.get(n1)==None and cluster.get(n2)==None):
		return False;
	else:
		return True;
	
def addNodeToGraph(G,distance,n1,n2):
	if G.get(n1)==None:
		G[n1] = [];
	G[n1].append((n2,distance))

	if G.get(n2) == None:
		G[n2] = [];
	G[n2].append((n1,distance))
	return G

# calculate hamming distance uaing strings
# converts each string to an array and calculates 
# distance by comparing each character
def hamming_distance(s1, s2):
	if s1 == s2:
		return 0
	sum = 0
	for ch1, ch2 in zip(s1, s2):
		if ch1 != ch2:
			sum = sum +1
			if sum >3:
				#exit early
				return sum
	return sum



					
f  = open('./clustering_big.txt', "r")
reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE)

# each vertext points to edges incident on it
G = {}; #hasmap,represents graph, each vertex is an index
		# each index has an array of vertexes
		#A : [(B,2),(C,3)]
		#B: [(A,2)]
		#C:[(A,3)]

clusters =[]; # we know size of clusters has to be 4 maximum


h =[];# heap that will store edges by distance
nodes = []; #nodes array

#read all nodes
for row in reader: 
	n1 = row[0]
	n1.strip()
	nodes.append(n1)	

# we really only need to calculate distances
# up to three, nodes that are further appart than that we can disregard
l = len(nodes)

# to use this you need to remove duplicates
for i in range(l):
	n1 = nodes[i]
	
	for j in range(i+1,l):
		n2 = nodes[j]
		distance = hamming_distance(n1,n2)
		if distance <=3:
			#print n1,n2,distance
			G = addNodeToGraph(G,distance,n1,n2);
			hp.heappush(h,(distance,[n1,n2]))

#now we have all data into a graph
size = len(G)
#print G

#nodes that we know will not be clustered
standAloneNodes = len(nodes)-len(G)

#print "stand Alone nodes"
#print standAloneNodes

#print " Created heap and graph";

actualNumberOfClusters = len(G);


distance = 0
maxDistance =3
#whether we are at the beginning or we have a distance less than minimum
while (len(clusters)==0 or distance <=maxDistance) and len(h)>0:
	startClusters = len(clusters)+len(G)
	edge = hp.heappop(h);
	clusters = addNewEdgeToClusterSet(clusters,edge)
	distance = edge[0];
	n1 = edge[1][0];
	n2 = edge[1][1];

	# delete nodes from main graph if pertains  which is the last cluster
	if (G.get(n1)!=None):
		del G[n1]		
	if (G.get(n2)!=None):
		del G[n2]
	endClusters = len(clusters)+len(G)
	if distance == maxDistance and startClusters >endClusters:
		finalClusters = startClusters
		break
	elif len(h)==0:
		finalClusters = endClusters



#print "last item joined two clusters, so max distance is 3 when we have"
#print finalClusters
#print "stand alone"
#print standAloneNodes
#print "total number of clusters"
#print standAloneNodes+finalClusters
exit()