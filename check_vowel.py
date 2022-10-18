print(end="Enter a Character: ")
c = input()

size = len(c)
if size>1:
    print("\nInvalid Input!")
else:
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            print("\n\"" +c+ "\" is a Vowel")
        elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
            print("\n\"" +c+ "\" is a Vowel")
        else:
            print("\n\"" +c+ "\" is a Consonant")
    else:
        print("\n\"" +c+ "\" is neither a Vowel nor a Consonant")
