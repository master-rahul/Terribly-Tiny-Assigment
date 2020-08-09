import requests

import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
def num ():
    count = 0;  
    word = "";  
    maxCount = 0;  
    words = [];  

    #Opens a file in read mode
    url = 'https://terriblytinytales.com/test.txt'
    r = requests.get(url, allow_redirects=True)
    #req = urllib2.Request('https://terriblytinytales.com/test.txt')
    #response = urllib2.urlopen(req)
    open('data.txt', 'wb').write(r.content)
    #file = response.read()
    file = open("data.txt", "r")  
          
    #Gets each line till end of file is reached  
    for line in file:  
        #Splits each line into words  
        string = line.lower().replace(',','').replace('.','').split(" ");  
        #Adding all words generated in previous step into words  
        for s in string:  
            words.append(s);  
       
    #Determine the most repeated word in a file  
    for i in range(0, len(words)):  
        count = 1;  
        #Count each word in the file and store it in variable count  
        for j in range(i+1, len(words)):  
            if(words[i] == words[j]):  
                count = count + 1;  
                  
        #If maxCount is less than count then store value of count in maxCount  
        #and corresponding word to variable word  
        if(count > maxCount):  
            maxCount = count;  
            word = words[i];  
              
    print("Most repeated word: " + word);  
    file.close();
button1 = tk.Button(text='Get the Square Root', command=num)
canvas1.create_window(200, 180, window=button1)


  
root.mainloop()
