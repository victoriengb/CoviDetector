"""
    FILE TO TEST THE CODE TO LOAD DATA IN DATASETS
"""

import os
import torchxrayvision as xrv
from tqdm import tqdm
import sys

#Enables us to be able to deploy the code on any OS and to deploy it easily
working_directory = os.path.dirname(__file__)
 
#Creates a dataset with the data needed
d_covid19 = xrv.datasets.COVID19_Dataset(views=["PA", "AP", "AP Supine"],
                                         imgpath= working_directory + os.sep + "images",
                                         csvpath= working_directory + os.sep + "metadata.csv"
                                         )
#Print the dataset just to see if the loading worked                                         
print(d_covid19)

#add each element of the dataset to a variable just to see if it works
for i in tqdm(range(len(d_covid19))):
    try:
        a = d_covid19[i]
    except KeyboardInterrupt:
        break
    except:
        print("Error with {}".format(i) + d_covid19.csv.iloc[i].filename)
        print(sys.exc_info()[1])