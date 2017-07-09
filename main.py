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
		self.client_id = ""

		# User ID
		self.user_id = "4430277"
		
		# Repost URL
		self.repost = "https://api-v2.soundcloud.com/profile/soundcloud:users:" + self.user_id + "?limit=50&offset=0" + self.client_id

		# Likes URL
		self.likes = "https://api-v2.soundcloud.com/users/" +  + self.user_id + "/likes?offset=0&limit=50" + self.client_id

		
		self.last = False
		self.got = 0
		self.tracks = 0
			
		
		print("Start...")

		self.out.write("<table>")
		self.out.write("<tbody>")

		self.out.write("<tr>")
		self.out.write("<th>#</th>")
		self.out.write("<th>Track</th>")
		self.out.write("<th>Artist</th>")
		self.out.write("</tr>")

		self.url = self.likes
		
		while self.url != self.last:
			self.fetch(self.url)
			
			
		self.out.write("</tbody>")
		self.out.write("</table>")

		self.got = 0
		self.tracks = 0
			
		
		print("Start...")

		self.out.write("<table>")
		self.out.write("<tbody>")

		self.out.write("<tr>")
		self.out.write("<th>#</th>")
		self.out.write("<th>Track</th>")
		self.out.write("<th>Artist</th>")
		self.out.write("</tr>")

		print("Repost:")
		
		self.url = self.repost
		
		while self.url != self.last:
			self.fetch(self.url)		
			
		self.out.write("</tbody>")
		self.out.write("</table>")


	def fetch(self, url):

		# Gets JSON
		o = requests.get(url)
		
		# Request Sent
		self.got += 1
		
		# Parse JSON
		i = o.json()

		# Write Track Info
		for track in i["collection"]:
			
			try:
			
				self.tracks += 1
				
				# Track Title
				# Track URL
				title = track["track"]["title"]
				track_url = track["track"]["permalink_url"]
			
				# Artist Title
				# Artist URL
				artist = track["track"]["user"]["username"]
				artist_url = track["track"]["user"]["permalink_url"]
				
				self.out.write("<tr>")
				self.out.write("<td>" + str(self.tracks) + "</td>")
				self.out.write("<td><a href='" + track_url + "'>" + title + "</a></td>")
				self.out.write("<td><a href='" + artist_url + "'>" + artist + "</a></td>")
				self.out.write("</tr>")

				# Return next href			
				print(str(self.tracks) + ": " + str(title) + " - " + str(artist) + " " + str(track_url)).encode("utf-8")
			
			except:
				
				continue
			
		self.last = url
		
		try:
			
			self.url = i["next_href"] + self.client_id
		
		except:
			
			print(i["next_href"])

			
main()
