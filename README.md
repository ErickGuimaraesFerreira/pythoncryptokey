# Python Crypto Key

![Build Status](https://github.com/ErickGuimaraesFerreira/pythoncryptokey/actions/workflows/ci.yml/badge.svg)
[![Python Version](https://img.shields.io/pypi/pyversions/pythoncryptokey?style=flat-square)](https://pypi.org/project/pythoncryptokey/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Uma ferramenta de linha de comando simples e uma biblioteca Python para gerar chaves de criptografia simétrica [Fernet](https://github.com/pyca/cryptography).

## Principais Funcionalidades

-   Gera uma chave criptograficamente segura.
-   Salva a chave em um arquivo (`chave.key` por padrão).
-   Pode ser usada como uma ferramenta de linha de comando ou importada em outros projetos Python.

## Instalação

Você pode instalar diretamente do GitHub:

```bash
pip install git+[https://github.com/ErickGuimaraesFerreira/pythoncryptokey.git](https://github.com/ErickGuimaraesFerreira/pythoncryptokey.git)
```
*(Em breve, disponível via `pip install pythoncryptokey`)*

## Como Usar

### 1. Como Ferramenta de Linha de Comando

Após a instalação, você pode simplesmente executar o seguinte comando no seu terminal:

```bash
py-generate-key
```

A saída será:

```
✅ Chave de criptografia gerada com sucesso!
   Salva em: /caminho/completo/para/sua/chave.key
```

### 2. Como Biblioteca Python

Você também pode importar e usar a função `generate_key` em seu próprio código.

```python
from pythoncryptokey.key_generator import generate_key
from pathlib import Path

# Gera a chave no local padrão ('chave.key')
generate_key()

# Gera a chave em um local personalizado
caminho_customizado = Path("minha_chave_secreta.key")
generate_key(output_path=caminho_customizado)

print(f"Chave gerada em {caminho_customizado}")
```

## Como Contribuir

Contribuições são muito bem-vindas! Por favor, leia o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para saber como participar.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.