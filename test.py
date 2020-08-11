import os

dog_list = os.listdir('pet_images')
#print(dog_list)
results_dic = {}

for name in dog_list:
    
    name_temp =name.split('_')
    name_temp.pop(-1)
    #print(name_temp)
    # print(" ".join(name_temp).lower())
    label = " ".join(name_temp).lower()
    results_dic[name]=label
    #results_dic[results_dic] = 
    
print(results_dic)