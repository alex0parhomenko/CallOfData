# CallOfData
Hackaton 14.07.2018

Short APi

**Список папок**
http(s)://domain/api/v1/folders

**Добавить папку**
http(s)://domain/api/v1/folders/add
```json
folders = [
    { 
        "name": "Важное",
        "parent": "-1",
        /* user | archive | social | promotions | newsletters */
        "type": "user",
        "only_web": false
    }
]
```
**Очистить папку**
http(s)://domain/api/v1/folders/clear /* Список идентификаторов папок */
```json
ids= [
	"1"
]
```

**Редактировать папку**
http(s)://domain/api/v1/folders/edit
```json
folders = [
	{
		/* Идентификатор папки (string) */
		"id": "0",
		/* Имя папки (string) */
		"name": "Важное",
		/* Идентификатор родительской папки, -1 значит родительской папки нет (string) */ "parent": "-1",
		/* Тип папки. Создавать можно папки следующих типов: user | archive | social | promotions | newsletters */
		"type": "user",
		/* Отключен доступ для почтовых клиентов по POP3/IMAP (boolean) (если параметра нет, значит false) */
		"only_web": false,
		/* Токен сгенерированый методом генерации токенов может быть использован в место пароля от папки (Не обязательный) */
		"folder_access_token": "dsfafsadafsdfads
	}
]
```

**Удалить папку**
http(s)://domain/api/v1/folders/remove /* Список идентификаторов папок */
```json
ids= [
	"1"
]
```

**Список аттачей**
http(s)://domain/api/v1/messages/attaches /* ID письма */
id = 14389463440000000000
/* Email пользователя */
email = ozherelev@mail.ru
/* (Optional) отфильтровать аттачи только из списка типов (attach|link|cloud|cloud_stock) */ 
```json
attach_types = [
"attach"
]
```
**Поиск по вложениям**
http(s)://domain/api/v1/messages/attaches/search /* OPTIONAL Поисковый запрос (string) */
query = фото
/* OPTIONAL Папка (int) */
folder = 0
/* OPTIONAL Тип вложения (image|document|audio|video|other) */
type = image
/* OPTIONAL Искать только в скрытых вложениях (boolean) */
hidden_only = false
/* OPTIONAL Смещение (int) */
offset = 0
/* OPTIONAL Лимит (int) */
limit = 100
/* OPTIONAL Дополнительный размеры тамбнейлов (object) */
extra_thumbs = {"image": "137x59", "doc": "30x30"}
/* OPTIONAL Дополнительный размеры табнейлов (boolean) */
extra_thumbs_only = false
/* OPTIONAL Какие поля нужно исключить из ответа, доступно: thumbnails, href ([]string) */ 
```json
exclude = [
	"href"
]
```
/* OPTIONAL Вид сортировки (date) и направление (asc | desc) (object) */
```json
sort= {
	"type": "date",
	"order": "desc"
}
```

**Успешное получение письма**
http(s)://domain/api/v1/messages/message
/* Идентификатор письма (string) */
id = 12345
/* OPTIONAL Если поле передано и true, то сервер помечает письмо прочитанным. */ 
mark_read = true
/* OPTIONAL Если поле передано и true, то в body.body не передаётся поле text. */
only_html = false

**Перемещение писем**
http(s)://domain/api/v1/messages/move 
/* Идентификаторы писем для перемещения */
```json
ids= [
	"0", "1", "2"
]
```
/* Идентификатор папки, в которую переместить */
folder = 0


**Поиск писем**
http(s)://domain/api/v1/messages/search /* OPTIONAL Поисковый запрос (string) */
query = Пробка
/* Смещение в письмах */
offset = 0
/* Ограничение по количеству писем */
limit = 25
/* OPTIONAL Ограничение по длинне снипета в символах */ 
snippet_limit = 100
/* OPTIONAL Флаги (hash) */
```json
flags= {
	/* OPTIONAL Признак прочитанности (boolean) */
	"unread": true,
	/* OPTIONAL Помечанно флагом (boolean) */ 
	"flagged": true,
	/* OPTIONAL Содержит атачи (boolean) */ 
	"attach": true
}
```
/* OPTIONAL Заголовок письма (string) */
subject = Re: Api mail.ru
/* OPTIONAL Участники письма */
mPop/OAuth токен
```json
correspondents = { 
	/* От кого */
	"from": "Путин", 
	/* Кому */ 
	"to": "Обама"
}
```
/* OPTIONAL Транзакционная категория order|travel|finance|registration|event (string) */
transaction_category = order
/* OPTIONAL Отрезок времени, за который производить поиск */ 
```json
interval = {
	/* С (timestamp) */
	"from": 486849600,
	/* По (timestamp) */ "
	to": 1393444800
}
```