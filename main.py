song = "I like to eat, eat, eat, apples and bananas"

def sing(vowel):
    # your code here
    new_song = ""
    for character in song:
        new_song = new_song + character*3 
    print(new_song)

    for character in song:
        if character == vowel:
            new_song = new_song + character*3
        else:
            new_song = new_song + character
    print(new_song)

sing("ay")
sing("ee")
sing("i")
sing("o")
sing("u")

x = "I like to eat, eat, eat, apples and bananas"
print(x.replace("a", "ay"))
print(x.replace("a", "o"))
print(x.replace("a", "i"))
print(x.replace("a", "ee"))
print(x.replace("a", "u"))


