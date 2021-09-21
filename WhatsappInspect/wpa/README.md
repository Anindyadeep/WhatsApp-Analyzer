# Whatsapp-Analysis-version-1.0.5
This is the version 1 of this project, some more insights with some NLP techniques would be used to track some more insights form the group chat and all,
which will all come in the next versions


## Changes made
1. Fixed different bugs
2. Made the full system modular, in order to make the library and publish.
3. Genaralised the whole thing for platform independency
4. Documented the essential code params

## Features and how to use
This total project is continuously evolving as I am learning newer stuffs, though the version v1.0.1 came too late.
This version is totally modularised, and is abstracted in such a way that user can easily use the classes and come out with other great stuffs out of it. 
As well as, when visualisation is concerened, this project would be perfect fit for this, as all sorts of different visualizations tasks are also available.

**Here we go to the main features available here**

#### Features in `functions.py` 
This module is fully focussed to get all the tabular data for the whatsapp groups or for a specific user in the whatsapp groups
Calling the class, is done some way like this.

```py
from functions import WpFunctions
wpf = WpFunctions(path)
```
Here `path` argument is the path to the exported whatsapp chats of a groups or a chats.

```py
user_stats_data = wpf.get_stats_frame()
```
This will return a dataframe where all the user statstics will be retrived from those chats in a cleaned manner. Here are the columns of the `user_stats_data` dataframe:
```
1. User             : Specifying the unique user name or the number
2. Total_msg        : Total number of messages sent by the user.
3. Total_media      : Total number of medias (like pics, videos, gifs, sticker) sent by the user.
4. Total_link       : Total number of links sent by the user.
5. Emojies          : Different number emojies sent by the user.
6. Total_emojies    : Total number of emojies sent by the user.
```

Here is the another dataframe function specially made for analysising the emojies used in the chats
```py
emojies_used = wpf.get_all_emojies_used()
```
This will return the dataframe containing these information all follows:
```
1. Emoji            : The unique emojies used in the chats
2. Emoji_desc       : Those emojies are demojised, and the descriptions of the emojies are extracted
3. Emoji_frequency  : The number of times, those emojies are used in the chats
```
Users can take this data as well as the `user_stats_data` and analyse sentiments very easily, though the sentiment analysis feature is comming soon on the next versions.

Here is an another dataframe function that is made for full fleged data analysis, containing all sort of information about users as well as all other informations related informations related to the chats
```py
data  = wpf.get_data_to_plot()
```
This will return the dataframe containing these information all follows:

```
1. Date_Time        : Specifying the date and the time, when the user sent the message
2. Date             : The date (only) in which the user sent the message
3. Time             : The time (only) in which the user sent the message
4. User             : Specifying the unique user name or the number
5. Msg              : The raw message of the user
6. msg_text_only    : The cleaned message sent by the user
7. Day_of_week      : In which day of the week the message has been sent
8. Hour             : In which hour of the time, the message has been sent
```

Here is one another amazing function provided, which will return all the specific information of either the user (if exists) or all the users conraining in the groups, in just one line. For getting the information of all the users in the group use this, here `ALL` means, that retrive info all users in group

```py
wpf.get_full_track_msgs('ALL')
```
For getting the information of a single user, just use this:
```py
wpf.get_full_track_msgs('Anindya') # where Anindya is a example user name
```
Here `Anindya` is the username, and this will only return if the user exists in the group, and **this is case sensitive, keeping name redundacy in mind.**
This a sample output returned when used for a specfic user:
```
The name of the user is:   Anindya
The total no of messages sent by  Anindya  is:  51
The total number of media (including the pics, vids, gifs, stickers by  Anindya  is:  3
The total number of links sent by  Anindya  is:  0
The total number of emojies sent by  Anindya  is:  4
The emojies used by  Anindya  are:  ['🤔', '🎂', '😅']
```
And for arg as `ALL` it will be just return the same result as above but for all the user present.


#### Features in `visualize.py` 
This module is solely focussed to get the pictorial data based on the data present in the raw form of the users and all other informations, in order to use this type this:
```
from visualize import WpVisualize
wpv = WpVisualize(test_path)
```
Here `path` argument is the path to the exported whatsapp chats of a groups or a chats.

In order to get the group chatting activity based on `day` use this:
```py
wpv.get_active_days('ALL')
```
This is the result we see after that:

![image](https://user-images.githubusercontent.com/58508471/133550924-8d2e0a2f-d1ba-45e5-9f09-6c71f3478a0b.png)

To see the similar results just for a specific user, then type:
```py
wpv.get_active_days('Anindya') # where Anindya is a example user name
```
This is the result, we see after this:

![image](https://user-images.githubusercontent.com/58508471/133551092-9bcf8332-84a0-42af-bcaa-55d68c87ccf7.png)

Similarly in order to see the group activity based on the time of the activity use this:
```py
wpv.get_active_times('ALL')
```
This is the result, we see after this:

![image](https://user-images.githubusercontent.com/58508471/133551222-4dc6f48f-8c41-4866-922d-de28b2bae721.png)

Getting the simlar kind of the result, for a particular user, just use this:
```py
wpv.get_active_times('Anindya') # where Anindya is a example user name
```
This is what we get after using this:

![image](https://user-images.githubusercontent.com/58508471/133551326-facf0393-1d86-4092-90b4-707fd4a196fd.png)

To see the wordcloud of a specific `user`, just type this:
```py
wpv.make_word_cloud('Anindya') # where Anindya is a example user name
```
And this is what we will get after using this:

![image](https://user-images.githubusercontent.com/58508471/133551660-03dfec43-0e42-4b49-95e6-89c13d7d5c4c.png)

And sinimilary we can use this to see the word cloud of the group, just replacing the user name with `ALL`

In order to get the emoji frequency of the group, we can type this:
```py
wpv.plot_emoji_frequency()
```
This is what we will get after this:

![image](https://user-images.githubusercontent.com/58508471/133551844-89228942-84a9-42a1-9c02-025d1ef4b691.png)


To see the frequency of the medias sent by the users in the group, we can just type this: 
```py
wpv.plot_user_media_freq()
```
And we see this:

![image](https://user-images.githubusercontent.com/58508471/133552180-ac906a25-8043-4501-9de6-a17ef8a13040.png)

**The ph numbers or user names will show, but here I am cropping the image for some privacy issues.**

Similarly, in order to which user sents how much emojies, we can use this:
```py
wpv.plot_user_emoji_freq()
```
And we see this:

![image](https://user-images.githubusercontent.com/58508471/133552324-34d91438-48a9-4b73-a14c-bb14559290e2.png)

Similarly, in order to see the how much messages each of the users is sending we can write this up:
```py
wpv.plot_user_msg_freq()
```
And in order to see how much links the user is sending, we can use this:
```py
wpv.plot_user_link_freq()
```

And there is one just more function left, which will give both the textual and the pictorial analysis of the activity of a specific user in the group or for te full group using this function:
Here if we want to see for a specific user like : `Anindya` as an example
```
wpv.track_me('Anindya')
```
This will return this things as follows:

![image](https://user-images.githubusercontent.com/58508471/133552905-9d6c9753-7947-408b-a171-b4bc5f0bd43e.png)

![image](https://user-images.githubusercontent.com/58508471/133552934-fb3cbc7a-19ac-4eae-89ed-e86bdc69c692.png)


## Future works and improvements:
Here is the list of the things, that I wanna improve the existing features and add some new features as follows:
1. Wrap it as library and publish the inital version in pypi
2. Add some existing features of sentiment analysis in order to save some time of the user.
3. Make a simple one page website in django that can be used in phones or anywhere where user can upload the exported txt file, and can see all the results in a      dashboard.

## Acknowledgements
I am really grateful to @Maarten Grootendorst the developer of the soan project where I could learn, some cool stuffs, as a begginer I really learned some cool stuffs like how to use regex, make  extract features from txt files and make a dataframe, and all, and finally come up with some functions which I made and give those visualisations. And finally came with my own original and user friendly version of it.
Thank you.
