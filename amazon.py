import requests
from bs4 import BeautifulSoup
import smtplib
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"}
url="https://www.amazon.in/All-new-Echo-Dot/dp/B084DWH53T/ref=sr_1_3?keywords=echo&qid=1636381906&qsid=262-7936126-8513038&sr=8-3&sres=B07PFFMP9P%2CB085FY9NK8%2CB084DWH53T%2CB07SMNPCGK%2CB085M5R82K%2CB084KSRFXJ%2CB07PDJ9JBK%2CB085HK322L%2CB084TNMLTB%2CB08KGVYX6F%2CB084J4MZQM%2CB08KGXGSRR%2CB07PDHTHNN%2CB096S89393%2CB08HWM7ZZF%2CB085TFC6VW"
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
price1=soup.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price2=price1.getText()
price3=price2.split(".")[0].strip("₹").split(",")
price=int(price3[0]+price3[1])
title=soup.find(id="productTitle").getText()
if price<4000:
    connection=smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user="divyamautomated@gmail.com",password="")
    connection.sendmail(from_addr="divyamautomated@gmail.com",to_addrs="aroradivyam3@gmail.com",msg=f"{title}\nNow available below target price at {price}\nBuy Link:{url}")
    connection.close()

