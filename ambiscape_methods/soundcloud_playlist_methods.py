from sclib import SoundcloudAPI, Playlist


def get_playlist(playlist_name):
    playlist_name_formatted = playlist_name.replace(" ", "-").replace("'", "")
    print(playlist_name_formatted)
    url = 'https://soundcloud.com/tessssa8/sets/'+ playlist_name_formatted
    print(url)
    try:
        api = SoundcloudAPI()
        playlist = api.resolve(url)

        assert type(playlist) is Playlist

        for track in playlist.tracks:
            filename = f'../mp3_files/{track.artist} - {track.title}.mp3'
            print(filename)
            with open(filename, 'wb+') as fp:
                track.write_mp3_to(fp)

        return 0
    except Exception:
        return 1
