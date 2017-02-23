from mutagen import File
from library_management.models import Song, Metadata


class SongMetadataLoader:
    def __init__(self, song_instance):
        self.song_instance = song_instance
        self.name = None
        self.album = None
        self.artist = None
        self.load_metadata_from_file()

    def load_metadata_from_file(self):
        file_path = self.song_instance.song_file.file.name
        audio_file = File(file_path)
        self.name = str(audio_file.get('TIT2', None))
        self.album = str(audio_file.get('TALB', None))
        self.artist = str(audio_file.get('TPE1', None))

    def populate_metada_for_song(self):
        new_metadata = Metadata.objects.create(name=self.name,
                                               album=self.album,
                                               artist=self.artist)
        self.song_instance.metadata = new_metadata
        self.song_instance.save()
