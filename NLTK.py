# NLTK for english text : 

import nltk, string
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

text = """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a way which had not happened before."""
text = text.lower()
text_p = "".join([char for char in text if char not in string.punctuation])
words = nltk.word_tokenize(text_p)
stop_words = stopwords.words('english')
filtered_words = [word for word in words if word not in stop_words]
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in filtered_words]
pos = pos_tag(filtered_words)

for tree in pos:
           print(tree)

#_____________________________________________________________________________

#NLTK for arabic text :
import nltk, string
from nltk.stem.isri import ISRIStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')


text = u'ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و المقادير الهندسية و غيرها، أن تتعامل على أنها أجسام جبرية، و أعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل'
text_p = "".join([char for char in text if char not in string.punctuation])
"""isri_stemmer = ISRIStemmer()
stem_word = isri_stemmer.stem(text)
print(stem_word)"""
print(text_p)
words = word_tokenize(text_p)
print(words)
arb_stopwords = set(nltk.corpus.stopwords.words("arabic"))
filtered_words = [word for word in words if word not in arb_stopwords]
print(filtered_words)

sentence = nltk.tokenize.sent_tokenize(text)

# tokens = [nltk.tokenize.word_tokenize(s) for s in sentence]
tokens = [nltk.tokenize.wordpunct_tokenize(s) for s in sentence]

# Here pos tagging isn't right :'(
PosTokens = [nltk.pos_tag(e) for e in tokens]

chunks = nltk.ne_chunk_sents(PosTokens)

for tree in chunks:
    print(tree)

#porter = PorterStemmer()
#stemmed = [porter.stem(word) for word in filtered_words]
#print(stemmed)

