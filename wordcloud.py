#wordcloud.py
#Jessica Napolitano jnapolit@conncoll.edu
#March 25, 2014
#This creates either a word cloud with a text file the user inputs or with a
#file that is defaulted. 


from graphics import*
from random import *
from time import sleep


"""This function displays a splash screen of a wordcloud showing the word 'word cloud'
in all different sizes, colors, and in different positions. This is a preview of
what will result from the program. For the position it picks a random number between
0 and 600 which is how big the window is. It picks a size between 5 and 90 because those
are the max and the min for font size in my graphics module. I went in and changed it from
32 to 90. I then use randrange to set a random color. I used sleep so that the splash screen would
flash for two seconds and then it would continue onto the next thing in the main."""
def splash_screen(win):    
    for i in range(50):
        message=Text(Point(randrange(0,600),randrange(0,600)), 'word cloud')        
        message.setSize(randrange(5,90))
        message.setTextColor(color_rgb(randrange(0,255),randrange(0,255),randrange(0,255)))
        message.draw(win)
    sleep(2)

#_______________________________________________________________________________________________   

"""This function is used in the default cloud and the custom cloud. It allows for the sorting of
the list of words and their frequencies. It sorts them from greatest occurance to least. the [1]
means that it is sorting it from the number rather than the word since the word comes first then
the number in the list. """
def sortFreq(value):
    return value[1]


#_______________________________________________________________________________________________

"""This function is what is initiated when the user does not have a specific text file they would like
to use. It is a simple program with very few words in it. """
def defaultCloud(win,numWords):
    #This clears the main menu and draws a button to go back after the word cloud is made
    win.delete('all')
    Text(Point(280,30),'Main Menu').draw(win)
    Rectangle(Point(240,40),Point(320,20)).draw(win)   
    
    #This opens the default file and puts it all into lower case. It then removes the punctuation
    #and splits it at the spaces. 
    defaultFile=open('default.txt','r',encoding="utf-8")
    defaultContents=defaultFile.read()
    defaultContents=defaultContents.lower()
    defaultContents=defaultContents.replace(':',' ')
    defaultContents=defaultContents.replace(':',' ')
    defaultContents=defaultContents.replace('"',' ')
    defaultContents=defaultContents.replace('"',' ')
    defaultContents=defaultContents.replace(',',' ')
    defaultContents=defaultContents.replace('.',' ')
    defaultContents=defaultContents.replace('!',' ')
    defaultContents=defaultContents.replace('?',' ')
    defaultContents=defaultContents.replace('(',' ')
    defaultContents=defaultContents.replace(')',' ')
    defaultContents=defaultContents.replace('[',' ')
    defaultContents=defaultContents.replace(']',' ')
    defaultContents=defaultContents.replace('}',' ')
    defaultContents=defaultContents.replace('{',' ')
    defaultContents=defaultContents.split()

    #This opens the stopwords file which includes all useless words such as the and to. It
    #lower cases them and splits them at the commas
    stopFile=open('stopwords.txt','r',encoding="utf-8")
    stopContent=stopFile.read()
    stopContent=stopContent.lower()
    stopContents=stopContent.split(',')

    #This retrieves how many words the user wants in the word cloud, creates and empty
    #freq dictionary, and then takes out all the stop words. It also records the freq
    #of the actual words we are interested in. Then it takes the dictionary and converts
    #it into a list. From there we use the sort method and put in the reverse=True so that
    #it sorts the freq from most occuring to least. 
    x=eval(numWords.getText())
    freq={ }
    for word in defaultContents:
        if word not in stopContent:
            if word in freq:
                freq[word] = freq[word]+1
            else:
                freq[word]=1
    freq_list=list(freq.items())
    freq_list.sort(key=sortFreq,reverse=True)

    #The following is in attempt to rid overlapping and cutting off at edges
    grid = 0
    if x < 100:
        grid = 10
    elif x < 225:
        grid = 15
    elif x < 400:
        grid = 20
    else:
        grid = 40   #max 1600 words
        
    #I then create and empy list where I make however many slots I need depending on
    #how many words the user inputs. I then shuffle these slots, pop the last one out
    #and use this for get my position into the xyList. The +50 in the math accounts
    #for not getting cut off at the sides. The (500/grid)/2 makes the words appear
    #in the center of each grind. 
    gridSlots = []
    for i in range(grid*grid):
        gridSlots.append(i)
    shuffle(gridSlots)
    xyList = []
    for i in range(x):
        pos=gridSlots.pop()
        xyList.append(Point((pos//grid)*(500/grid)+50+(500/grid)/2,(pos%grid)*(500/grid)+50+(500/grid)/2))
    #I then set the initial size to 90 because the first word in the list is the one that occurs
    #the most thus it is the one that must be the largest. 
    wordSize=90

    #This loops through for however many words the user wants in their word cloud. It also
    #picks a random color between 0 and 255 to use that the color of the words. As far as the
    #word sizing, it starts out at 90 and for each word after that it drops down 10. The minimum
    #it can drop to is 12. So eventually all the words will end up being the same size. 
    for words in freq_list[0:x]:        
        wordDrawn=Text(xyList.pop(),words[0])#gets position
        r=0
        g=0
        b=0
        r_delta=randrange(0,255)/x
        g_delta=randrange(0,255)/x
        b_delta=randrange(0,255)/x
        for i in range(x):
            r=r+r_delta
            g=g+g_delta
            b=b+b_delta
        wordDrawn.setTextColor(color_rgb(r,g,b))#gets color
        wordSize=wordSize-10
        wordSize=min(90, max(12, wordSize))
        wordDrawn.setSize(wordSize)#get size
        wordDrawn.draw(win)#draws
        

    defaultFile.close()
#___________________________________________________________________________________________________________         

"""This function is the same exact thing as the defaultCloud however this one takes the
file name input from the user and then opens that specific file. The file I used to test it is also
in the file that I submitted. It is of a recipe. It is called test.txt."""
def customCloud(win,numWords,customFile):
    
    win.delete('all')
    Text(Point(280,30),'Main Menu').draw(win)
    Rectangle(Point(240,40),Point(320,20)).draw(win)


    customFile=customFile.getText()
    customFile=open(customFile,'r',encoding="utf-8")
    customContents=customFile.read()
    customContents=customContents.lower()
    customContents=customContents.replace(':',' ')
    customContents=customContents.replace(':',' ')
    customContents=customContents.replace('"',' ')
    customContents=customContents.replace('"',' ')
    customContents=customContents.replace(',',' ')
    customContents=customContents.replace('.',' ')
    customContents=customContents.replace('!',' ')
    customContents=customContents.replace('?',' ')
    customContents=customContents.replace('(',' ')
    customContents=customContents.replace(')',' ')
    customContents=customContents.replace('[',' ')
    customContents=customContents.replace(']',' ')
    customContents=customContents.replace('}',' ')
    customContents=customContents.replace('{',' ')
    customContents=customContents.split()

    stopFile=open('stopwords.txt','r',encoding="utf-8")
    stopContent=stopFile.read()
    stopContent=stopContent.lower()
    stopContents=stopContent.split(',')
    
    x=eval(numWords.getText())
    freq={ }
    for word in customContents:
        if word not in stopContent:
            if word in freq:
                freq[word] = freq[word]+1
            else:
                freq[word]=1
    freq_list=list(freq.items())
    freq_list.sort(key=sortFreq,reverse=True)

    #for random positions and color
    grid = 0
    if x < 100:
        grid = 10
    elif x < 225:
        grid = 15
    elif x < 400:
        grid = 20
    else:
        grid = 40   #max 1600 words	
    
    gridSlots = []
    for i in range(grid*grid):
        gridSlots.append(i)
    shuffle(gridSlots)
    xyList = []
    for i in range(x):
        pos=gridSlots.pop()
        xyList.append(Point((pos//grid)*(500/grid)+50+(500/grid)/2,(pos%grid)*(500/grid)+50+(500/grid)/2))

    wordSize=90
    
    for words in freq_list[0:x]:        
        wordDrawn=Text(xyList.pop(),words[0])#gets position
        r=0
        g=0
        b=0
        r_delta=randrange(0,255)/x
        g_delta=randrange(0,255)/x
        b_delta=randrange(0,255)/x
        for i in range(x):
            r=r+r_delta
            g=g+g_delta
            b=b+b_delta
        wordDrawn.setTextColor(color_rgb(r,g,b))#gets color
        wordSize=wordSize-10
        wordSize=min(90, max(12, wordSize))
        wordDrawn.setSize(wordSize)#get size
        wordDrawn.draw(win)#draws
    
    customFile.close()

#____________________________________________________________________________________________

"""This function draws all the buttons and input boxes for the main menu. It also
takes into account for what happens when the user clicks the buttons by utilizing while statements"""
def mainMenu(win):
    
    #background
    background=Rectangle(Point(0,600),Point(600,0))
    background.setFill('pink')
    background.draw(win)
    
    #sets txt for inputs
    Text(Point(225,100),'How many words would you like to display in your word cloud?').draw(win)
    Text(Point(280,250),"If you have a file you would like to use, input name here").draw(win)
    Text(Point(280,420),'Or you can just use a default file').draw(win)
    
    #button for word cloud with custom file
    fileButton=Rectangle(Point(220,335),Point(340,365))
    fileButton.setFill('plum3')
    fileButton.draw(win)
    Text(Point(280,350),'Create Cloud').draw(win)    

    #button for word cloud with default file
    defaultButton=Rectangle(Point(220,440),Point(340,475))
    defaultButton.setFill('LightSkyBlue1')
    defaultButton.draw(win)
    Text(Point(280,455),'Create Cloud').draw(win)

    #button to exit
    exitButton=Rectangle(Point(250,180),Point(315,130))
    exitButton.setFill('PeachPuff2')
    exitButton.draw(win)
    exitText=Text(Point(280,155),'Exit')
    exitText.setSize(24)
    exitText.draw(win)

    #makes entry field for number of words in cloud
    numWords=Entry(Point(515,100),15)
    numWords.setText('Enter # (max1600)')
    numWords.setFill('PaleGreen2')
    numWords.draw(win)

    #makes entry field for filename
    customFile=Entry(Point(280,290),15)
    customFile.setText('      filename.txt')
    customFile.setFill('PaleGreen2')
    customFile.draw(win)

    pt=win.getMouse()

    #while they are not clicking the exit
    while not ((pt.getX()>=250 and pt.getX()<=315) and\
        (pt.getY()>=130 and pt.getY()<=180)):

        #if they click the custom cloud button execute that function
        if ((pt.getX()>=220 and pt.getX()<=340) and\
        (pt.getY()>=335 and pt.getY()<=365)):
            customCloud(win,numWords,customFile)
            pt=win.getMouse()

            #if they hit the main menu button then take them back to the beginnning screen
            if ((pt.getX()>=240 and pt.getX()<=320) and\
            (pt.getY()>=20 and pt.getY()<=40)):
                win.delete('all')
                mainMenu(win)
                
        #else if they click the default cloud then run that function   
        elif (pt.getX()>=220 and pt.getX()<=340) and\
        (pt.getY()>=440 and pt.getY()<=475):
            defaultCloud(win,numWords)
            pt=win.getMouse()

            #if they hit the main menu button then take them back to the beginning screen
            if ((pt.getX()>=240 and pt.getX()<=320) and\
            (pt.getY()>=20 and pt.getY()<=40)):
                win.delete('all')
                mainMenu(win)
                
    #if they click the exit button then close            
    win.close()



#______________________________________________________________________________________________    

"""This is the main function that calls and executes all the functions above"""
def main():
    
    win=GraphWin('word cloud',600,600)
    splash_screen(win)
    #deletes what is draw on the screen after the splash screen
    #so that the main menu has room to appear
    win.delete('all')    
    mainMenu(win)
    
    

main()
