# Implementing a K-Means on the data set to see if any patterns in the data

from packages import KMeans, np, pd, train_test_split
from HR_Recruitment_Draft_Dataset import data_df

data_df = data_df.drop('Total Average', axis = 1)
print(data_df.head())

index_values = data_df.loc[:,'Name']

X = data_df.drop('Name', axis = 1)
Y = pd.DataFrame(data = {'Y_Value':
                         [0,0,0,0,0,0,0,0]
                         })

X_train, X_test, Y_train, Y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.25,
                                                    random_state=0)

kmeans_model = KMeans(n_clusters = 2,
                      random_state = 0).fit(X_train)
kmeans_labels = kmeans_model.labels_
kmeans_prediction = kmeans_model.predict(X_test)
kmeans_centers = kmeans_model.cluster_centers_
