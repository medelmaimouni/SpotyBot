from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import spotify_client
from spotify_creds import client_id, client_secret

class GetTrack(Action):

    def name(self):
        return "get_artist"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        
        user_artist_name= tracker.get_slot('artist_name')

        client = SpotifyAPI(client_id, client_secret)

        artist_object = client.search(user_artist_name)
        artist_id = artist_object['artists']['items'][0]['id']
        tracks_object = client.get_track(artist_id)
        tracks_object = client.get_track(artist_id)['tracks']
        track_object = tracks_object[random.randin(0,len(tracks_object))]
        track_name = track_object['name']
        track_url_preview = track_object['preview_url']



        dispatcher.utter_message(track_name)
        return [SlotSet("artist_name", user_artist_name)]

    
class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        subscribe = tracker.get_slot('subscribe')
        if subscribe == "True":
            response = "You're successfully subscribed"
        if subscribe == "False":
            response = "You're successfully unsubscribed"

        dispatcher.utter_message(response)
        return [SlotSet("subscribe", subscribe)]
    
    
    