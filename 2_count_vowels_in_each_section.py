# Count the number of vowels in a text divided into sections.

def search_vowel(_text, _section):
    vowels = 'aeiouAEIOU'
    sections= {}
    text_without_space = _text.replace(' ','')

    for i in range(0, len(text_without_space),_section):
        sections[text_without_space[i:(i+_section)]] = 0

    for section in sections:
        for vowel in vowels:
            sections[section]+=section.count(vowel)
    print(sections)

search_vowel('Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.',7)