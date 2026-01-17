import os
import asyncio
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = 

intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@tree.command(name="run")
async def run_command(interaction: discord.Interaction):
    guild = interaction.guild

    if guild is None:
        await interaction.response.send_message( ephemeral=True)
        return

    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message( ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True, thinking=True)

    sent = 0
    failed = 0
    text = "Hey, check this out! https://example.com"

    for member in guild.members:
        if member.bot:
            continue
        try:
            await member.send(text)
            sent += 1
            await asyncio.sleep(0.7) 
        except Exception:
            failed += 1
    await interaction.channel.send("What a lovely day")
    await interaction.followup.send(
        f"Finished sending DMs.\nSent: {sent}\nFailed: {failed}",
        ephemeral=True,
    )

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot ready as {bot.user}")

if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Set DISCORD_BOT_TOKEN environment variable first.")
    bot.run(TOKEN)