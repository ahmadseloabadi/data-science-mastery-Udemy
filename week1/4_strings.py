# string manipulation

# concate
print("\n ---concatenation ---\n")


first="hello"
second="world"
concate=first+' '+second

print(concate)

# slicing
print("\n ---slicing ---\n")

text="python programming"
print(text)
print(text[0:6])
print(text[-11:])

print("\n ---formating ---\n")
name="sungep"
age=25

print(f'my name is {name} and i am {age} years old')

# common string methods
print("\n ---common string methods ---\n")
print("\n ---split() ---\n")

sentence1 = "Python is fun"
print(sentence1)
words1= sentence1.split()
print(words1)
sentence2 = "i;love;python"
print(sentence2)
words2= sentence2.split(';')
print(words2)

# join words
print("\n ---join() ---\n")
new_sentence1=' '.join(words1)
new_sentence2=';'.join(words2)

print(new_sentence1)
print(new_sentence2)

# update sentence with replace
print("\n ---replace() ---\n")
new_text='i love you'
print(new_text)
update_text=new_text.replace('you','me')
print(update_text)

# clean up sentence
text_messy="       i love indonesia"
clean_text=text_messy.strip()
print(clean_text)

# Regular expression for pattern matching

print("\n ---Regular expression(reGex) for pattern matching ---\n")
print("\n ---re.findall(pattern,string) ---\n")

import re

ex_text="contact me at 0808-1234-5768"
digits=re.findall(r'\d+',ex_text)
digits2=re.findall(r'\d',ex_text)
print(digits)
print(digits2)
print("\n ---re.sub(pattern,replacement,string) ---\n")

up_text=re.sub(r'\d',"x",ex_text)
print(up_text)

print("\n ---re.search(pattern,string) ---\n")

search_text=re.search('contact',ex_text)
print(search_text) 

# exercise
print("\n ---exercise clean text ---\n")

import re

def clean_text(text):
    # remove punctuation
    text = re.sub(r'[^\w\s]',"",text)
    # remove extra spaces
    text = " ".join(text.split())
    # convert  to lowercase
    text = text.lower()

    return text

input_text = "    Hello, everyone im a beginer in data science...."

print(clean_text(input_text))

# exercise 2
print("\n ---exercise check palindrome in string ---\n")

def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text1=input("enter a words/sentence :")
# ex input:
# madam
# a man , a plan , a canal , panama
if is_palindrome(input_text1):
    print(f'"{input_text1}" is a palindrome')
else:
    print(f'"{input_text1}" is not a palindrome')