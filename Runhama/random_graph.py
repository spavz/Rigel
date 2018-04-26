import sys
from random import shuffle

v = int(sys.argv[1])

adj_matrix = [[i+1 for i in range(v)] for x in range(v)]

for i in range(v-1):
	adj_matrix[i][i] = adj_matrix[i+1][i+1]
	shuffle(adj_matrix[i])
# adj_matrix[v-1][v-1] = 0

with open('input0.dat', 'w') as f: 
	for i in range(v):
		f.write('0\t' + str(i) + '\t' + '1\t')
		f.write('\t1\t0\t'.join(list(map(str,adj_matrix[i]))))
		f.write('\t1\t0\t\n')

# 0		1	1	2   1	0
# 0		2   1	1	1	0

#p v s v s p

