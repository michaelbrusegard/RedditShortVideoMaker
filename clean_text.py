import re

def clean_strings(strings):
    replacements = {
        "damn": "darn",
        "shit": "crud",
        "ass": "rear end",
        "bitch": "female dog",
        "piss": "tinkle",
        "fuck": "fudge",
        "cock": "rooster",
        "dick": "Richard",
        "pussy": "kitty",
        "cunt": "kitty",
        "bastard": "illegitimate child",
        "asshole": "jerk",
        "motherfucker": "jerk",
        "son of a bitch": "jerk",
        "bullshit": "nonsense",
        "wanker": "jerk",
        "bollocks": "nonsense",
        "twat": "jerk",
        "arse": "rear end",
        "fanny": "rear end",
        "douchebag": "jerk",
        "dipshit": "idiot",
        "schmuck": "fool",
        "prick": "jerk",
        "slut": "promiscuous person",
        "whore": "sex worker",
        "jackass": "jerk",
        "moron": "idiot",
        "numbnuts": "idiot",
        "nimrod": "idiot",
        "knob": "jerk",
        "bonehead": "idiot",
        "cretin": "fool",
        "doofus": "idiot",
        "goofball": "fool",
        "nitwit": "fool",
        "simpleton": "fool",
        "dumbass": "idiot",
        "asswipe": "jerk",
        "butthead": "jerk",
        "dickhead": "jerk",
        "dingleberry": "fool",
        "numb-nuts": "idiot",
        "shithead": "jerk",
        "skank": "disgusting person",
        "sucka": "fool",
        "twit": "fool",
        "dam": "darn",
        "shite": "crud",
        "arsehole": "jerk",
        "basterd": "illegitimate child",
        "fuk": "fudge",
        "p*ssy": "kitty",
        "c*nt": "kitty",
        "w*nker": "jerk",
        "d*ck": "Richard",
        "a$$hole": "jerk",
        "mothafucka": "jerk",
        "shyt": "crud",
        "bullshyt": "nonsense",
        "a$$": "rear end",
        "biatch": "female dog",
        "douche": "jerk",
        "dipsht": "idiot",
        "pr*ck": "jerk",
        "sl*t": "promiscuous person",
        "wh*re": "sex worker",
        "jacka$$": "jerk",
        "morron": "idiot",
        "numb-nut": "idiot",
        "nimrodd": "idiot",
        "kn*b": "jerk",
        "cretinn": "fool",
        "doofuss": "idiot",
        "goofballl": "fool",
        "nitwitt": "fool",
        "simpelton": "fool",
        "dumbazz": "idiot"
    }
    print('Cleaning text...')
    cleaned_strings = []
    for string in strings:
        cleaned_string = string
        for vulgar_word, replacement_word in replacements.items():
            insensitive_regex = re.compile(re.escape(vulgar_word), re.IGNORECASE)
            match_iter = insensitive_regex.finditer(cleaned_string)
            for match in match_iter:
                original_word = match.group(0)
                if original_word.islower():
                    replacement = replacement_word.lower()
                elif original_word.isupper():
                    replacement = replacement_word.upper()
                elif original_word.istitle():
                    replacement = replacement_word.title()
                else:
                    replacement = replacement_word
                cleaned_string = cleaned_string[:match.start()] + replacement + cleaned_string[match.end():]
        cleaned_strings.append(cleaned_string)
        
    return cleaned_strings