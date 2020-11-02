# Album Artwork for Mac Screensaver

This script might be very niche, but I have gotten great use out of it and wanted to use it as a portfolio builder.

I don't use iTunes, but have a ton of random mp3 files from DJing and making mixes. I wanted these files to have album artwork so that I could use
the "Album Artwork" screensaver on my Mac. 

&nbsp;-------

Basically, it takes the name of a .mp3 file, say:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**love-lies-louis-the-child-remix.mp3**

and searches for that exact name on SoundCloud. Therefore, it only searches for songs with logical names. Files like:

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**hir0.mp3** or **aaf83hge9g.mp3**
 
 will not be searched. Any errors encountered along the way will move the files to a refused folder for your review.
 
 It then clicks the first search result and saves that image. So, if your search might bring up the name of a SoundCloud user instead of a song, it will return an error. 
 This is also why, sometimes, the album artwork that you were expecting and the album artwork that you got, will be different. Some more popular songs will
 show up before the song you were expecting, and therefore the images might get mixed up. This seems to be the only real issue with the code.
 
 After downloading the image, it then adds the ID3 data such as the album and artist. iTunes requires an album and artist name for the artwork to be included
 in the screensaver. For this, the code just attaches random words as fillers. The updated files are then moved to a new folder from where you can filter the 
 songs that you want in your library.
 
 &nbsp;-------
 
 # File Path Naming Conventions
 
**org_musicfolder** is the folder that holds all of your music files

**ref_musicfolder** is the folder that will hold the refused files

**artfolder** is the folder that will hold all of the art files

**driver_path** is the folder that holds the ChromeDriver file***

**new_musicfolder** is the folder that will hold all of the new music files with artwork 
 
&nbsp;

***It should be noted that the code makes use of Selenium's ChromeDriver, so the actual driver file must be downloaded on your computer.
