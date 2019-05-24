import json
import difflib

data = json.load(open('data.json'))

word = input('Please enter a word: ')

def getDefinition(word):
        definitions = ""
        for definition in data[word]:
                definitions += ('\n%s' %(definition))
        return (definitions)

def translate(word):
    if word in data:
            return (getDefinition(word))
    else:
        closestMatch = difflib.get_close_matches(word, data.keys(), 1, .7)
        if (len(closestMatch) > 0):
                yesOrNo = input('Did you mean "%s"? (y or n): ' %(closestMatch[0]))

                while (yesOrNo != 'y' and yesOrNo != 'n'):
                        yesOrNo = input('I did not understand that response. Please enter a "y" or "n": ')

                if (yesOrNo.lower() == 'y'):
                        return(getDefinition(closestMatch[0]))
                elif (yesOrNo.lower() == 'n'):
                        return ('Word cannot be found. Please double check spelling.')
        else:
                return ('Word cannot be found. Please double check spelling.')

print(translate(word.lower()))