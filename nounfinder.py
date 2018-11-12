#first define sentence = "whatever you want to process" then run nounfinder()
def nounfinder():
	import nltk
	tokens = nltk.word_tokenize(sentence)
	tagged = nltk.pos_tag(tokens)
	length = len(tagged)
	a = list()
	for i in range (0, length):
		log = (tagged [i][1][0] == 'N')
		if log == True:
			a.append(tagged [i][0])
	print (a)
