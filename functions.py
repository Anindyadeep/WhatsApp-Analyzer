import pandas as pd
import demoji
import re

demoji.download_codes()


### This is the function to just get the raw data frame which is not feature engineered

def get_raw_data(path):
    with open(path, encoding='utf-8') as wp_file:
        raw_text = wp_file.readlines()
    Date = []
    Time = []
    User = []
    Msg = []
    Date_Time = []

    for line in raw_text:
        try:
            date_time = line.split('-')[0]
            user_msg = line.split('-')[1]

            date = date_time.split(',')[0]
            time = date_time.split(',')[1]

            user = user_msg.split(':')[0]
            msg = user_msg.split(':')[1]

        except:
            continue
        Date.append(date)
        Time.append(time)
        User.append(user)
        Msg.append(msg)
        Date_Time.append(date_time)

    data = {'Date_Time': Date_Time,
            'Date': Date,
            'Time': Time,
            'User': User,
            'Msg': Msg}

    raw_data = pd.DataFrame(data)
    raw_data['msg_text_only'] = raw_data.apply(lambda row: re.sub(r'[^a-zA-Z]+', ' ', row.Msg.lower()), axis=1)
    return raw_data


### Making a dataframe that will return the total no of messages of each user

def get_stats_frame(raw_data):
    USER = []
    TOTAL_MSG = []
    TOTAL_MEDIA = []
    TOTAL_LINK = []

    users = {user: raw_data[raw_data.User == user] for user in raw_data.User.unique()}
    for user in users.keys():
        total_msg_with_media = users[user].shape[0]
        media = list(users[user].loc[users[user].Msg.str.contains('<Media omitted>'), 'Msg'].index)
        link = list(users[user].loc[users[user].Msg.str.contains('https'), 'Msg'].index)
        USER.append(user)
        TOTAL_MSG.append(total_msg_with_media - len(media))
        TOTAL_MEDIA.append(len(media))
        TOTAL_LINK.append(len(link))

    # Getting the emojies to append too with the user
    NAME = []
    EMOJIES = []
    EMOJIES_LEN = []
    for user in users.keys():
        NAME.append(user)
        EMOJIES.append(list(demoji.findall(str(users[user].Msg)).keys()))
        EMOJIES_LEN.append(len(list(demoji.findall(str(users[user].Msg)).keys())))

    Stat_data = {"User": USER,
                 "Total_msg": TOTAL_MSG,
                 "Total_media": TOTAL_MEDIA,
                 "Total_link": TOTAL_LINK,
                 "Emojies": EMOJIES,
                 "Total_emojies": EMOJIES_LEN}

    Stat_data_frame = pd.DataFrame(Stat_data)
    return Stat_data_frame


### The emoji part(under construction)

def get_all_emojies_used(stats_data):
    import emoji as EMO
    ALL_EMOJIES = []
    EMOJI_FREQ_DICT = {}

    EMOJIS = []
    EMOJIS_FREQ = []
    EMOJIS_DESC = []

    for emojies in stats_data.Emojies:
        if not emojies:
            continue
        else:
            for i in range(len(emojies)):
                ALL_EMOJIES.append(emojies[i])
    for emoji in ALL_EMOJIES:
        if emoji in EMOJI_FREQ_DICT:
            EMOJI_FREQ_DICT[emoji] += 1
        else:
            EMOJI_FREQ_DICT[emoji] = 1

    for emo in EMOJI_FREQ_DICT.keys():
        EMOJIS.append(emo)
        EMOJIS_FREQ.append(EMOJI_FREQ_DICT[emo])
        EMOJIS_DESC.append(EMO.demojize(emo))

    EMOJI_USER_USED = {"Emoji": EMOJIS,
                       "Emoji_desc": EMOJIS_DESC,
                       "Emoji_frequency": EMOJIS_FREQ}
    EMOJI_USER = pd.DataFrame(EMOJI_USER_USED)
    return EMOJI_USER


# The function will track the user record of the every user

def get_full_track_msgs(name, stats_data):
    if name != 'ALL':
        name = " " + name
        # users = {user: raw_data[raw_data.User == user] for user in raw_data.User.unique()}

        index = stats_data[stats_data['User'] == name].index.values.astype(int)[0]

        total_msg = stats_data.Total_msg[index]
        total_media = stats_data.Total_media[index]
        total_link = stats_data.Total_link[index]
        total_emojies = stats_data.Total_emojies[index]
        emojies = stats_data.Emojies[index]

        print("The name of the user is: ", name)
        print("The total no of messages sent by", name, " is: ", total_msg)
        print("The total number of media (including the pics, vids, gifs, stickers by", name, " is: ", total_media)
        print("The total number of links sent by", name, " is: ", total_link)
        print("The total number of emojies sent by", name, " is: ", total_emojies)
        print("The emojies used by", name, " are: ", emojies)

    else:
        for user in set(stats_data.User):
            index = stats_data[stats_data['User'] == user].index.values.astype(int)[0]

            total_msg = stats_data.Total_msg[index]
            total_media = stats_data.Total_media[index]
            total_link = stats_data.Total_link[index]
            total_emojies = stats_data.Total_emojies[index]
            emojies = stats_data.Emojies[index]

            print("The name of the user is: ", user)
            print("The total no of messages sent by", user, " is: ", total_msg)
            print("The total number of media (including the pics, vids, gifs, stickers by", user, " is: ", total_media)
            print("The total number of links sent by", user, " is: ", total_link)
            print("The total number of emojies sent by", user, " is: ", total_emojies)
            print("The emojies used by", user, " are: ", emojies)
            print('\n')


# This function will return a new data frame in order to make the plots which are based on date and time

def get_data_to_plot(raw_data):
    data_to_plot = raw_data
    data_to_plot['Date_Time'] = pd.to_datetime(data_to_plot['Date_Time'], infer_datetime_format = True)
    data_to_plot['Day_of_week'] = data_to_plot.apply(lambda row: row.Date_Time.dayofweek, axis = 1)
    data_to_plot['Hour'] = data_to_plot.apply(lambda row: row.Date_Time.hour, axis=1)
    return data_to_plot

