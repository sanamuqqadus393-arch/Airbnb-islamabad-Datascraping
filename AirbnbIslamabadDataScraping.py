import requests
from bs4 import BeautifulSoup
import pandas as pd
name_list = []
price_list = []
reviews_list = []
description_list = []


url = "https://www.airbnb.com/s/Islamabad--Pakistan/homes?place_id=ChIJF2ke4Py-3zgRwJglPt7gZj4&refinement_paths%5B%5D=%2Fhomes&query=Islamabad%2C%20Pakistan&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2026-05-01&monthly_length=3&monthly_end_date=2026-08-01&price_filter_input_type=2&channel=EXPLORE&pagination_search=true&price_filter_num_nights=5&federated_search_session_id=e3b25bb7-0ae4-401b-ad69-3b53763ff5d4&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D"
r = requests.get(url)
# print (r)
soup = BeautifulSoup(r.text, "lxml")


try:
    while True:
        name = soup.find_all("div",{"class":"t1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_ld_l4hv9n atm_gp_7iojc0 atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_hfv0h6 atm_cs_1mexzig atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr"})
        for i in name:
            n = i.text
            name_list.append(n)
        print(name_list)

        price = soup.find_all("div",{"class":"touu2u1 atm_9s_116y0ak atm_mk_h2mmj6 dir dir-ltr"})
        for i in price:
            n = i.text
            price_list.append(n)
        print(price_list)

        review = soup.find_all("div",{"class": "t1phmnpa atm_da_1ko3t4y atm_dm_kb7nvz atm_fg_h9n0ih dir dir-ltr"})
        for i in review:
            n = i.text
            reviews_list.append(n)
        print(reviews_list)

        description = soup.find_all("div", {"class": "s1cjsi4j atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vlb1yz atm_7l_xeyu1p atm_ks_zryt35__1rgatj2 f1v0rf5q atm_da_cbdd7d dir dir-ltr"})
        for i in description:
            n = i.text
            description_list.append(n)
        print(description_list)

        np = soup.find("a" , {"aria-label": "Next"}).get("href")
        cnp = "https://www.airbnb.com"+np
        #print(cnp)

        url = cnp
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
except:
    pass

from itertools import zip_longest

df = pd.DataFrame(
    zip_longest(name_list, price_list, reviews_list, description_list, fillvalue="N/A"),
    columns=["Name", "Price", "Stars and Review", "Description"]
)

df.to_csv("airbnbIslamabadData.csv")