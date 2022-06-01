from email import message
import discord 
import requests
import asyncio
from json import loads
#import time


# 트위치에서 가져와야하는 값들
twitch_Application_ID = '!랜도프 트위치 클라이언트 ID를 입력해 주세요!!' 
twitch_Application_secret = '!랜도프 트위치 클라이언트 시크릿을 입력해 주세요 !!!'

# 디스코드에서 가져와야 하는 값들
discord_TEXTChannels_channelID = !랜도프 디스코드 채팅방 ID를 입력해 주세요!!!
discord_BOT_Token = '!랜도프 디스코드 봇 토큰을 입력해 주세요'

#디스코드 출력할 문장
discord_bot_state = '디스코드 봇의 상태를 알려줍니다 (ex 라디유 방송 기다리는중)'

#검색할 스트리머님의 ID
twitchID = 'radiyu' # !랜도프 해당 부분 값을 변경하면 원하는 스트리머분의 방송 알림을 받을수 있습니다.
ment = '!랜도프 방송이 시작하면 출력될 문자 입니다! (ex 머찐 라디유 두두두두둥장!'
Service_bot = discord.Client()

@Service_bot.event
async def on_ready():
    print(Service_bot.user.id)
    print("준비 완료")

    # 디스코드 봇 상태 설정
    game = discord.Game(discord_bot_state)
    await Service_bot.change_presence(status=discord.Status.online, activity=game)

    # 채팅 채널 설정
    TEXT_channel = Service_bot.get_channel(discord_TEXTChannels_channelID)
    
    # 트위치 api 2차인증
    # 
    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + twitch_Application_ID + "&client_secret=" + twitch_Application_secret + "&grant_type=client_credentials")
    access_token = loads(oauth_key.text)["access_token"]
    token_type = 'Bearer '
    Managerauthorization = token_type + access_token
    print(Managerauthorization)
    a = 0   

    while True:
        print("봇이 방송을 기다리고 있습니다... 아 봇도 디유타임은 킹정이라 합니다.")

        Information = {'client-id': twitch_Application_ID, 'Authorization': Managerauthorization}
        api_response = requests.get('https://api.twitch.tv/helix/streams?user_login=' + twitchID, headers=Information)
        print(api_response.text)

        try:            
            if loads(api_response.text)['data'][0]['type'] == 'live' and a == 0:
                await TEXT_channel.send(ment +'\n https://www.twitch.tv/' + twitchID)
                print("뱅송 ON!!!")
                a = 1
        except:
            print("뱅송 없어...?")
            a = 0
        await asyncio.sleep(15) #time.sleep(15) # !랜도프 해당 부분 값을 변경하면 분당 감시 빈도를 늘릴수는 있다만 너무 짧게주지는 마세요, 우리 컴퓨터 힘들어 합니다.. 

Service_bot.run(discord_BOT_Token)