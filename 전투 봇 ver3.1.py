import discord
import random
import asyncio
import sqlite3

'''app = __import__("flask").Flask(__name__)

def 호스트실행():
    app.run()       

@app.route("/")
def main():
    return "봇 가동중"

__import__("threading").Thread(target=호스트실행).start()'''

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    bar = discord.Game("전투 봇 부활 중...")
    await client.change_presence(status=discord.Status.offline, activity=bar)
    conn = sqlite3.connect("PlayerData.db")
    cur = conn.cursor()
    cur.execute('''create table PlayerData(id text,name text, server text)''')
    conn.commit()
    conn.close()


def Insert(Data):
    conn = sqlite3.connect("PlayerData.db")
    cur = conn.cursor()
    ins_sql = 'insert into PlayerData values(?,?,?)'
    cur.execute(ins_sql, Data)
    conn.commit()
    conn.close()


def CheckData():
    conn = sqlite3.connect("PlayerData.db")
    cur = conn.cursor()
    cur.execute('select * from PlayerData')
    Ids = cur.fetchall()
    conn.close()
    print(Ids)
    return Ids


def Update(name, Cname, S):
    id = int(name)
    conn = sqlite3.connect("PlayerData.db")
    cur = conn.cursor()
    cur.execute('SELECT server FROM PlayerData WHERE id= %d' % id)
    result = cur.fetchall()
    S = int(S)
    for i in range(len(result)):
        if int(result[i][0]) == int(S):
            cur.execute(
                'UPDATE PlayerData SET name = "%s" WHERE id = %d and server=%d' % (Cname, id, S))
    conn.commit()
    conn.close()


PlayerId = [[527500397645004800, "브루니"], [558169794646507541, "빼미요"], [
    404936174902444033, "붸"], [665823140915445760, "브루시우"], [503194657673707552, "포션"]]
NumberList = [1, 2, 3]
Delete = []
PlayerList = []
PlayerName = []
ChoiceSkill = []
User1Dot = []
User1Turn = []
User2Dot = []
User2Turn = []
CommonSkill = [["스킬명 : 강타 / 스킬등급 : 커먼 / 스킬타입 : 공격 / 스킬데미지 : 10 / 스킬설명 : 완전쎔", 10, " 는(은) 10데미지를 입었다!", "Attack"], [
    "스킬명 : 유혹 / 스킬등급 : 커먼 / 스킬타입 : 무 / 스킬데미지 : 0 / 스킬설명 : 상대를 유혹시켜 혼란에 빠지게 한다 근데 우린 다 남잔걸?", 0, " : ...?", "Attack"], ["스킬명 : 습격 / 스킬등급 : 커먼 / 스킬타입 : 공격 / 스킬데미지 : 20 / 스킬설명 : 상대를 습격한다", 20, " 는(은) 습격을 당했다!", "Attack"], ["스킬명 : 침뱉기 / 스킬등급 : 커먼 / 스킬타입 : 무 / 스킬데미지 : 0 / 스킬설명 : 상대에게 침을뱉는다", 0, " 는(은) 노란 침전물을 눈에 맞았다!", "Attack"], ["스킬명 : 치킨 / 스킬등급 : 커먼 / 스킬타입 : 회복 / 스킬데미지 : 40 / 스킬설명 : 치.느.님", 40, " 는(은) 치킨을 먹고 기운을 차렸다!", "selfHeal"],
    ["스킬명 : 뱀의 독/ 스킬등급 : 커먼 / 스킬타입 : 도트뎀 / 스킬데미지 : 3(3턴) / 스킬설명 : 독에 중독된거 같은 느낌이 든다", 3, 3, " 는(은) 손에 독이 퍼지는것을 느꼈다...", " 는(은) 뱀의 독 때문에 몸에 힘이 빠졌다.(-3HP)", "Dotdem"], ["스킬명 : 코딱지 튕기기 / 스킬등급 : 일반 / 스킬타입 : 공격 / 스킬데미지 : 1 / 스킬설명 : 전혀 아프지 않지만 기분은 세상에서 제일 더럽다", 1, " 는(은) 초록색의 무언가가 볼에 붙었다.", "Attack"], ["스킬명 : 딱밤 / 스킬등급 : 일반 / 스킬타입 : 공격 / 스킬데미지 : 5 / 스킬설명 : 이마가 빨개질수도 있다", 5, " 는(은) 딱밤을 맞았다.", "Attack"], ["스킬명 : 선빵필승 / 스킬등급 : 커먼 / 스킬타입 : 공격 / 스킬데미지 : 1 / 스킬설명 : 게임이 시작하고 첫 턴에 이 스킬을 쓸 경우 이 스킬의 데미지가 두배가 된다.", 1, " 는(은) 선빵을 맞아 패기를 잃었다.", "Special2"]]
RareSkill = [["스킬명 : 자애로운 손길 / 스킬등급 : 레어 / 스킬타입 : 회복 / 스킬데미지 : 50 / 스킬설명 : 상대의 HP를 일정량 회복시킨다", -
              50, " 는(은) 자애롭게 보다듭어졌다.(HP + 50)", "Heal"], ["스킬명 : 썬더태클 / 스킬등급 : 레어 / 스킬타입 : 공격 / 스킬데미지 : 200 / 스킬설명 : 상대에게 빛의속도로 돌진하여 데미지를 준다", 200, " 는(은) 빛의 속도의 공격력을 느꼈다.", "Attack"], ["스킬명 : [새]총 / 스킬등급 : 레어 / 스킬타입 : 공격 / 스킬데미지 : 100 / 스킬설명 : 총처럼 생긴 새로 때린다", 100, " 는(은) 총처럼 생긴 새에게 맞았다.", "Attack"], ["스킬명 : 러시안마피아 / 스킬등급 : 레어 / 스킬타입 : 공격 / 스킬데미지 : 150 / 스킬설명 : 공중에서 점프 후 앞으로 대쉬해서 상대에게 큰 데미지를 준다", 150, " 는(은) 러시안마피아 스킬에 정통으로 맞았다.", "Attack"], ["스킬명 : 단련된 강타 / 스킬등급 : 레어 / 스킬타입 : 공격 / 스킬데미지 : 100 / 스킬설명 : 단련된 강타를 날림", 100, " 는(은) 단련된 강타를 맞았다!", "Attack"], ["스킬명 : 방울뱀 / 스킬등급 : 레어 / 스킬타입 : 도트뎀 / 스킬데미지 : 30(3턴) / 스킬설명 : 꼬리에 방울이 달려있는 뱀이다 소리는 아름답지만 한번 물리면 더이상 아름답지 않다", 30, 3, " : 이 방울 소리는 뭐지..? ", " 는(은) 방울소리가 들려오는것만 같았다(-30HP)", "Dotdem"], ["스킬명 : 헥토파스칼 킥 / 스킬등급 : 레어 / 스킬타입 : 공격 / 스킬데미지 : 150 / 스킬설명 : 풍속 23m의 속도로 날아서 명치에 꽃는다", 150, " 는(은) 명치에 치명타를 맞았다.", "Attack"], ["스킬명 : 보건실 침대 / 스킬등급 : 레어 / 스킬타입 : 회복 / 스킬데미지 : 150 / 스킬설명 : 누워만 있어도 치유되는 마법의 침대", 150, " 는(은) 보건실 침대에 누웠다.(+150HP)", "selfHeal"]]
EpicSkill = [["스킬명 : 벽력일섬 / 스킬등급 : 에픽 / 스킬타입 : 공격 / 스킬데미지 : 300 / 스킬설명 : 카미나리노코큐-이치노카타...헤키레키잇셈",
              300, " 는(은) 반으로 갈라졌다.", "Attack"], ["스킬명 : 아마겟돈 / 스킬등급 : 에픽 / 스킬타입 : 공격 / 스킬데미지 : 300 / 스킬설명 : 매우 크고 강력한 폭탄. 폭발하면 주변 모든 생명체를 소멸시킨다", 300, " 는(은) 폭탄덕분에 몸이 터졌다.", "Attack"], ["스킬명 : 대지의기운 / 스킬등급 : 에픽 / 스킬타입 : 회복 / 스킬데미지 : 350 / 스킬설명 : 대지의 기운을 끌어모아서 몸을 재생시킨다", 350, " 가 대지의 기운으로 체력을 회복했다.", "selfHeal"], ["스킬명 : 카케구루이 / 스킬등급 : 에픽 / 스킬타입 : 공격 / 스킬데미지 : -500~500 / 스킬설명 : 모 아니면 빽도!", 0, "", "Special1"], ["스킬명 : 비현실적인 강타 / 스킬등급 : 에픽 / 스킬타입 : 공격 / 스킬데미지 : 350 / 스킬설명 : 비현실적으로 쌘 강타를 날림", 350, " 는(은) 비현실적인 강타를 맞았다!", "Attack"], ["스킬명 : 아나콘다 / 스킬등급 : 에픽 / 스킬타입 : 도트뎀 / 스킬데미지 : 100(3턴) / 스킬설명 : 깊은 산 속 어딘가에 존재하는 뱀. 호랑이를 먹었다고 전해진다 호랑이도 먹었는데 사람을 못먹을까?", 100, 3, " 는(은) 아나콘다가 조이는것을 느꼈다...", " 는(은) 아나콘다에 의해 점점 몸이 옥죄어졌다(-100HP)", "Dotdem"]]
LegendarySkill = [["스킬명 : 시작의 호흡 / 스킬등급 : 레전더리 / 스킬타입 : 공격 / 스킬데미지 : 900 / 스킬설명 : 히노코큐...엔부",
                   900, " 는(은):fire: !시작의 호흡! :fire:을 정통으로 맞았다.", "Attack"], ["스킬명 : 엑시드하이퍼 파워플리 엔플로션 펜타이즈세크리전스 오버시드 네온 퓨어플레이트 노바 / 스킬등급 : 레전더리 / 스킬타입 : 공격 / 스킬데미지 : 1333 / 스킬설명 : 태초의우주에 떠돌던 태고의 에너지를 끌어모아 만들어낸 아주 강력한 에너지결정을 307억년에 거쳐서 제련해 만들어진 전설의 무기", 1333, " 는(은) 몸에 구멍이 났다.", "Attack"], ["스킬명 : 한 대 / 스킬등급 : 레전더리 / 스킬타입 : 공격 / 스킬데미지 : 999 / 스킬설명 : 짱 센 대머리가 떠오르는 장갑이다", 999, " 는(은) 한대에 의해 머리가 날아갔다.", "Attack"], ["스킬명 : 전설적인 강타 / 스킬등급 : 레전더리 / 스킬타입 : 공격 / 스킬데미지 : 1500 / 스킬설명 : 전설적인 강타를 날림", 1200, " 는(은) 전설적인 강타를 맞았다!", "Attack"], ["스킬명 : 코브라 / 스킬등급 : 레전더리 / 스킬타입 : 도트뎀 / 스킬데미지 : 400(3턴) / 스킬설명 : 코끼리를 잡아먹는 뱀이다. 생존할 가능성은 없다", 400, 3, " 는(은) 코브라의 먹잇감으로 인식되었다.", "의 심장이 코브라의 독에 의해 짓눌린다..(-400HP)", "Dotdem"], ["스킬명 : 플래그 / 스킬등급 : 레전더리 / 스킬타입 : 회복 / 스킬데미지 : 1000 / 스킬설명 : 해치웠나....?", 1000, " 는(은) 플래그를 밟아 피를 회복했다.", "selfHeal"]]

Count2 = 0
Once = False
Count = 0
User1_HP = 3000
User2_HP = 3000
Start = False
Receive = False
GameStart = False
User1 = False
User2 = False
notAgain = False
SkilNumber = False
Cnt = 0
Check = False
Check2 = False


@ client.event
async def on_message(message):
    global Start, Receive, Count, GameStart, User1, User2, notAgain, SkilNumber, User1_HP, User2_HP, Cnt, Once, Count2, Check, Check2
    global PlayerList, PlayerId, PlayerName, ChoiceSkill, NumberList, RareSkill, EpicSkill, LegendarySkill, User1Dot, User2Dot, Delete, User1Turn, User2Turn
    if message.content.startswith("!가입"):
        Count3 = 0
        id = str(message.author.id)
        name = message.content[4:]
        Ser = str(message.guild.id)
        DataList = CheckData()
        if len(DataList) == 0:
            AddData = (id, name, Ser)
            Insert(AddData)
            await message.channel.send("```" + name + " 님 가입되었습니다!```")
            await message.channel.send("```혹시나 닉넴을 바꾸고싶거나 오류가 나서 게임이 진행되지 않을경우 다시 한번 !가입을 해주세요.```")
            return
        for x in range(len(DataList)):
            if DataList[x][1] == name and DataList[x][2] == Ser:
                await message.channel.send("```" + name + " 닉네임은 이미 사용중입니다.```")
                return
        for x in range(len(DataList)):
            Count3 += 1
            if DataList[x][1] != name:
                if DataList[x][0] == id and DataList[x][2] == Ser:
                    Update(DataList[x][0], name, Ser)
                    await message.channel.send("```" + name + " 으로 닉네임이 변경 되었습니다.```")
                    return
                elif DataList[x][0] == id and DataList[x][2] != Ser and Count3 == len(DataList):
                    AddData = (id, name, Ser)
                    Insert(AddData)
                    await message.channel.send("```" + name + " 님 가입되었습니다!```")
                    await message.channel.send("```혹시나 닉넴을 바꾸고싶거나 오류가 나서 게임이 진행되지 않을경우 다시 한번 !가입을 해주세요.```")
                    return
        AddData = (id, name, Ser)
        Insert(AddData)
        await message.channel.send("```" + name + " 님 가입되었습니다!```")

    if message.content.startswith("!봇정보") or message.content.startswith("!봇 정보"):
        DataList2 = CheckData()
        ServerList = []
        for guild in client.guilds:
            ServerList.append(guild.name)
        length = len(ServerList)
        embed1 = discord.Embed(color=0x00ff00)
        embed1.add_field(name="서버 수 : ", value=length, inline=False)
        embed1.add_field(name="인원 수 : ", value=len(DataList2), inline=True)
        await message.channel.send(embed=embed1)

    if message.content.startswith("!전투신청"):
        if Start == False:
            Count3 = 0
            twoP = message.content[6:]
            Pid = str(message.author.id)
            Ser2 = str(message.guild.id)
            DataList2 = CheckData()
            for x in range(len(DataList2)):
                Count3 += 1
                if DataList2[x][0] == Pid and DataList2[x][2] == Ser2:
                    PlayerList.append(int(DataList2[x][0]))
                    PlayerName.append(DataList2[x][1])
                    Count3 = 0
                    Check = True
                    break
                elif DataList2[x][0] != Pid and Count3 == len(DataList2):
                    PlayerList = []
                    PlayerName = []
                    Start = False
                    Receive = False
                    Check = False
                    Check2 = False
                    await message.channel.send("```!가입 (닉넴) 을 먼저하셔야합니다.```")
                    return
            for x in range(len(DataList2)):
                Count3 += 1
                if DataList2[x][1] == twoP and DataList2[x][2] == Ser2:
                    PlayerList.append(int(DataList2[x][0]))
                    PlayerName.append(DataList2[x][1])
                    Count3 = 0
                    Check2 = True
                    break
                elif DataList2[x][1] != twoP and Count3 == len(DataList2):
                    PlayerList = []
                    PlayerName = []
                    Start = False
                    Receive = False
                    Check = False
                    Check2 = False
                    await message.channel.send("```전투를 받은 사람이 가입되어 있지 않습니다.```")
                    return

            if Check == True and Check2 == True:
                Start = True
                Receive = True
                await message.channel.send("```" + PlayerName[0] + " 님이 " + PlayerName[1] + " 님에게 전투를 신청했습니다.```")
                await message.channel.send("```전투(수락/거절) 로 전투 여부를 결정해주세요.```")

    if message.content.startswith("!전투수락"):
        author3 = message.author.id
        if PlayerList[1] == author3 and Receive == True:  # 신청을 받은 사람과 수락한 사람이 같은지 확인
            await message.channel.send("```" + PlayerName[1] + " 님이 전투를 수락했습니다!" + "```")
            GameStart = True  # 게임을 시작하기 위한 변수
            Receive = False  # 다시 전투수락을 못하도록 막는 변수
            await message.channel.send("```" + "룰 : 공격차례가 오면 (!공격)은 한번만 쳐주세요!\n명령어는 딱한번만 쳐주세요!" + "```")
            await message.channel.send("```" + "준비가 끝났다면, (!전투시작)을 쳐주세요!" + "```")
        elif PlayerList[1] != author3 and Receive == True:
            await message.channel.send("```" + "다른사람의 전투를 자신이 수락 할 수 없습니다" + "```")
        elif PlayerList[1] == author3 and Receive == False:
            await message.channel.send("```전투수락을 두번 할 수 없습니다.```")

    if message.content.startswith("!전투거절"):
        author3 = message.author.id
        if PlayerList[1] == author3 and Receive == True:  # 신청을 받은 사람과 수락한 사람이 같은지 확인
            await message.channel.send("```" + PlayerName[1] + "님이 전투를 거절했습니다!" + "```")
            Start = False  # 전투를 거절했기 때문에 모든 변수와 리스트 초기화
            Receive = False
            PlayerList = []
            PlayerName = []
            Count = 0
        elif PlayerList[1] != author3 and Receive == True:
            await message.channel.send("```" + "다른사람의 전투를 자신이 거절 할 수 없습니다" + "```")

    if message.content.startswith("!전투시작") or message.content.startswith("!전투 시작"):
        author4 = message.author.id
        if PlayerList[0] == author4 or PlayerList[1] == author4:  # 지금 전투 중인 사람만 시작 가능
            FirstAttack = random.randint(0, 1)  # 먼저 시작할 사람을 랜덤으로 정하는 변수
            if GameStart == True:
                await message.channel.send("```" + "먼저 시작할 사람을 랜덤으로 정하겠습니다." + "```")
                if FirstAttack == 0:
                    await message.channel.send("```" + PlayerName[FirstAttack] + "님이 선공입니다! 공격할려면 (!공격)을 치세요!" + "```")
                    GameStart = False  # 다시 전투시작을 막기 위한 변수
                    User1 = True  # 플레이어1이 공격이 가능하게 만들어주는 변수
                    User2 = False  # 플레이어2는 공격을 못하게 만들어주는 변수
                elif FirstAttack == 1:
                    await message.channel.send("```" + PlayerName[FirstAttack] + "님이 선공입니다! 공격할려면 (!공격)을 치세요!" + "```")
                    GameStart = False
                    User1 = False
                    User2 = True

    if message.content.startswith("!공격"):
        author5 = message.author.id
        if len(PlayerList) == 0:
            return
        if PlayerList[0] == author5 and User1 == True and notAgain == False:
            notAgain = True  # 다시 공격을 못 하도록 막는 변수
            for i in range(3):
                RandomSkill = random.randint(1, 100)  # 랜덤으로 스킬 뽑는 코드
                await message.channel.send(RandomSkill)
                if RandomSkill >= 1 and RandomSkill <= 50:  # 일반 스킬
                    Skill = random.choice(CommonSkill)
                    ChoiceSkill.append(Skill)  # 뽑은 스킬을 ChoiceSkill에 넣어줌
                if RandomSkill >= 51 and RandomSkill <= 85:  # 레어 스킬
                    Skill = random.choice(RareSkill)
                    ChoiceSkill.append(Skill)
                if RandomSkill >= 86 and RandomSkill <= 99:
                    Skill = random.choice(EpicSkill)
                    ChoiceSkill.append(Skill)
                if RandomSkill == 100:
                    Skill = random.choice(LegendarySkill)
                    ChoiceSkill.append(Skill)
            await message.channel.send("```" + "스킬을 선택하셨다면 !(스킬번호)를 입력해주세요!" + "```")
            await message.channel.send("```" + "1." + ChoiceSkill[0][0] + "```\n```" + "2." + ChoiceSkill[1][0] + "```\n```" + "3." + ChoiceSkill[2][0] + "```")
            SkilNumber = True  # 스킬을 고를 수 있게 해주는 변수

        elif PlayerList[1] == author5 and User2 == True and notAgain == False:
            notAgain = True
            for i in range(3):
                RandomSkill = random.randint(1, 100)
                await message.channel.send(RandomSkill)
                if RandomSkill >= 1 and RandomSkill <= 50:
                    Skill = random.choice(CommonSkill)
                    ChoiceSkill.append(Skill)
                if RandomSkill >= 51 and RandomSkill <= 85:
                    Skill = random.choice(RareSkill)
                    ChoiceSkill.append(Skill)
                if RandomSkill >= 86 and RandomSkill <= 99:
                    Skill = random.choice(EpicSkill)
                    ChoiceSkill.append(Skill)
                if RandomSkill == 100:
                    Skill = random.choice(LegendarySkill)
                    ChoiceSkill.append(Skill)
            await message.channel.send("```" + "스킬을 선택하셨다면 !(스킬번호)를 입력해주세요!" + "```")
            await message.channel.send("```" + "1." + ChoiceSkill[0][0] + "```\n```" + "2." + ChoiceSkill[1][0] + "```\n```" + "3." + ChoiceSkill[2][0] + "```")
            SkilNumber = True

    if message.content.startswith("!"):
        author6 = message.author.id
        if len(PlayerList) == 0:
            return
        if PlayerList[0] == author6 and User1 == True and SkilNumber == True:  # 전투 중인 사람인지 확인하는 조건문
            Num = message.content[1:2]  # 무슨 스킬을 골랐는지 뽑는 변수
            if Num == "공":  # !공격을 방지
                return
            if Num == "전":
                return
            Num = int(Num)  # 변수 int
            if Num in NumberList:
                if len(User1Dot) >= 1:
                    for i in range(len(User1Dot)):
                        User1_HP -= User1Dot[i][1]
                        User1Turn[i] -= 1
                        await message.channel.send("```" + PlayerName[0] + User1Dot[i][4] + "```")
                    for i in range(len(User1Dot)):
                        if User1Turn[i] <= 0:
                            Delete.append(i)
                            Cnt += 1
                    for i in range(Cnt):
                        del User1Dot[Delete[0]]
                        del User1Turn[Delete[0]]
                        del Delete[0]
                        for x in range(len(Delete)):
                            Delete[x] -= 1
                    Cnt = 0
                    Delete = []
                if len(User2Dot) >= 1:
                    for i in range(len(User2Dot)):
                        User2_HP -= User2Dot[i][1]
                        User2Turn[i] -= 1
                        await message.channel.send("```" + PlayerName[1] + User2Dot[i][4] + "```")
                    for i in range(len(User2Dot)):
                        if User2Turn[i] <= 0:
                            Delete.append(i)
                            Cnt += 1
                    for i in range(Cnt):
                        del User2Dot[Delete[0]]
                        del User2Turn[Delete[0]]
                        del Delete[0]
                        for x in range(len(Delete)):
                            Delete[x] -= 1
                    Cnt = 0
                    Delete = []
                if User1_HP <= 0 and User2_HP <= 0:
                    await message.channel.send("```!!무승부!!```")
                    Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                    User1_HP = 3000
                    User2_HP = 3000
                    Start = False
                    Receive = False
                    GameStart = False
                    User1 = False
                    User2 = False
                    notAgain = False
                    SkilNumber = False
                    PlayerList = []
                    PlayerName = []
                    ChoiceSkill = []
                    User1Dot = []
                    User2Dot = []
                    User1Turn = []
                    User2Turn = []
                    Once = False
                    Check = False
                    Check2 = False
                elif User2_HP <= 0:  # 상대방 피가 0보다 작거나 같다면 게임 끝
                    await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[0])
                    await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[1])
                    Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                    User1_HP = 3000
                    User2_HP = 3000
                    Start = False
                    Receive = False
                    GameStart = False
                    User1 = False
                    User2 = False
                    notAgain = False
                    SkilNumber = False
                    PlayerList = []
                    PlayerName = []
                    ChoiceSkill = []
                    User1Dot = []
                    User2Dot = []
                    User1Turn = []
                    User2Turn = []
                    Once = False
                    Check = False
                    Check2 = False
                elif User1_HP <= 0:
                    await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[1])
                    await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[0])
                    Count = 0
                    User1_HP = 3000
                    User2_HP = 3000
                    Start = False
                    Receive = False
                    GameStart = False
                    User1 = False
                    User2 = False
                    notAgain = False
                    SkilNumber = False
                    PlayerList = []
                    PlayerName = []
                    ChoiceSkill = []
                    User1Dot = []
                    User2Dot = []
                    User1Turn = []
                    User2Turn = []
                    Once = False
                    Check = False
                    Check2 = False
                # 공격이거나 힐이라면
                if ChoiceSkill[Num - 1][3] == "Attack" or ChoiceSkill[Num - 1][3] == "Heal":
                    Once = True
                    User2_HP -= ChoiceSkill[Num - 1][1]  # 상대방 데미지 주는 코드
                    await message.channel.send("```" + PlayerName[1] + ChoiceSkill[Num - 1][2] + "```")
                    if User2_HP <= 0:  # 상대방 피가 0보다 작거나 같다면 게임 끝
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[0])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[1])
                        Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User1_HP > 0 and User2_HP > 0:  # 아직 피가 남아있다면 게임 계속 진행
                        if User1_HP > 3000:
                            User1_HP = 3000
                        if User2_HP > 3000:
                            User2_HP = 3000
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[1] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = False  # 플레이어 변환
                        User2 = True
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][3] == "selfHeal":  # 자힐이라면 아래 코드 실행
                    Once = True
                    User1_HP += ChoiceSkill[Num - 1][1]
                    await message.channel.send("```" + PlayerName[0] + ChoiceSkill[Num - 1][2] + "```")
                    if User1_HP > 0 and User2_HP > 0:  # 아직 피가 남아있다면 게임 계속 진행
                        if User1_HP > 3000:
                            User1_HP = 3000
                        if User2_HP > 3000:
                            User2_HP = 3000
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[1] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = False  # 플레이어 변환
                        User2 = True
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][3] == "Special1":
                    Once = True
                    Damage = random.randint(-500, 500)
                    if Damage > 0:
                        User2_HP -= Damage
                        await message.channel.send("```모!! " + PlayerName[1] + " 는(은) " + str(Damage) + "데미지를 입었다.```")
                    elif Damage < 0:
                        User1_HP += Damage
                        await message.channel.send("```빽도!! " + PlayerName[0] + " 는(은) " + str(Damage) + "데미지를 입었다.```")
                    elif Damage == 0:
                        await message.channel.send("```" + "아무일도 일어나지 않았다..." + "```")
                    if User2_HP <= 0:  # 상대방 피가 0보다 작거나 같다면 게임 끝
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[0])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[1])
                        Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User1_HP <= 0:
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[1])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[0])
                        Count = 0
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User1_HP > 0 and User2_HP > 0:  # 아직 피가 남아있다면 게임 계속 진행
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[1] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = False  # 플레이어 변환
                        User2 = True
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][3] == "Special2":
                    if Once == False:
                        await message.channel.send("```" + PlayerName[1] + " 는(은) 선빵을 맞아 패기를 잃었다." + "```")
                        User2_HP -= (ChoiceSkill[Num - 1][1]) * 2
                    elif Once == True:
                        await message.channel.send("```" + PlayerName[1] + " 는(은) 전혀 아프지 않은 공격을 맞았다." + "```")
                        User2_HP -= ChoiceSkill[Num - 1][1]
                    Once = True
                    if User2_HP <= 0:  # 상대방 피가 0보다 작거나 같다면 게임 끝
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[0])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[1])
                        Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User1_HP > 0 and User2_HP > 0:  # 아직 피가 남아있다면 게임 계속 진행
                        if User1_HP > 3000:
                            User1_HP = 3000
                        if User2_HP > 3000:
                            User2_HP = 3000
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[1] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = False  # 플레이어 변환
                        User2 = True
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][5] == "Dotdem":
                    Once = True
                    DotSkill = ChoiceSkill[Num - 1]
                    User2Turn.append(ChoiceSkill[Num - 1][2])
                    User2Dot.append(DotSkill)
                    await message.channel.send("```" + PlayerName[1] + ChoiceSkill[Num - 1][3] + "```")
                    await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                    await message.channel.send("```" + PlayerName[1] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                    User1 = False  # 플레이어 변환
                    User2 = True
                    SkilNumber = False
                    notAgain = False
                    ChoiceSkill = []

        # User2 버젼 코드 위에 코드랑 똑같다, 단 User2 기준
        if PlayerList[1] == author6 and User2 == True and SkilNumber == True:
            Num = message.content[1:2]
            if Num == "공":
                return
            Num = int(Num)
            if Num in NumberList:
                if len(User1Dot) >= 1:
                    for i in range(len(User1Dot)):
                        User1_HP -= User1Dot[i][1]
                        User1Turn[i] -= 1
                        await message.channel.send("```" + PlayerName[0] + User1Dot[i][4] + "```")
                    for i in range(len(User1Dot)):
                        if User1Turn[i] <= 0:
                            Delete.append(i)
                            Cnt += 1
                    for i in range(Cnt):
                        del User1Dot[Delete[0]]
                        del User1Turn[Delete[0]]
                        del Delete[0]
                        for x in range(len(Delete)):
                            Delete[x] -= 1
                    Cnt = 0
                    Delete = []
                if len(User2Dot) >= 1:
                    for i in range(len(User2Dot)):
                        User2_HP -= User2Dot[i][1]
                        User2Turn[i] -= 1
                        await message.channel.send("```" + PlayerName[1] + User2Dot[i][4] + "```")
                    for i in range(len(User2Dot)):
                        if User2Turn[i] <= 0:
                            Delete.append(i)
                            Cnt += 1
                    for i in range(Cnt):
                        del User2Dot[Delete[0]]
                        del User2Turn[Delete[0]]
                        del Delete[0]
                        for x in range(len(Delete)):
                            Delete[x] -= 1
                    Cnt = 0
                    Delete = []
                if User1_HP <= 0 and User2_HP <= 0:
                    await message.channel.send("```!!무승부!!```")
                    Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                    User1_HP = 3000
                    User2_HP = 3000
                    Start = False
                    Receive = False
                    GameStart = False
                    User1 = False
                    User2 = False
                    notAgain = False
                    SkilNumber = False
                    PlayerList = []
                    PlayerName = []
                    ChoiceSkill = []
                    User1Dot = []
                    User2Dot = []
                    User1Turn = []
                    User2Turn = []
                    Once = False
                    Check = False
                    Check2 = False
                elif User2_HP <= 0:  # 상대방 피가 0보다 작거나 같다면 게임 끝
                    await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[0])
                    await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[1])
                    Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                    User1_HP = 3000
                    User2_HP = 3000
                    Start = False
                    Receive = False
                    GameStart = False
                    User1 = False
                    User2 = False
                    notAgain = False
                    SkilNumber = False
                    PlayerList = []
                    PlayerName = []
                    ChoiceSkill = []
                    User1Dot = []
                    User2Dot = []
                    User1Turn = []
                    User2Turn = []
                    Once = False
                    Check = False
                    Check2 = False
                elif User1_HP <= 0:
                    await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[1])
                    await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[0])
                    Count = 0
                    User1_HP = 3000
                    User2_HP = 3000
                    Start = False
                    Receive = False
                    GameStart = False
                    User1 = False
                    User2 = False
                    notAgain = False
                    SkilNumber = False
                    PlayerList = []
                    PlayerName = []
                    ChoiceSkill = []
                    User1Dot = []
                    User2Dot = []
                    User1Turn = []
                    User2Turn = []
                    Once = False
                    Check = False
                    Check2 = False
                if ChoiceSkill[Num - 1][3] == "Attack" or ChoiceSkill[Num - 1][3] == "Heal":
                    Once = True
                    User1_HP -= ChoiceSkill[Num - 1][1]
                    await message.channel.send("```" + PlayerName[0] + ChoiceSkill[Num - 1][2] + "```")
                    if User1_HP <= 0:
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[1])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[0])
                        Count = 0
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User1_HP > 0 and User2_HP > 0:
                        if User1_HP > 3000:
                            User1_HP = 3000
                        if User2_HP > 3000:
                            User2_HP = 3000
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[0] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = True
                        User2 = False
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][3] == "selfHeal":  # 자힐이라면 아래 코드 실행
                    Once = True
                    User2_HP += ChoiceSkill[Num - 1][1]
                    await message.channel.send("```" + PlayerName[1] + ChoiceSkill[Num - 1][2] + "```")
                    if User1_HP > 0 and User2_HP > 0:  # 아직 피가 남아있다면 게임 계속 진행
                        if User1_HP > 3000:
                            User1_HP = 3000
                        if User2_HP > 3000:
                            User2_HP = 3000
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[0] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = True  # 플레이어 변환
                        User2 = False
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][3] == "Special1":
                    Once = True
                    Damage = random.randint(-500, 500)
                    if Damage > 0:
                        User1_HP -= Damage
                        await message.channel.send("```모!! " + PlayerName[0] + " 는(은) " + str(Damage) + "데미지를 입었다.```")
                    elif Damage < 0:
                        User2_HP += Damage
                        await message.channel.send("```빽도!! " + PlayerName[1] + " 는(은) " + str(Damage) + "데미지를 입었다.```")
                    elif Damage == 0:
                        await message.channel.send("```" + "아무일도 일어나지 않았다..." + "```")
                    if User1_HP <= 0:
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[1])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[0])
                        Count = 0
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User2_HP <= 0:  # 상대방 피가 0보다 작거나 같다면 게임 끝
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[0])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[1])
                        Count = 0  # 게임이 끝났으므로 모든 변수 초기화
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User1_HP > 0 and User2_HP > 0:
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[0] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = True
                        User2 = False
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][3] == "Special2":
                    if Once == False:
                        await message.channel.send("```" + PlayerName[0] + " 는(은) 선빵을 맞아 패기를 잃었다." + "```")
                        User1_HP -= (ChoiceSkill[Num - 1][1]) * 2
                    elif Once == True:
                        await message.channel.send("```" + PlayerName[0] + " 는(은) 전혀 아프지 않은 공격을 맞았다." + "```")
                        User1_HP -= ChoiceSkill[Num - 1][1]
                    Once = True
                    if User1_HP <= 0:
                        await message.channel.send(":fire:" + " 승리자 " + ":fire:" + " :: " + PlayerName[1])
                        await message.channel.send(":poop:" + " 패배자 " + ":poop:" + " :: " + PlayerName[0])
                        Count = 0
                        User1_HP = 3000
                        User2_HP = 3000
                        Start = False
                        Receive = False
                        GameStart = False
                        User1 = False
                        User2 = False
                        notAgain = False
                        SkilNumber = False
                        PlayerList = []
                        PlayerName = []
                        ChoiceSkill = []
                        User1Dot = []
                        User2Dot = []
                        User1Turn = []
                        User2Turn = []
                        Once = False
                        Check = False
                        Check2 = False
                    elif User1_HP > 0 and User2_HP > 0:
                        if User1_HP > 3000:
                            User1_HP = 3000
                        if User2_HP > 3000:
                            User2_HP = 3000
                        await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                        await message.channel.send("```" + PlayerName[0] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                        User1 = True
                        User2 = False
                        SkilNumber = False
                        notAgain = False
                        ChoiceSkill = []

                elif ChoiceSkill[Num - 1][5] == "Dotdem":
                    Once = True
                    DotSkill = ChoiceSkill[Num - 1]
                    User1Turn.append(ChoiceSkill[Num - 1][2])
                    User1Dot.append(DotSkill)
                    await message.channel.send("```" + PlayerName[0] + ChoiceSkill[Num - 1][3] + "```")
                    await message.channel.send("```" + PlayerName[0] + "의 체력 : " + str(User1_HP) + "  " + PlayerName[1] + "의 체력 : " + str(User2_HP) + "```")
                    await message.channel.send("```" + PlayerName[0] + "님의 차례입니다! (!공격)을 하세요!" + "```")
                    User1 = True
                    User2 = False
                    SkilNumber = False
                    notAgain = False
                    ChoiceSkill = []


client.run("ODE3NzQ5MDE4NjA4MjcxMzYx.YEOCHw.pyOE8GQq5kxBND2V-8PUxfGnsUQ")
