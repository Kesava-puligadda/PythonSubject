import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

############### Loading the data ###################

Credit_Card_Data = pd.read_csv('CC.csv')
Credit_Card_Data.head()

############ print five rows ###################
############ Find null values  #######

Credit_Card_Data.isnull().sum()

###### get mean of values ######

mean_value=Credit_Card_Data['MINIMUM_PAYMENTS'].mean()
print('Mean value or column MINIMUM_PAYMENTS is :', mean_value)

######### Replace Null with the mean of values ##################

Credit_Card_Data['MINIMUM_PAYMENTS'].fillna(value=Credit_Card_Data['MINIMUM_PAYMENTS'].mean(), inplace=True)
Credit_Card_Data.isnull().sum()

######## get mean of values in column CREDIT_LIMIT ##########3

mean_value_CREDIT_LIMIT=Credit_Card_Data['CREDIT_LIMIT'].mean()
print('Mean value or column CREDIT_LIMIT is :', mean_value_CREDIT_LIMIT)

#### Replace Null with the mean of values #######

Credit_Card_Data['CREDIT_LIMIT'].fillna(value=Credit_Card_Data['CREDIT_LIMIT'].mean(), inplace=True)
Credit_Card_Data.isnull().sum()

###### Splitting data into x, y ########3
x = Credit_Card_Data.iloc[:,1:]
print('shape of x is : ' ,x.shape)
------------------------------------------
y = Credit_Card_Data.iloc[:,-1]
print('shape of y is : ' ,y.shape)

#elbow method to know the number of clusters
wcss = []
for i in range(1,5):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=30,n_init=5,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
-------------------------------------------------
plt.plot(range(1,5),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

##########3 Silhouette score ########3

nclusters = 3 # this is the k in kmeans , from above graph
km = KMeans(n_clusters=nclusters)
km.fit(x)

########3 predict the cluster for each data point ########

y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print()
print('Silhouette score when k = 3 is :',score)

# Applying PCA #

scaler = StandardScaler() #Applying scaling
scaler.fit(x)

# Apply transform to both the training set and the test set.#

x_scaler = scaler.transform(x)
pca = PCA(2)

x_pca = pca.fit_transform(x_scaler)
newdata = pd.DataFrame(data=x_pca)

## elbow method to know the number of clusters ##

wcss = []
for i in range(1,5):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=30,n_init=5,random_state=0)
    kmeans.fit(x_pca)
    wcss.append(kmeans.inertia_)
----------------------------------------
plt.plot(range(1,5),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

nclusters = 4 # this is the k in kmeans from above graph
km = KMeans(n_clusters=nclusters)
km.fit(x_pca)

### Silhouette score ###

y_cluster_kmeans = km.predict(x_pca)
score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print('Silhouette score after scaling when k = 4 is :',score)

