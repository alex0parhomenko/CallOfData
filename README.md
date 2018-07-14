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
		"id": "0",//Идентификатор папки (string) 
		"name": "Важное", //Имя папки (string) 
		 // Идентификатор родительской папки, -1 значит родительской папки нет (string)  "parent": "-1",
		 // Тип папки. Создавать можно папки следующих типов: user | archive | social | promotions | newsletters 
		"type": "user",
		 //Отключен доступ для почтовых клиентов по POP3/IMAP (boolean) (если параметра нет, значит false) 
		"only_web": false,
		 // Токен сгенерированый методом генерации токенов может быть использован в место пароля от папки (Не обязательный) 
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
email = ozherelev@mail.ru Email пользователя <br/>
(Optional) отфильтровать аттачи только из списка типов (attach|link|cloud|cloud_stock) <br/>
```javascript
attach_types = [
"attach"
]
```
**Поиск по вложениям**<br/>
http(s)://domain/api/v1/messages/attaches/search  
query = фото OPTIONAL Поисковый запрос (string) <br/><br/>
folder =  0 OPTIONAL Папка (int)<br/>
type = image OPTIONAL Тип вложения (image|document|audio|video|other)<br/>
hidden_only = false OPTIONAL Искать только в скрытых вложениях (boolean)<br/>
offset = 0 OPTIONAL Смещение (int)<br/>
limit = 100 OPTIONAL Лимит (int) <br/>
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
```javascript
//  OPTIONAL Вид сортировки (date) и направление (asc | desc) (object) <br/>
sort= {
	"type": "date",
	"order": "desc"
}
```

**Успешное получение письма**<br/>
http(s)://domain/api/v1/messages/message<br/>
id = 12345 Идентификатор письма (string) <br/>
mark_read = true OPTIONAL Если поле передано и true, то сервер помечает письмо прочитанным.  <br/>
only_html = false OPTIONAL Если поле передано и true, то в body.body не передаётся поле text. <br/>

**Перемещение писем**
http(s)://domain/api/v1/messages/move <br/>
```javascript
// Идентификаторы писем для перемещения <br/>
ids= [
	"0", "1", "2"
]
```
folder = 0 Идентификатор папки, в которую переместить <br/>


**Поиск писем**<br/>
http(s)://domain/api/v1/messages/search  
query = Пробка OPTIONAL Поисковый запрос (string) <br/>
offset = 0 Смещение в письмах <br/>
limit = 25 Ограничение по количеству писем <br/>
snippet_limit = 100 OPTIONAL Ограничение по длинне снипета в символах  <br/>
```javascript
// OPTIONAL Флаги (hash) <br/>
flags= {
	 OPTIONAL Признак прочитанности (boolean) 
	"unread": true,
	 OPTIONAL Помечанно флагом (boolean)  
	"flagged": true,
	 OPTIONAL Содержит атачи (boolean)  
	"attach": true
}
```
subject = Re: Api mail.ru OPTIONAL Заголовок письма (string) <br/>
```javascript
//OPTIONAL Участники письма <br/>
correspondents = { 
	 От кого 
	"from": "Путин", 
	 Кому  
	"to": "Обама"
}
```
transaction_category = order OPTIONAL Транзакционная категория order|travel|finance|registration|event (string) <br/>
```javascript
//OPTIONAL Отрезок времени, за который производить поиск <br/>
interval = {
	 С (timestamp) 
	"from": 486849600,
	 По (timestamp)  "
	to": 1393444800
}
```