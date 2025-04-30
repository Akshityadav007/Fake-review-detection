import kagglehub
from loadData import DataLoader

# Download latest version (csv file)
filePath = kagglehub.dataset_download("arhamrumi/amazon-product-reviews")+'/Reviews.csv'

# print('Path where file is present: ', filePath)

DataLoader(filePath)