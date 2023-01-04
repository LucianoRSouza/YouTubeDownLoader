#In order to install the library we must create a virtual environment into the folder we´ll create the program. 
# This is the comand on the terminal: python -m venv /Users/skneuropa/Desktop/Py-exercices/Pytube/venv
# command: python -m "the address of the folder" /venv

from pytube import YouTube

def Download(link):
    youtubeObect = YouTube(link)
    youtubeObect = youtubeObect.streams.get_highest_resolution()
    try:
        youtubeObect.download()
    except:
        print("There has been an error in downloading your youtube video")
    print("This download is completed! Yeah!")

link = input("Put your youtube link here!! URL: ")
Download(link)
