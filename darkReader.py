'''  RSS - Dark Reader

Description:  An RSS windowed reader to read while you work, simple interface, and more feeds can be added as needed.  Current url is darkreading.com.

Author: Nick Sepe
License: The Unlicense


'''
#import windowing and rss parser
import tkinter
import feedparser
import webbrowser


def rssUrl():
    link = []
    title = []
    url = "https://www.darkreading.com/rss_simple.asp?f_n=645&f_ln=Application%20Security"
    d = feedparser.parse(url)
    for i in range(0,19,1):
        title.append(d.entries[i].title)
        link.append(d.entries[i].link)
    print(link)


#create a new window
window = tkinter.Tk()
#set the window title
window.title("Dark Reader")
#set the window icon


#def callback(url):
    #webbrowser.open(url, new=1)


#create a new button, and provide an argument called 'command'
#which in this case calls a function called 'callback'
#for i in range (0,19,1):
    #btn = tkinter.Button(window, text=title[i], command=callback(link[i]))
    #btn.pack()

#draw the window, and start the 'application'
window.mainloop()


rssUrl()
