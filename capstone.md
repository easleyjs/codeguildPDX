w3.bbs - A Tribute to 90's PC Bulletin Board Systems (BBSes)
============================================================

## By J. Easley  

Project Overview
This project will attempt to replicate the appearance, features, and experience of accessing a 1990s-era PC-based BBS. The primary functionality I'll focus on replicating is the multi-user message board that BBSes provided. While some of the BBS software from the 90's has been modified to accept Telnet connections, and there are some in-browser Java-based Telnet applications, this is an attempt to offer a "native" experience.

The development stack will be the following:
Model/DB - Django/SQLite (ported to a RDBMS if I have time)
Controller - Django (Views returning JSON)
View - Vue.js  

User Stories
--Tasks

Data Models
* User
* Message

Schedule
--Week 1: Multi-User Message List
----Unstyled HTML in place, Models created, User creation/multi-user working, Message Board topic areas and individual messages accessible.
----Possibly, messages/topic areas rendered with vanilla JS for proof-of-concept/testing the models.

--Week 2: Main Menu, Enhanced message controls, AJAX functionality.
----Main menu with links to the message board/features.
----Users will have the ability to reply to messages/create threads.
----Implementation of Vue.js to render pages/handle functionality

--Week 3: CSS/UI
----Implementation and styling of CP437 Vintage IBM font.
----Retro "DOS"/ANSI styling of existing HTML
----Keyboard navigation/hotkeys implemented

--Week 4: Additonal Features, Testing
----If time permits, will implement some of the features in "Really great to have(s)"
----Testing to ensure that all planned features were sucessfully implemented.

--Essential Features:
* User system/authentication system
* Message Board with topic areas which are drilled down into for individual messages.

--Really great to have:
* "Last 10 Callers" display on Main menu
* User Profile editor
* Some type of trivia game/text-based game.

--Nice-to-have:
* Files (downloads section)
* Chat Room
* Additonal games
