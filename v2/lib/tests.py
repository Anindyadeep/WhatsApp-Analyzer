from functions import WpFunctions
from visualize import WpVisualize
from tabulate import tabulate

test_path = "/home/anindya/Documents/project_wp/WPv1.0.1/v2/lib/WhatsApp Chat with Bro code clan 🧑‍💻🧑‍💻.txt"
wpf = WpFunctions(test_path)

# stats_data = wpf.get_stats_frame()
# emoji_data = wpf.get_all_emojies_used()


# print(wpf.get_full_track_msgs('ALL'))

wpv = WpVisualize(test_path)
df = wpv.show()

print(wpf._get_raw_data())