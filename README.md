# Order Management API

## Visão Geral

É uma API de registro de pedidos desenvolvida com Flask e MongoDB.

O projeto implementa um fluxo simples de criação, consulta e atualização de pedidos usando uma arquitetura de domínio claro:
- rotas HTTP em Flask
- casos de uso que orquestram lógica de negócio
- repositório MongoDB para persistência
- validação de payloads com Cerberus
- tratamento de erros HTTP consistente

## Funcionalidades Principais

- Registrar novos pedidos com dados de cliente, endereço, cupom e itens
- Consultar pedidos por `order_id`
- Atualizar campos de pedidos existentes
- Retornar erros claros para entradas inválidas e pedidos não encontrados


## Requisitos

- Python 3.11
- Flask
- MongoDB

## Instalação

1. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate    # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o servidor:

```bash
python run.py
```

O servidor abrirá em `http://0.0.0.0:3000`.

## Endpoints

### Criar pedido

`POST /delivery/order`

Corpo esperado:

```json
{
  "data": {
    "name": "Nome do cliente",
    "address": "Rua Exemplo, 123",
    "cupom": false,
    "items": [
      { "item": "pizza", "quantidade": 2 },
      { "item": "refrigerante", "quantidade": 1 }
    ]
  }
}
```

Resposta de sucesso:

```json
{
  "data": {
    "type": "Order",
    "count": 1,
    "registry": true
  }
}
```

### Consultar pedido

`GET /delivery/order/<order_id>`

Resposta de sucesso:

```json
{
  "data": {
    "count": 1,
    "type": "Order",
    "attributes": {
      "_id": "<order_id>",
      "name": "...",
      "address": "...",
      "cupom": false,
      "items": [...],
      "created_at": "..."
    }
  }
}
```

### Atualizar pedido

`PATCH /delivery/order/<order_id>`

Corpo válido:

```json
{
  "data": {
    "name": "Novo nome",
    "address": "Novo endereço",
    "cupom": true
  }
}
```

Resposta de sucesso:

```json
{
  "data": {
    "order_id": "<order_id>",
    "type": "Order",
    "count": 1
  }
}
```

## Tratamento de Erros

- `404` para pedidos não encontrados
- `422` para payloads inválidos
- `500` para erros internos do servidor

As respostas de erro seguem o padrão:

```json
{
  "errors": "ErrorType",
  "detail": "Mensagem de erro"
}
```

## Testes

O projeto contém testes de unidade para repositórios e casos de uso.

Execute-os com:

```bash
pytest
```

## Observações

- A aplicação persiste pedidos na coleção `orders` do MongoDB.
- Cada pedido recebe um campo `created_at` quando é registrado.
- A atualização de pedidos permite modificar apenas campos específicos: `name`, `address` e `cupom`.
