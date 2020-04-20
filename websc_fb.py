from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp4&fm=neo%2Fmerchandising&iid=M_b1984316-7da2-4330-a750-1efb4a9f445e_5.25DMXHG2C5AT&ssid=55nzkdldu80000001587398880678"
uCLient = uReq(my_url)
page_html = uCLient.read()
uCLient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"_3O0U0u"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]
#print(container)
name = (container.findAll("div", {"class": "_3wU53n"}))
#print(name[0].text)

price = (container.findAll("div", {"class": "_1vC4OE _2rQ-NK"}))
#print(price[0].text)

ratings = (container.findAll("div", {"class": "hGSR34"}))
#print(ratings[0].text)

filename = "products.csv"
f=open(filename,"w")
headers = "Product_name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name = (container.findAll("div", {"class": "_3wU53n"}))
    name = product_name[0].text
    price_container = (container.findAll("div", {"class": "_1vC4OE _2rQ-NK"}))
    price = price_container[0].text.strip()
    ratings_container = (container.findAll("div", {"class": "hGSR34"}))
    ratings= ratings_container[0].text
    # print("productname:"+name)
    # print("price:" + price)
    # print("ratings:"+ratings)
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." +rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    print(name.replace(",","|")+","+final_price+","+ratings+"\n")
    f.write(name.replace(",","|")+","+final_price+","+ratings+"\n")

f.close()