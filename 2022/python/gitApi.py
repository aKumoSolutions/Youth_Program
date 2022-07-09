# import requests module
import requests, json, pprint, random, os
from gtts import gTTS
pp = pprint.PrettyPrinter(indent=4)

def create_repo(token, name):
    # Making a get request
    url = 'https://api.github.com/user/repos'
    data = json.dumps({"name": name, "private": "True"})
    header = {'Authorization': 'token ' + token}

    response = requests.post(url, headers=header, data=data)

    if response.status_code == 201:
        print(name + " repo created")
    else:
        print(response.text)

token = os.getenv('github_token')
create_repo(token=token, name="new_repo2")


def find_anime(title):
    url = 'https://animechan.vercel.app/api/available/anime'
    anime = requests.get(url)
    data = anime.json()

    # pp.pprint(anime.json())
    # print(len(anime.json()))

    # narutos = data.index('Naruto')
    # print(data[narutos])

    if title in data:
        return title
    else:
        return "Not Found"


# print(find_anime(title="One Punch Man"))

def get_quote(title):
    url = 'https://animechan.vercel.app/api/quotes/anime?title=%s' % title
    anime_q = requests.get(url)
    data = anime_q.json()
    pp.pprint(data)

# get_quote(title=find_anime(title="One Punch Man"))

def read_quote(quote):
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=quote, lang='en', slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("quote.mp3")
    # Playing the converted file
    os.system("open quote.mp3")
    os.system("sleep 10")
    os.system("rm -rf quote.mp3")



def anime_quote_quiz(title):
    url = 'https://animechan.vercel.app/api/quotes/anime?title=%s' % title
    anime_q = requests.get(url)
    data = anime_q.json()
    
    # pp.pprint(data)
    index = random.randint(0, len(data))
    print(data[index]['quote'])
    read_quote(quote=str(data[index]['quote']))
    guess = input("Who is this quote from: ")
    if guess in data[index]['character']:
        print("Correct! Great Job 👍")
    else:
        print("Wrong! The answer is " + data[index]['character'])


anime_quote_quiz(title='Naruto')