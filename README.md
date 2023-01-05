## About
This bot is designed to simplify the moderation and management of Telegram groups.

## Features

* Admin commands
* Member roles       
* Automatic user data update
* Report users
* Silent commands
* User complaints
* Save admin actions in database

## Installation

- Required: python3.x, poetry/pip
- Clone this repo
- Telegram API Service on port 5326(you can run systemd unit in systemd/)
- Move the .env.dist text template to .env and configure him
- First start use `!reload` for parsing members and permissions

## Configuration .env

| environment variables         | description                      |
|-------------------------------|----------------------------------|
| `bot_token`                   | telegram bot token               |
| `api_id` and `api_hash`       | telegram application data        |
| `group_id`                    | group id                         |
| `second_group_id`             | seconds group for admins         |
| `telegram_bot_api_server`     | telegram bot api server          |
| `db_url`                      | connection info to database      |
| `limit_of_warns`              | limit user warnings              |
| `update_interval`             | interval for update of user data |    

## TODO  

- [ ] Docker
- [ ] Write antithrotling midlware middleware(anti flood system)                         
- [ ] Site for group moderator(in development)

## Support 

Every investition helps in maintaining this project and making it better.

<img src="https://img.shields.io/badge/btc-bc1qzp7q3rghzcx70534e7xf6tj0ns3dqvvnex80kf-green?logo=bitcoin">

Don't donate to this wallet yet, I've lost access to it. Wait until I restore the wallet or create a new one.
