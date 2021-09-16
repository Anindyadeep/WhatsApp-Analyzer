import functions as wpf
import visualise as wpv
import plotly.offline
import plotly.graph_objs as go


def track_me(raw_data, user):
    stats_data = wpf.get_stats_frame(raw_data)
    data_to_plot = wpf.get_data_to_plot(raw_data)

    print("####### THE TOTAL TRACK RECORD OF THE USER #######")
    print("\nUser name: ", user)
    wpf.get_full_track_msgs(user, stats_data)
    print('\n')
    wpv.get_active_days(data_to_plot, user)
    wpv.get_active_times(data_to_plot, user)
    user = " "+user
    data_cloud = raw_data.loc[raw_data.User == user]
    wpv.make_word_cloud(data_cloud)


