import numpy
import min_hashing

doc_num = 10
doc_size = 100
permutation_num = 50

doc_mat = numpy.random.randint(2,size=(doc_num,doc_size))
#doc_mat = numpy.array([[1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1]])
print '***********input doc:************'
print doc_mat

jaccard_mat = min_hashing.get_jaccard_mat(doc_mat)

sig_mat=min_hashing.min_hashing(doc_mat,permutation_num)

band_size = 5
band_num = permutation_num/band_size

hash_map = {}
for i in xrange(doc_num):
	for j in xrange(band_num):
		key = str(sig_mat[i][j*band_size : (j+1)*band_size])
		#print (key+str(i))
		if key in hash_map:
			if i not in hash_map[key]:				
				hash_map[key].append(i)
			else:
				pass
		else:
			hash_map[key] = [i]
for i in hash_map.items():
	print i

