
import json

# creating a timer to see how fast the program is
import time
start_time = time.time()

# name of the file we are looking through
file_name = "user_data"

# open json file and create a variable "data"
with open('tiktok/data/{}.json'.format(file_name), 'r') as t_dict:
    data = json.load(t_dict)

# information about the direction of each json attribute we are looking for
attributes= [
    ["Favorite Hashtags", "FavoriteHashtagList", "Link"], 
    ["Favorite Videos", "FavoriteVideoList", "Link"], 
    ["Following List", "Following", "UserName"], 
    ["Like List", "ItemFavoriteList", "Link"]]


# look through every listed json attribute
for idx, att in enumerate(attributes):

    try:
        # find each value in pointed json direction
        values = [l[attributes[idx][2]] for l in data['Activity'][attributes[idx][0]][attributes[idx][1]]]

        # kill duplicates
        values = list(dict.fromkeys(values))

    except:
        values = []
        print("no data")

    # create file "{}.txt" and adds found values
    f = open("tiktok/screened data/{}.txt".format(attributes[idx][0]), "w")

    for i in range(len(values)):
        f.write(values[i] + "\n")

# favorite hashtags - 6
# favorite videos - 29
# following list - 65
# like list - 158
