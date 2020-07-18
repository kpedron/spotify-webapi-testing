import unittest
from Resources import utils as Utils
from Requests.request_oauth2 import MyOAuth2
from Requests.requests import Requests


class Playlists(unittest.TestCase):

    def setUp(self):
        self.data = Utils.load_json_file("data.json")

        # Get Token
        oauth2 = MyOAuth2()
        self.token = oauth2.access_token_get(self.data["client_id"],
                                             self.data["client_secret"],
                                             self.data["scope"],
                                             self.data["callback_uri"],
                                             self.data["token"])

        self.access_token = self.token["access_token"]
        self.request = Requests()

    def test_get_playlists(self):
        response = self.request.playlists_get(self.access_token, "kpedron")

        assert response.status_code == 200

    def test_create_new_playlist(self):
        body = {
            "name": "Playlist Python",
            "description": "Essa playlist foi criado via python requests",
            "public": True
        }

        response = self.request.playlist_create(self.access_token, "kpedron", body)
        assert response.status_code == 201

    def tearDown(self):
        # Update the access token and refresh token in data.json
        self.data["token"] = self.token
        Utils.update_json_file("data.json", self.data)
