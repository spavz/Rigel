import sys
from random import shuffle

v = int(sys.argv[1])
e = int(sys.argv[2]) if len(sys.argv) > 2 else v - 1
n_partitions = int(sys.argv[3]) if len(sys.argv) > 3 else v
n_subgraphs = int(sys.argv[4]) if len(sys.argv) > 4 else v


adj_matrix = [[i+1 for i in range(e)] for x in range(v)]

for i in range(v):
	shuffle(adj_matrix[i])
print(adj_matrix)
with open('input0.dat', 'w') as f: 
	for i in range(v):
		f.write( '\t'.join( [ str( i % n_partitions), str(i), str((i % n_subgraphs) + 1)] ) + '\t')
		# f.write('0\t' + str(i) + '\t' + '1\t')
		for x in adj_matrix[i]:
			# f.write(str(x) + '\t1\t0\t')
			f.write( '\t'.join( [ str(x), str((x % n_subgraphs) + 1), str(x % n_partitions) ] ) + '\t')
		f.write('\n')
		# f.write('\t1\t0\t'.join(list(map(str,adj_matrix[i]))))
		# f.write('\t1\t0\t\n')

# 0		1	1	2   1	0
# 0		2   1	1	1	0

#p v s v s p

