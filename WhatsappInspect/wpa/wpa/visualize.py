import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wpa.functions import WpFunctions
from wordcloud import WordCloud, STOPWORDS

"""
TODO
----

2. check if the user exists
3. define each and every functions as returns and args
"""

class WpVisualize(object):
    def __init__(self, path):
        self.path = path 
        self.wpf = WpFunctions(self.path)
        self.raw_data = self.wpf._get_raw_data()
        self.stats_data = self.wpf.get_stats_frame()
        self.emoji_stats_data = self.wpf.get_all_emojies_used()
        self.data_to_plot = self.wpf.get_data_to_plot()
    
    ########################## Group's total user specific visualisations ##########################

    # The plot of the emojies vs the number of the frequencies of the emojies

    def plot_emoji_frequency(self):
        fig = px.bar(
            self.emoji_stats_data, 
            x="Emoji", y="Emoji_frequency",
            title="The emojies vs the frequencies of their usages")
        fig.show()
    

    # The plot of the users vs the number of the messages sent by the users

    def plot_user_msg_freq(self, figsize=None):
        if figsize:
            plot_figsize = figsize
        else:
            plot_figsize = (12,6)
        
        plt.figure(figsize=plot_figsize)
        plt.xticks(rotation=90)
        plt.title("The users used vs the frequencies of the messages sent")
        sns.barplot(
            x = "User",
            y = "Total_msg",
            data = self.stats_data
        )
        plt.show()


    # The plot of the users vs the number of the media sent by the users

    def plot_user_media_freq(self, figsize=None):
        if figsize:
            plot_figsize = figsize
        else:
            plot_figsize = (12,6)
        
        plt.figure(figsize=plot_figsize)
        plt.xticks(rotation=90)
        plt.title("The users used vs the frequencies of the medias sent includes (pics, vids, stickesrs, gifs)")
        sns.barplot(
            x = "User",
            y = "Total_media",
            data = self.stats_data
        )
        plt.show()
    

    # The plot of the users vs the number of the links sent by the users

    def plot_user_link_freq(self, figsize=None):
        if figsize:
            plot_figsize = figsize
        else:
            plot_figsize = (12,6)
        
        plt.figure(figsize=plot_figsize)
        plt.xticks(rotation=90)
        plt.title("The users used vs the number of link sent")
        sns.barplot(
            x = "User",
            y = "Total_link",
            data = self.stats_data
        )
        plt.show()


    # The plot of the users vs the number of the emojies sent by the user

    def plot_user_emoji_freq(self, figsize=None):
        if figsize:
            plot_figsize = figsize
        else:
            plot_figsize = (12,6)
        
        plt.figure(figsize=plot_figsize)
        plt.xticks(rotation=90)
        plt.title("The users used vs the frequencies of the emojies sent")
        sns.barplot(
            x = "User",
            y = "Total_emojies",
            data = self.stats_data
        )
        plt.show()
    

    ######### Particular uers's visualisations of the progressions of the messages w.r.t the day #########

    def _get_time_format(self, time):
        if time == 0:
            t = "12 AM"
        elif time == 1:
            t = "1 AM"
        elif time == 2:
            t = "2 AM"
        elif time == 3:
            t = "3 AM"
        elif time == 4:
            t = "4 AM"
        elif time == 5:
            t = "5 AM"
        elif time == 6:
            t = "6 AM"
        elif time == 7:
            t = "7 AM"
        elif time == 8:
            t = "8 AM"
        elif time == 9:
            t = "9 AM"
        elif time == 10:
            t = "10 AM"
        elif time == 11:
            t = "11 AM"
        elif time == 12:
            t = "12 PM"
        elif time == 13:
            t = "1 PM"
        elif time == 14:
            t = "2 PM"
        elif time == 15:
            t = "3 PM"
        elif time == 16:
            t = "4 PM"
        elif time == 17:
            t = "5 PM"
        elif time == 18:
            t = "6 PM"
        elif time == 19:
            t = "7 PM"
        elif time == 20:
            t = "8 PM"
        elif time == 21:
            t = "9 PM"
        elif time == 22:
            t = "10 PM"
        elif time == 23:
            t = "11 PM"
        return t

    def get_active_times_user(self, user):
        user = " " + user
        all_users = list(self.stats_data.User)
        if user not in all_users:
            print("The user does not exists, try again with another user")
            return None
        
        data = self.data_to_plot.loc[self.data_to_plot.User == user]
        hours = data.Hour.value_counts().sort_index().index
        counts = data.Hour.value_counts().sort_index().values
        Time = hours
        Time_words = []

        for time in Time:
            t = self._get_time_format(time)
            Time_words.append(t)

        sns.set(rc={'figure.figsize': (8, 6)})
        g = sns.barplot(counts, hours, orient='h')
        g.set(yticklabels=Time_words)
        Title = "The active hours stats of "+user
        plt.title(Title)
        plt.show()


    ######## Group's as well as user wise visualisations of the progressions of the messages w.r.t the day's hours ########

    def get_active_times(self, user):
        if user != 'ALL':
            self.get_active_times_user(user)
        else:
            hours = self.data_to_plot.Hour.value_counts().sort_index().index
            counts = self.data_to_plot.Hour.value_counts().sort_index().values
            Time = hours
            Time_words = []
            for time in Time:
                t = self._get_time_format(time)
                Time_words.append(t)

            sns.set(rc={'figure.figsize': (8, 6)})
            g = sns.barplot(counts, hours, orient='h')
            g.set(yticklabels=Time_words)
            Title = "The active hours stats of the group"
            plt.title(Title)
            plt.show()


    ######### Particular uers's visualisations of the progressions of the messages w.r.t the day #########
    
    def _get_day_word(self, day):
        if day == 0:
            day_word = "Mon"
        elif day == 1:
            day_word = "Tue"
        elif day == 2:
            day_word = "Wed"
        elif day == 3:
            day_word = "Thu"
        elif day == 4:
            day_word = "Fri"
        elif day == 5:
            day_word = "Sat"
        elif day == 6:
            day_word = "Sun"
        return day_word

    def get_active_days_user(self, user):
        user = " " + user
        all_users = list(self.stats_data.User)
        if user not in all_users:
            print("The user does not exists, try with another user ...")
            return None
        
        data_day_wise = self.data_to_plot.loc[self.data_to_plot.User == user]
        days_of_week = data_day_wise.apply(lambda row: row.Date_Time.dayofweek, axis=1)
        days = days_of_week.value_counts().sort_index().index
        count_days = days_of_week.value_counts().sort_index().values

        Day_words = []
        for day in days:
            day_word = self._get_day_word(day)
            Day_words.append(day_word)

        sns.set(rc={'figure.figsize': (8, 6)})
        g = sns.barplot(count_days, days, orient='h')
        g.set(yticklabels=Day_words)
        Title = "The active days stats of "+user
        plt.title(Title)
        plt.show()


    ######## Group's as well as user wise visualisations of the progressions of the messages w.r.t the day ########

    def get_active_days(self, user):
        if user != 'ALL':
            self.get_active_days_user(user)
        else:
            data_day_wise = self.data_to_plot
            days_of_week = data_day_wise.apply(lambda row: row.Date_Time.dayofweek, axis=1)
            days = days_of_week.value_counts().sort_index().index
            count_days = days_of_week.value_counts().sort_index().values
            Day_words = []
            for day in days:
                day_word = self._get_day_word(day)
                Day_words.append(day_word)
            sns.set(rc={'figure.figsize': (8, 6)})
            g = sns.barplot(count_days, days, orient='h')
            g.set(yticklabels=Day_words)
            Title = "The active days stats of the group"
            plt.title(Title)
            plt.show()


    # The word cloud

    def make_word_cloud(self, user):
        if user  == 'ALL':
            data_cloud = self.raw_data
        else:
            user = " " + user
            all_users = list(self.stats_data.User)
            if user not in all_users:
                print("User does not exists, please try with another user ...")
                return None
            
            else: 
                data_cloud =  self.raw_data.loc[self.raw_data.User == user]
            
        indices_to_remove1 = list(data_cloud.loc[data_cloud.msg_text_only.str.contains('media'), 'msg_text_only'].index)
        indices_to_remove2 = list(data_cloud.loc[data_cloud.msg_text_only.str.contains('deleted'), 'msg_text_only'].index)
        data_cloud = data_cloud.drop(indices_to_remove1)
        data_cloud = data_cloud.drop(indices_to_remove2)

        data = data_cloud
        final_msg = ' '
        stop_words = set(STOPWORDS)

        for msg in data.msg_text_only:
            msg = str(msg)
            tokens = msg.split()

            final_msg += " ".join(tokens) + " "

        wordcloud = WordCloud(width=800, height=800,
                            background_color='white',
                            stopwords=stop_words,
                            min_font_size=10).generate(final_msg)
        plt.figure(figsize=(8, 8))
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.show()


    def track_me(self, user):
        print("####### THE TOTAL TRACK RECORD OF THE USER #######")
        if user == 'ALL':
            print("\nALL USERS:")
        else: 
            print("User name: ", user)
        self.wpf.get_full_track_msgs(user)
        print('\n')

        self.get_active_days(user)
        self.get_active_times(user)
        self.make_word_cloud(user)
