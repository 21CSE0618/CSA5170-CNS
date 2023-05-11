def printString(S, N):
	
	
	plaintext = [None] * 5
	
	
	freq = [0] * 26
	
	
	freqSorted = [None] * 26
	
	
	used = [0] * 26
	
	
	for i in range(N):
		if S[i] != ' ':
			freq[ord(S[i]) - 65] += 1
			
			
	for i in range(26):
		freqSorted[i] = freq[i]
		
		
	T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
	
	
	freqSorted.sort(reverse = True)
	
	for i in range(5):
		ch = -1
		
		
		for j in range(26):
			if freqSorted[i] == freq[j] and used[j] == 0:
				used[j] = 1
				ch = j
				break
			
		if ch == -1:
			break
		
		
		x = ord(T[i]) - 65
		
		
		x = x - ch
		
		
		curr = ""
		for k in range(N):
			
			
			if S[k] == ' ':
				curr += " "
				continue
