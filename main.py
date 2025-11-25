from bs4 import BeautifulSoup
import requests
import ollama
word = input("Type a word. ")
url = "https://www.merriam-webster.com/dictionary/" + word
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
definitions_list = soup.find_all('div', class_='sb-entry')
# create a string variable to collect all the elements of definitions_list as you loop through
definitions = ""
for definition in definitions_list:
    definitions += definition.get_text().strip()
# print(definitions)
response = ollama.chat(model='gemma3:1b', messages=[
    {
        'role': 'system',
        'content': (
            "Let's play a game!"
            "You will be given a list of definitions."
            "You have to guess the word they define!"
            "Have fun!"
        )},
  {
    'role': 'user',
    'content': definitions
  }
])
print(response['message']['content'])
