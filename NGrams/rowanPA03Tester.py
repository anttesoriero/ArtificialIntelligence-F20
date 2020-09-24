#!/usr/bin/python3

import ngram
import ngramData
import string


class Tester():  
    def __init__(self):
        # These are class vars not instance vars!!
        self.maxPoints = 0
        self.totalPoints = 0
        
        
         
    # --------------------- report --------------------------------------
    def report(self, string, success, points):
        print(string.rjust(25) + ": ", end="")       
        if success:
            print ("---> PASS ({}/{})".format(points, points))
            self.maxPoints += points
            self.totalPoints += points
        else: 
            print ("---> FAIL (0/{})".format(points))
            self.maxPoints += points


    # ------------------ finalReport --------------------------------------
    def finalReport(self):
        print ("\n" + "="*47)
        print ("="*47)
        print ("="*13 + "  Test Results " +
                 str(self.totalPoints)+ "/" + str(self.maxPoints) +
                 "  " + "="*13 )
        print ("="*47)
        print ("="*47)
        print ("\n")
        print ("(This is NOT your final grade - see assignment!)")

    # ------------------- doTests --------------------------------------
    # Run a bunch of tests in a single category    
    def doTests(self, categoryName, listOfTests):
        print("\n" + "="*10 + " " + categoryName + " " + "="*10)
        myTotal = 0
        myMax = 0
        
        for i in listOfTests:
            funcName, points = i
            name, success = funcName()
            if success:
                score = points
            else:
                score = 0
            
            myTotal += score
            myMax += points
            self.report(name, success, points)
        print ()
        print ("******* {} Total: ({}/{}) *******".format(categoryName, myTotal, myMax).upper().rjust(40))
            


# ----------------------- getNWords ------------------------------------------
# Get the first N words from a file
# If there aren't enough words, add a bunch of "Rowan"s 
# at the end
def getNWords(textFilePath, numWords):

    with open(textFilePath, 'r') as handle:
        text = handle.read().lower()
    text = text.translate(
        str.maketrans(string.punctuation,
                         " " * len(string.punctuation)))
    text=text.split()
    
    while len(text) < numWords:
        text.append("Rowan")
        
    return text[:numWords] 


# ----------------------- Unigram Tests ----------------------------------------
def unigramTest1():
    unigrams = ngram.computeUnigramProbs(["rowan", "profs", "are", 
                                            "rowan", "proud"])
    if unigrams == ngramData.UNIGRAM_FREQS:
        return("Unigram Demo Test", True)
    else:
        return("Unigram Demo Test", False)
            

# ----------------------- Bigram Tests ------------------------------------------


# Make sure that if you ask for 10 things you get 10 things
def bigramTest1():
    result = False
    try:
        textSeq = ngram.generateRandomBigramSequence("rowan", ngramData.BIGRAM_FREQS, 10)
        if len(textSeq.split()) == 10:
            result = True 
    except: 
        pass
    
    return("Bigram Length Test", result)    


# Make sure the first word is the one we specified    
def bigramTest2():    
    try:
        textSeq = ngram.generateRandomBigramSequence("rowan", ngramData.BIGRAM_FREQS, 10)
        result = textSeq.split()[0]=="rowan"
        textSeq = ngram.generateRandomBigramSequence("profs", ngramData.BIGRAM_FREQS, 10)
        result = result and textSeq.split()[0] == "profs"
    except: 
        result = False
        
    return("Bigram Start Test", result)
 
# make sure that the text generated is actually possible   
def bigramTest3():
    try:
        result = True
        textSeq = ngram.generateRandomBigramSequence("rowan", ngramData.BIGRAM_FREQS, 100).split()
        prev = "rowan"
        for i in range(1, len(textSeq)):
            current = textSeq[i]
            result = result and (ngramData.BIGRAM_FREQS[prev][current] > 0)
            prev = current
    except:
        result = False
    return ("Bigram Text is Possible", result)


# Compute probabilities and see if it's the same as expected

def bigramTest4():
    bigrams = ngram.computeBigramProbs(["rowan", "profs", "are", 
                                            "rowan", "proud", "rowan", "profs", 
                                            "rowan", "profs"])
    if bigrams == ngramData.BIGRAM_FREQS:
        return("Bigram Frequency Test", True)
    else:
        return("Bigram Frequency Test", False)    
    


# check stuff based on alice.txt
def bigramTest5():
    try:
        words = ngram.textToList('alice.txt')
        bigramProbs = ngram.computeBigramProbs(words)
        result = True
        for i in ngramData.BIGRAM_EXAMPLES:
            word = i[0]
            value = i[1]
            if bigramProbs.get(word)!= value:
                result = False
    except:
        result = False
    return ("Bigram Alice Test", result)
        
  


# ----------------- Trigram Tests  ------------


# Make sure that if you ask for 10 things you get 10 things
def trigramTest1():
    result = False
    try:
        text = ngram.generateRandomTrigramSequence("rowan", "profs", ngramData.BIGRAM_FREQS,
                                            ngramData.TRIGRAM_FREQS, 10)
        if text and (len(text.split())==10):
            result = True
    except:
        pass

    return ("Trigram Length Test", result)
            
     
# Make sure the first two words are as specified
def trigramTest2():
    try:
        text = ngram.generateRandomTrigramSequence("rowan", "profs", ngramData.BIGRAM_FREQS,
                                            ngramData.TRIGRAM_FREQS, 10)
        result = text.split()[0]=="rowan" and text.split()[1]== "profs"
            
        text = ngram.generateRandomTrigramSequence("proud", "rowan", ngramData.BIGRAM_FREQS,
                                            ngramData.TRIGRAM_FREQS, 10)
        result = result and (text.split()[0]=="proud") and (text.split()[1] == "rowan")
    except:
        result = False
          
    return ("Trigram Start Text", result)

# Make sure that the sequence is legal
def trigramTest3():
    try:
        words = ngram.generateRandomTrigramSequence(
            "rowan", "profs", ngramData.BIGRAM_FREQS, ngramData.TRIGRAM_FREQS, 100).split()
        prev = "rowan"
        result = True
        for i in range(1, len(words)):
            current = words[i]
            
            result = result and (ngramData.BIGRAM_FREQS[prev][current] > 0)
            prev = current
        
        first = "rowan"
        second = "profs"
        for i in range(2, len(words)):
            third = words[i]
            pair = (first,second)
            result = result and (ngramData.TRIGRAM_FREQS)[pair][third] > 0
            first = second
            second = third
        
    except:
        result = False
     
    return ("Trigram Text is Possible", result)

# make sure the probabilities generated are correct
def trigramTest4():
    result = False
    try:
        trigrams = ngram.computeTrigramProbs(["rowan", "profs", "are", 
                                               "rowan", "proud", "rowan", "profs", 
                                               "rowan", "profs"])
        if trigrams == ngramData.TRIGRAM_FREQS:
            result = True
    except:
        pass
        
    return ("Trigram Frequency Test", result)
        
        
def trigramTest5():
    try:
        words = ngram.textToList('alice.txt')
        trigramProbs = ngram.computeTrigramProbs(words)
        result = True
        for i in ngramData.TRIGRAM_EXAMPLES:
            word = i[0]
            value = i[1]
            if trigramProbs.get(word)!= value:
                result = False
    except:
        result = False
    return ("Trigram Alice Test", result)
        
  

if __name__ == '__main__':

    allTests = Tester()
    allTests.doTests("Unigram Tests", [(unigramTest1,0)] )
    allTests.doTests("Bigram Tests", [(bigramTest1,2), (bigramTest2,2), (bigramTest3,5), (bigramTest4,5), (bigramTest5,5)])
    allTests.doTests("Trigram Tests", [(trigramTest1,2), (trigramTest2,2), (trigramTest3,2), (trigramTest4,2), (trigramTest5,3)])
    allTests.finalReport()
    
