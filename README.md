# Album Artwork for Mac Screensaver

This script might be very niche, but I have gotten great use out of it and wanted to use it as a portfolio builder.

I don't use iTunes, but have a ton of random mp3 files from DJing and making mixes. I wanted these files to have album artwork so that I could use
the "Album Artwork" screensaver on my Mac. 

&nbsp;-------

Basically, it takes the name of a .mp3 file, say:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**lotus-eater-pluko-flip(1).mp3**

![](images/Before.png)

and searches for that exact name on SoundCloud. It removes any dashes, underlines, and anything else that might prevent the correct result from showing. Because of
this, it only searches for songs with logical names. Files like:

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**hir0.mp3** or **aaf83hge9g.mp3**
 
 will not be searched.
 
 It then clicks the first search result and saves that image. Right now, and due to the ambiguity of some of the file names, there is no distinction between what is
 the correct album artwork and what is not. But, assuming that the file name was specific enough, the file will be moved out of the original music folder and into a
 new, modified one.
 
 ![](images/After.png)
 
 After downloading the image, it then adds the ID3 data such as the album and artist. iTunes requires an album and artist name for the artwork to be included
 in the screensaver. For this, the code just attaches random words as fillers, see below.
 
 ![](images/iTunes.png)
 

 
 
 
 &nbsp;-------
 
 ### File Path Naming Conventions
 
**org_musicfolder** is the folder that holds all of your music files

**ref_musicfolder** is the folder that will hold the refused files

**artfolder** is the folder that will hold all of the art files

**driver_path** is the folder that holds the ChromeDriver file***

**new_musicfolder** is the folder that will hold all of the new music files with artwork 
 
&nbsp;

***It should be noted that the code makes use of Selenium's ChromeDriver, so the actual driver file must be downloaded on your computer.
