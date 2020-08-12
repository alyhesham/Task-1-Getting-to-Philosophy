from bs4 import BeautifulSoup, SoupStrainer
import urllib
import time
import requests


first_rand_url = "https://en.wikipedia.org/wiki/Special:Random"
philo_url = "https://en.wikipedia.org/wiki/Philosophy"
visited_urls = [first_rand_url]


def parseURL(URL):

  response = requests.get(URL)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")

  # avoid images and login
  parserStart = soup.find(id="mw-content-text").find(class_="mw-parser-output")

  article_link = None

  # check every paragraph for existing links
  for link in parserStart.find_all('p', recursive=False):
    if link.find('a',  recursive=False):
      for ref in link.find_all('a', recursive=False):
       article_link = ref.get('href')
       if article_link:
         #avoid citations and help for pronunciation pages
        if not article_link.startswith("#cite") and not article_link.startswith("/wiki/Help"):
         break
      break

  if not article_link:
    return

  curr_link = urllib.parse.urljoin(
    'https://en.wikipedia.org/', article_link)

  return curr_link


def searching(search_history, philo_url, max_steps=50):
  if search_history[-1] == philo_url:
    print(search_history[-1])
    print("Philosophy article reached. TERMINATING.")
    return False
  # max iterations
  elif len(search_history) > max_steps:
    print("50 searches reached and philosophy not found. Increase limit to continue. TERMINATING.")
    return False
  elif search_history[-1] in search_history[:-1]:
    print("program is in a loop. TERMINATING.")
    return False
  else:
    return True


while searching(visited_urls, philo_url):

  print(visited_urls[-1])

  curr_link = parseURL(visited_urls[-1])
  if not curr_link:
    print("Article has no links. DEAD END.")
    break

  visited_urls.append(curr_link)

  time.sleep(0.5)

visited_urls = [first_rand_url]
