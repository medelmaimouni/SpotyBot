This document synthetizes and explain what SpotyBot aim to do. Let we begin by its context of the development.

## Context: SpotyBot is a chatbot for recommending and suggesting track titles for a specific artist on Spotify.

## SPOTYBOT ’S SCOPE
As a friend, SpotyBot shoud be able to:

•	Greet users dynamically
•	Understand whether user is asking for playlists, track, recommendations
•	Ask again for the artist name if he didn’t catch user’s responses
•	Furthermore, support user to pick an artist name


Before any further developments, we should list our bot’s intents, i.e the intention of users when chatting with SpotyBot 

## SPOTYBOT ’S INTENT
•	Default welcome: when receiving the first message from user (for the session)
•	Get Music Intent: User asking for a music to listen
•	Get Artist Intent: User telling the artist to who he wants to listen
•	Get track trial: User confirms a song ( => direct him to a trial for a try)
•	
•	User thanks: SpotyBot have to reply to thank you messages 

## ENTITIES
•	Artist_items

Let us simulate a scenario where the user wants some Labess music

## Prototype
User:  Hello!
SpotyBot : Hello and welcome, how may I help you?
User: I want to listen to some music
SpotyBot : Sure, do you have a specific artist in mind ?
User: Yeah sure, I want to listen to Labess
SpotyBot: Voilà – what about Leila track, do you want a trial
User: Sure, I do
SpotyBot : You can listen to this track, by visiting : WWW
User: Thanks
SpotyBot : Thank you for your trust, SpotyBot is in your service
