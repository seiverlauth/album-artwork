#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:03:55 2020

@author: seiverlauth
"""
import os,glob,re,time,urllib.request,shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from mutagen.easyid3 import EasyID3
from essential_generators import DocumentGenerator


'''
The following paths are specific to my machine (macOS). 
Read the readme.md file for correct naming convensions of the file paths.
'''
org_musicfolder = '/Users/seiverlauth/Desktop/Orange/Music/music/'
ref_musicfolder = '/Users/seiverlauth/Desktop/Orange/Music/Refused/'
artfolder = '/Users/seiverlauth/Desktop/Orange/Music/artwork/PythonArtwork/'
driver_path = '/Users/seiverlauth/Desktop/Orange/Python/driver/chromedriver'
new_musicfolder = '/Users/seiverlauth/Desktop/Orange/Music/PythonAltered/'

i = 0           # Should always be zero, starting index
end = 71            # How ever many songs you would like analyzed...




'''
No need to edit further...
'''

os.chdir(org_musicfolder)
files = glob.glob(org_musicfolder+"*.mp3")

options = Options() 
options.headless = True 

gen = DocumentGenerator() 

class File:
    def __init__(self,path):
        self.path = path
        file = (os.path.basename(path).split(".mp3")[0])
        file = re.sub(r'\W',' ',file)
        file = re.sub('_',' ',file)
        file = re.sub(r'\d',' ',file)
        file = re.sub('  ',' ',file)
        self.name = file
    def __str__(self):
        return 'Current file: ' + self.name
    
def format_name(name,path):
    if len(name) < 10:
        shutil.move(path,ref_musicfolder+'SHORTNAME_'+name.replace(' ','-')+".mp3")
        return  name + ' did not satisfy search requirements'
    else:
        pass  

def url(name):
    words = re.findall(r'[^\s]+',name)
    url = ('https://soundcloud.com/search?q=')
    for j in words:
        url += '%20'+j
    return url
    
def search(url):
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get(url)
        time.sleep(2)
        art = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div/ul/li[1]/div/div/div/div[1]/a')
        art.click()
        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)
        ps = driver.page_source
        start_url = re.search('https://i1.sndcdn.com/artworks-',ps)
        end_url = re.search('500x500.jpg',ps)
        photo_url = ps[start_url.start():end_url.end()]
        driver.close()
        driver.quit()
        return photo_url
    
def analyze(photo_url,path,name):
    if photo_url == '':
        shutil.move(path,ref_musicfolder+'URL_TypeERROR_'+name.replace(' ','-')+".mp3")
        return 'URL is blank...'
    elif len(photo_url) > 75:
        shutil.move(path,ref_musicfolder+'URL_LenERROR'+name.replace(' ','-')+".mp3")
        return 'URL is too long...'
    else:
        urllib.request.urlretrieve(photo_url, artfolder+name.replace(' ','-')+".jpg") 
        return 'Saved!'
    
def audio(path,name):
    try:   
        audio = MP3(path, ID3=ID3)
        try:
            audio.add_tags()
        except:
            pass
        audio.tags.add(APIC(mime='image/jpg',type=3,desc=u'Cover',data=open(artfolder+name.replace(' ','-')+".jpg",'rb').read()))
        audio.save()
        shutil.move(path,new_musicfolder+name.replace(' ','-')+".mp3")
        aspects = EasyID3(new_musicfolder+name.replace(' ','-')+".mp3")
        aspects['Artist'] = gen.word() + gen.word()
        aspects['Album'] = gen.word() + gen.word()
        aspects['Title'] = name
        aspects.save()
        return('Success!')
    except:
        shutil.move(files[i],ref_musicfolder+'CORRUPT'+name.replace(' ','-')+".mp3")
        return('This file is most liklely corrupt.')

errors = 0
nonimports = 0
success = 0

while i < end:
    print()
    file = File(files[i])
    path = file.path
    name = file.name
    print(str(i+1)+' out of '+str(end)+' files')
    print(file)
    print()
    
    test_name = format_name(name,path)
    if test_name is not None:
        print(test_name)
        print()
        i += 1
        nonimports += 1
        continue
    else:
        pass

    try:
        print('Generating URL...')
        link = url(name)
        print('Searching...')
        photo = search(link)
        print('Analyzing link...')
        test_url = analyze(photo, path, name)
        time.sleep(1)
        if test_url != 'Saved!':
            print(test_url)
            print()
            i += 1
            nonimports += 1
            continue
        else:
            print(test_url)

        
        saved_file = audio(path,name)
        if saved_file != 'Success!':
            print(saved_file)
            print()
            i += 1
            errors += 1
            continue
        else:
            print(saved_file)
            print()
            success += 1
    except KeyboardInterrupt:
        print('\nStopped')
        i = 1000
        break
    except:
        print('There was an error...')
        shutil.move(files[i],ref_musicfolder+'ERROR'+name.replace(' ','')+".mp3")
        errors += 1
    
    i += 1
   
print()
print('Successful downloads : {}'.format(success))
print('Failed downloads : {}'.format(errors))
print('Refused downloads : {}'.format(nonimports))
    
    
    
    
    
    
        


