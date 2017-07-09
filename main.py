import requests
import json
import time


class main:


	def __init__(self):

		# Output File
		file = "out-likes.html"
		
		# Open File
		self.out = open(file, "w", encoding = "utf-8")

		# The Key
		self.client_id = "2t9loNQH90kzJcsFCODdigxfp325aq4z"

		# User ID
		self.user_id = "4430277"
		
		# Repost URL
		repost = "https://api-v2.soundcloud.com/profile/soundcloud:users:" + self.user_id + "?limit=50&offset=0&client_id=" + self.client_id

		# Likes URL
		self.likes = "https://api-v2.soundcloud.com/users/" + self.user_id + "/likes?offset=0&limit=50&client_id=" + self.client_id

		# Request Sent
		self.got = 0
		
		# Tracks iterated
		self.tracks = 0
			
		# Start Table
		self.table_start()
			
		# Loop until 
		while repost:
		
			# Function
			self.output(self.fetch(repost))
			
		# End Table
		self.table_end()
		
		# Start Table
		self.table_start()
		
		# Loop until 
		while repost:
		
			# Function
			likes = self.fetch(likes)
		
		# End Table
		self.table_end()
		
			
	def table_start(self):

		# Start Table
		self.out.write("<table>")
		self.out.write("<tbody>")
		self.out.write("<tr>")
		self.out.write("<th>#</th>")
		self.out.write("<th>Artwork</th>")
		self.out.write("<th>Track</th>")
		self.out.write("<th>Artist</th>")
		self.out.write("</tr>")
			
			
	def out_track(self, track_object):
		
		# Up the count 
		self.tracks += 1
		
		# Artwork url
		artwork_url = track_object["track"]["artwork_url"]
		
		# Track Title
		# Track URL
		title = track_object["track"]["title"]
		track_url = track_object["track"]["permalink_url"]
	
		# Artist Title
		# Artist URL			
		artist = track_object["track"]["user"]["username"]
		artist_url = track_object["track"]["user"]["permalink_url"]
		
		self.out.write("<tr>")
		self.out.write("<td>" + str(self.tracks) + "</td>")
		self.out.write("<td><a href='" + track_url + "'><img src='" + artwork_url + "'></a></td>")
		self.out.write("<td><a href='" + track_url + "'>" + title + "</a></td>")
		self.out.write("<td><a href='" + artist_url + "'>" + artist + "</a></td>")
		self.out.write("</tr>")
	
		# Return next href			
		print(str(self.tracks) + ": " + str(title) + " - " + str(artist) + " " + str(track_url)).encode("utf-8")

		
	def table_end(self):
	
		# End Table
		self.out.write("</tbody>")
		self.out.write("</table>")

		
	def fetch(self, url):

		# Gets JSON
		o = requests.get(url)
		
		# Request Sent
		self.got += 1
		
		# Parse JSON
		i = o.json()

		# Return Object
		return i
		
		
	def output(self, object):
		
		# Write Track Info
		for track in object["collection"]:
			
			try:
				
				self.out_track(track)
			
			except:
					
				continue
				
		# Check for end of stream
		if object["next_href"] == None:
			
			# Return False
			return False
		
		else:
			
			# Return the next URL
			return object["next_href"] + "&client_id=" + self.client_id
		
			
main()
