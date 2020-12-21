#from DefiningClasses.Practise.project import song as s, album as a

class Band:
    def __init__(self, name):
            self.name = name

    albums=[]

    def add_album(self,album):
        for band_album in self.albums:
            if album.name==band_album.name:
                return f'Band {self.name} already has {album.name} in their library.'
        else:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self,album_name: str):
        for band_album in self.albums:
            if album_name==band_album.name:
                if band_album.published:
                    return f'Album has been published. It cannot be removed.'
                else:
                    self.albums.remove(band_album)
                    return f'Album {album_name} has been removed.'

        else:
            return f'Album {album_name} is not found.'

    def details(self):
        output=f'Band {self.name}\n'
        for album in self.albums:
            output+=f'{album.details()}'
        return output

#song = s.Song("Running in the 90s", 3.45, False)
#song1 = s.Song("Bla-bla", 3.45, False)
#print(song.get_info())
#album = a.Album("Initial D")
#second_song = s.Song("Around the World", 2.34, False)
#print(album.add_song(song))
#print(album.add_song(song1))
#print(album.details())
#print(album.publish())
#band = Band("Manuel")
#print(band.add_album(album))
#print(band.remove_album("Initial D"))
#print(band.details())
#print(band.details())

