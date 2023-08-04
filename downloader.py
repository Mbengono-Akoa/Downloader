from pytube import YouTube

def download(link):
    youtubeobject = YouTube(link)
    youtubeobject = youtubeobject.streams.get_highest_resolution()
    try:
        youtubeobject.download()
    except:
        print("There is a problem with your download!!!")
    print("Your video has been downloaded!!!")    
    
link = input("Enter your video link: ")    
download(link)