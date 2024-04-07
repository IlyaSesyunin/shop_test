
# Инкапсуляция
Самодокументируемость кода, а так же соблюдение принципов вроде DRY и KISS
позволяет избежать дублирования кода и упростить его поддержку.

# Объектный подход - абстракция
Класс - это абстракция, которая описывает поведение и состояние объекта.
Экземпляр - это конкретный объект, который создан на основе класса.

# Наследование
Наследование позволяет создавать новые классы на основе уже существующих.
Новый класс может расширять функциональность существующего, а так же переопределять его поведение.

# Полиморфизм
Полиморфизм позволяет использовать один и тот же интерфейс для разных типов объектов.


# Модули и классы
Файлы и папки в Python - это модули. 
Модули могут содержать в себе функции, классы, переменные и другие объекты.

# Для чего нужен self?
Ключевое слово self используется в методах класса для обращения к экземпляру класса, на котором вызывается метод. 
Это позволяет методу изменять свойства объекта и выполнять задачи, уникальные для конкретного экземпляра.

# Как используется __init__() в классе?
Используется для инициализации новых экземпляров класса. 
Он служит конструктором класса и вызывается автоматически при создании нового объекта. 
Этот метод позволяет устанавливать начальные значения атрибутов объекта и выполнять любую другую необходимую инициализацию.

# Что такое @classmethod?
Используется для превращения метода в классовый метод, который получает класс в качестве первого аргумента вместо экземпляра. 
Это позволяет методу работать с самим классом, а не с объектом класса.

# Что такое @staticmethod?
Используется для определения статического метода в классе. 
Статический метод привязан к классу, а не к объекту класса, и не получает неявный первый аргумент, который обычно является self. 
Это означает, что статический метод не может изменять состояние класса и не имеет доступа к атрибутам экземпляра класса.

# Что такое @property?
Используется для создания свойств в классе, что позволяет управлять доступом к атрибутам экземпляра. 
С его помощью можно определить методы в классе, которые можно вызывать как атрибуты без скобок. 
Это полезно для инкапсуляции, валидации и вычисления значений атрибутов.

# Зачем нужны дата-классы?
Дата-классы в Python предоставляют удобный способ для создания классов, которые в основном содержат данные. 
Они уменьшают количество шаблонного кода, необходимого для инициализации объектов, их представления и сравнения. 
С помощью декоратора @dataclass, Python автоматически добавляет специальные методы, такие как __init__() и __repr__(), что делает код более чистым и легко читаемым.

# Какие типы данных удобно использовать с Enum?
Строки, числа. Когда есть ограниченный набор значений.