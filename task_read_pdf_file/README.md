## Task description:
Разработать метод, на вход которого подается PDF файл (сам файл предоставляется во вложении). Нужно прочитать всю возможную информацию из файла и на выходе вернуть в виде словаря.

Используя этот файл как эталон, разработать механизм, проверяющий входящие pdf-файлы на наличие всех элементов и соответствие структуры (расположение на листе). 

### Notes:
1. При сохранении информации в словарь, ключи не сохраняются в том порядке, в котором они были добавлены.
2. Для проверки наличия всех ключей и соответствия структуры в словаре, учитывая их порядок, можно использовать OrderedDict из модуля collections. Этот класс сохраняет порядок элементов таким, каким они были добавлены.
3. Значения после двоеточия считаются изменяемыми, поэтому для сравнения не используются.
4. Название фирмы является изменяемым, но местоположение в PDF-файле остается неизменным. Чтобы добавить название фирмы в значение, можно использовать ключ "company_name". Если требуется проверка наличия названия фирмы, можно использовать список всех фирм для проверки.