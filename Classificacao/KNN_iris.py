from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

performance_values = {}
k = 1

while k <= 25:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    forecast = knn.predict(x_test)
    hits = metrics.accuracy_score(y_test, forecast)
    performance_values[k] = round(hits, 4)
    k += 1

#print(performance_values)

plt.plot(list(performance_values.keys()), list(performance_values.values()))
plt.xlabel('Valores de K')
plt.ylabel('Performance')
plt.show()


#species = knn.predict([[5.01, 6.98, 0.37, 7.28]])[0]

#print(iris.target_names[species])
