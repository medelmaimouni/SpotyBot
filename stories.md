## story_001
* greeting
  - utter_greet
* get_artist
  - utter_ask_artist_name
* get_artist{"artist_name": "Labess"}
  - slot{"artist_name": "Labess"}
  - get_track
  - utter_subscribe


## story_002
* greeting
  - utter_greet
* get_artist{"artist_name": "Snor"}
  - slot{"artist_name": "Snor"}
  - get_track
  - utter_subscribe
* subscription
  - slot{"subscribe": "True"}
  - subscribe_user

## Track query with artist_name
* greeting
    - utter_greet
* get_artist
    - utter_ask_artist_name
* get_artist{"artist_name": "ElGrandeToto"}
    - slot{"artist_name": "ElGrandeToto"}
    - get_track
    - slot{"artist_name": "ElGrandeToto"}
    - utter_subscribe
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}

## Request with artist name provided
* greeting
    - utter_greet
* get_artist{"artist_name": "Draganov"}
    - slot{"artist_name": "Draganov"}
    - get_track
    - slot{"artist_name": "Draganov"}
    - utter_subscribe
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}

## When user directly asks for subscription
* greeting
    - utter_greet
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}
