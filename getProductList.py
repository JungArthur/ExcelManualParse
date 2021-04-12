import requests
import xml.etree.ElementTree as ET


# Function Start
def getAPI(url):

    # request URL
    # url = "http://isparkmom/apriso/Help/en-us/DB/xmls/Table_CALENDAR.xml"

    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        print("접속 성공")

        # print(f"앞에서 <  : {req.text.find('<')}")
        front_no = req.text.find('<')
        # print(f"뒤에서 >  : {req.text.rfind('>')}")
        back_no = req.text.rfind('>') + 1

        root = ET.fromstring(req.text[front_no:back_no])


        FK_From = len(root.findall('FKFCONST'))
        FK_To = len(root.findall('FKTCONST'))
        SDESCR = root.find('SDESCR').text

        for x in [elem for elem in root.iter('FKFCONST')]:
            if x.text == None :
                print(x.text)
                FK_From = 0
                break

        for x in [elem for elem in root.iter('FKTCONST')]:
            if x.text == None :
                print(x.text)
                FK_To = 0
                break

        print(f'FK_From : {FK_From}   |    FK_To : {FK_To}')

        return {"FK_From" : FK_From, "FK_To" : FK_To, "SDESCR" : SDESCR}
    else:
        print("Error Code")
        print(req)
        return "Error Code"
    # Function end


