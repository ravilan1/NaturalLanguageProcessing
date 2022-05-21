import nltk
import spacy
from spacy import displacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

nlp= spacy.load('en_core_web_sm')
doc=nlp(u'snoopy jumped yesterday and drank milk')
print(doc[1].text)
print(doc[1].pos_)
print(doc[1].tag_)

for token in doc:
    print(f"{token.text:{10}} {token.pos:{10}} {token.pos_:{10}} {token.tag:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")

POS_Counts=doc.count_by(spacy.attrs.POS)
print(POS_Counts)

print(doc.vocab[92].text)

print(POS_Counts.items())

for k,v in (POS_Counts.items()):
    print(f"{k} {doc.vocab[k].text} {v}")


TAG_Counts=doc.count_by(spacy.attrs.TAG)
print(TAG_Counts)
for k,v in (TAG_Counts.items()):
    print(f"{k} {doc.vocab[k].text} {v}")

DEP_Counts=doc.count_by(spacy.attrs.DEP)
print(DEP_Counts)
for k,v in (DEP_Counts.items()):
    print(f"{k} {doc.vocab[k].text} {v}")

#Visualizing Partsofspeech
options={'distance':110,'compact':True,'color':'blue','font':'Times'}
#displacy.serve(doc,style='dep',options=options)

#Sentences splitting
sentences=nlp(u"This is Rajesh This is Ravi")
listSpc = list(sentences.sents)
print(listSpc)
for ls in listSpc:
    print(ls)


def nameEntity(ent):
    print(f"entities are {ent.ents}")
    if(ent.ents):
        for i in ent.ents:
            print(f"{i.text} {i.label_} {spacy.explain(i.label_)}")
    else:
        print('No entities found')

def addEntityIfAnyMissed(ent):
    print('ravi')
    ORG=ent.vocab.strings[u"ORG"]
    print(ORG)
    new_ent=Span(ent,12,13,label=ORG)
    ent.ents = list(ent.ents)+[new_ent]
    for i in ent.ents:
        print(f"{i.text} {i.label_} {spacy.explain(i.label_)}") 

def addingMultipleNamedEntities(ent):
    phMatcher=PhraseMatcher(nlp.vocab)
    pattern_list=['good-boy','goodboy']
    phrase_matching=[nlp(text) for text in pattern_list]
    phMatcher.add('newphrase',phrase_matching)
    foundmatches=phMatcher(ent)
    print(foundmatches)
    for match_id,start,end in foundmatches:
        id=nlp.vocab.strings[match_id]
        strend=ent[start:end]
        print(match_id,id,start,end,strend)
    PROD=ent.vocab.strings[u"PRODUCT"]
    #addPhrase=Span(ent,match[1],match[2],label=PROD)
    new-ents=[(Span(ent,match[1],match[2],addPhrase) for match in foundmatches]
    


ent=nlp(u"In India population is high so india is a big country and Google is Big Country..")
newent=nlp(u"In India population is good-boy so india is a big country and Google is goodboy Country..")
nameEntity(ent)
addEntityIfAnyMissed(ent)
addingMultipleNamedEntities(newent)

