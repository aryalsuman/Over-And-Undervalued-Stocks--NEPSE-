
import requests,bs4
def latest_company_list(websitelink):
    r=requests.get(websitelink)
    soup=bs4.BeautifulSoup(r.content,'lxml')
    tabledata=soup.find_all('tr')#getting all tr tag
    symbols=[]
    # print(tabledata[1])
    for i in tabledata[1:]:#first one is header of table so we are skipping it
        symbol=i.find_all('a')#in each row ie tr tag we are finding all a tag and it is making a list 
        symbols.append(symbol[0].text)#since symbol is a list of 1 element therefore taking using [0] index and text of that element
        
    return symbols