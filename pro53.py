import string
input = raw_input
 
def ispangram(sentence, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(sentence.lower())
 
print ( ispangram(input('The Sentence is: ')) )
