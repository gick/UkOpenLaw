import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
pageRange=range(1,5087)
f= open("Progression.log",'a')

for currentPage in pageRange:
    try:
        time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
  
        print "Progression" + str(currentPage)+ " sur" + str(5086)
        response = urllib2.urlopen('http://www.legislation.gov.uk/') #whatever you want here
        uklaw = response.read()
        soup=BeautifulSoup(uklaw,'xml')
        links=soup.select('link[title="RDF/XML"]')
        for index,link in enumerate(links):
            file=open("rdfUk"+str(currentPage)+str(index),'wb')
            response=urllib2.urlopen(str(link['href']))
            file.write(response.read())
            file.close()
    except:
          pass
    # for index,tag in soup.findAll:
    #     print tag
    #     rdf_response=urllib2.urlopen(tag)
    #     rdf_file=rdf_response.read()
    #     f=open("resultUK"+str(currentPage)+str(index)+".xml","wb")
    #     rdf_response
    #




