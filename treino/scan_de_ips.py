#Imports
from ping3 import ping
from time import sleep

#Variáveis
endereco_ips = ["192.168.0.17"]
resultado_ping = []
resultado_anterior_de_ping = []

def pingar_ips(lista_de_ips):
    global resultado_ping
    resultado_ping = []
    try:
        for ip in lista_de_ips:
            resposta = ping(ip, timeout=1)
            status = 'OFFLINE' if resposta is None else 'ONLINE'
            #print(ip,status)
            resultado_ping = resultado_ping+[status]

    except PermissionError:
        print('Erro nas permissções do sistema')

    except KeyboardInterrupt:
        print("A varredura foi interrompida via teclado")

def verificar_mudanca():
    posicao = 0
    for resultado in resultado_ping:
        if resultado == resultado_anterior_de_ping[posicao]:
            print("O endereço IP {} continua: {}".format(endereco_ips[posicao],resultado))
        else:
            print("O endereço IP {} agora está {}".format(endereco_ips[posicao],resultado))
        posicao = posicao+1
        
    


pingar_ips(endereco_ips)
resultado_anterior_de_ping = resultado_ping

while True:
    pingar_ips(endereco_ips)
    verificar_mudanca()
    resultado_anterior_de_ping = resultado_ping

    #print(resultado_ping,"\n")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    sleep(2)
    







#___--- Funções ---___
def verificar_status():
    print("teste")

def mapeia_ips(ips):
    end_IP_ON = []
    end_IP_OFF = []

    try:
        for ip in ips:
            t = ping(ip, timeout=2)
            status = 'OFFLINE' if t is None else 'ONLINE'

            #print(f'IP: {ip} [{status}]')
            #print("Thread : {}".format(os.getpid()))

            if status == 'ONLINE':
                end_IP_ON = end_IP_ON+[ip]
            else:
                end_IP_OFF = end_IP_OFF+[ip]
            global quantidade_atual_de_progresso
            quantidade_atual_de_progresso = quantidade_atual_de_progresso+1

        #Define a lista de ips como equipamentos ONLINE
        #listaDeIPs = end_IP_ONline

    except PermissionError:
        print('Erro nas permissções do sistema')

    except KeyboardInterrupt:
        print("A varredura foi interrompida via teclado")

    finally:
        global end_IP_ONline
        global end_IP_OFFline

        end_IP_ONline = end_IP_ONline+end_IP_ON
        end_IP_OFFline = end_IP_OFFline+end_IP_OFF

        #print("FINALIZADO")

def scanear_rede():

    #___---¨¨¨ Sub-Funções do scanner ¨¨¨---___
    def preparar_faixa_de_ips():
        #Prepara um arry contendo todos os IPs possíveis dentro das faixas base 
        global ips_totais_da_faixa
        for posi in range(ipsIniciais.__len__()):
            ips_totais_da_faixa = ips_totais_da_faixa+[str(IPv4Address(ip)) for ip in range(int(IPv4Address(ipsIniciais[posi])), int(IPv4Address(ipsFinais[posi])))]
        #print("QTD total de IPs: ",ips_totais_da_faixa.__len__())
    
    def remover_ips_banidos_da_faixa():
        # Remove os IPs banidos da faixa de IP, usado para remover equipamentos que o scrip não deve ter acesso
        global ips_totais_da_faixa
        global ips_banidos
        try:
            arquivo = open('system/ip_banido.txt','r',encoding=cod_do_arquivo)
            numero_linha_atual = 0

            for linha in arquivo:
                numero_linha_atual = numero_linha_atual+1
                # Pulando as linhas de comentários do arquivo
                if numero_linha_atual > 4:
                    # Leva em consideração somente linhas no padrão esperado ("elemento1;elemento2") / legenda = ("IP do cliente;Nome") 
                    if ((str(linha.replace("\r","").replace("\n",""))).split(";")).__len__() == 2:
                        ipban = str((linha.replace("\r","").replace("\n","").split(';'))[0])
                        try:
                            ips_totais_da_faixa.remove(ipban)
                            ips_banidos = ips_banidos+[ipban]
                            #print("a"+ipban+"a")
                        except ValueError:
                            print("O IP {} consta banido, mas não esta na faixa de IP".format(ipban))
            

        except FileNotFoundError:
            print("\nO Arquivo de IPs banidos não foi encontrado!\nO SCRIPT tentará PINGAR todos os IPs da faixa total\n")
    
    def coletar_ping_ip(ip):
        global resultados_do_ping_ultra_rapido
        tempo_de_resposta = ping(ip,timeout=2)
        resultados_do_ping_ultra_rapido[ip] = tempo_de_resposta

    def controlador_de_threads_do_ping():
        # Lista para armazenar as threads
        threads = []

        # Criar e iniciar uma thread para cada IP
        for ip in ips_totais_da_faixa:
            thread = threading.Thread(target=coletar_ping_ip, args=(ip,))
            thread.start()
            threads.append(thread)

        # Aguardar o término de todas as threads
        for thread in threads:
            thread.join()

    def descomprimir_dados_do_ping():
        global ping_online
        global ping_offline
        global ping_erro

        for ip_separado, tempo_de_resposta_separado in resultados_do_ping_ultra_rapido.items():
            t_ip = str(ip_separado)
            t_tr = str(tempo_de_resposta_separado)

            if t_tr == "False":
                ping_offline = ping_offline + [t_ip]
            else:
                if t_tr == "None":
                    ping_erro = ping_erro + [t_ip]
                else:
                    ping_online = ping_online + [t_ip]
        
    def exibir_resumo_final_do_ping():
        print("""
        ##################################
        ##  -Mapeamento concluído-       ##
        ## {} IPs ONLINE               ##
        ## {} IPs OFFlines/Disponíveis ##
        ## {} IPs que retornaram ERRO ##
        ## {} Total ips mapeado       ##
        ## {} IPs Banidos              ##
        ##################################
        """.format(ping_online.__len__(),ping_offline.__len__(),ping_erro.__len__(),ips_totais_da_faixa.__len__(),ips_banidos.__len__()))

    def gravar_dados_de_ping():
        dia = str(data.split(" ")[0])
        mapeamentoON = open('dados/ping/ping On {}.dadosmr'.format(data),'a')
        for equipamentoOn in ping_online:
            mapeamentoON.write("{};{}\n".format(equipamentoOn,dia))
        mapeamentoON.close()

        mapeamentoOFF = open('dados/ping/ping Off {}.dadosmr'.format(data),'a')
        for equipamentoOff in ping_offline:
            mapeamentoOFF.write("{};{}\n".format(equipamentoOff,dia))
        mapeamentoOFF.close()

        mapeamentoERRO = open('dados/ping/ping Erro {}.dadosmr'.format(data),'a')
        for equipamentoERRO in ping_erro:
            mapeamentoERRO.write("{};{}\n".format(equipamentoERRO,dia))
        mapeamentoERRO.close()



    #___---¨¨¨ Inicio da função principal de escanear rede ¨¨¨---___
    preparar_faixa_de_ips()
    remover_ips_banidos_da_faixa()
    controlador_de_threads_do_ping()
    descomprimir_dados_do_ping()
    gravar_dados_de_ping()
    exibir_resumo_final_do_ping() 
 