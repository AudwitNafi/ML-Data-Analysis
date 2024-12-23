from abc import ABC, abstractmethod
class MP4MediaPlayer(ABC):
    def play_mp4(self, filename):
        pass
    
class VLCMediaPlayer(ABC):
    def play_vlc(self, filename):
        pass
    
class MediaPlayer:
    def __init__(self):
        pass
    def play_mp3(self, filename):
        #check if filename ends with .mp3 extension
        if filename.split(".")[1]=="mp3":
            print(f"Playing song: {filename}")
        else:
            print(f"Unsupported file format: {filename}")
    
class MP3MP4Adapter(MP4MediaPlayer):
    def __init__(self, media_player: MediaPlayer):
        self.media_player = media_player
    def play_mp4(self, filename):
        #convert mp4 file to mp3 format
        print("Converting mp4 file to mp3 format...")
        name = filename.split(".")
        name[1] = "mp3"
        converted_filename = (".").join(name)
        self.media_player.play_mp3(converted_filename)
    
class MP3VLCAdapter(VLCMediaPlayer):
    def __init__(self, media_player: MediaPlayer):
        self.media_player = media_player
    def play_vlc(self, filename):
        #convert mp4 file to mp3 format
        print("Converting VLC file to mp3 format...")
        name = filename.split(".")
        name[1] = "mp3"
        converted_filename = (".").join(name)
        self.media_player.play_mp3(converted_filename)
        
if __name__ == "__main__":
    media_player = MediaPlayer()
    media_player.play_mp3("title_song.mp3")
    
    mp4_player = MP3MP4Adapter(media_player)
    mp4_player.play_mp4("random_song.mp4")
    
    vlc_player = MP3VLCAdapter(media_player)
    vlc_player.play_vlc("video_game.vlc")