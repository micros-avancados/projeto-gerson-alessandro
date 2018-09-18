# **Placa escolhida:**

**Raspberry Pi 3**, escolhida pela força da sua comunidade de usuários, é compatível com uma quantidade de sistemas operacionais muito grande, passando do Raspbian – seu OS original – à outras distribuições de Gnu/Linux, Android  e algumas distribuições especializadas como a  XBMC. Também possui um vasto conteúdo que podem ser aplicados ao nosso projeto que foi definido.

![Pinos](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg)

# **Definições do projeto:**

Marcação de ponto móvel, utilizando modulo fingerprint, modulo GPS e modulo GSM.
A ideia consiste em criar um embarcado para registro do ponto móvel, o protótipo deve:

 1. Ler a impressão digital e valida-la com a base existente.
 2. Realizar o registro do ponto informando hora, localização e quem foi o colaborador o qual realizou a operação. 
 3. Enviar esses dados utilizando algum meio de acesso a rede (GSM, WIFI) ou por SMS. 
 
 Por ultimo, caso o tempo possibilite a implementação. Ter uma interface amigável para visualização dos dados.

# MÓDULOS:
## Módulo Sensor Leitor Biométrico
![leitor](http://www.theorycircuit.com/wp-content/uploads/2016/08/fingerprint-sensor-pinout.jpg)
<br>
**ESPECIFICAÇÕES:**  

 - Modelo: FPM10A;
 - Alimentação: 3.3 VDC;
 - Corrente de Funcmionamento: 120mA max;
 - Corrente de pico: 140mA ax;
 - Tempo de imagem da impressão digital: <1,0 segundo;
 - Área da janela: 14 milímetros x 18 milímetros;
 - Arquivo de assinatura: 256 bytes;
 - Arquivo de modelo: 512 bytes;
 - Capacidade de armazenamento: 162 digitais na memória interna / 1000
   digitais software PC;
 - Classificações de segurança (1-5 baixo - alto nível de segurança);
 - Taxa de aceitação de identificações falsas: <0,001% (segurança nível
   3);
 - Taxa de rejeição de identificações falsas: <1,0% (nível de segurança
   3);
 - Interface: TTL Serial;
 - Taxa de transmissão: 9600, 19200, 28800, 38400, 57600 (o padrão é
   57600);
 - Temperatura de trabalho: -20C a + 50C;
 - Umidade de trabalho: 40% -85% RH;
 - Dimensões totais: 56 x 20 x 21,5 milímetros;
 

**PINAGEM:**
 - Pino 1 = GND
 - Pino 2 = RX 
 - Pino 3 = TX 
 - PIno 4 = VCC +3.3V 


O Sensor ascende a luz do leitor somente após estabelecer a conexão com a placa estando com a biblioteca instalada e o programa carregado.  
   
**BIBLIOTECA:** Adafrut Optical Fingerprint Sensor;  

## Módulo RTC DS1302 (Relógio)
## Módulo GPS GY-GPS6MV2 

**ESPECIFICAÇÕES**:

-   Módulo GPS GY-NEO6MV2
-   Tensão de Operação: 3,3V
-   Corrente: 45mA
-   Número de Canais: 50
-   Protocolo de comunicação: Serial TTL (TxRx)
-   Acompanha mini bateria para backup
-   Baudrate: 9600bps
-   Precisão: 5 metros
-   Dimensões: 35 x 25 x 25mm
-   Cold Start: 27s
-   Warm Start: 27s
-   Hot Start: 1
