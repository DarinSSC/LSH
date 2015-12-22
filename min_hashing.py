#encoding: utf-8
import numpy

def get_jaccard_mat(doc_mat):
	doc_num,doc_size = numpy.shape(doc_mat)
	jaccard_mat = numpy.zeros((doc_num,doc_num))
	for i in xrange(doc_num):
		for j in xrange(doc_num):
			jaccard_mat[i][j] = float(numpy.sum(numpy.equal(doc_mat[i],doc_mat[j])))/doc_size
	print '***********Jaccard matrix:*************'
	print jaccard_mat
	return jaccard_mat

def min_hashing(doc_mat,permutation_num):
	doc_num,doc_size = numpy.shape(doc_mat)
	
	#随机permutation_num个置换函数
	#permutation_num = 5
	permu_group = numpy.random.randint(1,size = (permutation_num,doc_size))
	for i in xrange(permutation_num):
		permu_group[i] = (numpy.random.permutation(doc_size))
	print '************Permutation Group:***********'
	print permu_group

	#使用permu_group对doc_mat进行hash,获得Signature Matrix
	sig_mat = numpy.random.randint(1, size=(doc_num,permutation_num))
	for i in xrange(permutation_num):
		for j in xrange(doc_num):
			shuffled_doc = doc_mat[j][permu_group[i]]
			sig_mat[j][i] = numpy.where(shuffled_doc == 1)[0][0]
	print '*************Signature Matrix:************'
	print sig_mat
	return sig_mat

if __name__ == '__main__':
	doc_num = 4
	doc_size = 10

	doc_mat = numpy.random.randint(2,size=(doc_num,doc_size))
	print '***********input doc:************'
	print doc_mat

	print '***********Jaccard matrix:*************'
	print get_jaccard_mat(doc_mat)

	min_hashing(doc_mat,5)

