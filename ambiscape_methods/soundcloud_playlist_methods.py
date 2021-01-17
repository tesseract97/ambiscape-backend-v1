from sclib import SoundcloudAPI, Playlist
import os


def get_playlist(playlist_name):
    playlist_name_formatted = playlist_name.replace(" ", "-").replace("'", "")
    url = 'https://soundcloud.com/tessssa8/sets/'+ playlist_name_formatted
    try:
        dir_path = os.curdir + f"/mp3_files/{playlist_name_formatted}"
        os.mkdir(dir_path)
    except OSError:
        return 1
    try:
        api = SoundcloudAPI()
        playlist = api.resolve(url)

        assert type(playlist) is Playlist

        for track in playlist.tracks:
            filename = os.curdir + f'/mp3_files/{playlist_name_formatted}/{track.artist} - {track.title}.mp3'
            print(filename)
            with open(filename, 'wb+') as fp:
                track.write_mp3_to(fp)

        return 0
    except Exception:
        return 1
