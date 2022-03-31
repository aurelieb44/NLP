# Determine what a certain text is about
# Break down the different parts of a text and give you a summary.

import spacy
nlp = spacy.load('en_core_web_sm')
document = nlp('The Mars Orbiter Mission (MOM), informally known as Mangalyaan, was launched into Earth orbit on 5 November 2013 by the Indian Space Research Organisation (ISRO) and has entered Mars orbit on 24 September 2014. India thus became the first country to enter Mars orbit on its first attempt. It was completed at a record low cost of $74 million.')

for entity in document.ents:
    print(entity.text, ':', entity.label_)

from pathlib import Path

document1 = nlp(Path('RomeoAndJuliet.txt').read_text())
document2 = nlp(Path('EdwardTheSecond.txt').read_text())

print(document1.similarity(document2))