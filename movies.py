import bs4
import urllib.request as url
import pandas as pd
while True:
    print('''
             1. Date Of Release
             2. Genre
             3. Imdb Rating
             4. Kitni lambi hai movie
             5. Kon Kon Hai Movie Mein
             6. Summary of the Movie
             7. Review
             8. Nominations and Awards Won
             9. Bahaar nikaalo mujhe''')
    path="https://www.imdb.com/"
    http_response=url.urlopen(path)
    webpage = bs4.BeautifulSoup(http_response,'html.parser')
    newpath = path+"find?ref_=nv_sr_fn&q="
    movie_name=input("Enter Movie Name :")

    x=int(input("Kya Dekhna Hai : "))

    newpath1=newpath+movie_name
    http_response2 = url.urlopen(newpath1)
    webpage1= bs4.BeautifulSoup(http_response2,'html.parser')
    td=webpage1.find('td',class_="result_text")
    href=td.find('a')['href']
    newpath2=path+href
    http_response3=url.urlopen(newpath2)
    webpage2=bs4.BeautifulSoup(http_response3,'html.parser')
    if x==1:
        div=webpage2.find('div',class_="title_wrapper")
        year=div.find('h1')
        print(year.text)
    elif x==2:
        div=webpage2.find('div',class_="subtext")
        genre=div.findAll('a')
        print(genre)
    elif x==3:
        div=webpage2.find('div',class_="ratingValue")
        rating=div.find('span')
        print(rating.text)
    elif x==4:
        div=webpage2.find('div',class_="subtext")
        time=div.find('time')
        print(time.text)
    elif x==5:
        v=webpage2.find('table',class_="cast_list")
        c=v.findAll('tr',class_='odd')
        cast=[]
        cast2=[]
        
        for i in c:
            i=i.text
            cast.append(i)

        b=v.findAll('tr',class_='even')
        for i in b:
            i=i.text
            cast2.append(i)
        d=v.findAll('td',class_='character')
        cast3=[]
        for i in d:
            i=i.text
            cast3.append(i)

        caste=(cast+cast2+cast3)

        for i in range(len(caste)):
            caste[i] = caste[i].replace("'",' ')
            caste[i] = caste[i].replace(".",' ')
            caste[i] = caste[i].replace("\n",' ')
            caste[i] = caste[i].replace(",",' ')
            caste[i] = caste[i].replace("[",' ')
            caste[i] = caste[i].replace("]",' ')
        
        star=pd.DataFrame(caste)
        print(star)
    elif x==6:
        summ=webpage2.find('div',class_="inline canwrap")
        print(summ.text)
        
    elif x==7:
        review=webpage2.find('div',class_="user-comments")
        reviews=review.find('span')
        print(reviews.text)
    elif x==8:
        award=webpage2.find('div',class_="article highlighted")
        awards=award.find('span',class_="awards-blurb")
        print(awards.text)
    elif x==9:
        break
