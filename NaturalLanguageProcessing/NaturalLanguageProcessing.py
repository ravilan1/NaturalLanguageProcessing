import spacy
from spacy import displacy
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from spacy.matcher import Matcher

nlp=spacy.load('en_core_web_sm')
words = nlp(u'please search in youtube')
sentences=nlp(u'This is Ravi This is my name')
for sent in words:
    print(sent,sent.pos_)
for sentences in sentences.sents:
    print(sentences)
print(nlp.pipeline)
print(nlp.pipe_names)
print(type(words))

def Tokenization():
    #examples
    moresentences=nlp(u'please login to my website http://www.gmail.com. or send email to ravilankalapalli@gmail.com.')
    print(len(moresentences))
    for sent in moresentences:
        print(sent,end='*')
    print('\n')
    orgRecognition=nlp(u'IBM is where i am working on and want to move to GOOGLE what should i do and price $6 million..')
    for org in orgRecognition.ents:
        print(org,org.label_)
        print(spacy.explain(org.label_))
    for nchunks in orgRecognition.noun_chunks:
        print(nchunks,nchunks.label_)
        print(spacy.explain(nchunks.label_))
    #displacy.serve(orgRecognition,style='dep',options={'distance':10})

def stemming():
     poStemmer = PorterStemmer()
     word=['go','going','fair','fairness','searching','drafting']
     for w in word:
        print(poStemmer.stem(w))

     #Snowball Stemmer
     snStemmer = SnowballStemmer(language='english')
     for w in word:
         print(snStemmer.stem(w))

def Lemmatization():
    sen=nlp(u'I loved her because i love her!')
    for s in sen:
        print(f'{s.text:{12}} {s.pos_:{6}} {s.lemma:<{22}} {s.lemma_}')

def stopWords():
    print(nlp.Defaults.stop_words)
    print(len(nlp.Defaults.stop_words))
    print(nlp.vocab['hence'].is_stop)
    print(nlp.vocab['speak'].is_stop)


def matchVocabulary(fullsentence):
    m_tool=Matcher(nlp.vocab)
    patterns=[[{'LOWER':'goodboy'}],[{'LOWER':'good'},{'IS_PUNCT':True},{'LOWER':'boy'}],[{'LOWER':'good'},{'LOWER':'boy'}]]
    m_tool.add('GoodBoy',patterns)
    matchPhrase=m_tool(fullsentence)
    print(matchPhrase)
    for match_id, start, end in matchPhrase:
        id=nlp.vocab.strings[match_id]
        strend=fullsentence[start:end]
        print(match_id,id,start,end,strend)

Tokenization() #Tokenise the word
stemming() # stem wording like going is mapped to gp
Lemmatization() #Lemmatization looks similaer to stemming but it wont cut words but round or keep same words
stopWords() #like is,the are stop words
fullsentence=nlp(u'Ravi is a goodboy not because of he is good-boy because he is a Goodboy!')
matchVocabulary(fullsentence)
