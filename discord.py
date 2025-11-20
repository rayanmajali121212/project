import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class MyModal(Modal):
    def __init__(self):
        super().__init__(title="أدخل النص")
        self.text_input = TextInput(label="اكتب هنا", style=discord.TextStyle.paragraph)
        self.add_item(self.text_input)

    async def callback(self, interaction: discord.Interaction):
        # هنا نستخدم مكتبة PIL أو أي مكتبة لإنشاء صورة من النص
        from PIL import Image, ImageDraw, ImageFont
        import io

        text = self.text_input.value
        # إعداد الصورة
        img = Image.new('RGB', (400, 200), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        d.text((10,10), text, font=font, fill=(255,255,0))
        
        # حفظ الصورة في بايت
        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await interaction.response.send_message(file=discord.File(fp=image_binary, filename='image.png'))

@bot.command()
async def start(ctx):
    button = Button(label="أرسل نص", style=discord.ButtonStyle.primary)

    async def button_callback(interaction):
        modal = MyModal()
        await interaction.response.send_modal(modal)

    button.callback = button_callback
    view = View()
    view.add_item(button)
    await ctx.send("اضغط على الزر أدناه لإدخال النص", view=view)

bot.run('MTM3ODAzMjA2MjcwNzAwNzU5OQ.GLl0To.UYvn9uY9Dak6aWFIgf26fvyVdqgo2DfnvIi5n8')
