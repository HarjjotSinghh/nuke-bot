# Discord Channels Nuke Bot
**NOTE: Usage of this bot is not at all recommended as its against the [Terms of Service](https://discord.com/terms) of discord.**
**Your accout can get banned if you use this bot.**
- The bot requires `Manage Channels` permission in every server.
- Deletes (or at least tries to) delete all the channels accessible to the bot.
- Use this at your own risk.
- Channels once deleted cannot come back.
- **Made strictly for educational purposes only.**
- I won't be responsible for any stupid things which any of you might not / might do.
# Requirements
- Must have [Python 3.7](https://www.python.org/downloads/release/python-370/) or above.
- Must have at least some knowledge of python and how packages work.
- Must have installed the following dependencies:
  - [discord.py](https://pypi.org/project/discord.py/) v1.5+
  - [colorama](https://pypi.org/project/colorama/) v0.4+
- Must know how to [clone a repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) on GitHub.
# How To Use
- Go to [discord developer portal](https://discord.com/developers/applications).
- Create a [New Application](https://ibb.co/xD5B9cz).
- Name it whatever you want.
- Go to the [`BOT` settings tab](https://ibb.co/GRRcS2y).
- Click on [Add a bot](https://ibb.co/FVxJxYv).
- Go back to the General Information settings tab.
- Click on `Copy ID`.
- Go to any [discord permissions calculator](https://discordapi.com/permissions.html).
- Paste your ID in the `Client ID` box.
- Select/Check the `Manage Channels` permission.
- Copy the link formed and open it in another window.
- Select the server you would like to nuke.
- Click on the `Authorize` button.
- Verify that you are not a robot by checking the verification box.
- Once it says `Authorized`, it means that the bot is now in the server you selected.
- Now, head back to the [discord developer portal](https://discord.com/developers/applications).
- Select the application which you just created.
- Go the BOT settings paga again.
- Click on `COPY` button under the `TOKEN` menu.
- Create a json file named `config.json` in your cloned project directory.
- The json file should look like this:
```json
{
  "BOT_TOKEN" : "paste the token youy copied here (inside the quotes)"
}
```
Once you have created the `config.json` file and followed all the steps correctly, you can just start the `main.py` file by the command:
```bash
python main.py
```
