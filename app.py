import requests
from bs4 import BeautifulSoup as bs ,Comment
from pprint import pprint
import markdownify 
from time import sleep
import os
  
def get_pages(soup):
    links=soup.find(id='leftmenuinnerinner').find_all('a')
    return [link.get('href')for link in links]

def data_cleaing(_soup,lang='js'):
    # print('removing script and other tags') 
    for s in _soup(["script","style",'hr','button','br']):
        s.extract()
    main=_soup.find(id='main')
    # for el in main.find_all('hr'):
    #     el.extract()
    # print('removing unwanted ancher tags') 
    if main.find_all('a') is not None:
        for el in main.find_all('a'):
            try:
                if '.asp?filename=' in el.get('href') or 'examples.asp' in el.get('href'):
                    el.extract()
            except Exception as e:
                print(e)
                el.extract()
    
    # print('removing midcontentadcontainer') 
    if main.find(id='midcontentadcontainer') is not None:
        for el in main.find(id='midcontentadcontainer').find_all_next():
            el.extract()
        main.find(id='midcontentadcontainer').extract()
    # print('removing mypagediv2') 
    if main.find(id='mypagediv2') is not None:
        main.find(id='mypagediv2').decompose()
    
    # print('removing mainLeaderboard') 
    if main.find(id='mainLeaderboard') is not None:
        main.find(id='mainLeaderboard').decompose()
    # print('changing to pre tag')
    codes=main.find_all('div',{'class':f'{lang}High'})
    if codes:
        for code in codes:
            tag=_soup.new_tag('pre')
            tag.string=code.get_text().replace(';',';\n').replace('{','{\n').replace('}','}\n').lstrip()
            code.replace_with(tag)
    els=main.find_all('div',{'class':'w3-clear nextprev'})
    # print('removing w3-exerciseform')
    if main.find(id='w3-exerciseform') is not None:
        main.find(id='w3-exerciseform').decompose()

    # print('removing getdiploma')
    if main.find(id='getdiploma') is not None:
        main.find(id='getdiploma').decompose()

    # print('removing p tags with b')
    for el in main.find_all('p'):
        if el.find('b'):
            el.decompose()

    # print('removing ancher tag with class w3-btn w3-margin-bottom ')
    for _ in main.find_all('a',{'class':'w3-btn w3-margin-bottom'}):
        _.decompose()

    # print('removing nextprev btn')
    for el in els:
        el.decompose()

    # delete the comment in the page
    # print('removing comment')
    for element in main(text=lambda text: isinstance(text, Comment)):
        element.extract()
    
    return main
def get_courses(URL,prefix):
    error=[]
    try:
        lang=URL.lower().split('/')[3]
        req=requests.get(URL)
        html=req.text
        soup=bs(html,'html.parser')
        pages=get_pages(soup)
        for page in pages:
            reqw= requests.get(f'{URL}{page}')
            print(f'status[{reqw.status_code}] : connecting to {URL}')
            if reqw.status_code==200:
                _soup=bs(reqw.content,'html.parser')

                main=data_cleaing(_soup,lang)
                # pprint(main)
                # print('_'*100)
                markdown = markdownify.markdownify(main.encode('utf-8'),code_language=lang)
                # pprint(markdown)
                dirname=URL.split('/')[3].capitalize()
                filename=_soup.title.string
                filename=filename.lower().removeprefix(prefix)
                filename=filename.capitalize()
                filename="".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()
                if not os.path.exists(dirname):
                    os.makedirs(dirname)

                with open(f'./{dirname}/{filename}.md','wb') as f:
                    print(f'Writing {filename} to file ✍️')
                    f.write(markdown.encode('utf-8'))
            else:
                error.append(page)
                continue
            sleep(2)
        print('Finished')
    except Exception as e:
        print(e)
    finally:
        print(error)

if __name__=='__main__':
    # choice=input("which language you need?\n").strip()
    # URL =f'https://www.w3schools.com/{choice}/'
    URL =f'https://www.w3schools.com/python/'
    # prefix=input("which prefix you want to exclude?\n").strip()
    get_courses(URL,'python')