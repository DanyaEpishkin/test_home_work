## Подготовка и запуск
Грузим зависимости
```bash
pip3 install -r requirements.txt
```

Находясь в `src` (`cd src`)
```bash
python3 -m aiohttp.web -P 8080 application:create_application
```

Всё! Сервер слушает порт `8080`.

## Page
Можно получить HTML страницу с данными о пользователе в рамках сессии.
Для этого достаточно пе рейти по URL `http://localhost:8080/session/{ssid}`. 
Идентификатор сессии - `ssid` можно получить средствами API `/api/v1/user/login`.

## API
Варианты ответа API:

**Запрос успешено обработан**
```JSON
{
  "success": true,
  "result": ...
}
```

**При обработке запроса возникла ошибка**
```JSON
{
  "success": false,
  "error": "Some error details"
}
```


### Регистрация
> **POST** /api/v1/user/registration

#### Параметры запроса:  
**[headers]**  
**-**   

**[path]**  
**-**   

**[body]**
- `user` - данные пользователя
- `user.login` - логин
- `user.password` - пароль


#### Параметры ответа
**[body]**
- `success` - успешность обработки запроса
- `result` - объект с результатом запроса
- `result.user` - данные созданного пользователя
- `result.user.login` - логин пользователя
- `result.user.contacts` - список контактов пользователя
- `result.user.contacts[].id` - идентификатор контакта
- `result.user.contacts[].type` - тип контакта
- `result.user.contacts[].content` - данные контакта (`phone` / `email`)

Запрос:
```bash
curl -XPOST http://localhost:8080/api/v1/user/registration -d '{"user": {"login": "username", "password": "******"}}'
```

Ответ:
```JSON
{
  "success": true,
  "result": {
    "user": {
      "login": "username",
      "contacts": []
    }
  }
}
```
 
 
 
 
 
 
### Авторизация
> **POST** /api/v1/user/login

#### Параметры запроса:  
**[headers]**  
**-**   

**[path]**  
**-**   

**[body]**
- `user` - данные пользователя
- `user.login` - логин
- `user.password` - пароль


#### Параметры ответа
- `success` - успешность обработки запроса
- `result` - объект с результатом запроса
- `result.ssid` - идентификатор созданной сессии. Используется для передачи в заголовке `ssid`
- `result.user` - данные созданного пользователя
- `result.user.login` - логин пользователя
- `result.user.contacts` - список контактов пользователя
- `result.user.contacts[].id` - идентификатор контакта
- `result.user.contacts[].type` - тип контакта
- `result.user.contacts[].content` - данные контакта (`phone` / `email`)


#### Пример
Запрос:
```bash
curl -XPOST http://localhost:8080/api/v1/user/login -d '{"user": {"login": "username", "password": "******"}}'
```

Ответ:
```JSON
{
  "success": true,
  "result": {
    "ssid": "fd2f6760-8388-4be3-8af7-bb3920180dfd",
    "user": {
      "login": "username",
      "contacts": []
    }
  }
}
```



### Получение данных пользователя
> **GET** /api/v1/user

#### Параметры запроса:  
**[headers]**
- `ssid` - идентификатор сессии, полученный в результате вызова `/api/v1/user/login`   

**[path]**  
**-**   

**[body]**  
**-**   


#### Параметры ответа
**[body]**
- `success` - успешность обработки запроса
- `result` - объект с результатом запроса
- `result.ssid` - идентификатор созданной сессии. Используется для передачи в заголовке `ssid`
- `result.user` - данные созданного пользователя
- `result.user.login` - логин пользователя
- `result.user.contacts` - список контактов пользователя
- `result.user.contacts[].id` - идентификатор контакта
- `result.user.contacts[].type` - тип контакта (`phone`, `email`)
- `result.user.contacts[].content` - данные контакта 


#### Пример

Запрос:
```bash
curl -XGET http://localhost:8080/api/v1/user -H 'ssid: 0c9298d7-6f97-4e73-9ad2-6d5a5b5a1503'
```

Ответ:
```JSON
{
  "success": true,
  "result": {
    "user": {
      "login": "username",
      "contacts": [
        {
          "id": 2,
          "type": "phone",
          "content": "+000"
        },
        {
          "id": 5,
          "type": "phone",
          "content": "+100"
        }
      ]
    }
  }
}
```

### Добавить контакт пользователя
> **POST** /api/v1/user/contact

#### Параметры запроса:  
**[headers]**
- `ssid` - идентификатор сессии, полученный в результате вызова `/api/v1/user/login`   

**[path]**  
**-**   

**[body]**  
- `contact` - данные создаваемого контакта
- `contact.type` - тип создаваемого контакта (`phone`, `email`)
- `contact.content` - данные контакта

#### Параметры ответа
**[body]**
- `success` - успешность обработки запроса
- `result` - объект с результатом запроса
- `result.ssid` - идентификатор созданной сессии. Используется для передачи в заголовке `ssid`
- `result.user` - данные созданного пользователя
- `result.user.login` - логин пользователя
- `result.user.contacts` - список контактов пользователя
- `result.user.contacts[].id` - идентификатор контакта
- `result.user.contacts[].type` - тип контакта (`phone`, `email`)
- `result.user.contacts[].content` - данные контакта 

#### Пример

Запрос:
```bash
curl -XPOST http://localhost:8080/api/v1/user/contact -H 'ssid: d03f3a3f-e778-4e43-b23d-c579274a4c48' -d '{
  "contact": {
      "type": "phone",
      "content": "+79990001122"
  }
}'
```

Ответ:
```JSON
{
  "success": true,
  "result": {
    "user": {
      "login": "username",
      "contacts": [
        {
          "id": 2,
          "type": "phone",
          "content": "+000"
        },
        {
          "id": 5,
          "type": "phone",
          "content": "+100"
        },
        {
          "id": 6,
          "type": "phone",
          "content": "+79990001122"
        }
      ]
    }
  }
}
```


### Удалить контакт пользователя
> **POST** /api/v1/user/contact/{id}

#### Параметры запроса:  
**[headers]**
- `ssid` - идентификатор сессии, полученный в результате вызова `/api/v1/user/login`   

**[path]**  
- `id` - идентификатор контакта к удалению 

**[body]**  
**-**   


#### Параметры ответа
**[body]**
- `success` - успешность обработки запроса
- `result` - объект с результатом запроса
- `result.ssid` - идентификатор созданной сессии. Используется для передачи в заголовке `ssid`
- `result.user` - данные созданного пользователя
- `result.user.login` - логин пользователя
- `result.user.contacts` - список контактов пользователя
- `result.user.contacts[].id` - идентификатор контакта
- `result.user.contacts[].type` - тип контакта (`phone`, `email`)
- `result.user.contacts[].content` - данные контакта 


#### Пример

Запрос:
```bash
curl -XDELETE http://localhost:8080/api/v1/user/contact/2 -H 'ssid: 9d60dbb2-92ae-407c-80fb-91ebbbf8c1c9'
```

Ответ:
```JSON
{
  "success": true,
  "result": {
    "user": {
      "login": "username",
      "contacts": [
        {
          "id": 5,
          "type": "phone",
          "content": "+100"
        },
        {
          "id": 6,
          "type": "phone",
          "content": "+79990001122"
        }
      ]
    }
  }
}
```

