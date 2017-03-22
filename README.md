# sentenize
A simple Python script that uses NLTK to split documents into sentences.

### Steps to take prior to running sentenize.py
1. Copy sentenize.py into the directory that contains the documents you wish to sentenize
2. Edit sentenize.py to include the full path to the directory that contains the documents in `directory = 'path/to/dir/with/docs/'`
3. Set the file type to the relevant type in `if filename.endswith('.xml'):`
4. Make sure you save the changes.

### Running sentenize.py 

`sentenize.py` was written for Python 3, so it may not behave itself on Python 2.7. 

1. Open a terminal and navigate to the directory that contains your documents and sentenize.py 
2. Execute `sudo python3 sentenize.py`

### The output

The script outputs the sentences for each document as a `.sents` file. I've tested int on `.txt` and `.xml` input data and it works fine. 
