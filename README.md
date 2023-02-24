# Assetto-Corsa-Server-Listener-Discord-Webhook-
<h3 align="center">Shows player JOIN and DISCONNECT in any assetto corsa server and writes to a discord channel via a webhook.</h3>

  <p align="center">
    <img src="images/example_discord.PNG" alt="Logo" >
    <br />
    <a href="https://iiferedon.xyz"><strong>My Website »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Monitor any Assetto Corsa server to check if a player has joined or left the server.

I haven't seen anyone do this yet publicly so here is my code. :D

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Discord.py](https://discordpy.readthedocs.io/en/stable/api.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

```sh
git clone https://github.com/iiferedon/Assetto-Corsa-Server-Listener-Discord-Webhook-.git
cd /Assetto-Corsa-Server-Listener-Discord-Webhook-/
pip install -r requirements.txt

```

### Installation

_Below is an example of how you can install this webhook!_

1. Create a discord webhook
  ```sh
  Choose a channel to display messages > edit channel > integrations > webhooks > create webhook > name it anything > copy the webhook URL.
  ```
2. Edit ACbot.py
   ```py
    webhook = DiscordWebhook(url="WEBHOOK_URL")
    server_address = "SERVER_IP:SERVER_PORT"
   ```
   
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
```sh
#Start Script
python3 ACbot.py
```
Ensure script is started before anyone is in the server.
<p align="right">(<a href="#top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Discord - iiferedon#7337 or iiferedon#1337

Project Link: [https://github.com/iiferedon/Assetto-Corsa-Server-Listener-Discord-Webhook-/](https://github.com/iiferedon/Assetto-Corsa-Server-Listener-Discord-Webhook-/)

<p align="right">(<a href="#top">back to top</a>)</p>
