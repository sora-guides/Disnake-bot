import disnake
from disnake.ext import commands

from ext.convenient_time import convert_time_format


class ModCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.has_permissions(kick_members=True)
    @commands.slash_command(name="kick", description="kicking members out of the server")
    async def kick_member(
            self, 
            inter: disnake.ApplicationCommandInteraction,
            member: disnake.Member=commands.Param(name="member"),
            reason: str=commands.Param(name="reason", description="write reason for kicking member", default="violation of the rule")
        ) -> None:
        """Kicks member"""
        if member.top_role > inter.author.top_role:
            await inter.response.send_message(embed=disnake.Embed(
                description=f"You don't have enough rights to kick {member.mention}",
                color=0xFF3333,
            ))
        
        # Example of writing an embed
        embed = disnake.Embed(
            description=f"User {member.mention} was kicked due to {reason}"
        )
        embed.add_field(name="Moderator:", value=inter.author.display_name)
        embed.set_footer(text=f"Asked: {inter.author.display_name}", icon_url=inter.author.display_avatar)
        
        # Permission is required for this action (select bot in scopes, then choose permissions you want)
        # await member.kick()
        await inter.send(embed=embed)
        
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(name="ban", description="ban members")
    async def ban_member(
            self,
            inter: disnake.ApplicationCommandInteraction,
            member: disnake.Member=commands.Param(name="member"),
            reason: str=commands.Param(name="reason", description="write reason for banning member", default="violation of the rule")
        ) -> None:
        """Bans this member"""    
        if member.top_role > inter.author.top_role:
            await inter.response.send_message(embed=disnake.Embed(
                title=f"You don't have enough rights to ban {member.mention}",
                color=0xFF9122,
            ))
        
        embed = disnake.Embed(
            description=f"User {member.mention} was banned due to {reason}"
        )
        embed.add_field(name="Moderator:", value=inter.author.display_name)
        embed.set_footer(text=f"Asked: {inter.author.display_name}", icon_url=inter.author.display_avatar)
        
        # Permission is required for this action (select bot in scopes, then choose permissions you want)
        # await member.ban()
        await inter.send(embed=embed)
    
    @commands.has_permissions(mute_members=True)
    @commands.slash_command(name="mute", description="mute members")
    async def mute_member(
            self,
            inter: disnake.ApplicationCommandInteraction,
            member: disnake.Member=commands.Param(name="member"),
            time: str=commands.Param(name="time", description="indicate time 10s/10m/10h/10d"),
            reason: str=commands.Param(name="reason", description="write reason for muting member", default="violation of the rule")
        ) -> None:
        """Mute members"""
        if member.top_role > inter.author.top_role:
            await inter.response.send_message(embed=disnake.Embed(
                title=f"You don't have enough rights to mute {member.mention}",
                color=0xFF9122,
            ))
        converted_time = convert_time_format(time)
        await inter.response.send_message(embed=disnake.Embed(
            description=f"{member.mention} was muted for {converted_time['answer']} due to {reason}"
        ))
        # Permission is required for this action (select bot in scopes, then choose permissions you want)
        # await member.timeout(duration=converted_time["duration"])
        
    @commands.has_permissions(manage_messages=True)
    @commands.slash_command(name="clear", description="clear chat")
    async def clear_chat(
            self,
            inter: disnake.ApplicationCommandInteraction
        ) -> None:
        await inter.response.send_message()
    
    

def setup(bot: commands.Bot) -> None:
    bot.add_cog(ModCommands(bot))