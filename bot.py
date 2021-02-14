import discord
import random
import os
import datetime
from discord.ext import commands


client = commands.Bot( command_prefix ='.' )

# Words

hello_words = ['hello','hi']
answer_words = ['info server','command','command server',]
goodbye_words = ['goodbye','bb']


@client.event

async def on_ready():
	print ('BOT connected')
	await client.change_presence(activity=discord.Game(name='CS:GO'))
	activity = discord.Activity(name='my activity', type=discord.ActivityType.watching)
	await client.change_presence(activity=activity)

# clear message
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def clear(ctx,amount = 100):
	await ctx.channel.purge(limit = amount)

# Kick
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member,*,reason = None):
	await ctx.channel.purge(limit = 1)

	await member.kick(reason = reason)
	await ctx.send( f'kick user{ member.mention }')

# ban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member,*,reason = None):
	await ctx.channel.purge(limit = 1)

	await member.ban(reason = reason)
	await ctx.send( f'Banned user{ member.mention }')

# unban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member ):
	await ctx.channel.purge(limit=1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'Unbanned user{user.mention}')

		return

# mute
@client.command()
@commands.has_permissions(administrator = True)

async def user_mute(ctx,member:discord.Member):
	await ctx.channel.purge(limit = 1)

	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')

	await member.add_roles(mute_role)
	await ctx.send( f'{member.mention}, chat restriction for breaking the rules')

#time
@client.command()

async def time(ctx):
	emb=discord.Embed(title='My bot',colour = discord.Color.green(),url= 'https://www.timeserver.ru/')

	emb.set_author(name= client.user.name, icon_url = client.user.avatar_url )
	emb.set_image(url='https://files.fm/thumb.php?i=nm5shk6xm')

	now_date = datetime.datetime.now()

	emb.add_field (name='Time',value = 'Time:{}'.format(now_date))

	await ctx.send(embed = emb)


@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@client.command()
async def helps(ctx):
    embed = discord.Embed(title="My bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name=".clear", value="aaaaaaaaaa", inline=False)
    embed.add_field(name=".time", value="aaaaaaaaaa", inline=False)
    embed.add_field(name=".kick", value="aaaaaaaaaa", inline=False)
    embed.add_field(name=".ban", value="aaaaaaaaaa", inline=False)
    embed.add_field(name=".unban", value="aaaaaaaaaa", inline=False)
    embed.add_field(name=".user_mute", value="aaaaaaaaaa", inline=False)
    embed.add_field(name=".info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name=".helps", value="Gives this message", inline=False)

    await ctx.send(embed=embed)



@client.command()
async def info(ctx):
    embed = discord.Embed(title="My bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="Maksym Miroshnychenko")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Numer albumu", value="W60054")

    await ctx.send(embed=embed)



@client.event

async def on_message( message ):
	await client.process_commands(message)
	msg = message.content.lower()

	if msg in hello_words:
		await message.channel.send('Hi,what did you want?')

	if msg in answer_words:
	    await message.channel.send('Write command .helps and find out everything')

	if msg in goodbye_words:
		await message.channel.send('Goodbye,good luck!')


# Connect

token = ('ODAwMzcxNDk1Njg2ODk3Njg0.YARKCg.pM43zKKdgeV89vO96CudZ1cSFW0')

client.run( token )



