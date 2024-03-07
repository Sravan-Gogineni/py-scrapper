import requests 
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://www.flipkart.com/search?q=mobiles%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

soup = BeautifulSoup(req.content, "html.parser")

mobile_name = soup.findAll("div", class_="_4rR01T")
mobile_rating = soup.findAll("div", class_="_3LWZlK")
mobile_price = soup.findAll("div", class_="_30jeq3 _1_WHN1")
mobile_reviews = soup.findAll("span",class_="_2_R_DZ")
mobiles = []
mobilerating = []
mobileprice = []
mobilereview= []

counter = 0

min_length = min(len(mobile_name), len(mobe_rating),len(mobile_price),len(mobile_reviews))

for i in range(min_length):
    mobiles.append(mobile_name[i].get_text())
    mobilerating.append(mobile_rating[i].get_text())
    mobileprice.append(mobile_price[i].get_text())
    mobilereview.append(mobile_reviews[i].get_text())
    
    counter += 1
    if counter == 100:
        break

df = pd.DataFrame(mobiles)
df2 = pd.DataFrame(mobilerating)
df4 = pd.DataFrame(mobileprice) 
df6 = pd.DataFrame(mobilereview)
result_df = pd.concat([df, df2, df4,df6], axis=1)
result_df.columns=['Mobile_name','Mobile_rating','Mobile_price','mobile_reviews']
result_df.to_csv('MOBILE.csv')








