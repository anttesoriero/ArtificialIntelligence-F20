
# Python doesn't have the concept of constants, but we write them in ALL CAPS to
# hint that they are   

# -------------------------------------------------------------
#Frequencies based on the sentence "Rowan Profs are Rowan Proud"
UNIGRAM_FREQS = {"rowan": 0.4, "profs": 0.2, "are": 0.2, "proud": 0.2}

# -------------------------------------------------------------
# Frequencies based on the sentence "Rowan Profs are Rowan Proud Rowan Profs Rowan Profs"    
BIGRAM_FREQS = {"rowan":  {"proud": 0.25, "profs": 0.75},
                   "profs": {"rowan": 0.5, "are": 0.5},
                   "are": {"rowan": 1.0},
                   "proud": {"rowan": 1.0},
                    None: {"rowan": 1.0}}
    
TRIGRAM_FREQS = {("profs", "rowan"): {"profs": 1.0},
                         ("rowan", "proud"): {"rowan": 1.0},
                         (None, None): {"rowan": 1.0},
                         ("are", "rowan"): {"proud": 1.0},
                         ("profs", "are"): {"rowan": 1.0},
                         ("rowan", "profs"): {"rowan": 0.5, "are": 0.5},
                         (None, "rowan"): {"profs": 1.0},
                         ("proud", "rowan"): {"profs": 1.0}}

# -----------------------------------------------------------------------
# Frequencies based alice.txt

BIGRAM_CURIOSITY = ('curiosity', {'and': 0.2, 'what': 0.2, 'it': 0.2,'she': 0.2, 'soles': 0.2})
BIGRAM_QUADRILLE = ('quadrille', {'chapter': 0.2, 'the': 0.4, 'is': 0.2, 'that': 0.2})
BIGRAM_CROQUET = ('croquet', {'ground': 0.4,'the': 0.2, 'then': 0.1, 'she': 0.1, 'with': 0.2})
BIGRAM_MILK = ('milk',{'at': 0.5, 'jug': 0.5})
BIGRAM_NAME = ('name', {'of': 0.2, 'again': 0.1, 'w': 0.1, 'however': 0.1, 
               'child': 0.1, 'is': 0.1, 'alice': 0.1, 'signed': 0.1, 'like': 0.1})
BIGRAM_EXAMPLES = [BIGRAM_CURIOSITY, BIGRAM_QUADRILLE, BIGRAM_CROQUET, BIGRAM_MILK, BIGRAM_NAME]

TRIGRAM_HAD_NO = (('had', 'no'), {'pictures': 0.2, 'idea': 0.4, 'very': 0.2, 'reason': 0.2})
TRIGRAM_LOBSTER_QUADRILLE = (('lobster', 'quadrille'), {'chapter': 0.2, 'the': 0.4, 'is': 0.2, 'that': 0.2})
TRIGRAM_SHE_OUGHT = (('she', 'ought'), {'to': 0.5, 'not': 0.5})
TRIGRAM_LIKE_TO = (('like', 'to'), {'drop': 0.1, 'go': 0.1, 'see': 0.1, 'be': 0.3, 
                                    'go': 0.1, 'see': 0.1, 'hear': 0.1, 'show': 0.1, 'try': 0.1, 'have': 0.1})
TRIGRAM_GLOVES_AND = (('gloves', 'and'), {'as': 0.2, 'she': 0.2, 'a': 0.2,'the': 0.2, 'was': 0.2})

TRIGRAM_EXAMPLES = [TRIGRAM_HAD_NO, TRIGRAM_LOBSTER_QUADRILLE, TRIGRAM_SHE_OUGHT, TRIGRAM_LIKE_TO]



