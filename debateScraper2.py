import re
import mechanize
import subprocess
import os
subprocess.call("rm -rf results/", shell=True)
subprocess.call("rm -rf *.pdf*", shell=True)
subprocess.call("rm -rf *.txt*", shell=True)
subprocess.call("mkdir results", shell=True)

br = mechanize.Browser()
year = 2008
for year in range(2008, 2015):
    subprocess.call("mkdir results/" + str(year), shell=True)
    subprocess.call("mkdir results/htmlFiles", shell=True)
    linkToResults = "http://www.joyoftournaments.com/sc/state/" + str(year)
    br.open(linkToResults)

    numberOfResultsAvailable = 0
    for link in br.links():
        print numberOfResultsAvailable
        numberOfResultsAvailable += 1

    for i in range(0, numberOfResultsAvailable):
        event = br.follow_link(nr = i)
        results = event.geturl()
        br.back()
        print results
        subprocess.call("wget " + results, shell=True)
        # batchConversion = "for f in *.pdf; do pdftotext $f; done" 
        # subprocess.call(batchConversion, shell=True)

        ##
    pdf_files = subprocess.check_output("ls *.pdf", shell=True)
    assert len(pdf_files) > 0, "there should be a minimum of one pdf file"
    pdf_files = pdf_files.split("\n")
    del pdf_files[-1]
    for pdf in pdf_files:
        pdf =  pdf.replace(" ",'\ ')
        print "executing -------------- pdftotext "+pdf+" "+pdf.replace(".pdf",".txt")
        subprocess.call("pdftotext "+pdf+" "+pdf.replace(".pdf",".txt"), shell=True)

    ##
    subprocess.call( ('mkdir results/'+str(year) if not os.path.exists("results/"+str(year)) else ''), shell=True )
    print "mv *.txt " + str(year) + "/"
    subprocess.call("mv *.txt results/" + str(year) + "/", shell=True)
    subprocess.call( ('mkdir results/htmlFiles/' if not os.path.exists('results/htmlFiles') else ''), shell=True )
    # subprocess.call("mv *.htm results/htmlFiles/", shell=True)

#clean up shit ass files
subprocess.call("rm -rf *.pdf*", shell=True)
subprocess.call("rm -rf *.txt*", shell=True)
subprocess.call("rm -rf *.htm*", shell=True)
subprocess.call("rm -rf *.xls*", shell=True)



