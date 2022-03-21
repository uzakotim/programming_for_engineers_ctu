#!/usr/bin/python3
# Programming for Engineers - KYR 2021
# Date Finder
# CVUT
# Timur Uzakov


def main():
	n = input()
	sentences = []
	monthes = ['January','February','March','April','May','June','July','August','September','October','November','December']

	global_day = ''
	global_month = ''
	for i in range(int(n)):
		sentence = input()
		sentence = sentence.replace(","," ")
		sentence = sentence.replace("\""," ")
		sentence = sentence.replace("?"," ")
		sentence = sentence.replace("!"," ")
		if sentence[-1] == '.':
			sentence = sentence[:-1]
		sentence = list(sentence.split())

		sentences.append(sentence)
		
	for i in range(int(n)):
		count_dm = 0
		count_month = 0
		for j,word in enumerate(sentences[i]):
			minimal_distance = len(sentences[i])
			if '.' in word:
				if  word[-1]=='.':
					word = word[:-1]
				tmp_list = word.split('.')
				day   = int(tmp_list[0])
				month = int(tmp_list[1])
			
				if month <13 and month>0:
					global_month = str(month)
				else:
					continue
				if day < 32 and day > 0:
					if month == 2 and day <29:
						global_day = str(day)
						count_dm +=1
					if month != 2:
						global_day = str(day)
						count_dm +=1
				else:
					continue                
					
		
			elif word in monthes:
				month  = word
				count_month +=1
				for x in sentences[i]:
					try:
						int(x)
					except:
						continue

					if int(x)>0 and int(x)<32:
						if month == 'February' and int(x) > 28:
							continue
						distance = abs(sentences[i].index(month) - sentences[i].index(x))
						if distance < minimal_distance:
							minimal_distance = distance
							global_day = x
							global_month = month

		if count_dm == 1 and count_month == 0 and global_month != '' and global_day != '':
				print(str(i+1)+'. '+monthes[int(global_month)-1]+' ' + global_day)
			
		elif count_dm ==0 and count_month == 1 and global_month != '' and global_day != '':
				print(str(i+1)+'. '+global_month +' ' + global_day)
		global_month = ''
		global_day = ''
	    
	
if __name__ == "__main__":
	main()    
	    
