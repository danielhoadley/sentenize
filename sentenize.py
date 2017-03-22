import codecs
import nltk.data
import os
import io

# Add the path to the folder containing the documents you want to sentenize

directory = 'path/to/dir/with/docs/'

print ('Tokenizing documents to sentences...')

for filename in os.listdir(directory):
    
    # Specify the file type of the documents 
     if filename.endswith('.xml'):
             doc = codecs.open(filename, 'r', 'utf-8')
             content = doc.read()
             tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
             with io.open (filename + '.sents', 'w', encoding='utf-8') as g:
                     g.write('\n-----\n'.join(tokenizer.tokenize(content)))
                     print (filename + ' has been sentenized!')
                    
