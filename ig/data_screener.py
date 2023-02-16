
import json

# creating a timer to see how fast the program is
import time
start_time = time.time()

# name of each file we are looking through
data_types = ["your_topics", "saved_posts", "ads_interests", "videos_watched"]

# screens every file in the array "data_types" and gets their indexes
for idx, t in enumerate(data_types):

  # open json file and create a variable "data"
  with open('ig/data/{}.json'.format(t), 'r') as t_dict:
    data = json.load(t_dict)

  try:

    # looks for the right value in the right type of file
    if idx == 0:
      values = [v['value'] for v in [e['Name'] for e in [d['string_map_data'] for d in data['topics_your_topics']]]]
    elif idx == 1:
      values = [v['title'] for v in data['saved_saved_media']]
    elif idx == 2:
      values = [v['value'] for v in [e['Interest'] for e in [d['string_map_data'] for d in data['inferred_data_ig_interest']]]]
    elif idx == 3:
      # the "Author" KeyWord is not present all the time
      smd = [d['string_map_data'] for d in data['impressions_history_videos_watched']]
      values = []

      # looking through every item to see if there is a "Author" KeyWord
      for smd_idx, i in enumerate(smd):
        try:
          values.append(smd[smd_idx]["Author"]["value"])
        except:
          print("no author name")

    # kill duplicates
    values = list(dict.fromkeys(values))

    # create file "{}.txt" and adds found values
    f = open("ig/screened data/{}.txt".format(t), "w")

    for i in range(len(values)):
        f.write(values[i] + "\n")

  # will catch empty json files
  except:
    print("no values")

# printing the timer value
print("--- %s seconds ---" % (time.time() - start_time))