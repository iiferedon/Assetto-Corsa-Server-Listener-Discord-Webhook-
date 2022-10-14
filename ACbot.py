#Imports
import json
from urllib.request import urlopen, Request
import time
import os
import sys
from discord_webhook import DiscordWebhook, DiscordEmbed

#Change these values
webhook = DiscordWebhook(url="WEBHOOK_URL")
server_address = "SERVER_IP:SERVER_PORT"
print("Script Started!")
print("Developed by www.iiferedon.xyz")
print("Discord: iiferedon#1337")
#Main Loop
def main_loop():
      buffer = "buffer.json"
      #Load the JSON using http request
      try:  
         url = "http://"+server_address+"/JSON%7C"
         request = Request(url)
         response = urlopen(request)
         jso = response.read()
         response.close()
         #Load JSON
         parsed = json.loads(jso)
      except:
         print("Error, server unavailable.")
         sys.exit()
         
      #Check if file is empty on startup and writes to it
      filesize = os.path.getsize(buffer)
      while filesize == 0:
         with open(buffer, 'w') as json_file:
            json.dump(parsed, json_file)
            break
            
      #Counts the lines
      cars = parsed["Cars"]
      num_lines = sum(1 for line in cars)
      x = range(1, num_lines)
   
   #Send Discord Messages
      def send_webhook(title, player, colour, model, skin, type):
         if type == 1:   
            embed = DiscordEmbed(title=title, color=colour)
            embed.set_footer(text=' ')
            embed.set_timestamp()
            embed.add_embed_field(name='Player Name', value=player)
            embed.add_embed_field(name='Car', value=model)
            embed.add_embed_field(name='Skin', value=skin)
            webhook.add_embed(embed)
            response = webhook.execute()
         else:
            embed = DiscordEmbed(title=title, description = player + " left",color=colour)
            embed.set_footer(text=' ')
            embed.set_timestamp()
            webhook.add_embed(embed)
            response = webhook.execute()
            
      #Logic
      f = open(buffer, "r")
      read_buffer = f.read()
      read_json = json.loads(read_buffer)
      if True:
         for i in range(num_lines):
            if parsed["Cars"][i]["IsConnected"] and read_json["Cars"][i]["IsConnected"]: #Value stays same, no join or leave
               print("Users in session")
            elif read_json["Cars"][i]["IsConnected"] != True and parsed["Cars"][i]["IsConnected"]: #Joined Game
               print("JOINED GAME: Player: " + parsed["Cars"][i]["DriverName"] + ", is driving: " + parsed["Cars"][i]["Model"] + ", with skin: " + parsed["Cars"][i]["Skin"])
               title = "Player Connected"
               player = parsed["Cars"][i]["DriverName"]
               colour = 5763719
               model = parsed["Cars"][i]["Model"]
               skin = parsed["Cars"][i]["Skin"]
               type = 1
               send_webhook(title, player, colour, model, skin, type)
            elif parsed["Cars"][i]["IsConnected"] != True and read_json["Cars"][i]["IsConnected"]: #Left Game
               print("LEFT GAME: Player: " + parsed["Cars"][i]["DriverName"])
               title = "Player Disconnected"
               player = parsed["Cars"][i]["DriverName"]
               model = parsed["Cars"][i]["Model"]
               skin = parsed["Cars"][i]["Skin"]
               colour = 15548997
               type = 0
               send_webhook(title, player, colour, model, skin, type)
               f.close()
               
      #overwrite previous buffer with current server JSON
      with open(buffer, 'w') as json_file:
            json.dump(parsed, json_file)
            print("wrote to buffer")
            print("..")


while True:    
   main_loop()
   time.sleep(2)
