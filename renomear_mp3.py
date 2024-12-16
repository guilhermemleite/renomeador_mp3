import os
import re

def renomear_mp3(pasta):
    try:
        # Percorre todas as subpastas e arquivos
        for raiz, _, arquivos in os.walk(pasta):
            # Filtrar apenas os arquivos .mp3
            arquivos_mp3 = [f for f in arquivos if f.endswith(".mp3")]
            # Ordena para manter consistência nos nomes
            arquivos_mp3.sort()

            for i, arquivo in enumerate(arquivos_mp3, start=1):
                # Extrair somente os caracteres após os números
                nome_sem_numeros = re.sub(r"^\d+\s*", "", arquivo)  # Remove números iniciais e espaços
                # Cria o novo nome com numeração sequencial
                novo_nome = f"{i:02d} {nome_sem_numeros}"
                # Caminhos completos
                caminho_antigo = os.path.join(raiz, arquivo)
                caminho_novo = os.path.join(raiz, novo_nome)
                # Renomeia o arquivo
                os.rename(caminho_antigo, caminho_novo)
                print(f"{caminho_antigo} -> {caminho_novo}")

        print("\nRenomeação concluída com sucesso!")
    except Exception as e:
        print(f"Erro ao renomear arquivos: {e}")

# Função principal com loop para múltiplas pastas
def main():
    while True:
        # Solicitar caminho da pasta ao usuário
        pasta = input("\nDigite o caminho da pasta principal: ")
        if not os.path.isdir(pasta):
            print("O caminho fornecido não é válido. Tente novamente.")
            continue

        # Chamar a função de renomeação
        renomear_mp3(pasta)

        # Perguntar se deseja processar outra pasta
        repetir = input("\nDeseja realizar o processo em outra pasta? (Tecle S para Sim ou N para Não): ").strip().upper()
        if repetir == "N":
            print("Encerrando o programa. Até logo!")
            break
        elif repetir != "S":
            print("Opção inválida. Encerrando o programa.")
            break

# Executar o programa
if __name__ == "__main__":
    main()
