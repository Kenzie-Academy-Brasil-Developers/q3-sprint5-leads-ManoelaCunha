# Leads

Esse é o repositório usado no desenvolvimento da API da Entrega - **Leads** - com SQLAlchemy, Dataclass, Blueprint, Migrations e Padrão Flask Factory.

Essa aplicação tem como objetivo realizar o controle de **Leads**.

**Lead**: São pessoas que podem estar interessados em algum tipo de produto ou serviço. Esses possíveis futuros clientes podem ser coletados através de preenchimento de formulários ou cliques em páginas da internet, os dados geralmente são utilizados em campanhas publicitárias.

## Endpoints

A API possui 1 endpoint - **_/leads_** e 4 rotas - **_POST / GET / PATCH / DELETE_**

Onde é possível **registrar** um novo **Lead** no banco de dados, **listar** todos os **Leads** por **ordem de visitas**, **atualizar** o registro de **visitas** de um **Lead** e **deletar** um **Lead** específico.

O url base da API é https://api-leads-q3-kenzie.herokuapp.com

## POST

**Registrando um novo Lead**

**POST /leads - FORMATO DA REQUISIÇÃO**

```javascript
{
  "name": "Kenzinha",
  "email": "kenzinha@mail.com",
  "phone": "(41)90000-1111"
}
```

**POST /leads - FORMATO DA RESPOSTA - STATUS 201 - CREATED**

```javascript
{
  "name": "Kenzinha",
  "email": "kenzinha@mail.com",
  "phone": "(41)90000-1111",
  "creation_date": "Mon, 21 Feb 2022 09:02:03 GMT",
  "last_visit": "Mon, 21 Feb 2022 09:02:03 GMT",
  "visits": 1
}
```

## GET

**Listando Leads**

**GET /leads - FORMATO DA RESPOSTA - STATUS 200 - OK**

```javascript
[
  {
    name: "Kenzinha",
    email: "kenzinha@mail.com",
    phone: "(41)90000-1111",
    creation_date: "Mon, 21 Feb 2022 09:02:03 GMT",
    last_visit: "Thu, 24 Feb 2022 10:03:00 GMT",
    visits: 8,
  },
  {
    name: "Kenzinho",
    email: "kenzinho@mail.com",
    phone: "(41)90000-2222",
    creation_date: "Thu, 24 Feb 2022 10:02:09 GMT",
    last_visit: "Thu, 24 Feb 2022 10:02:09 GMT",
    visits: 1,
  },
];
```

## PATCH

**Atualizando registro de visitas de um Lead**

**PATCH /leads - FORMATO DA REQUISIÇÃO**

_Corpo da requisição obrigatoriamente apenas com ***email***_

```javascript
{
  "email": "kenzinha@mail.com"
}
```

**PATCH /leads - FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT**

No body returned for response

## DELETE

**Deletando um Lead específico**

**DELETE /leads - FORMATO DA REQUISIÇÃO**

_Corpo da requisição obrigatoriamente apenas com ***email***_

```javascript
{
  "email": "kenzinha@mail.com"
}
```

**DELETE /leads - FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT**

No body returned for response

## Avaliação da Entrega

| Critérios                                                                                                      | Pts. |
| -------------------------------------------------------------------------------------------------------------- | ---- |
| Utilizar **SQLAlchemy**, **Dataclass**, **Blueprint**, **Migrations** e **Padrão Flask Factory** corretamente. | 1    |
| [GET] **/leads** - Rota funcionando e ordenada de acordo com o enunciado.                                      | 1    |
| [GET] **/leads** - [ERRO] Nenhum dado encontrado.                                                              | 0.5  |
| [POST] **/leads** - Rota funcionando de acordo com o enunciado.                                                | 1    |
| [POST] **/leads** - [ERRO] E-mail e telefone únicos.                                                           | 0.5  |
| [POST] **/leads** - [ERRO] Telefone obrigatoriamente no formato (xx)xxxxx-xxxx.                                | 0.5  |
| [PATCH] **/leads** - Rota funcionando de acordo com o enunciado.                                               | 2    |
| [PATCH] **/leads** - [ERRO] - Corpo da requisição obrigatoriamente apenas com email e deve ser uma string;     | 0.5  |
| [PATCH] **/leads** - [ERRO] - Nenhum dado encontrado.                                                          | 0.5  |
| [DELETE] **/leads** - Rota funcionando de acordo com o enunciado.                                              | 1    |
| [DELETE] **/leads** - [ERRO] - Corpo da requisição obrigatoriamente apenas com email e deve ser uma string;    | 0.5  |
| [DELETE] **/leads** - [ERRO] - Nenhum dado encontrado.                                                         | 0.5  |
| Arquivos **requirements.txt**, **.env**, **.env.example** e **.gitignore** (**venv** e **.env** adicionados)   | 0.5  |
