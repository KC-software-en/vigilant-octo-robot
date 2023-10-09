# Create a file called semantic.py and run all the code extracts above in the lesson
# import spacy
import spacy

###################################################################
###################################################################
print("Run all the code extracts in the lesson above \n\n")
#SIMILARITY WITH SPACY

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print("0.5929930274321619 - There is an average semantic similarity between the animals")
print(word3.similarity(word2))
print("0.40415016164997786 - The similarity is below average considering one is an animal and the other a fruit")
print(word3.similarity(word1))

print("0.22358825939615987 - Indicates a weak semantic similarity")

# think of an example of your own
# check similarities between character villians
print("\nExample of your own:")
word4 =nlp("Vecna")
word5 =nlp("Klaus")
word6 =nlp("Steppenwolf")
print("\tSemantic similarity between Vecna & Klaus:")
print(word4.similarity(word5))
print("\tSemantic similarity between Klaus & Steppenwolf:")
print(word5.similarity(word6))
print("\tSemantic similarity between Vecna & Steppenwolf:")
print(word4.similarity(word6))
print("")

###################################################################
print('=' * 100)

# WORKING WITH VECTORS
# a series of words to compare with one another
# use two for loops to allow us to undertake a comparison of the words.
# We will first compare one word (token1) to all the other ‘tokens’ in the string,
# and then do the same for the next word (token2) and repeat the cycle
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()

###################################################################
print('=' * 100)

# WORKING WITH SENTENCES
# Many NLP applications need to compute the similarity in meaning between short texts

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    # comment out print with '+' because of TypeError: can only concatenate str (not "float") to str
    # print(sentence + "-" + similarity)
    # fix print statement with ','
    print(sentence, "-", similarity)

###################################################################
print('=' * 100)

# Run the example file on with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice different from the model 'en_core_web_md'

        
print('''
In semanticsimilarity_example.py, I replaced nlp = spacy.load('en_core_web_md') with nlp = spacy.load('en_core_web_sm')
by commenting out the former. I found that after running the program with the simpler language model ‘en_core_web_sm’,
three warnings presented itself. One for each section stating:

"Warning (from warnings module):
UserWarning: [W007] The model you're using has no word vectors loaded,
so the result of the Doc.similarity method will be based on the tagger, parser and NER,
which may not give useful similarity judgements.
This may happen if you're using one of the small models, e.g. `en_core_web_sm`,
which don't ship with word vectors and only use context-sensitive tensors.
You can always add your own word vectors, or use one of the larger models instead if available."

The semantic similarity floating decimal decreased for all comparisons.
The `en_core_web_sm` resulted in every comparison being more dissimilar than the results yielded with
the `en_core_web_md.` 
''')




