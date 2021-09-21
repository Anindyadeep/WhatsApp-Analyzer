from typing import Dict
import pandas as pd
import demoji
import re 
import warnings
import emoji as EMO
from dateutil.parser import parse
warnings.filterwarnings("ignore")
demoji.download_codes()

class WpFunctions(object):
    def __init__(self, path):
        self.path = path 

    def _is_date(self, string, fuzzy=False):
        try:
            parse(string, fuzzy=fuzzy)
            return True
        except ValueError:
            return False
    
    def _get_raw_data(self):
        """
        args: self
        ----
        There are no such args
        This function takes the raw path of the exported txt file and 
        then splits the raw txt file, based on the different parsms 
        like '-', ',' etc, in order to  get different user data per 
        messages and then we store the raw data into a datafrme , which
        will be processed further, to get good results
        """
        with open(self.path, encoding='utf-8') as wp_file:
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
            
            if self._is_date(date_time):
                Date.append(date)
                Time.append(time)
                User.append(user)
                Msg.append(msg)
                Date_Time.append(date_time)
            else:
                continue
        
        data = {
            'Date_Time': Date_Time,
            'Date': Date,
            'Time': Time,
            'User': User,
            'Msg': Msg
            }
        
        raw_data = pd.DataFrame(data)
        raw_data['msg_text_only'] = raw_data.apply(lambda row: re.sub(r'[^a-zA-Z]+', ' ', row.Msg.lower()), axis=1)
        return raw_data

    
    def get_stats_frame(self):
        raw_data = self._get_raw_data()
        USER = []
        TOTAL_MSG = []
        TOTAL_MEDIA = []
        TOTAL_LINK = []

        """
        This User profiles, will search for each of the unique users and 
        will map all their messages and all sorts of the data, and will 
        this dict will return all the different dataframes with keys is the unique 
        users.
        """
        USER_PROFILES = {
            user: raw_data[raw_data.User == user] for user in raw_data.User.unique()
        }

        for user in USER_PROFILES.keys():
            total_msg_with_media = USER_PROFILES[user].shape[0]
            media = list(USER_PROFILES[user].loc[USER_PROFILES[user].Msg.str.contains('<Media omitted>'), 'Msg'].index)
            link = list(USER_PROFILES[user].loc[USER_PROFILES[user].Msg.str.contains('https'), 'Msg'].index)

            USER.append(user)
            TOTAL_MSG.append(total_msg_with_media - len(media))
            TOTAL_MEDIA.append(len(media))
            TOTAL_LINK.append(len(link))
        
        # Getting the emojies to append too with the user
        NAME = []
        EMOJIES = []
        EMOJIES_LEN = []
        for user in USER_PROFILES.keys():
            NAME.append(user)
            EMOJIES.append(
                list(demoji.findall(str(USER_PROFILES[user].Msg)).keys())
            )
            EMOJIES_LEN.append(
                len(list(demoji.findall(str(USER_PROFILES[user].Msg)).keys()))
                )
        
        Stat_data = {
            "User": USER,
            "Total_msg": TOTAL_MSG,
            "Total_media": TOTAL_MEDIA,
            "Total_link": TOTAL_LINK,
            "Emojies": EMOJIES,
            "Total_emojies": EMOJIES_LEN
        }

        Stat_data_frame = pd.DataFrame(Stat_data)
        return Stat_data_frame

    
    def get_all_emojies_used(self):
        """
        args: self
        -----
        returns a dataframe, which will be containing
        Unique emojies used in the chat, the description of those emojies,
        and the frequencies of those emojies used. 
        """
        Stats_data = self.get_stats_frame()
        
        ALL_EMOJIES = []
        EMOJI_FREQ_DICT = {}
        
        EMOJIES = []
        EMOJIES_FREQ = []
        EMOJI_DESC = []

        for emojies in Stats_data.Emojies:
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
            EMOJIES.append(emo)
            EMOJIES_FREQ.append(EMOJI_FREQ_DICT[emo])
            EMOJI_DESC.append(str(EMO.demojize(emo)[1:-1]))
        
        EMOJI_USER_USED = {
            "Emoji": EMOJIES,
            "Emoji_desc": EMOJI_DESC,
            "Emoji_frequency": EMOJIES_FREQ
        }
        EMOJI_USER_DF = pd.DataFrame(EMOJI_USER_USED)
        return EMOJI_USER_DF

    
    # The function will track the user record of the every user

    def get_full_track_msgs(self, name):
        """
        args:
        ----
        name -> str : if name is ALL, then it will return stats summary of all users else if the name exists 
                      it will return the stats summary of that specific user, other wise through error 
        """

        Stats_data = self.get_stats_frame()
        if name != "ALL":
            name = " " + name

            all_users = list(Stats_data.User)
            if name not in all_users:
                print("The user does not exists, try with another user")
                return None
                
            else:
                index = Stats_data[Stats_data['User'] == name].index.values.astype(int)[0]
                
                total_msg = Stats_data.Total_msg[index]
                total_media = Stats_data.Total_media[index]
                total_link = Stats_data.Total_link[index]
                total_emojies = Stats_data.Total_emojies[index]
                emojies_used = Stats_data.Emojies[index]

                print("The name of the user is: ", name)
                print("The total no of messages sent by", name, " is: ", total_msg)
                print("The total number of media (including the pics, vids, gifs, stickers by", name, " is: ", total_media)
                print("The total number of links sent by", name, " is: ", total_link)
                print("The total number of emojies sent by", name, " is: ", total_emojies)
                print("The emojies used by", name, " are: ", emojies_used)

        else: 
            for user in set(Stats_data.User):
                index = Stats_data[Stats_data['User'] == user].index.values.astype(int)[0]

                total_msg = Stats_data.Total_msg[index]
                total_media = Stats_data.Total_media[index]
                total_link = Stats_data.Total_link[index]
                total_emojies = Stats_data.Total_emojies[index]
                emojies = Stats_data.Emojies[index]

                print("The name of the user is: ", user)
                print("The total no of messages sent by", user, " is: ", total_msg)
                print("The total number of media (including the pics, vids, gifs, stickers by", user, " is: ", total_media)
                print("The total number of links sent by", user, " is: ", total_link)
                print("The total number of emojies sent by", user, " is: ", total_emojies)
                print("The emojies used by", user, " are: ", emojies)
                print('\n')
    

    def get_data_to_plot(self):
        data_to_plot = self._get_raw_data()
        data_to_plot['Date_Time'] = pd.to_datetime(data_to_plot['Date_Time'], infer_datetime_format = True)
        data_to_plot['Day_of_week'] = data_to_plot.apply(lambda row: row.Date_Time.dayofweek, axis = 1)
        data_to_plot['Hour'] = data_to_plot.apply(lambda row: row.Date_Time.hour, axis=1)
        return data_to_plot
