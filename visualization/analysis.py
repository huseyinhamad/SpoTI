import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv("../data/trackFeatures.csv")
    df.insert(loc=0, column='Playlist Name', value=df['playlistName'])
    df.insert(loc=1, column='Track Name', value=df['trackName'])
    df = df.drop(columns=['Unnamed: 0', 'trackName', 'playlistName'])

    fig = plt.figure(figsize=(100, 50))
    playlists = df['Playlist Name'].unique()
    means = df.groupby('Playlist Name').mean()

    plt.bar(playlists, means['danceability'], color='maroon',
            width=0.4)
    plt.xlabel("User Playlists")
    plt.xticks(rotation=90)  # Rotates X-Axis Ticks by 45-degrees
    plt.ylabel("Danceability")
    plt.title("Playlists / Danceability")
    plt.show()