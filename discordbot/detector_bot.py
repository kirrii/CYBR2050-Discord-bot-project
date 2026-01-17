import discord
from discord.ext import commands

# ========= CONFIG =========
TOKEN =   
TRIGGER_TEXT = "What a lovely day"     
# ==========================

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Detector bot logged in as {bot.user}")

@bot.event
async def on_message(message: discord.Message):
    print(f"SEEN: {message.author} ({message.author.id}): {message.content!r}")

    if message.author.id == bot.user.id:
        return

    if message.author.bot and TRIGGER_TEXT in message.content:
        await message.channel.send(
            "📢 It is not a lovely day I'm on to you jimbo. There has been a dm sent to everyone be careful!!! "
        )

    await bot.process_commands(message)

if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Set TOKEN at the top of the file.")
    bot.run(TOKEN)