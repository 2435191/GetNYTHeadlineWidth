"""
    Unfortunately, the NYT API doesn't have a GET for headline font size. 
    Thus, scraping is the viable alternative.
"""

import requests
from bs4 import BeautifulSoup

def get_headline():
    soup = BeautifulSoup(requests.get('http://www.nyt.com').text, parser='lxml', features='lxml')

    spotlight = soup.findAll('section', {'data-block-tracking-id' : 'Spotlight'})
    assert len(spotlight) == 1

    main_story_wrapper = spotlight[0].findAll('section', class_='story-wrapper')
    assert len(main_story_wrapper) > 0

    # Grab url of main story, check there's only one.
    link_urls = set()
    for a_tag in main_story_wrapper[0].findAll('a'):
        url = a_tag.get('href')
        if url is not None:
            link_urls.add(url)
    
    assert len(link_urls) == 1
    (link,) = link_urls

    main_story_title = main_story_wrapper[0].find('a').find('h3')
    # Grab size
    size = float( main_story_title['size'] )

    # Grab title
    title = main_story_title.find('span').text

    return {
        'link' : link,
        'size' : size,
        'title' : title
    }


if __name__ == '__main__':
    print(get_headline())
