# CallOfData
Hackaton 14.07.2018

Short API<br/>

**Список папок**<br/>
http(s)://domain/api/v1/folders<br/>

**Добавить папку**<br/>
http(s)://domain/api/v1/folders/add<br/>
```javascript
folders = [
    { 
        "name": "Важное",
        "parent": "-1",
        "type": "user", //user | archive | social | promotions | newsletters 
        "only_web": false
    }
]
```
**Очистить папку**<br/>
http(s)://domain/api/v1/folders/clear Список идентификаторов папок <br/>
```javascript
ids= [
	"1"
]
```

**Редактировать папку**<br/>
http(s)://domain/api/v1/folders/edit<br/>

```javascript
folders = [
	{
		 //Идентификатор папки (string) 
		"id": "0",
		 Имя папки (string) 
		"name": "Важное",
		 Идентификатор родительской папки, -1 значит родительской папки нет (string)  "parent": "-1",
		 Тип папки. Создавать можно папки следующих типов: user | archive | social | promotions | newsletters 
		"type": "user",
		 Отключен доступ для почтовых клиентов по POP3/IMAP (boolean) (если параметра нет, значит false) 
		"only_web": false,
		 Токен сгенерированый методом генерации токенов может быть использован в место пароля от папки (Не обязательный) 
		"folder_access_token": "dsfafsadafsdfads
	}
]
```

**Удалить папку**<br/>
http(s)://domain/api/v1/folders/remove Список идентификаторов папок<br/>
```javascript
ids= [
	"1"
]
```

**Список аттачей**<br/>
http(s)://domain/api/v1/messages/attaches ID письма <br/>
id = 14389463440000000000<br/>
Email пользователя <br/>
email = ozherelev@mail.ru<br/>
(Optional) отфильтровать аттачи только из списка типов (attach|link|cloud|cloud_stock) <br/>
```javascript
attach_types = [
"attach"
]
```
**Поиск по вложениям**<br/>
http(s)://domain/api/v1/messages/attaches/search  OPTIONAL Поисковый запрос (string) <br/>
query = фото<br/>
OPTIONAL Папка (int)<br/>
folder = 0<br/>
 OPTIONAL Тип вложения (image|document|audio|video|other) <br/>
type = image<br/>
 OPTIONAL Искать только в скрытых вложениях (boolean) <br/>
hidden_only = false<br/>
 OPTIONAL Смещение (int) <br/>
offset = 0<br/>
 OPTIONAL Лимит (int) <br/>
limit = 100<br/>
 OPTIONAL Дополнительный размеры тамбнейлов (object) <br/>
extra_thumbs = {"image": "137x59", "doc": "30x30"}<br/>
 OPTIONAL Дополнительный размеры табнейлов (boolean) <br/>
extra_thumbs_only = false<br/>
 OPTIONAL Какие поля нужно исключить из ответа, доступно: thumbnails, href ([]string)  <br/>
```javascript
exclude = [
	"href"
]
```
 OPTIONAL Вид сортировки (date) и направление (asc | desc) (object) <br/>
```javascript
sort= {
	"type": "date",
	"order": "desc"
}
```

**Успешное получение письма**<br/>
http(s)://domain/api/v1/messages/message<br/>
 Идентификатор письма (string) <br/>
id = 12345<br/>
 OPTIONAL Если поле передано и true, то сервер помечает письмо прочитанным.  <br/>
mark_read = true<br/>
 OPTIONAL Если поле передано и true, то в body.body не передаётся поле text. <br/>
only_html = false<br/>

**Перемещение писем**
http(s)://domain/api/v1/messages/move <br/>
 Идентификаторы писем для перемещения <br/>
```javascript
ids= [
	"0", "1", "2"
]
```
 Идентификатор папки, в которую переместить <br/>
folder = 0<br/>


**Поиск писем**<br/>
http(s)://domain/api/v1/messages/search  OPTIONAL Поисковый запрос (string) <br/>
query = Пробка<br/>
 Смещение в письмах <br/>
offset = 0<br/>
 Ограничение по количеству писем <br/>
limit = 25<br/>
 OPTIONAL Ограничение по длинне снипета в символах  <br/>
snippet_limit = 100<br/>
 OPTIONAL Флаги (hash) <br/>
```javascript
flags= {
	 OPTIONAL Признак прочитанности (boolean) 
	"unread": true,
	 OPTIONAL Помечанно флагом (boolean)  
	"flagged": true,
	 OPTIONAL Содержит атачи (boolean)  
	"attach": true
}
```
 OPTIONAL Заголовок письма (string) <br/>
subject = Re: Api mail.ru<br/>
 OPTIONAL Участники письма <br/>
mPop/OAuth токен<br/>
```javascript
correspondents = { 
	 От кого 
	"from": "Путин", 
	 Кому  
	"to": "Обама"
}
```
 OPTIONAL Транзакционная категория order|travel|finance|registration|event (string) <br/>
transaction_category = order<br/>
 OPTIONAL Отрезок времени, за который производить поиск <br/>
```javascript
interval = {
	 С (timestamp) 
	"from": 486849600,
	 По (timestamp)  "
	to": 1393444800
}
```