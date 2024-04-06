import disnake
from disnake.ext import commands


class ModCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.has_permissions()
    @commands.slash_command(name="kick", description="kicking members from server")
    async def kick_member(
            self, 
            inter: disnake.ApplicationCommandInteraction,
            member: disnake.Member=commands.Param(name="member"),
            reason: str=commands.Param(name="reason", description="write reason for kicking member", default="breaking rules")
        ) -> None:
        if member.top_role > inter.author.top_role:
            await inter.response.send_message(embed=disnake.Embed(
                    description=f"You don't have enough permition to kick {member.mention}",
                    color=0xFF3333,
                )
            )
        await inter.response.send_message(f"User {member.mention} was kicked for {reason}")
        await member.kick()
        
        embed = disnake.Embed(
            description="something for example"
        )
        embed.add_field(name="Moderator:", value=inter.author)
        embed.set_footer(text=f"Asked: {inter.author}", icon_url=inter.author.display_avatar)
        await inter.send(embed=embed)
    

def setup(bot: commands.Bot) -> None:
    bot.add_cog(ModCommands(bot))