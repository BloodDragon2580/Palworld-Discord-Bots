import nextcord
from nextcord.ext import commands
from util.economy_system import (
    add_points,
    get_points,
    set_points,
    link_steam_account,
    update_discord_username,
)
import json

class EconomyManageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_config()

    def load_config(self):
        config_path = "config.json"
        with open(config_path) as config_file:
            self.economy_config = json.load(config_file)
        self.economy_config = self.economy_config.get("ECONOMY_SETTINGS", {})
        self.currency = self.economy_config.get("currency", "points")

    @nextcord.slash_command(
        name="economyset",
        description="Economy management.",
        default_member_permissions=nextcord.Permissions(administrator=True),
    )
    async def economyset(self, _interaction: nextcord.Interaction):
        pass

    @economyset.subcommand(name="addpoints", description="Füge einem Benutzer Punkte hinzu.")
    async def addpoints(
        self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(description="Wähle den Benutzer aus"),
        points: int = nextcord.SlashOption(description="Wie viele Punkte sollen hinzugefügt werden?"),
    ):
        user_id = str(user.id)
        user_name = user.display_name
        add_points(user_id, user_name, points)
        emebd = nextcord.Embed(
            title=f"{self.currency} hinzugefügt",
            description=f"{points} {self.currency} zu {user_name} hinzugefügt.",
            color=nextcord.Color.blurple(),
        )
        await interaction.response.send_message(embed=emebd, ephemeral=True)

    @economyset.subcommand(name="checkpoints", description="Überprüfe die Punkte eines Benutzers.")
    async def checkpoints(
        self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(description="Wähle den Benutzer aus"),
    ):
        user_id = str(user.id)
        user_name = user.display_name
        user_name, points = get_points(user_id, user_name)

        embed = nextcord.Embed(
            title=f"Überprüfe {self.currency}",
            description=f"{user_name} hat {points} {self.currency}.",
            color=nextcord.Color.blurple(),
        )
        if user_name:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("Benutzer nicht gefunden.", ephemeral=True)

    @economyset.subcommand(name="setpoints", description="Lege die Punkte eines Benutzers fest.")
    async def setpoints(
        self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(description="Wähle den Benutzer aus"),
        points: int = nextcord.SlashOption(description="Wie viele Punkte sollen gesetzt werden?"),
    ):
        user_id = str(user.id)
        user_name = user.display_name
        set_points(user_id, user_name, points)
        embed = nextcord.Embed(
            title=f"{self.currency} festlegen",
            description=f"Setze die {self.currency} von {user_name} auf {points}.",
            color=nextcord.Color.blurple(),
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @economyset.subcommand(
        name="forcesteam", description="Erzwinge die Verknüpfung des Steam-Kontos eines Benutzers."
    )
    async def force_steam(
        self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(description="Wähle den Benutzer aus"),
        steam_id: str = nextcord.SlashOption(description="Gebe die Steam-ID des Benutzers ein"),
        verification_code: str = nextcord.SlashOption(
            description="Gebe den Bestätigungscode ein"
        ),
    ):
        user_id = str(user.id)
        user_name = user.display_name
        await link_steam_account(user_id, steam_id, verification_code)

        await update_discord_username(user_id, user_name)

        await interaction.response.send_message(
            f"Steam-Konto {steam_id} mit {user.display_name} verknüpft.", ephemeral=True
        )

    @economyset.subcommand(
        name="removepoints", description="Punkte von einem Benutzer entfernen."
    )
    async def removepoints(
        self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(description="Wähle den Benutzer aus"),
        points: int = nextcord.SlashOption(description="Wie viele Punkte sollen entfernt werden?"),
    ):
        user_id = str(user.id)
        user_name = user.display_name
        user_name, current_points = get_points(user_id, user_name)
        if current_points < points:
            await interaction.response.send_message(
                f"{user_name} verfügt nicht über genügend {self.currency} zum Entfernen.",
                ephemeral=True,
            )
            return
        new_points = current_points - points
        set_points(user_id, user_name, new_points)
        embed = nextcord.Embed(
            title=f"{self.currency} entfernt",
            description=f"{points} {self.currency} von {user_name} entfernt.",
            color=nextcord.Color.blurple(),
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @economyset.subcommand(
        name="help", description="Hilfe für die Economy befehle anzeigen."
    )
    async def help(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="Economy Management Help", color=nextcord.Color.blurple()
        )
        embed.add_field(
            name="Commands",
            value="`/economyset addpoints` - Einem Benutzer Punkte hinzufügen.\n"
            "`/economyset checkpoints` - Überprüfe die Punkte eines Benutzers.\n"
            "`/economyset setpoints` - Lege die Punkte eines Benutzers fest.\n"
            "`/economyset removepoints` - Punkte von einem Benutzer entfernen.\n"
            "`/economyset forcesteam` - Erzwinge die Verknüpfung des Steam-Kontos eines Benutzers.",
            inline=False,
        )
        await interaction.response.send_message(embed=embed)

def setup(bot):
    config_path = "config.json"
    with open(config_path) as config_file:
        config = json.load(config_file)

    economy_settings = config.get("ECONOMY_SETTINGS", {})
    if not economy_settings.get("enabled", False):
        return

    bot.add_cog(EconomyManageCog(bot))
