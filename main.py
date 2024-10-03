import os
import discord
from discord.ui import Button,View
from discord.ext import commands
import asyncio
import random
import re
from response import get_response

bot = commands.Bot(command_prefix = ["baka! ","Baka! ","BAKA! ","baka!","Baka!","BAKA!"])
TOKEN = os.getenv('TOKEN')

#names collection to be used in future
names = ["Elon Musk","Emma Watson","Bliie Eilish","Tom Holland","Scarlett Johanson","Hero Alom","Donal Trump","Narendra Modi","Mamta Bannerjee",
"Chris Hemsworth","Harry Styles","Vin Disel","Pew Die Pie","Great KHali","John Cena","Jungkook","Jeff Bezos","Bill Gates","Selena Gomez",
"Taylor Swift","Ed Sheeran","Elizabeth Olsen","Zendaya","Newton","Einstein","Itachi"]

#gifs collection
#cry nani hawt
kills = ["https://i.pinimg.com/originals/cc/87/65/cc87656cf72979fb8ee01c3eebc5cdff.gif",
"https://giffiles.alphacoders.com/207/207976.gif",
"https://c.tenor.com/c9KEUCrTarUAAAAM/home-alone-macaulay-culkin.gif",
"https://data.whicdn.com/images/159568456/original.gif",
"https://c.tenor.com/1dtHuFICZF4AAAAC/kill-smack.gif",
"https://gifimage.net/wp-content/uploads/2017/09/anime-kill-gif.gif",
"https://thumbs.gfycat.com/ImpureShockedAfricanwildcat-size_restricted.gif",
"https://media0.giphy.com/media/BTV1vUcOWht2U/200.gif",
"https://cdn.myanimelist.net/s/common/uploaded_files/1479320732-107a459629d29cd6ae1eb576262ac190.gif",
"https://i.kym-cdn.com/photos/images/original/000/923/728/c01.gif",
"https://thumbs.gfycat.com/TautEllipticalHoneycreeper-size_restricted.gif",
"https://i1.wp.com/i.pinimg.com/originals/4b/dc/c0/4bdcc062ba6e5a3ec9ab57ca19be1f76.gif",
"https://c.tenor.com/LB8TaR89f_4AAAAC/attack-on-titan-captain-levi.gif",
"https://c.tenor.com/kjzNRi1MxkQAAAAC/levi-attack-on-titan.gif"
]

dance1 = ["https://c.tenor.com/VXcXebvlFNcAAAAC/hestia-dance.gif",
"https://66.media.tumblr.com/7fc40877365a72262bc73409b36e69f9/tumblr_ptfw6evtSB1v57tj1o1_500.gif",
"",
"https://i.kym-cdn.com/photos/images/newsfeed/001/062/639/3fc.gif",
"https://i.kym-cdn.com/photos/images/newsfeed/000/934/874/b59.gif",
"https://c.tenor.com/mGodtR952CIAAAAC/kono-suba-dance.gif",
"https://bestanimations.com/media/anime-dancing/1886969398anime-kawaii-cute-dance-animated-gif-image-7.gif",
"https://i0.wp.com/gifimage.net/wp-content/uploads/2017/06/anime-dancing-gif-8.gif?",
"http://i.imgur.com/XCgUrhx.gif",
"https://c.tenor.com/7r2Vr6KDS0cAAAAC/dancing-meme.gif",
"https://media4.giphy.com/media/y5efFpqW5knlu/giphy.gif",
"https://i.pinimg.com/originals/00/63/71/0063719c03ad81912a165ade89967d6c.gif",
"http://31.media.tumblr.com/2dd5c5e7ca4410fe9e59a6a82a678642/tumblr_mnw1q5R5AE1rygc5yo1_500.gif",
"https://i.pinimg.com/originals/b8/be/9d/b8be9da95dd9eeae2fe924eb0764b23d.gif",
]

dance2 = ["https://i.gifer.com/3yzz.gif",
"https://c.tenor.com/DbRUHnh1JfsAAAAM/chika-chika-dance.gif",
"https://c.tenor.com/7Ek4VLQbEasAAAAM/anime-excited.gif",
"https://i.pinimg.com/originals/30/79/43/307943df6fd23a4676c1594b72702af2.gif",
"https://bestanimations.com/media/anime-dancing/1821875339anime-kawaii-cute-dance-animated-gif-image-13.gif",
"https://c.tenor.com/jWRFHjiNdkgAAAAd/anime-dance.gif",
"https://data.whicdn.com/images/243563502/original.gif",
"https://c.tenor.com/qXWBVDCCcWoAAAAM/anime-dance.gif",
"https://c.tenor.com/x8yveWSI8V4AAAAC/sasuke-dance.gif",
"https://c.tenor.com/_8cIj9LxLIgAAAAC/sasuke-dancing.gif",
"https://i.pinimg.com/originals/e8/84/99/e884990a7863c90811e37b275cae3f0c.gif",
"https://i.gifer.com/3uvV.gif",
"https://c.tenor.com/woWcvZkct68AAAAM/naruto-sakura.gif",
"https://c.tenor.com/TvizESDwQ8QAAAAd/sakura-dancing.gif",
"https://c.tenor.com/v7_qayccrrwAAAAC/hinata-naruto.gif",
"https://c.tenor.com/CiJuhjUFaeIAAAAC/gojo-satoru-jujutsu-kaisen.gif",
"https://c.tenor.com/l-LG-VDGd_wAAAAC/dancing-levi-levi-spin.gif",
"https://c.tenor.com/DZ-2jJ6_NQkAAAAM/anime-anime-boy.gif",
"https://c.tenor.com/JVpawg5EBtIAAAAC/levi-police-costume.gif",
"https://i.pinimg.com/originals/5f/cc/31/5fcc31fe5bf4807a707ac8dd63ea874a.gif",
"http://pa1.narvii.com/6079/1aa547baf4dbfa6cea24236bc65d64d90c051d62_00.gif",
]

kisses = ["https://media4.giphy.com/media/G3va31oEEnIkM/giphy.gif",
"https://c.tenor.com/WijnhV9LiWAAAAAC/anime-kiss.gif",
"https://c.tenor.com/kUv5IOW0uW4AAAAd/anime-kiss.gif",
"https://c.tenor.com/3xq8k7sR3-gAAAAC/anime-kissing.gif",
"https://c.tenor.com/-736RHc6hIUAAAAC/anime-kiss.gif",
"https://c.tenor.com/dByCkw_u8e4AAAAC/kiss-anime.gif",
"https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-14.gif",
"https://c.tenor.com/PH8QymVbkNQAAAAd/anime-kiss-anime-hug.gif",
"https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-27.gif",
"https://c.tenor.com/1idq5OdQ4rUAAAAC/anime-kissing.gif",
"https://animesher.com/orig/1/134/1347/13472/animesher.com_cute-boruto-sakura-1347291.gif",
"https://c.tenor.com/sByA9H6jg1AAAAAM/naruto-shippuden-anime.gif",
"https://thumbs.gfycat.com/AncientUltimateImago-size_restricted.gif",
"https://c.tenor.com/rTJm1eRFD-sAAAAC/first-kiss-naruhina.gif",
"https://c.tenor.com/sSlbQU_9MmYAAAAC/hinata-sasuke.gif",
"https://c.tenor.com/-FL3wqNmAtEAAAAC/beijo-kiss.gif",
]

hugs = ["https://c.tenor.com/vontOjN9km4AAAAd/horimiya-anime-horimiya.gif",
"https://i.pinimg.com/originals/51/5d/9b/515d9b46b65c34207eb97d6fb538a3b4.gif",
"https://media4.giphy.com/media/ShAchOHe38Aak/200.gif",
"https://i.pinimg.com/originals/9b/20/53/9b2053e2b021f0338cd1c9be181adab7.gif",
"https://cdn.myanimelist.net/s/common/uploaded_files/1461068547-d8d6dc7c2c74e02717c5decac5acd1c7.gif",
"https://thumbs.gfycat.com/BitterEthicalIsabellinewheatear-size_restricted.gif",
"https://media4.giphy.com/media/PHZ7v9tfQu0o0/giphy.gif",
"https://c.tenor.com/iOxlB5V7lIkAAAAC/naruto-run.gif",
"https://c.tenor.com/kmr7MdW60jQAAAAC/anime-boobs.gif",
"https://c.tenor.com/XnclPox6NU0AAAAd/meliodas-hug.gif",
"https://i.pinimg.com/originals/f0/2c/7e/f02c7e8d52dac534526dbb86ccc5289e.gif",
"https://animesher.com/orig/1/152/1527/15275/animesher.com_anime-gif-hug-anime-hug-1527584.gif",
"https://cutewallpaper.org/21/cute-anime-hug/Top-15-Cutest-Anime-Hugs-Scenes-of-all-time.gif",
"https://c.tenor.com/otWKB7_a6iUAAAAC/anime-hug.gif",
"https://i.pinimg.com/originals/7d/b5/f1/7db5f172665f5a64c1a5ebe0fd4cfec8.gif",
"https://cdn.myanimelist.net/s/common/uploaded_files/1460992224-9f1cd0ad22217aecf4507f9068e23ebb.gif",
"https://acegif.com/wp-content/gif/anime-hug-45.gif",
"http://25.media.tumblr.com/tumblr_ma7l17EWnk1rq65rlo1_500.gif",
"https://c.tenor.com/1fXGbo7KvNUAAAAM/hug-anime.gif",
"https://i.pinimg.com/originals/64/b6/13/64b613ce35875db573e6fcc9c394c588.gif",
"https://c.tenor.com/SPs0Rpt7HAcAAAAM/chiya-urara.gif"
]

tickling = ["https://c.tenor.com/L5-ABrIwrksAAAAC/tickle-anime.gif",
"https://c.tenor.com/PXL1ONAO9CEAAAAC/tickle-laugh.gif",
"https://thumbs.gfycat.com/DaringGrossJellyfish-size_restricted.gif",
"https://i.imgur.com/ZKri92O.gif",
"https://i.gifer.com/8TK0.gif",
"https://c.tenor.com/9KCaFFBc_lkAAAAC/anime-tickle.gif",
"https://i.makeagif.com/media/4-06-2017/eBu9NS.gif",
"https://i.makeagif.com/media/5-18-2016/-BfbPD.gif",
"https://i.imgur.com/OYDvv2W.gif",
"https://i.imgur.com/VD8nvU5.gif",
"https://i.kym-cdn.com/photos/images/original/001/785/880/bae.gif",
"https://thumbs.gfycat.com/ThunderousShowyArmyant-size_restricted.gif",
"https://i.imgur.com/bt2ZRjJ.gif",
"https://i.imgur.com/4oiGtwW.gif",
"https://i.imgur.com/nexl6h4.gif"]

pats = ["https://c.tenor.com/edHuxNBD6IMAAAAC/anime-head-pat.gif",
"https://i.gifer.com/7eXf.gif",
"https://i.kym-cdn.com/photos/images/original/000/503/535/75c.gif",
"https://c.tenor.com/SONjh216O60AAAAC/pat-head-anime.gif",
"https://data.whicdn.com/images/297125550/original.gif",
"https://i.imgur.com/T80ei8L.gif",
"https://c.tenor.com/DCMl9bvSDSwAAAAC/pat-head-gakuen-babysitters.gif",
"https://i.gifer.com/1tZL.gif",
"https://c.tenor.com/o0re0DQzkd8AAAAC/anime-head-rub.gif",
"https://c.tenor.com/bAzYYE0VmV0AAAAC/aoharuxmachinegun-head-pat.gif",
"https://i.imgur.com/hHZYIf8.gif?noredirect",
"https://c.tenor.com/EoTyJ9XIwwgAAAAC/pat-sora.gif",
"https://c.tenor.com/lUnX8TExql8AAAAd/kyoukai-no.gif",
"https://c.tenor.com/2ryKlSRWZ8wAAAAC/sasuke-tap.gif",
"http://24.media.tumblr.com/3ee0fbd58e72ba0003155dfa26bd7b71/tumblr_mwoq8gn9wD1qhjnoso1_500.gif",
"https://25.media.tumblr.com/tumblr_lqd4mhaDTi1qjqz6co1_500.gif"
]

bonks = ["https://c.tenor.com/CrmEU2LKix8AAAAC/anime-bonk.gif",
"https://c.tenor.com/ur4zKUfK-s0AAAAM/fail-funny.gif",
"https://i.gifer.com/B6ya.gif",
"https://i.gifer.com/origin/d7/d77de33d229370f023a24ca6e4cf6079.gif",
"https://media4.giphy.com/media/30lxTuJueXE7C/giphy.gif",
"https://c.tenor.com/LYvlVL2udjEAAAAd/anime-kugiski-nobara.gif",
"https://i.imgur.com/3RgoNYy.gif",
"https://i.chzbgr.com/full/6167718656/hDB37C48C/bonk",
"https://media0.giphy.com/media/qgVnduXSn5Hy7DbW3r/200w.gif",
"https://c.tenor.com/_ZvbLvrT_QcAAAAC/horny-jail-bonk.gif",
"https://c.tenor.com/U6Sn_MmZleMAAAAM/go-to.gif",
"https://c.tenor.com/pcDYckPtnGwAAAAC/bonk.gif"]

cuddles = ["https://c.tenor.com/dbIbtIyByEwAAAAM/cuddle-anime.gif",
"https://c.tenor.com/H7i6GIP-YBwAAAAC/a-whisker-away-hug.gif",
"https://c.tenor.com/ch1kq7TOxlkAAAAC/anime-cuddle.gif",
"https://c.tenor.com/08vDStcjoGAAAAAd/cuddle-anime-hug-anime.gif",
"https://c.tenor.com/YCjsK-JgrPEAAAAC/anime-cuddle.gif",
"https://cutewallpaper.org/21/anime-couple-hugs/Anime-Couple-GIF-Anime-Couple-Hug-Discover-Share-GIFs.gif",
"http://pa1.narvii.com/6307/48833c48ef15114a1cd18aad434ffad6016dee59_00.gif",
"https://c.tenor.com/kvdkbEPFFQwAAAAC/kagehina-in-bed.gif",
"https://pa1.narvii.com/6103/57a8748b56d6f34b678a3998c92522883ae45749_hq.gif",
"https://d.wattpad.com/story_parts/910891886/images/16216fc1aecee80b286582049178.gif"]

smirking = ["https://c.tenor.com/3FNn5kxYsCUAAAAC/anime-smirk.gif",
"https://thumbs.gfycat.com/ImpoliteMarriedAmericanshorthair-size_restricted.gif",
"https://i.pinimg.com/originals/97/f9/4c/97f94cf54f7d823e2e4959b1e3f8af9f.gif",
"https://www.icegif.com/wp-content/uploads/karma-akabane-icegif-1.gif",
"https://i.imgur.com/p4RzFxP.gif",
"https://thumbs.gfycat.com/ImpoliteMarriedAmericanshorthair-size_restricted.gif"
"https://i.pinimg.com/originals/62/ed/00/62ed000780e575631164c08f3b583e12.gif",
"https://c.tenor.com/vMdqAAXoj6MAAAAC/kageyama-tobio-ready.gif",
"https://c.tenor.com/WgwGiXzQGK0AAAAC/anime-smirking.gif",
"https://i.gifer.com/RylD.gif"]

stares  = ["https://media3.giphy.com/media/Blo52zq6T0cO4/200.gif",
"https://i.pinimg.com/originals/05/aa/4f/05aa4fc7315cdb9424060eea26574e65.gif",
"https://i.gifer.com/9jXw.gif",
"https://i.pinimg.com/originals/76/d8/b1/76d8b1ae60c2a4e8db2b72b2e15c36a1.gif",
"https://c.tenor.com/TkhySghTXtIAAAAd/fierce-anime.gif",
"https://c.tenor.com/y445Jeq54BEAAAAC/anime-food-wars.gif",
"https://c.tenor.com/il3flm3FkTAAAAAC/darling-in-the-franxx-anime.gif",
"https://i.pinimg.com/originals/c1/cf/89/c1cf89fa64901ebfe9a5999eb62951d9.gif",
"https://i.pinimg.com/originals/76/19/d7/7619d77a277015d0c822aa1147fdaef8.gif",
"https://c.tenor.com/dAcNU9ZL7KUAAAAC/itachi-uchiha.gif",
"https://c.tenor.com/CKk34xHiJ2UAAAAC/itachi-meme.gif",
"https://c.tenor.com/cT5F9Vtvf2cAAAAC/boobs-tsunade.gif",
"https://i.makeagif.com/media/4-28-2015/tnzbK6.gif",
"https://thumbs.gfycat.com/InsecureAgedGemsbok-max-1mb.gif",
"https://i.makeagif.com/media/2-04-2016/5GluIg.gif",
"https://c.tenor.com/LGCS8U0fTFkAAAAd/gojo-satoru-jjk.gif",

]

punches = ["https://c.tenor.com/U_LbHhKhjJ8AAAAC/jujutsu-kaisen-jujutsu.gif",
"https://c.tenor.com/VrWzG0RWmRQAAAAC/anime-punch.gif",
"https://giffiles.alphacoders.com/169/169717.gif",
"https://c.tenor.com/o0FEX0ZcSAEAAAAd/hibiki-punch-anime-punch.gif",
"https://i.pinimg.com/originals/66/76/7a/66767af902113b20978f5880593b29af.gif",
"https://media0.giphy.com/media/12NV85Ttcs71Kg/giphy-downsized.gif",
"https://c.tenor.com/6m7lWU-7P7MAAAAC/anime-punch.gif",
"https://c.tenor.com/eKUQI_vt_VAAAAAC/daily-life-of-the-immortal-king.gif",
"https://i.kym-cdn.com/photos/images/newsfeed/001/057/927/eac.gif",
"https://c.tenor.com/EdV_frZ4e_QAAAAM/anime-naruto.gif",
"https://c.tenor.com/0KFmiw0laqAAAAAd/soul-eater-sword.gif",
"https://c.tenor.com/94rx9Tga94YAAAAC/reiner-punch.gif",
"https://i.gifer.com/9eUJ.gif",
"https://i.gifer.com/9rSV.gif"]

kicks  = ["https://media0.giphy.com/media/wOly8pa4s4W88/giphy.gif",
"https://giffiles.alphacoders.com/172/172576.gif",
"http://38.media.tumblr.com/ccfb562515974aafd5e879b75439ff18/tumblr_nece2jUD3p1tsd042o1_500.gif",
"https://c.tenor.com/466rKrer_CgAAAAC/mikey-tokyo-revengers-mikey-kick.gif",
"https://c.tenor.com/-vd5_5l0AXMAAAAd/tokyo-revengers-tokyo-revengers-mikey.gif",
"https://c.tenor.com/EUif99vl0n4AAAAC/anime-tokyo-revengers.gif",
"https://c.tenor.com/ueuCuE42zq0AAAAC/sasuke-uchiha-kakashi-hatake.gif",
"https://c.tenor.com/5s8Y_vkLu6UAAAAC/madara-uchiha.gif",
"https://i.pinimg.com/originals/63/c4/53/63c453899833312ea1afd8f4b4d92db8.gif",
"https://c.tenor.com/mwuwE5zLBiQAAAAC/naruto-naruto-dab.gif",
"https://giffiles.alphacoders.com/125/125270.gif",
"https://acegif.com/wp-content/uploads/funny-anime-gif-91.gif"]

slaps = ["https://c.tenor.com/CvBTA0GyrogAAAAC/anime-slap.gif",
"https://i.pinimg.com/originals/fe/39/cf/fe39cfc3be04e3cbd7ffdcabb2e1837b.gif",
"https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b02c16d5-1b1b-4139-92e6-ca6b3d768d7a/d6wv007-5fbf8755-5fca-4e12-b04a-ab43156ac7d4.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2IwMmMxNmQ1LTFiMWItNDEzOS05MmU2LWNhNmIzZDc2OGQ3YVwvZDZ3djAwNy01ZmJmODc1NS01ZmNhLTRlMTItYjA0YS1hYjQzMTU2YWM3ZDQuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.4MVfHXfzK83yI6L2NpBfVb2knaJtyGd7TlSEDH79bH8",
"https://i.pinimg.com/originals/68/de/67/68de679cc20000570e8a7d9ed9218cd3.gif",
"https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif",
"https://cdn.quotesgram.com/img/50/92/797193858-UXqzzab.gif",
"https://c.tenor.com/VlSXTbFcvDQAAAAC/naruto-anime.gif",
"https://giffiles.alphacoders.com/183/183799.gif",
"https://media.vanityfair.com/photos/5841d1deba2ef6d738a212bb/master/w_1600%2Cc_limit/hollywoods-best-slaps-pokemon-pikachu.gif",
"https://c.tenor.com/M1MLHpGTwusAAAAC/tengen-uzui-demon-slayer.gif",
"https://i.pinimg.com/originals/41/73/a4/4173a49cf302675f25f850cf21234a8c.gif"]

cries = ["https://c.tenor.com/OfYt0T0tgCYAAAAC/anime-cry.gif",
"https://c.tenor.com/PMSEpGeHk6QAAAAC/crying-anime.gif",
"https://www.icegif.com/wp-content/uploads/sad-anime-icegif.gif",
"https://animesher.com/orig/0/94/949/9490/animesher.com_anime-girl-anime-gif-crying-gif-949058.gif",
"https://media0.giphy.com/media/TRgyI2f0hRHBS/giphy.gif",
"http://24.media.tumblr.com/86e3fd9c2c56d4cde3277f112512fbd1/tumblr_mrh5xtoUjM1s13iszo1_500.gif",
"http://mrwgifs.com/wp-content/uploads/2013/05/Dramatic-Crying-In-Anime-Gif.gif",
"https://c.tenor.com/YM3fW1y6f8MAAAAC/crying-cute.gif",
"https://c.tenor.com/DTThhk0oPCAAAAAd/your-name-cry.gif",
"https://c.tenor.com/Ly3W7A0nGe4AAAAC/kimi-no-na-wa-anime.gif",
"https://c.tenor.com/WKkmocWZQ2AAAAAC/haikyu-crying.gif",
"https://c.tenor.com/51Ldyb5W4UAAAAAC/haikyuu-cry.gif",
"https://c.tenor.com/MtQWQtHxXCwAAAAM/haikyuu-anime.gif",
"https://i.pinimg.com/originals/82/e9/e7/82e9e7713acefba2eccc892a0abe7493.gif",
"https://i.pinimg.com/originals/d9/2a/1c/d92a1cf8aef657f514349872e882dae6.gif"]

blushing = ["https://c.tenor.com/JhO1fYhvP14AAAAC/face-blush.gif",
"https://c.tenor.com/KKLSi3AgXuoAAAAC/anime-girl.gif",
"https://i.pinimg.com/originals/91/ef/7d/91ef7d7d92f360ef3487056a82765526.gif",
"https://c.tenor.com/hXGbCYQfO6oAAAAC/anime-blush.gif",
"https://c.tenor.com/RMqL77sBpisAAAAC/anime-cute.gif",
"https://c.tenor.com/X-qlRuQy7vsAAAAC/anime-cute.gif",
"https://c.tenor.com/AYEuFHjE1kcAAAAC/hori-blush.gif",
"https://c.tenor.com/opMLrta2u6sAAAAC/i-am-not-a-otaku-horimiya.gif",
"https://data.whicdn.com/images/143256071/original.gif",
"https://data.whicdn.com/images/118933647/original.gif",
"https://c.tenor.com/Dc6CyYz71xkAAAAd/hinata-hyuga-hinata-hyuuga.gif"]

@bot.event
async def on_ready():
    print(f"We have logged in as {bot}")
    await bot.change_presence(status = discord.Status.idle, activity=discord.Game("Type baka! ohayo to get started 👻"))

@bot.command(name = "Ohayo",help = "This command starts your journey with this bot",aliases= ["OHAYO","start","Start","Begin","begin","ohayo"])
async def ohayo(ctx):
    butt = Button(label = "Click Me For Help!!",style = discord.ButtonStyle.green, emoji = "👻")
    embed  = discord.Embed(title = "Ohayo!!", color = discord.Color.purple())
    async def button_callback(interaction):
        embed.clear_fields()
        embed.add_field(name = "You need help don't you?",value = f"Here's a list of command to save your ass!!\nnote: the commands must all be in lowercase")
        embed.add_field(name = "baka! about", value = "It's bascially a section about the mastermind who is behind this bot")
        embed.add_field(name = "baka! kill",value = f"This commands let's you kill someone xD")
        embed.add_field(name = "baka! dance",value = f"This let's you dance with the person you want to")
        embed.add_field(name = "baka! kiss",value = f"This let's you kiss your crush with whom you can't even talk to")
        embed.add_field(name = "baka! hug",value = f"This let's you hug and forget the fact that u're adopted")
        embed.add_field(name = "baka! tickle",value = f"This let's you tickle someone and forget u're depressed")
        embed.add_field(name = "baka! pat",value = f"This let's you pat someone and get brozoned")
        embed.add_field(name = "baka! bonk",value = f"This let's you bonk the horny people")
        embed.add_field(name = "baka! cuddle",value = f"This let's you cuddle virtually cuz in real lief you ain't getting it")
        embed.add_field(name = "baka! smirk",value = f"This let's you smirk at people (the only thing that u're good at)")
        embed.add_field(name = "baka! stare",value = f"This let's you stare at people and make them believe that u're a creep")
        embed.add_field(name = "baka! punch",value = f"Punch the people in their face if you don't like them")
        embed.add_field(name = "baka! kick",value = f"Now that's for nut busting moments")
        embed.add_field(name = "baka! slap",value = f"This is what you do to perverts")
        embed.add_field(name = "baka! cry",value = f"Aww you wanna cry? here you go cry as much as you want!")
        embed.add_field(name = "baka! blush",value = f"Well try using this when your crush is online")
        await interaction.response.send_message(embed = embed)
    
    butt.callback = button_callback

    view = View()
    view.add_item(butt)

    embed.add_field(name = "Is it morning already?",value = f"ohayo {ctx.author.mention} san!! ")
    "https://discord.com/api/oauth2/authorize?client_id=848613937360142376&permissions=414501559104&scope=bot"
    embed.add_field(name="Wanna Add this cool bot to your own server?", value = "https://rb.gy/8hxr4q")

    msg = await ctx.send(embed = embed, view = view)

@bot.command(name = "About",help = "This command tells you about the creator",aliases= ["info","ABOUT","about"])
async def about(ctx):
    butt = Button(label = "Click Me To Invite",url = "https://rb.gy/8hxr4q", emoji = "🥵")
    embed  = discord.Embed(title = "Ohayo!!", color = discord.Color.green())

    view = View()
    view.add_item(butt)

    embed.add_field(name = "What is this bot?",value = f"This bot is an inspiration from the senpai bot which used to have gif for funny situations to use in between conversations. Since it has been discontinued Aritro Saha programmed this bot for the same intention to make chats more fun!! Hope you will enjoy it here!!")
    embed.add_field(name="Wanna support the creator?", value = "you don't have to do much just follow him in Instagram \nhttps://www.instagram.com/halcyon_past/ \n to get started with the bot type ```baka! ohayo``` ")

    msg = await ctx.send(embed = embed, view = view)

@bot.command(name = "Kill",help = "This commands let's you kill someone xD",aliases= ["murder","slay","Murder","Slay","KILL","kill"])
async def kill(ctx):
    embed  = discord.Embed(title = "Killing is Real", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "Omg! a murderer",value = f"{ctx.author.mention} just killed {message[0]}" )
            embed.set_image(url= f"{random.choice(kills)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Omg! you took your heart out!!",value = f"{ctx.author.mention} it seem's you just cant't die" )
            embed.set_image(url= f"https://c.tenor.com/0w3AFTfAiaoAAAAC/sukuna-itadori.gif")
            await ctx.send(embed = embed)
    else:
        print("This")
        embed.add_field(name = "Omg! you took your heart out!!",value = f"{ctx.author.mention} it seem's you just cant't die" )
        embed.set_image(url= f"https://c.tenor.com/0w3AFTfAiaoAAAAC/sukuna-itadori.gif")
        await ctx.send(embed = embed)  

@bot.command(name = "Dance",help = "This let's you dance with the person you want to",aliases= ["DANCE","party","vibe","Party","Vibe","dance"])
async def dance(ctx):
    embed  = discord.Embed(title = "Dance is life!", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "Go with the flow",value = f"{ctx.author.mention} danced with {message[0]}" )
            embed.set_image(url= f"{random.choice(dance1)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Go with the flow",value = f"{ctx.author.mention} danced with their imaginary friend I suppose" )
            embed.set_image(url= f"{random.choice(dance1)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "Go with the flow",value = f"{ctx.author.mention} started dancing" )
        embed.set_image(url= f"{random.choice(dance2)}")
        await ctx.send(embed = embed)
        
@bot.command(name = "Kiss",help = "This let's you kiss your crush with whom you can't even talk to",aliases= ["KISS","kiss","smooch","Smooch","muah","Muah"])
async def kiss(ctx):
    embed  = discord.Embed(title = "Kiss me told you eyes!", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "Ahm Ahm!!",value = f"{ctx.author.mention} kissed {message[0]} passionately" )
            embed.set_image(url= f"{random.choice(kisses)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Ahm Ahm!!",value = f"{ctx.author.mention} kissed {random.choice(names)} passionately omg!!" )
            embed.set_image(url= f"{random.choice(kisses)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "Ahm Ahm!!",value = f"{ctx.author.mention} kissed their imaginary partner and woke up from the dream" )
        embed.set_image(url= f"{random.choice(kisses)}")
        await ctx.send(embed = embed)

@bot.command(name = "Hug",help = "This let's you hug and forget the fact that u're adopted",aliases= ["HUG","grab","Grab","hug"])
async def hug(ctx):
    embed  = discord.Embed(title = "The warmth", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "I feel safe",value = f"{ctx.author.mention} hugged {message[0]} tightly" )
            embed.set_image(url= f"{random.choice(hugs)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "I feel safe",value = f"{ctx.author.mention} hugged {random.choice(names)} tightly" )
            embed.set_image(url= f"{random.choice(hugs)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "I feel safe",value = f"{ctx.author.mention} got hugged by their crush... wait what?" )
        embed.set_image(url= f"{random.choice(hugs)}")
        await ctx.send(embed = embed)

@bot.command(name = "Tickle",help = "This let's you tickle someone and forget u're depressed",aliases= ["TICKLE","katakutu","Katakutu","tickle"])
async def tickle(ctx):
    embed  = discord.Embed(title = "Yamete!!", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "Kudasaii!!",value = f"{ctx.author.mention} tickled {message[0]} " )
            embed.set_image(url= f"{random.choice(tickling)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Kudasai!!",value = f"{ctx.author.mention} got tickled by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(tickling)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "KUdasai!!",value = f"{ctx.author.mention} got tickled" )
        embed.set_image(url= f"{random.choice(tickling)}")
        await ctx.send(embed = embed)

@bot.command(name = "Pat",help = "This let's you pat someone and get brozoned",aliases= ["PAT","headpat","Headpat","pat"])
async def pat(ctx):
    embed  = discord.Embed(title = "Heddo Patto", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "It's okay",value = f"{ctx.author.mention} pats {message[0]} " )
            embed.set_image(url= f"{random.choice(pats)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "It's Okay",value = f"{ctx.author.mention} got pat by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(pats)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "It's Okay",value = f"{ctx.author.mention} got pat" )
        embed.set_image(url= f"{random.choice(pats)}")
        await ctx.send(embed = embed)

@bot.command(name = "Bonk",help = "This let's you bonk the horny people",aliases= ["BONK","nohorny","NoHorny","bonk"])
async def bonk(ctx):
    embed  = discord.Embed(title = "Boink", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "No horny",value = f"{ctx.author.mention} bonks {message[0]} " )
            embed.set_image(url= f"{random.choice(bonks)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "No horny",value = f"{ctx.author.mention} got bonked by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(bonks)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "No horny",value = f"{ctx.author.mention} got bonked" )
        embed.set_image(url= f"{random.choice(bonks)}")
        await ctx.send(embed = embed)

@bot.command(name = "Cuddle",help = "This let's you cuddle virtually cuz in real lief you ain't getting it",aliases= ["CUDDLE","sleep","Sleep","cuddle"])
async def cuddle(ctx):
    embed  = discord.Embed(title = "Comfyy!!", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "I love it here",value = f"{ctx.author.mention} started cuddling with {message[0]} " )
            embed.set_image(url= f"{random.choice(cuddles)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "I love it here",value = f"{ctx.author.mention} started cuddling with {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(cuddles)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "I love it here",value = f"{ctx.author.mention} started cuddling with their imaginary partner" )
        embed.set_image(url= f"{random.choice(cuddles)}")
        await ctx.send(embed = embed)

@bot.command(name = "Smirk",help = "This let's you smirk at people (the only thing that u're good at)",aliases= ["SMIRK","HMMM","hmm","smirk"])
async def smirk(ctx):
    embed  = discord.Embed(title = "Sussy Baka", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "Hmmmmmm!!",value = f"{ctx.author.mention} started smirked at {message[0]} " )
            embed.set_image(url= f"{random.choice(smirking)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Hmmmmmm!!",value = f"{ctx.author.mention} got smirked by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(smirking)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "Hmmmmmm!!",value = f"{ctx.author.mention} started smirking at literally nothing" )
        embed.set_image(url= f"{random.choice(smirking)}")
        await ctx.send(embed = embed)

@bot.command(name = "Stare",help = "This let's you stare at people and make them believe that u're a creep",aliases= ["STARE","look","LOOK","stare"])
async def stare(ctx):
    embed  = discord.Embed(title = "Sussy Baka", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "Hmmmmmm!!",value = f"{ctx.author.mention} started staring at {message[0]} " )
            embed.set_image(url= f"{random.choice(stares)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Hmmmmmm!!",value = f"{ctx.author.mention} got stared by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(stares)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "Hmmmmmm!!",value = f"{ctx.author.mention} started staring at literally nothing" )
        embed.set_image(url= f"{random.choice(stares)}")
        await ctx.send(embed = embed)

@bot.command(name = "Punch",help = "Punch the people in their face if you don't like them",aliases= ["PUNCH","fist","FIST","punch"])
async def punch(ctx):
    embed  = discord.Embed(title = "Thousand Years of death!!", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "kaboom!!!!",value = f"{ctx.author.mention} punched {message[0]} " )
            embed.set_image(url= f"{random.choice(punches)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "kaboom!!!!",value = f"{ctx.author.mention} got punched by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(punches)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "kaboom!!!!",value = f"{ctx.author.mention} started punching thin air" )
        embed.set_image(url= f"{random.choice(punches)}")
        await ctx.send(embed = embed)

@bot.command(name = "Kick",help = "Now that's for nut busting moments",aliases= ["KICK","nutbreak","nutcrack","kick"])
async def kick(ctx):
    embed  = discord.Embed(title = "Thousand Years of pain!!", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "The world shall know pain",value = f"{ctx.author.mention} kicked {message[0]} " )
            embed.set_image(url= f"{random.choice(kicks)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "The world shall know pain",value = f"{ctx.author.mention} got kicked by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(kicks)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "The world shall know pain",value = f"{ctx.author.mention} started kicking asses" )
        embed.set_image(url= f"{random.choice(kicks)}")
        await ctx.send(embed = embed)

@bot.command(name = "Slap",help = "This is what you do to perverts",aliases= ["SLAP","smack","Smack","slap"])
async def slap(ctx):
    embed  = discord.Embed(title = "Ittai!!", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "ouch!!",value = f"{ctx.author.mention} slapped {message[0]} " )
            embed.set_image(url= f"{random.choice(slaps)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "ouch!!",value = f"{ctx.author.mention} got slapped by {random.choice(names)}" )
            embed.set_image(url= f"{random.choice(slaps)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "ouch!!",value = f"{ctx.author.mention} started slapping facts" )
        embed.set_image(url= f"{random.choice(slaps)}")
        await ctx.send(embed = embed)

@bot.command(name = "Cry",help = "Aww you wanna cry? here you go cry as much as you want!",aliases= ["CRY","breakdown","Breakdown","cry"])
async def cry(ctx):
    embed  = discord.Embed(title = "If i die don't cry", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "Just look at the sky",value = f"{ctx.author.mention} cried on {message[0]} " )
            embed.set_image(url= f"{random.choice(cries)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Just look at the sky",value = f"{ctx.author.mention} started crying and {random.choice(names)} came to give comfort" )
            embed.set_image(url= f"{random.choice(cries)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "Just look at the sky",value = f"{ctx.author.mention} started crying for no reason such a mumma's baby" )
        embed.set_image(url= f"{random.choice(cries)}")
        await ctx.send(embed = embed)

@bot.command(name = "Blush",help = "Well try using this when your crush is online",aliases= ["BLUSH","uwu","UwU","blush"])
async def blush(ctx):
    embed  = discord.Embed(title = "UwU", color = discord.Color.purple())
    pattern1 = r"<@!\d{14,}>"
    pattern2 = r"<@\d{14,}>"
    message = ctx.message.content.split()
    if len(message) >2:
        message = ctx.message.content.split()[2:]
        if re.match(pattern1,message[0]) or re.match(pattern2,message[0]):
            embed.add_field(name = "I swear i'm fine",value = f"{ctx.author.mention} blushes when {message[0]} is near" )
            embed.set_image(url= f"{random.choice(blushing)}")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "I swear i'm fine",value = f"{ctx.author.mention} starts to blush seeing that {random.choice(names)} came to check out" )
            embed.set_image(url= f"{random.choice(blushing)}")
            await ctx.send(embed = embed)
    else:
        embed.add_field(name = "I swear i'm fine",value = f"{ctx.author.mention} started blushing randomly" )
        embed.set_image(url= f"{random.choice(blushing)}")
        await ctx.send(embed = embed)

@bot.command(name = "aiAnime",help = "This command let's you chat with the bot",aliases= ["ai","chat","Chat","AI"])
async def aiAnime(ctx):
    await ctx.send("Hi! What would you like to chat about?")

    # Wait for the user's message
    try:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        user_message = await bot.wait_for('message', check=check, timeout=60)  # 60 seconds timeout

        # Generate AI response
        response = get_response(user_message.content)

        # Send the AI's response
        await ctx.send(response)

    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! Try again when you're ready.")

    

bot.run(TOKEN)
