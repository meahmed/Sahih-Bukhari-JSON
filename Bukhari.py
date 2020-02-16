from bs4 import BeautifulSoup
import requests
import json
import os
import time


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
hadithBookTitlesPage = requests.get('https://sunnah.com/bukhari')
ahadithList = []
soup = BeautifulSoup(hadithBookTitlesPage.text, 'html.parser')
hadithBookTitlesList = []
for hBTL in soup.find_all(class_="english_book_name"):
    hadithBookTitlesList.append(hBTL.text)
l = len(hadithBookTitlesList)
printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
for i, hadithCollection in enumerate(hadithBookTitlesList):
    hadithArr = []
    indexStr = str(i+1)
    htmlString = requests.get('https://sunnah.com/bukhari/' + indexStr)
    soup1 = BeautifulSoup(htmlString.text, 'html.parser')
    for allhadith in soup1.find_all(class_="actualHadithContainer"):
        for engHad in allhadith.find_all(class_="english_hadith_full"):
            narrator = "Empty" if str(engHad.find(class_="hadith_narrated")) == 'None' else " ".join(
                (engHad.find(class_="hadith_narrated").get_text()).split(None))
            engHadith = " ".join(
                (engHad.find(class_="text_details").get_text()).split(None))
            hadithObj = {
                "narrator": narrator,
                "hadith": engHadith
            }
            hadithArr.append(hadithObj)
        bookObj = {
            "Book": hadithCollection,
            "Ahadith": hadithArr
        }
        path = "Bukhari/Book_" + indexStr
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path+'/Book_'+indexStr+'.json', 'w') as outfile:
            json.dump(bookObj, outfile, indent=3)
    time.sleep(0.1)
    printProgressBar(i + 1, l, prefix='Progress:',
                     suffix='Complete', length=50)
