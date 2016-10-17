import numpy
import sklearn.decomposition
import matplotlib.pyplot as plt
 
dim=2
data=numpy.loadtxt("test.csv", delimiter=",")
pca=sklearn.decomposition.PCA(dim)
result=pca.fit_transform(data)
plt.plot(result,'ro')
plt.show()
numpy.savetxt("result.csv", result, delimiter=",")