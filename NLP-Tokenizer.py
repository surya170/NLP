# %%
pip install nltk

# %%
import nltk

# %%

# Add the new NLTK data path
nltk.data.path.append(r'E:\Python_Libraries\nltk_data')

# Download specific resources
nltk.download('all', download_dir=r'E:\Python_Libraries\nltk_data')


# %% [markdown]
# Tokenization:
# Tokenization is the process of breaking a stream of text into words, phrases, or symbols. It is a crucial step in natural language processing (NLP) as it allows us to identify the individual words and phrases in a sentence and group them together into meaningful units. The NLTK library provides various tokenizers that can be used to tokenize text into words, sentences, or paragraphs.
# 

# %%
# Word Tokenization
# Word tokenization is the process of breaking a text into individual words or tokens.
# In Python, we can use the `nltk` library to tokenize a text into words.
# Importing the word_tokenize function from the nltk.tokenize module
#  The word_tokenize function splits a string into individual words.
# It uses regular expressions to tokenize text as individual words,
# using a list of common English words to filter out uninteresting words.

from nltk.tokenize import word_tokenize
word_tokenize("I love my country")

# %%
# TreebankwordTokenizer 
# word_tokenize() function is used to tokenize the text into words. It uses the TreebankWordTokenizer to tokenize the text.
# word_tokenize module, used above is basically a wrapper function that calls tokenize() function as an instance of the TreebankWordTokenizer class.
# It will give the same output as we get while using word_tokenize() module for spliting the sentence into word.
# Let us see the same example implemented above.

from nltk.tokenize import TreebankWordTokenizer
tokenizer_wrd = TreebankWordTokenizer()
tokenizer_wrd.tokenize("I love my country india")



# %%
tokenizer_wrd.tokenize('Hello, How are you')

# %%
# Contradictory situations with Punctuations

tokenizer_wrd.tokenize("Why don't you come here")

# %% [markdown]
# ###### Note: 
# - Such kind of convention by TreebankWordTokenizer is unacceptable in NLP.
# - That's why we have two alternative word tokenizers namely PunctWordTokenizer and WordPunctTokenizer.
# 

# %%
# WordPunchTokenizer
# WordPunchTokenizer is a tokenizer that splits text into words based on punctuation and whitespace.
# It also handles contractions and abbreviations.   
# It is based on the PunktSentenceTokenizer from the NLTK library.

word_tokenize("I can't allow you to go home early")

# %%
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
tokenizer.tokenize("I can't allow you to go home early")

# %%
tokenizer.tokenize("I can't allow you to go home early")

# %%
# Sent_Tokenize 
# it splits texts/paras into sentences and then tokenizes each sentence.

from nltk.tokenize import sent_tokenize
text = "Let us understand the working of NLP. NLP is a subfield of artificial intelligence that is used to analyze."
sentences = sent_tokenize(text)
print(sentences)

# %% [markdown]
# #### Regexp Tokenizer
# - it uses regular expression for matching  alphanumeric tokens plus signs quotes so that we don't split words like "don't" into "do" and "n't"

# %%
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")
tokenizer.tokenize("i don't allow this")

# %%
# PuncktSentenceTokenizer
# Read from given corpus Seperate sentence as token  from paragraphs/sentences.
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext

text = webtext.raw('E:/Datascience/NLP/text.txt')


# %%
sent_tokenizer = PunktSentenceTokenizer(text)
sents_i = sent_tokenizer.tokenize(text)
print(sents_i)


# %%
print(sents_i[3])

# %%
print(sents_i[4])

# %%
for i in sents_i:
    print(i)

# %%
words = []
for i in sents_i:
    words.append(word_tokenize(i))

print(words)



