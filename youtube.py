from pytube import YouTube
link = input("enter the video link hear->")

y_tube = YouTube(link)
print =(f"video title->{y_tube.title}")
stream =y_tube.streams.all()
video =list(enumerate(stream))
for i in video:
    print(i)
print("==========================")
index =int(input("give the index of the desired stream =="))
stream[index].download()
print("sucesfully download video")
                     