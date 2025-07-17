import os
from cryptography.fernet import Fernet, InvalidToken

# --- Funções para a Chave ---

def gerar_chave():
    """
    Gera uma chave de criptografia e a salva no arquivo 'secret.key'.
    Aviso: Se já existir uma chave, ela NÃO será substituída por segurança.
    """
    if not os.path.exists("secret.key"):
        chave = Fernet.generate_key()
        with open("secret.key", "wb") as arquivo_chave:
            arquivo_chave.write(chave)
        print("Chave 'secret.key' gerada com sucesso!")
        print("IMPORTANTE: Guarde este arquivo em um local MUITO seguro.")
    else:
        print("A chave 'secret.key' já existe. Nenhuma nova chave foi gerada.")

def carregar_chave():
    """
    Carrega a chave do arquivo 'secret.key'.
    """
    if not os.path.exists("secret.key"):
        print("Erro: Arquivo 'secret.key' não encontrado.")
        print("Gere uma chave primeiro usando a opção 1 do menu.")
        return None
    return open("secret.key", "rb").read()

# --- Funções de Criptografia e Descriptografia ---

def processar_pasta(operacao, caminho_pasta, chave):
    """
    Função principal que percorre a pasta e aplica a operação (criptografar ou descriptografar).
    """
    try:
        fernet = Fernet(chave)
    except Exception as e:
        print(f"Erro: Chave inválida. Verifique o arquivo 'secret.key'. Detalhes: {e}")
        return

    print(f"\nIniciando operação de '{operacao}' na pasta '{caminho_pasta}'...")

    # os.walk percorre todos os arquivos e subpastas
    for pasta_raiz, _, arquivos in os.walk(caminho_pasta):
        for nome_arquivo in arquivos:
            # Ignora o próprio script e a chave
            if nome_arquivo == "cripto_pasta.py" or nome_arquivo == "secret.key":
                continue

            caminho_completo = os.path.join(pasta_raiz, nome_arquivo)

            try:
                with open(caminho_completo, "rb") as arquivo:
                    dados_originais = arquivo.read()

                if operacao == "criptografar":
                    dados_processados = fernet.encrypt(dados_originais)
                    print(f"  -> Criptografando: {caminho_completo}")
                elif operacao == "descriptografar":
                    dados_processados = fernet.decrypt(dados_originais)
                    print(f"  -> Descriptografando: {caminho_completo}")

                with open(caminho_completo, "wb") as arquivo:
                    arquivo.write(dados_processados)

            except InvalidToken:
                print(f"  -> [AVISO] Chave incorreta ou arquivo não criptografado: {caminho_completo}")
            except Exception as e:
                print(f"  -> [ERRO] Falha ao processar o arquivo {caminho_completo}: {e}")

    print(f"\nOperação '{operacao}' concluída!")

# --- Menu Principal ---

def menu():
    """
    Exibe o menu de opções para o usuário.
    """
    while True:
        print("\n--- Criptografador de Pastas ---")
        print("1. Gerar uma nova chave de segurança (Faça isso primeiro!)")
        print("2. Criptografar uma pasta")
        print("3. Descriptografar uma pasta")
        print("4. Sair")

        escolha = input(">> Escolha uma opção: ")

        if escolha == '1':
            gerar_chave()
        elif escolha == '2' or escolha == '3':
            chave = carregar_chave()
            if chave:
                caminho_pasta = input("Digite o caminho completo da pasta: ")
                if os.path.isdir(caminho_pasta):
                    operacao = "criptografar" if escolha == '2' else "descriptografar"
                    processar_pasta(operacao, caminho_pasta, chave)
                else:
                    print("O caminho especificado não é uma pasta válida.")
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()