from xml.dom.minidom import Document
import spacy
npl = spacy.load('en_core_web_sm')

document = npl("The Mars Orbiter Mission (MOM), informally known as Mangalyaan, was launched into Earth orbit on 5 November 2013 by the Indian Space Research Organisation (ISRO) and has entered Mars orbit on 24 September 2014. India thus became the first country to enter Mars orbit on its first attempt. It was completed at a record low cost of $74 million.")

for entity in document.ents:
    print(entity.text, ":", entity.label_) #give the description of the text
    
    
    
'''similarity of text'''

from pathlib import Path
document1 = npl(Path("RomeoAndJuliet.txt").read_text())
document2 = npl(Path("EdwardTheSecond.txt").read_text())

print(document1.similarity(document2))