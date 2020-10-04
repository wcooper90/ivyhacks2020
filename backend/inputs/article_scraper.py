from bs4 import BeautifulSoup
from UserInputs import UserInputs
import urllib.request
from newspaper import Article

print('Libraries Imported...')


def collect_text(article_url):
    # delete contents from input file originally
    raw = open(UserInputs.INPUT_FILE, "r+")
    contents = raw.read().split("\n")
    raw.seek(0)
    raw.truncate()

    page = urllib.request.urlopen(article_url)

    # parse the HTML from our URL into the BeautifulSoup parse tree format
    soup = BeautifulSoup(page, "lxml")

    texts = soup.find_all("p")
    file = open(UserInputs.INPUT_FILE, "ab")
    for text in texts:
        p = text.get_text()
        nlines = p.count('\n')
        p = p.encode('latin-1', 'ignore')

        # to prevent the printing of weird equations and characters
        if nlines <= 3:
            file.write(p)

    file.close


def url_text_conversion(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        return text
    except:
        return 0
        # return('Error: The entered URL does not exist!')



# change to determine what the url leads to
def article_or_video(url):
    if url:
        return True
    else:
        return False
