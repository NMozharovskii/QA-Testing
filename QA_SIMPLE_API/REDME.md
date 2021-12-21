## **Приложение для работы с API и тестирование этого приложение**

### **Раздел№1. Функции работы с API**
В это разделе я предоставлю краткое описание созданных функций и скриншоты иллюстрирующие их работу.

GET_api_key

Используя почту и пароль с которыми я регистрировался на сайте, 
отправляем запрос для получения ключа(используем метод GET). 
Этот этап необходимо провести прежде всех остальных, 
поскольку дальнейшая работа требует ключ.

![image](https://user-images.githubusercontent.com/90044616/146928091-5670af5d-44a8-49d9-8925-2c8b25fe05fa.png)


POST_pet_simple

Используя метод POST отправляем запрос на создание карточки животного по указанным параметрам **(без изображени)я**.

![image](https://sun9-69.userapi.com/impg/afD5gpswYfFIXJXo-m5ez0I5A2GJypW43aXgVg/T6NLkCeLF2c.jpg?size=843x181&quality=96&sign=47f4754548e3766f02a73caff8c91feb&type=album)
![image](https://sun9-86.userapi.com/impg/nMBNAwsj96yPkgOIvKJy1B1_X7weChN98lDMWQ/yXep_dB6xJE.jpg?size=649x182&quality=96&sign=0cf9544ab443d6a5ffbf758b08bff2fd&type=album)

GET_pet_list

Снова используем метод GET и получаем данные по созданным карточкам. Отсюда вытаскиваем **id**, который понадобится 
для внесения правок в карточку.

![image](https://sun9-68.userapi.com/impg/o23C5RTgX9MqemnX3rH2PrHHFhY7TDw9Jo1W7w/LLeNQV4EQus.jpg?size=1149x192&quality=96&sign=54e5b3da0208c621f69802a078613bf5&type=album)

POST_new_pet

Используя метод POST отправляем запрос на создание карточки животного по указанным параметрам **(с изображение)**.

![image](https://sun9-24.userapi.com/impg/I1CMODNytg4s-2fp4yZliZPUTbMbHKRqvvWL0g/Zoc7lLUdNUE.jpg?size=1280x238&quality=96&sign=25da206725e1bfee3ef177957b83fc5a&type=album)
![image](https://sun9-9.userapi.com/impg/WtvyM_TxkCKEUdfkNx0z8raGaA8g8O7-UjXs0A/dutG78CyqKI.jpg?size=663x187&quality=96&sign=08be50bc096a41585bbb3c7f6c014da2&type=album)

PUT_pet_info

Используя метод PUT мы можем внести изменения в карточку, что мы и делаем, используя тот самый **id**, 
который я упоминал ранее. А так же получаем данные по конкретной карточке.

![image](https://sun9-22.userapi.com/impg/IUxKK7W12aQyc67YuQYE_A8PgLs80jCuJ5Lu9g/6VXV3pc24DU.jpg?size=1062x208&quality=96&sign=a57d6958e9cc5325d4e976968bb00090&type=album)
![image](https://sun9-65.userapi.com/impg/gBFe5SZ7snEhRyimfBmprIVMq530r-xEtjYxLg/rRf1DEMP45Y.jpg?size=662x102&quality=96&sign=7050efe22f18d4c8c5528df15a7816bf&type=album)

DELETE_pet

Используем метод DELETE и удаляем карточку по ее **id**.

![image](https://sun9-34.userapi.com/impg/vuIa2pUDpwSu05_wx9uErID_i9s73MTsHjE0hQ/Bn7rH3v_lLA.jpg?size=808x187&quality=96&sign=731aea0bcbcebabf684b264949ff346c&type=album)
![image](https://sun9-86.userapi.com/impg/nMBNAwsj96yPkgOIvKJy1B1_X7weChN98lDMWQ/yXep_dB6xJE.jpg?size=649x182&quality=96&sign=0cf9544ab443d6a5ffbf758b08bff2fd&type=album)

### **Раздел№2. Тестирование**

В этом разделе я опишу как происходил процесс тестирования созданного приложения и само написание тестов.

Сам код, посвященный тестированию, я бы разделил на три части: **Задание параметров, Фикстуры и, разумеется, 
сами тесты**.

Начнем с начала. Я задал все необходимые параметры, ссылка, констаты, id, то есть данные для тестирования. 
Функции создания карточек: POST_pet_simple и POST_new_pet, создаются по данным отличным от тех, 
что использовались в самом приложении, 
а остальные используют данные уже созданных карточек. Это обусловлено необходимостью получения id для работы с ними. 

Следующим этапом стало создание фикстур для каждой из используемых функций. Фактически они представляют собой немного 
измененные изначальные функции.
Они возвращают **True** при статус коде равном 200 или **OK**, 
по которым далее будет проводиться проверка корректности выполнения.

Сами тесты реализованны через проверку соответствия результата работы функции, ожидаемому результату **True**. 
Тесты также параметризированны, 
что дает возможность изменять тестовые данные не дублируя код теста.

На скриншоте представлено успешное выполнение всех тестов.

![image](https://sun9-15.userapi.com/impg/4mxCFHjqUy7m1-Uw_XW03F0G7hPKn7hJ2MPajg/FeFxT0eKNxs.jpg?size=1070x528&quality=96&sign=f6ccdfea248ca950b7c2373e8fc29a00&type=album)




