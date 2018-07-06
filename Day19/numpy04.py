import numpy as np
data = np.loadtxt("movielens-1m/ratings.dat",
                  delimiter="::",dtype=np.int64)
print(data[:5,:])
print(data.shape)

mean_rating_total = data[:,2].mean()
print(mean_rating_total)
user_ids = np.unique(data[:,0])
print(user_ids.shape)

mean_rating_by_user_list = []

for user_id in user_ids:
    data_for_user = data[data[:,0]==user_id,:]
    mean_rating_for_user = data_for_user[:,2].mean()
    print(mean_rating_for_user)
    mean_rating_by_user_list.append([user_id, mean_rating_for_user])

mean_rating_by_user_array = np.array(user_ids,dtype=np.float32)
mean_rating_by_user_array = np.array(mean_rating_by_user_list,dtype=np.float32)

np.savetxt("mean_rating_by_user_array.csv",
           mean_rating_by_user_array,  fmt = "%.3f", delimiter=",")

#np.savetxt("user_ids.csv",user_ids,  fmt = "%d", delimiter=",")