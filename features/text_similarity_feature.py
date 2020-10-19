from features import Feature
import textdistance



class Text_Similarity_Feature(Feature):

	name = 'Text_Similarity_Feature'
	def __init__(self):
		pass
	
	def similarity(self, s1, s2):
		sim = {}
		sim['hamming_normalized_similarity'] = textdistance.hamming.normalized_similarity(s1, s2)
		sim['jaccard_normalized_similarity'] = textdistance.jaccard.normalized_similarity(s1, s2)
		sim['levenshtein_normalized_similarity'] = textdistance.levenshtein.normalized_similarity(s1, s2)
		
		
		return sim
	def getName(self):
		return self.name
	
datafile = 'data/syz/anchor-top-10w.txt'



if __name__ == '__main__':
	ts = Text_Similarity_Feature()



