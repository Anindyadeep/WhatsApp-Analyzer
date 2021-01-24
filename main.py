import functions as wpf
import visualise as wpv
import user_track as wpu

PATH1 = r'C:\Users\cosmi\Documents\Projects\Project whatsapp\WhatsApp Chat with 🍄...CHILLZONE...🍄.txt'
PATH2 = r'C:\Users\cosmi\Documents\Projects\Project whatsapp\WhatsApp Chat with Crazy World AGCS.txt'

raw_data = wpf.get_raw_data(PATH2)

# To know the user statistics of their messages
stats_data = wpf.get_stats_frame(raw_data)

# To get all the emojies used in the grp chat
emoji_stats_data = wpf.get_all_emojies_used(stats_data)

# To get the data which is for plotting purposes on the basis of date and time
data_to_plot = wpf.get_data_to_plot(raw_data)

print(stats_data.columns)

# wpv.get_active_days(data_to_plot, 'ALL')
# wpv.get_active_times(data_to_plot, 'ALL')
# wpv.make_word_cloud(raw_data)
# wpv.plot_emoji_frequency(emoji_stats_data)
# wpv.plot_user_emoji_freq(stats_data)
# wpv.plot_user_link_freq(stats_data)
# wpv.plot_user_msg_freq(stats_data)
# wpv.plot_user_media_freq(stats_data)

