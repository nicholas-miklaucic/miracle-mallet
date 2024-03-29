
import re

FEMALE_WORDS = [
    "she",
    "her",
    "hers",
    "her",
    "herself",
    "wife",
    "wives",
    "woman",
    "women",
    "chick",
    "chicks",
    "girlfriend",
    "girlfriends",    
    "lady",
    "lady",
    "ladies",
    "ladies",
    "girl",
    "girls",
    "gal",
    "gals",
    "dudette",
    "dudettes",
    "sis",
    "sisters",
    "mum",
    "mom",
    "mums",
    "moms",
    "mother",
    "mothers",
    "motherhood",
    "daughter",
    "daughters",
    "sister",
    "sisters",
    "sisterhood",
    "female",
    "females",
    "feminine",
    "femininity",
    "grandma",
    "grandmother",
    "grandmas",
    "grandmothers",
    "matriarch",
    "matriarchs",
    "queen",
    "queens",
]

MALE_WORDS = [
    "he",
    "him",
    "his",
    "his",
    "himself",
    "husband",
    "husbands",
    "man",
    "men",
    "guy",
    "guys",
    "boyfriend",
    "boyfriends",
    "gent",
    "gentleman",
    "gents",
    "gentlemen",
    "boy",
    "boys",
    "guy",
    "guys",
    "dude",
    "dudes",
    "bro",
    "bros",
    "dad",
    "dad",
    "dads",
    "dads",
    "father",
    "fathers",
    "fatherhood",
    "son",
    "sons",
    "brother",
    "brothers",
    "brotherhood",
    "male",
    "males",
    "masculine",
    "masculinity",
    "grandpa",
    "grandfather",
    "grandpas",
    "grandfathers",
    "patriarch",
    "patriarchs",
    "king",
    "kings",
]

FTM = {f: m for f, m in zip(FEMALE_WORDS, MALE_WORDS)}
MTF = {m: f for f, m in zip(FEMALE_WORDS, MALE_WORDS)}

def change_word(word):
    if word:
        if word[0].isupper():
            if word.lower() in FTM:
                return FTM[word.lower()].title()
            elif word.lower() in MTF:
                return MTF[word.lower()].title()
            else:
                return word
        else:
            if word.lower() in FTM:
                return FTM[word.lower()]
            elif word.lower() in MTF:
                return MTF[word.lower()]
            else:
                return word
    else:
        return word

def change_text(text):
    text = text.replace('’', "'").replace("”", '"').replace("“", '"')
    DELIMITERS = "[\n.,'\" \t!?$%1234567890():;/-]"
    words = re.split(DELIMITERS, text)
    spaces = re.findall(DELIMITERS, text)
    total = ["" for _ in range(len(words) + len(spaces))]
    total[::2] = map(change_word, words)
    total[1::2] = spaces
    return ''.join(total)

# TEST = """Wait fuck I’m supposed to be having sex? Damn I knew I was doing something wrong.

# Only issue I have is that 30-40% is too much you fucks given still. “Our” marriage is my wife’s responsibility so is sex - if she chooses to keep me happy I’ll stick around.

# Just last night my wife says “I hope that was as good for you as it was for me” and I kissed her on the forehead, squeezed her tight and said “mmmm yes” and she drops this nugget “it makes me happy to make you happy”.

# When you are a fucking prize she chases you and lives her life to make you happy."""
# print(change_text(TEST))
# print(change_text("wife’s"))
