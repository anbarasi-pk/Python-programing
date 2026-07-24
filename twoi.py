class song:                                                                                                                                                                                                                                                                                                                                                                                                        
    def __init__(self,name):
        self.name=name
        self.next= None
class playlist:
    def __init__(self):
        self.head= None
    def create(self,song_name):
        new_song=Song(song_name)
        if self.head is None:
            self.head=new_song
        else:
            temp=self.head
            while temp.next:
                    temp=temp.next
            temp.next=new_song
        print(song_name,"  added to playlist")
    def insert_bsong(self,song_name):
        new_song=Song(song_name)
        new_song.next=self.head
        self.head=new_song
    def insert_esong(self,song_name):
        temp=self.head
        if temp and temp.song==song:
            self.head=temp.next
            print("Song deleted.")
            return
    prev=None
    while temp and temp.song!=song:
           prev=temp
           temp=temp.next
    if temp is None:
           print("Song not found.")

prev.next=temp.next
print("Song deleted.")
def display(self):
        if self.head is None:
            print("Playlist is empty.")
        else:
            temp=self.head
            print("\n Playlist:")
            while temp:
                print(temp.song,end="   ")
                temp=temp.next
                print("None")   
Playlist=playlist()
while True:
        print("\n---MUSIC PLAYLIST MENU---")
        print("1.Create Playlist")
        print("2.Insert song at beginning")
        print("3.Insert song at end")
        print("4.Delete song")
        print("5.Display Playlist")
        print("6.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            n=int(input("Enter the number of songs:"))
            for i in range(n):
                song=input("Enter song name:")
                playlist.create(song)
        elif choice==2:
             song=input("Enter song name:")
             playlist.insert_bsong(song)
        elif choice==3:
             song=input("Enter song name:")
             playlist.insert_esong(song)
        elif choice==4:
              song=input("Enter song name to delete:")
              playlist.display()
        elif choice==5:
             playlist.display()
        elif choice==6:
              print("Exiting..")
        else:
              print("Invalid choice!")
