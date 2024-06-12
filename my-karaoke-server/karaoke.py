from typing import List

class Karaoke:
    def __init__(self):
        self.songs = {}
        self.cursor = 0
    
    def add_new_song(self,audio_src: any, sampling_rate: int = 16000) -> int:
        vocals, background = self.separate_vocals(audio_src,sampling_rate)
        pitch_info = self.get_pitch(vocals, sampling_rate)
        self.cursor += 1
        self.songs[self.cursor] = {
            "vocals": vocals,
            "background": background,
            "pitch_info": pitch_info,
            "sampling_rate":sampling_rate 
        }
        pass

    def get_songs(self) -> List[any]:
        return [v for v in self.songs.values()]

    def get_song(self, song_id: int) -> any:
        return self.songs[song_id]
    
    def separate_vocals(self,audio_src: any, sampling_rate: int = 16000)->tuple[any,any]:
        # TODO: get vocals and background from audio source
        return None,None
    
    def get_pitch(self, vocals_audio_src: any, sampling_rate: int = 16000) -> any:
        # TODO: get pitch information from the vocals
        return None

    def get_delete_song(self, song_id) -> None:
        del self.songs[song_id]