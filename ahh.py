#importerer moduler
from random import choice
#ordene som kan gjettes
word = choice(["pute", "seng"])
#hva som har blit gjettet
guessed = []
#hva som har blit gjettet feil
wrong = []
#hvor mange forsøk vi har
tries = 7
#hva skjer når vi har over 0 forsøk
while tries > 0:
    #en variabel som lagrer bokstaver
    out = ""
    #for bokstav i ordet
    for letter in word:
        #hvis bokstaven er i ordet
        if letter in guessed:
            #bokstaven legges til i "out"
            out = out + letter
    #hvis ikke bokstav i ordet
        else:
        #legger til en space for bokstavene som ikke er gjettet
            out = out + "_"
    #hvis out er lik ordet
    if out == word:
        #slutter loopen
        break
    #printer ordet + spacene du har ikke gjettet
    print("Gjett en bokstav i ordet:", out)
    #hvor mange forsøk igjen
    print(tries, "forsøk igjen")
    #et input for å gjette hvor mange bokstaver
    guess = input()
    #hvis du har allerede gjettet en bokstav
    if guess in guessed or guess in wrong:
        #printer det her
        print("Bokstaven er allerede gjettet på:", guess)
    #hvis det du har gjettet er i ordet
    elif guess in word:
        #yay
        print("Yay")
        #legger til bokstaven i guessed
        guessed.append(guess)
    #hvis du gjetter feil
    else:
        #nei
        print("Nope")
        #subtraherer fra dine forsjøk
        tries = tries - 1
        #legger til i "wrong"
        wrong.append(guess)
        #space
        print()
    #hvis du har forsøk igjen og gjettet ordet
if tries:
    #yay
    print("Du gjettet", word)
    #hvis du har ingen forsøk igjen
else:
    #nay
    print("Du klarte ikke å gjette", word)