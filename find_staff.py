import requests
from bs4 import BeautifulSoup

def query_page():
    headers = {
    'Connection': 'keep-alive',
    'Content-Length': '488',
    'Origin': 'https://courses.osu.edu',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'https://courses.osu.edu/psc/csosuct/EMPLOYEE/PUB/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL?PortalActualURL=https%3a%2f%2fcourses.osu.edu%2fpsc%2fcsosuct%2fEMPLOYEE%2fPUB%2fc%2fCOMMUNITY_ACCESS.CLASS_SEARCH.GBL&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fcourses.osu.edu%2fpsp%2fcsosuct%2f&PortalURI=https%3a%2f%2fcourses.osu.edu%2fpsc%2fcsosuct%2f&PortalHostNode=CAMP&NoCrumbs=yes&PortalKeyStruct=yes',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': 'courses.osu.edu'
    }

    session = requests.Session()

    raw_data = 'ICAJAX=1&ICNAVTYPEDROPDOWN=1&ICType=Panel&ICElementNum=0&ICStateNum=1&ICAction=CLASS_SRCH_WRK2_STRM%2435%24&ICModelCancel=0&ICXPos=0&ICYPos=0&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICSkipPending=0&ICAutoSave=0&ICResubmit=0&ICSID=o0oC32m%2B1bu9olOIeIxUF4%2FlB2qL4efrEm6xJvndnrY%3D&ICActionPrompt=false&ICBcDomData=&ICPanelName=&ICFind=&ICAddCount=&ICAPPCLSDATA=&CLASS_SRCH_WRK2_INSTITUTION$31$=OSUSI&CLASS_SRCH_WRK2_STRM$35$=1192&SSR_CLSRCH_WRK_CAMPUS$0='

    split_data = raw_data.split('&')
    data = {}
    for s in split_data:
        data_tuple = s.split('=')
        data[data_tuple[0]] = data_tuple[1]

    path = 'https://courses.osu.edu/psp/csosuct/EMPLOYEE/PUB/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL'
    """
    response = session.get(path)

    cookies = dict(response.cookies)
    print(cookies)
    print(response.headers)
    headers = dict(response.request.headers);
    print(headers)
    """
    response = session.post(path, data=data, headers=headers)

    if response.status_code is 200:
        #print('Headers: {}'.format(request.headers['content-type']))
        #print('Text:')
        print(response.text)
        with open('output.html', 'w') as output:
            output.write(response.text)
        #soup = BeautifulSoup(request.text, 'html.parser')
        #print(soup.find_all('a'))
        pass

    else:
        print("Did not return 200")

def main():
    query_page()

if __name__ == "__main__":
    main()
