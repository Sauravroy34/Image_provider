import pixabay.core
import os
from dotenv import load_dotenv
load_dotenv()

API = os.getenv("API_KEY")

px = pixabay.core(API)
name = input("enter what you want to search")

result = px.query(name)
limit  = (len(result))
number = int(input(f"enter number of images you need(max_limit ={limit})"))

os.makedirs(name,exist_ok=True)
for i in range(number):
    result[i].download(f"{name}/{i}.jpeg","largeImage")



