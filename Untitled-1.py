 import discord
 import openai

 # Replace 'your_discord_bot_token' and 'your_openai_api_key' with your actual tokens
 DISCORD_TOKEN = 'your_discord_bot_token'
 OPENAI_API_KEY = 'your_openai_api_key'

 # Set up OpenAI
 openai.api_key = OPENAI_API_KEY

 # Set up Discord client
 client = discord.Client(intents=discord.Intents.default())

 @client.event
 async def on_ready():
     print(f'We have logged in as {client.user}')

     @client.event
     async def on_message(message):
         # Don't let the bot reply to itself
             if message.author == client.user:
                     return

                         if message.content.startswith('!ask'):
                                 question = message.content[len('!ask '):].strip()
                                         if question:
                                                     response = openai.Completion.create(
                                                                     engine="davinci-codex",  # or "text-davinci-003"
                                                                                     prompt=question,
                                                                                                     max_tokens=100
                                                                                                                 )
                                                                                                                             await message.channel.send(response.choices[0].text.strip())
                                                                                                                                     else:
                                                                                                                                                 await message.channel.send("Please ask a question after the !ask command.")

                                                                                                                                                 client.run(DISCORD_TOKEN)
                                                                                                                                                 