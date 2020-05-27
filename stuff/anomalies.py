import numpy as np
anomalies = []
epicurve = [0,0,0,1,0,2,5,6,10,17,11,27,21,16,9,5,8,7,7,8,5,9,2,9,7,7,5,2,3,8,5,9,2,9,7,7,5,2,3,8,5,9,2,9,7,7,5]
#finding outliers usinng the mean
def find_anomalies(data):
    random_data_std = np.std(data)
    random_data_mean = np.mean(data)
    anomaly_cut_off = random_data_std * 3

    lower_limit = 0 
    upper_limit = random_data_mean + anomaly_cut_off

    print(upper_limit)
    print(lower_limit)

    for outlier in data:
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
    return anomalies

def donothing():
    print("outliers are ")
    print(find_anomalies(epicurve))






    

    knn = KNeighborsClassifier(n_neighbors=2, metric='minkowski', p=2)
    knn.fit()
    y_pred = knn.predict()
