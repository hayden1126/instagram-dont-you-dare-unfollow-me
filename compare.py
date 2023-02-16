import json

with open("followers_1.json") as followers_file:
    followersJSON = json.load(followers_file)
with open("following.json") as following_file:
    followingJSON = json.load(following_file)["relationships_following"]

followers = [f["string_list_data"][0]["value"] for f in followersJSON]
following = [f["string_list_data"][0]["value"] for f in followingJSON]

for f in following:
    if f not in followers:
        print(f)
    