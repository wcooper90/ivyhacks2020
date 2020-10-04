import os
import speech_recognition as sr
from lxml import html, etree
import requests



def downloadFile(AFileName):

    if 'www.youtube.com' in AFileName:
        # url of video
        url = AFileName
        # create video object
        video = pafy.new(url)
        # extract information about best resolution video available
        bestResolutionVideo = video.getbest()
        # download the video
        bestResolutionVideo.download()
    else:
        # extract file name from AFileName
        filename = AFileName.split("/")[-1]
        # download image using GET
        rawImage = requests.get(AFileName, stream=True)
        # save the image recieved into the file
        with open(filename, 'wb') as fd:
            for chunk in rawImage.iter_content(chunk_size=1024):
                fd.write(chunk)
    return



def video_to_text(link):
    # Get the original webpage html content
    # webpageLink = link
    webpageLink = 'http://www.howtowebscrape.com/examples/simplescrape1.html'
    page = requests.get(webpageLink)
    # convert the data received into searchable HTML
    extractedHtml = html.fromstring(page.content)
    # use an XPath query to find the image link (the 'src' attribute of the 'img' tag).
    imageSrc = extractedHtml.xpath("//img/@src") # in our example, result = ‘/images/GrokkingAlgorithms.jpg’
    # strip off the actual *page* being called as we only want to base url
    imageDomain = webpageLink.rsplit('/', 1) # in our example, result = http://www.howtowebscrape.com/examples/


    # test if this is an absolute link or relative
    if imageSrc[0].startswith("http"):
        # start with http, therefore take this as the full link
        imageLink = imageSrc[0]
    else:
        # does not start with http, therefore construct the full url from the base url plus the absolute image link
        imageLink = str(imageDomain[0]) + str(imageSrc[0])

    # extract file name from link
    filename = imageLink.split("/")[-1]
    # download image using GET
    rawImage = requests.get(imageLink, stream=True)
    # save the image received into the file
    with open(filename, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)
