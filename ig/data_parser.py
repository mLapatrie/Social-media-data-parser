
import os
import urllib.request

# creating a timer to see how fast the program is
import time
start_time = time.time()

# creates an array of all the names of the files in "screened data"
data = os.listdir("ig\screened data")

# array of interests that will be populated by "ads_interests" and "your_topics"
interests = []

# array of descriptions that will be populated by the descriptions of every account in "videos_watched" and "saved_posts"
descriptions = []


# takes the file name and transfer all of the content to the "interests" array
def transfer_interests(file_name):
    with open('ig/screened data/{}'.format(file_name)) as f:
        for i in f.read().splitlines():
            interests.append(i)


# gets bio from each creator in "videos_watched.txt"
def get_bio(file):

    with open('ig/screened data/{}'.format(file)) as f:

        # gets html of each account in "videos_watched.txt"
        for account_name in f.read().splitlines():

            # get html from url
            fp = urllib.request.urlopen("https://www.instagram.com/{}/".format(account_name))
            page = fp.read().decode("utf8")
            fp.close()

            # finds the bio by removing words before "description" and after "author"
            bio = page.split('description":"')[1].split('","author')[0]

            # clean up the bio
            bio = bio.replace("\\n", "").split()
            
            # does it 2 times
            for i in range(3):

                # remove every word starting with "\"
                for idx, word in enumerate(bio):
                    if word[0] == "\\":
                        bio.pop(idx)
            
            bio = " ".join(bio)

            # adds the bio to array "descriptions" if there is content
            if len(bio.split()) > 0:
                descriptions.append(bio)


# main
transfer_interests("ads_interests.txt")
transfer_interests("your_topics.txt")
get_bio("videos_watched.txt")
get_bio("saved_posts.txt")

# creates a file "interests.txt" with the array "interests"
i_file = open("ig/parsed data/interests.txt", "w")
for i in interests:
    i_file.write(i + '\n')

# creates a file "descriptions.txt" with the array "descriptions"
d_file = open("ig/parsed data/descriptions.txt", "w")
for d in descriptions:
    d_file.write(d + '\n')


# printing the timer value
print("--- %s seconds ---" % (time.time() - start_time))