import socket
import time

# Função que tenta conectar em um IP e Porta específicos
def verificar_porta(ip, porta):
    # Cria o conector de rede (IPv4, TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3) # Aguarda até 3 segundos pela resposta

    # O comando connect_ex retorna 0 se a conexão for bem sucedida
    resultado = sock.connect_ex((ip, porta))

    if resultado == 0:
        print(f"[OK] Sucesso: O IP {ip} está respondendo na porta {porta}.")
    else:
        print(f"[ALERTA] Falha: A porta {porta} no IP {ip} está inacessível!")

    sock.close()

# Lista de servidores e portas para monitorar
# Exemplo: Testando DNS do Google e HTTPS da Cloudflare
alvos = [
    ("8.8.8.8", 53),
    ("1.1.1.1", 443),
    ("10.10.1.254", 80) # Mude para o IP do seu roteador local
]

print("--- Iniciando Monitoramento de Infraestrutura ---")

# Loop que passa por cada servidor da lista e executa o teste
for ip, porta in alvos:
    verificar_porta(ip, porta)
    time.sleep(1) # Pausa de 1 segundo entre os testes para não sobrecarregar a rede

print("--- Monitoramento Concluído ---")