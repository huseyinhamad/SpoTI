import spotipy
import essentials.scopes as scopes
import essentials.functions as funcs
from spotipy.oauth2 import SpotifyOAuth

if __name__ == '__main__':
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="d6aba6218ec04200bddec389a859c8c4",
                                                   client_secret="276c6b885b374d8ca4291764b28e0c40",
                                                   redirect_uri="http://localhost:5000",
                                                   scope=scopes.userLibraryRead + " " + scopes.currentPlaying))
    funcs.getCurrentPlaying(sp)
    userPlaylistsIDs, userPlaylistsNames = funcs.getUserPlaylists(sp)
    for i in range(len(userPlaylistsIDs)):
        print(userPlaylistsIDs[i], ":", userPlaylistsNames[i])

    allPlaylistsTracks = funcs.getAllPlaylistTracks(sp, playlistIds=userPlaylistsIDs, playlistNames=userPlaylistsNames)
    trackFeatures = funcs.getTrackFeatures(sp, tracks=allPlaylistsTracks)
    dfTrackFeatures = funcs.convertTrackFeaturesToDataFrame(trackFeatures)
    print(dfTrackFeatures.tail())