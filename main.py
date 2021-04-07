import discord
import asyncio
import youtube_dl 
import time
import urllib.request
from urllib.parse import quote
import re
import random
import pickle
import json
import logging

client = discord.Client()
token = "ODIzNDMzMDU2MzkxNjU5NTMx.YFgvyw.CfYBAZ_CYVrCK1iGDt_8bP2T5VE"

@client.event
async def on_ready():
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    t = str(str(time.localtime(time.time()).tm_year) + "/" + str(time.localtime(time.time()).tm_mon) + "/" + str(time.localtime(time.time()).tm_mday) + "/" + str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min) + ":" + str(time.localtime(time.time()).tm_sec))
    game = discord.Game("송인봇 온라인") # 상태 메시지
    await client.change_presence(status=discord.Status.online, activity=game)
    logging.info(t+" [songinbot()] [songinbot()] login succeed")
    print(t+" [songinbot()] [songinbot()] login succeed")

@client.event
async def on_message(message):
    t = str(str(time.localtime(time.time()).tm_year) + "/" + str(time.localtime(time.time()).tm_mon) + "/" + str(time.localtime(time.time()).tm_mday) + "/" + str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min) + ":" + str(time.localtime(time.time()).tm_sec))

    if message.content == "송인아":
        await message.channel.send(message.author.mention+"  예 형님")
        await message.channel.send(message.author.mention+"```송인아 도움말```으로 송인봇을 이용해봐요!")
        print(t+" ["+message.guild.name+"("+str(+message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] test_str(송인아)")

    # voice channel join
    if message.content == "송인아 드가자" or message.content == "자 드가자" or message.content == "sj" :   
        await message.author.voice.channel.connect()
        await message.channel.send(str(message.author.voice.channel.name) + "으로 드가자~!")
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] entered")

    # voice channel exit
    if message.content == "송인아 나가자" or message.content == "자 나가자" or message.content == "꺼져" or message.content == "sl" or message.content == "송인아 꺼져":
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        await voice.disconnect()
        await message.channel.send("나가자~!")
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] lefted")

    # play 1 of search list
    if message.content == "송인아 틀어 1" or message.content == "송인아 틀어1":
        selected = 1
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        search_list = list()
        with open(str(message.author.id)+".searchlist", "rb") as search_list_file:
            search_list = pickle.load(search_list_file)
        print(t+" [play with search(selected = "+str(selected)+")]")
        url = "http://www.youtube.com/watch?v="+search_list[selected - 1]
        # play by url -----------------------
        option = {'format': 'bestaudio/best', 'postprocessors': [{'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio', 'preferredquality': '320',}], 'outtmpl' : "file/" + url.split('=')[1] + '.mp3'}
        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            title = info["title"]
        voice.play(discord.FFmpegPCMAudio("file/" + url.split("=")[1] + ".mp3"))
        embed = discord.Embed(title=title, herf="http://최송인.kro.kr",description="송인이의 노래실력..! 어때?", color=discord.Color.blue())
        await message.channel.send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] play ("+title+") ("+url+")")
        
    elif message.content == "송인아 틀어 2" or message.content == "송인아 틀어2":
        selected = 2
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        search_list = list()
        with open(str(message.author.id)+".searchlist", "rb") as search_list_file:
            search_list = pickle.load(search_list_file)
        print(t+" [play with search(selected = "+str(selected)+")]")
        url = "http://www.youtube.com/watch?v="+search_list[selected - 1]
        # play by url -----------------------
        option = {'format': 'bestaudio/best', 'postprocessors': [{'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio', 'preferredquality': '320',}], 'outtmpl' : "file/" + url.split('=')[1] + '.mp3'}
        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            title = info["title"]
        voice.play(discord.FFmpegPCMAudio("file/" + url.split("=")[1] + ".mp3"))
        embed = discord.Embed(title=title, description="송인이의 노래실력..! 어때?", color=discord.Color.blue())
        await message.channel.send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] play ("+title+") ("+url+")")
        
    elif message.content == "송인아 틀어 3" or message.content == "송인아 틀어3":
        selected = 3
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        search_list = list()
        with open(str(message.author.id)+".searchlist", "rb") as search_list_file:
            search_list = pickle.load(search_list_file)
        print(t+" [play with search(selected = "+str(selected)+")]")
        url = "http://www.youtube.com/watch?v="+search_list[selected - 1]
        # play by url -----------------------
        option = {'format': 'bestaudio/best', 'postprocessors': [{'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio', 'preferredquality': '320',}], 'outtmpl' : "file/" + url.split('=')[1] + '.mp3'}
        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            title = info["title"]
        voice.play(discord.FFmpegPCMAudio("file/" + url.split("=")[1] + ".mp3"))
        embed = discord.Embed(title=title, description="송인이의 노래실력..! 어때?", color=discord.Color.blue())
        await message.channel.send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] play ("+title+") ("+url+")")
        
    elif message.content == "송인아 틀어 4" or message.content == "송인아 틀어4":
        selected = 4
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        search_list = list()
        with open(str(message.author.id)+".searchlist", "rb") as search_list_file:
            search_list = pickle.load(search_list_file)
        print(t+" [play with search(selected = "+str(selected)+")]")
        url = "http://www.youtube.com/watch?v="+search_list[selected - 1]
        # play by url -----------------------
        option = {'format': 'bestaudio/best', 'postprocessors': [{'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio', 'preferredquality': '320',}], 'outtmpl' : "file/" + url.split('=')[1] + '.mp3'}
        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            title = info["title"]
        voice.play(discord.FFmpegPCMAudio("file/" + url.split("=")[1] + ".mp3"))
        embed = discord.Embed(title=title, description="송인이의 노래실력..! 어때?", color=discord.Color.blue())
        await message.channel.send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] play ("+title+") ("+url+")")
        
    elif message.content == "송인아 틀어 5" or message.content == "송인아 틀어5":
        selected = 5
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        search_list = list()
        with open(str(message.author.id)+".searchlist", "rb") as search_list_file:
            search_list = pickle.load(search_list_file)
        print(t+" [play with search(selected = "+str(selected)+")]")
        url = "http://www.youtube.com/watch?v="+search_list[selected - 1]
        # play by url -----------------------
        option = {'format': 'bestaudio/best', 'postprocessors': [{'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio', 'preferredquality': '320',}], 'outtmpl' : "file/" + url.split('=')[1] + '.mp3'}
        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            title = info["title"]
        voice.play(discord.FFmpegPCMAudio("file/" + url.split("=")[1] + ".mp3"))
        embed = discord.Embed(title=title, description="송인이의 노래실력..! 어때?", color=discord.Color.blue())
        await message.channel.send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] play ("+title+") ("+url+")")
        

    
    # play with search ---------------------------------------------------------------------------------------------------------------------------------------
    elif message.content.startswith("송인아 틀어") or message.content.startswith("틀어 송인아"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        # 검색이면
        if message.content.split(" ")[2].find("www.youtube.com") == -1 or message.content.split(" ")[2].find("watch?v=") == -1:
            keyword = quote(message.content.split(" ")[2])
            search_html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+keyword)
            s = re.findall(r"watch\?v=(\S{11})", str(search_html.read().decode()))
            # 검색 후 링크 리스트 구하기
            search_list = list()
            for i in range(5):
                search_list.append(s[i])
            with open(str(message.author.id)+".searchlist", "wb") as search_list_file:
                pickle.dump(search_list, search_list_file)
            a = str()
            for i in range(5):
                a += "\n"+str(i+1)+". "+getYoutubeTitle(search_list[i])
            embed = discord.Embed(title="뭐로 틀까?", description=a, color=discord.Color.red())
            await message.channel.send(embed=embed)
            print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] "+str(search_list))
        # 링크면
        else: 
            url = message.content.split(" ")[2]
            # play by url -----------------------
            option = {'format': 'bestaudio/best', 'postprocessors': [{'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio', 'preferredquality': '320',}], 'outtmpl' : "file/" + url.split('=')[1] + '.mp3'}
            with youtube_dl.YoutubeDL(option) as ydl:
                ydl.download([url])
                info = ydl.extract_info(url, download=False)
                title = info["title"]
            voice.play(discord.FFmpegPCMAudio("file/" + url.split("=")[1] + ".mp3"))
            embed = discord.Embed(title=title, description="송인이의 노래실력..! 어때?", color=discord.Color.blue())
            await message.channel.send(embed=embed)
            print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] voice_room ["+message.author.voice.channel.name+"("+str(message.author.voice.channel.id)+")] play ("+title+") ("+url+")")
        
    # stop
    if message.content == "송인아 노래꺼" or message.content == "송인아 꺼" or message.content == "송인아 멈춰" or message.content == "ss":
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        voice.stop()
        await message.channel.send("노래 듣는 행위 멈춰!")
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] stoped")

    # test
    if message.content == "김민재":
        await message.channel.send(message.author.mention+" 김민재는 바보지 ㄹㅇㅋㅋ")
        embed = discord.Embed(title=message.author.name+"님을 위한 섹시 남캠 민재의 방송국",url = "http://bj.afreecatv.com/minjae0645", description="↑ 민재의 방송국 링크!", color=discord.Color.red())
        await message.channel.send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] test_str(김민재)")
 
    # test
    if message.content == "한지호":
        embed = discord.Embed(title="우리 지호는요....", description="그만 찡찡대면 좋겠어요....\n지호야 찡찡대지 마\n", color=discord.Color.red())
        await message.channel .send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] test_str(한지호)")
    
    if message.content == "송인아 도움말":
        embed = discord.Embed(title="쉽고 편리한 송인봇의 도움말(명령어)", description="```송인아 드가자```로 음성채널에 입장!\n\n```송인아 나가자```로 음성채널에서 퇴장!\n\n```송인아 틀어 (링크)```를 통해 노래를 재생하거나\n\n```송인아 틀어 (검색할것)```을 통해 검색후 ```송인아 틀어 (숫자)```로 재생하기!\n\n```송인아 서버 등록하기```로 서버를 등록한후\n\n```송인아 등록 (반)반```로 반을 등록한후\n\n```송인아 줌 (과목)```으로 해당 과목의 줌 아이디를 쉽고 편리하게 조회할 수 있습니다", color=discord.Color.red())
        await message.author.send(embed=embed)
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] help_str")

    if message.content == "송인아 서버 등록하기":
        국어 = addZoomIdOnList(["6627759299",5],["3691746842",5])
        사회 = addZoomIdOnList(["2289609281",9],["9793678279",1])
        역사 = addZoomIdOnList(["9732942650",1],["5769687313",9])
        수학 = addZoomIdOnList(["8476477602",4],["3051680982",6])
        과학 = addZoomIdOnList(["5226261708",4],["9387780425",4],["5803453663",2])
        기술 = addZoomIdOnList(["8901737739",3],["2903268171",7])
        가정 = addZoomIdOnList(["7884204198",4],["5896143798",3],["7884204198",3])
        체육 = addZoomIdOnList(["9490648950",5],["5816179131",5])
        음악 = addZoomIdOnList(["4680601371",10])
        미술 = addZoomIdOnList(["4966355051",10])
        영어 = addZoomIdOnList(["3266839688",5],["9898320517",5])
        중국어 = addZoomIdOnList(["2740375494",9],["2738957009",1])
        subject = {"국어":국어,"사회":사회,"역사":역사,"수학":수학,"과학":과학,"기술":기술,"가정":가정,"체육":체육,"음악":음악,"미술":미술,"영어":영어,"중국어":중국어}
        await message.channel.send("checked!")
        with open(str(message.guild.id)+".zoomid", "wb") as zoomid_file:
            pickle.dump(subject, zoomid_file) 
        print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] set_server")

    # save sys.
    if message.content.startswith("송인아 등록 "):
        if message.content.split("송인아 등록 ")[1].find("반") != -1:
            await message.channel.send(message.author.mention+"은(는) "+str(message.content.split("송인아 등록 ")[1].split("반")[0])+"반 입니다")
            with open(str(message.author.id)+".zoomclass","wb") as class_file:
                pickle.dump(int(message.content.split("송인아 등록")[1].split("반")[0]),class_file)
                print(t+" ["+message.guild.name+"("+str(+message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] set_class (class :"+message.content.split("송인아 등록")[1].split("반")[0]+")")
    
    # find data sys.
    if message.content == "송인아 반":
        with open(str(message.author.id)+".zoomclass","rb") as class_file:
            _class = pickle.load(class_file)
            await message.channel.send(message.author.mention+"은(는) "+str(_class)+"반 입니다")
            print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] check_class (class : "+str(_class)+")")

    if message.content.startswith("송인아 줌 "):
        try:
            input_subject = message.content.split("송인아 줌 ")[1]
            with open(str(message.guild.id)+".zoomid", "rb") as zoomid_file:
                with open(str(message.author.id)+".zoomclass","rb") as class_file:
                    _class = pickle.load(class_file)
                    _zoom_id = pickle.load(zoomid_file)[input_subject][_class-1]
                # await message.channel.send(message.author.mention+"의 "+input_subject+"```"+pickle.load(zoomid_file)[input_subject][_class-1]+"```")
                    embed = discord.Embed(title=message.author.name+"님의 "+input_subject+" 줌 아이디", description="```"+_zoom_id+"```\n제목 클릭시 복사할수있는 사이트로 이동후, 좌클릭시 자동 복사됨", color=discord.Color.blue(), url="http://zoom.songinbot.kro.kr/="+str(_zoom_id))
                    await message.channel.send(embed=embed)
                    print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] check_zoom_id (class : "+str(_class)+")(subject : "+str(input_subject)+")(zoom_id : "+str(_zoom_id)+")")
        except Exception as err:
            await message.channel.send("아마.... 에러가 발생한 것 같네요..")
            await message.channel.send("```송인아 도움말```을 사용해보는건 어떨까요?")
            await message.channel.send("err :"+err)
            print(t+" ["+message.guild.name+"("+str(message.guild.id)+")] ["+message.author.name+"("+str(message.author.id)+")] error exist at 267(zoom id check)")

def getYoutubeTitle(VideoID):
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string
    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        return str(data['title'])

def addZoomIdOnList(*arg):
    value = list()
    for i in arg:
        for j in range(i[1]):
            value.append(i[0])
    return value

client.run(token)