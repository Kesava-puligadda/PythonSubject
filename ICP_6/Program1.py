########## Importing libraries below  #####
import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

######### Load the data ##########

Credit_Card_Data = pd.read_csv('CC.csv')
Credit_Card_Data.head()

######### Finding the unique values #########

Credit_Card_Data['TENURE'].value_counts()

#######  Find any null values in data  #######

Credit_Card_Data.isnull().sum()

###### get mean of values in minimum payments #######

mean_value=Credit_Card_Data['MINIMUM_PAYMENTS'].mean()
print('Mean value or column MINIMUM_PAYMENTS is :', mean_value)

####### Replace Null in column with the mean of values in the same column ########

Credit_Card_Data['MINIMUM_PAYMENTS'].fillna(value=Credit_Card_Data['MINIMUM_PAYMENTS'].mean(), inplace=True)
Credit_Card_Data.isnull().sum()

###### get mean of values in column CREDIT_LIMIT ######

mean_value_CREDIT_LIMIT=Credit_Card_Data['CREDIT_LIMIT'].mean()
print('Mean value or column CREDIT_LIMIT is :', mean_value_CREDIT_LIMIT)

##### Replace Null in column CREDIT_LIMIT with the mean of values in the same column ######

Credit_Card_Data['CREDIT_LIMIT'].fillna(value=Credit_Card_Data['CREDIT_LIMIT'].mean(), inplace=True)
Credit_Card_Data.isnull().sum()

########### Splitting data into x, y  ##############

x = Credit_Card_Data.iloc[:,1:]
print('shape of x is : ' ,x.shape)
----------------------------------------------------
y = Credit_Card_Data.iloc[:,-1]
print('shape of y is : ' ,y.shape)

########## elbow method for clusters #############

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
-------------------------------------------------
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

############ elbow method to know the number of clusters ##########

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
--------------------------------------------------
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

############ @ Silhouette score @###################

nclusters = 3 # this is the k in kmeans , from above graph
km = KMeans(n_clusters=nclusters)
km.fit(x)


########### predict the cluster for each data point ##########

y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print()
print('Silhouette score when k = 3 is :',score)

