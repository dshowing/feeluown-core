from fuocore.player import MpvPlayer
from fuocore.provider import providers
from fuocore.source import Source


class App(object):
    def __init__(self):
        self.player = MpvPlayer()
        self.source = Source()

    def list_providers(self):
        for provider in providers:
            yield provider

    def get_provider(self, name):
        for provider in providers:
            if provider.name == name:
                return provider
        return None

    def play(self, song_identifier):
        song = self.source.get_song(song_identifier)
        self.player.play_song(song)
