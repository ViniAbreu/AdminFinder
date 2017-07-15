import requests
from datetime import datetime

class colors():
    vermelho = '\033[3;31m'
    verde = '\033[1;32m'
    azul = '\033[1;34m'
    ciano = '\033[1;36m'
    magenta = '\033[1;35m'
    amarelo = '\033[1;33m'
    preto = '\033[1;30m'
    branco = '\033[1;37m'
    original = '\033[0;0m'
    reverso = '\033[2m'
    default = '\033[0m'

banner = '''
                     :I. ..
                    :III/ I.
                   : III  II
                  :  III .II
                  : .III III
                  : III' III					▄▄▄      ▓█████▄  ███▄ ▄███▓ ██▓ ███▄    █      █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███
                  : III  II'					▒████▄    ▒██▀ ██▌▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █    ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
                  : `I/__L_					▒██  ▀█▄  ░██   █▌▓██    ▓██░▒██▒▓██  ▀█ ██▒   ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
                ./'        ~~-.					░██▄▄▄▄██ ░▓█▄   ▌▒██    ▒██ ░██░▓██▒  ▐▌██▒   ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄
               ."   -~~-       `.				 ▓█   ▓██▒░▒████▓ ▒██▒   ░██▒░██░▒██░   ▓██░   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
               :    .==.         :				 ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒     ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
               |    `..b'      ___:				  ▒   ▒▒ ░ ░ ▒  ▒ ░  ░      ░ ▒ ░░ ░░   ░ ▒░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
               |           __.`\__/__				  ░   ▒    ░ ░  ░ ░      ░    ▒ ░   ░   ░ ░     ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░
                `.       ----   _i_----					░  ░   ░           ░    ░           ░            ░           ░    ░       ░  ░   ░
                / `-........:`----'
              /'    ,MMMMMMM.
            :'     .MMMMMMMMm.
           :'      mMMMMMMMMMm
          /:       MMMMMMMMMMM				          +-----------------------------------------------------------+
        /' :       MMMMMMMMMMM				          +                        Admin Finder                       +
      /"           `MMMMMMMMM'				          +-----------------------------------------------------------+
     :      \       `MMMMMMM'\				          |                     Coder: Sr. Biggs                      |
    :'       `:      MMMMMMM: `\				  |                     Telegram: @SrBiggs                    |
    :         `:     `MMMMM':   `:				  |                     Version: 1.0                          |
    :      mMMMm      MMMM' :    :				  |                     GitHub: BiggsCoder                    |
    :     mMMMMMMm    mMMm  :    :				  +-----------------------------------------------------------+
     \    `MMMMMMm    mMMm  :   /
    /~~~   MMMMMMm    mJVm  : /'___
  :'| |   /`JMMMMm . .m96m  \      \z
   ~~~~~~~        \_:_|   L_/~~~~~~
         '''
print(colors.amarelo+banner)
site = input(colors.azul+"[+] Informe o site\n[?] > "+colors.default)

class datas():
    now = datetime.now()
    dia = str(now.day)
    mes = str(now.month)
    ano = str(now.year)
    hora = str(now.hour)
    minut = str(now.minute)
    segundo = str(now.second)

word = open('wordlists.txt')
wordlists = word.readlines()
word.close()

if 'http://' in site:
    pass
elif 'https://' in site:
    pass
else:
    site = 'http://' + site

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.103 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 6.1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.87 Safari/537.36'
                      'Mozilla/5.0 (Windows NT 6.1; rv:45.0)'
                      'Gecko/20100101 Firefox/45.0'
    }

pages = open('pages.txt','w+')

for flag in wordlists:
    flag = flag.replace("\n","")
    try:
        url = site+flag
        req = requests.get(url)
        codigo = req.status_code

        if codigo == 200:
            print(colors.verde+"\n[+] ADMIN PAGE FOUND: "+colors.azul+url+"\n")
            pages.write(str("["+datas.hora+":"+datas.minut+"] "+" ADMIN PAGE : "+url+"\n"))
            pages.close()
        else:
            print(colors.ciano+"[-] ADMIN PAGE NOT FOUND: "+colors.default+url+"\n")

    except:
        print(colors.vermelho+"[!] Não foi possivel fazer requisição no site\n"+colors.default)

print(colors.verde+"[+] Procura finalizada com sucesso !")
print(colors.verde+"[+] Confira as paginas encontrada no arquivo 'pages.txt'"+colors.default)
