# Renomeador de arquivos MP3 com sequência numérica

Este script em Python renomeia arquivos .mp3 dentro de uma pasta específica, removendo números iniciais no nome dos arquivos e aplicando uma nova sequência numérica. Ele é útil para organizar arquivos de áudio que possuem nomes confusos ou desordenados.

Como Funciona:

O script segue os seguintes passos:

1. Solicita ao usuário o caminho da pasta principal onde estão localizados os arquivos .mp3.

2. Percorre todos os arquivos .mp3 dentro da pasta (e suas subpastas, se houver).

3. Renomeia os arquivos:
- Remove quaisquer números iniciais (e espaços adjacentes) no nome do arquivo.
- Aplica uma sequência numérica no formato XX (ex.: 01, 02, etc.), com base na ordem dos arquivos.
4. Exibe no terminal os nomes dos arquivos antes e depois da renomeação.

5. Após concluir, pergunta ao usuário se deseja realizar o mesmo processo em outra pasta ou encerrar o programa.

Exemplo:

Arquivos originais: 01 xpto.mp3, 157 apto.mp3, 4 zpto.mp3, 0065898787645kpto.mp3, 998 dpto655.mp3, 100000 jpto.mp3, 45 lpto 24.mp3

Arquivos renomeados: 01 xpto.mp3, 02 apto.mp3, 03 zpto.mp3, 04 kpto.mp3, 05 dpto655.mp3, 06 jpto.mp3, 07 lpto 24.mp3


Estrutura do código:

1. Função renomear_mp3:

- Realiza a renomeação dos arquivos.
- Remove números no início do nome usando uma expressão regular (re.sub).
- Adiciona uma nova sequência numérica em ordem crescente.

2. Função main:

- Controla a interação com o usuário.
- Permite que o processo seja repetido para múltiplas pastas, dependendo da escolha do usuário.

3. Uso de os.walk:

- Garante que todos os arquivos .mp3 em subpastas também sejam processados.

4. Mensagens informativas:

- Durante a execução, o script informa no terminal quais arquivos foram renomeados e exibe as opções disponíveis para o usuário.



