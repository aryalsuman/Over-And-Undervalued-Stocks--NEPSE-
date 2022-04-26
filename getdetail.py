import requests,bs4

def get_complete_detail(each_company,needed_items_from_website):
    url=f"https://merolagani.com/CompanyDetail.aspx?symbol={each_company}"
    data=requests.get(url)
    soup=bs4.BeautifulSoup(data.content,'lxml')
    get_table=soup.find_all('table',id="accordion")
    getallrow=get_table[0].find_all('tr')
    # print(getallrow)
    data=[]
    needed_items=[i.lower() for i in needed_items_from_website]
    for i in getallrow:
        if(len(i.find_all('th'))==1):
            header_from_website=(i.find_all('th')[0].text.strip())
            if header_from_website.lower() in needed_items:
                
                # print(header_from_website)
                companay_detial=(i.find_all('td')[0].text.replace(" ",""))
                companay_detial=companay_detial.split()
                data.append(companay_detial)
    # print(data)
    finaldata=[]
    for i in data:
        for j in i:
            if len(i)>1:
                j=" ".join(i)
            if j not in finaldata:  
                finaldata.append(j)
    finaldata.insert(0,each_company)
    print(finaldata)
    return finaldata