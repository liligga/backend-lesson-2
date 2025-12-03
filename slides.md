---
theme: seriph
background: https://cover.sli.dev
title: Урок 2
---

# Добро пожаловать

---

# GIT

## Основные команды

<v-clicks depth="3">

- один раз на компьютере для всех проектов
  - `git config --global user.name "Your Name"` - установить имя пользователя(для всех проектов, автор проектов)
  - `git config --global user.email "Your Email"` - установить электронную почту пользователя(для всех проектов, email автора проектов)
- каждый раз при создании нового проекта, **один** раз в проекте
  - `git init` - создать репозиторий
  - `git remote add origin https://github.com/username/repo.git` - добавить удалённый репозиторий(на сайте github)
  
</v-clicks>

---

 # GIT

## Основные команды
<v-clicks depth="3">

- в репозитории в любой момент
  - `git status` - проверить состояние репозитория, какие файлы были изменены, какие файлы еще не отслеживаются
  - `git add .` - добавить все изменения(со всех файлов)
  - `git add lesson1.py lesson2.py lesson3.py` - добавить изменения в конкретный файл
  - `git commit -m "commit message"` - создать коммит, сохранить изменения(со всех файлов), сделать checkpoint
    - `-m` - (message): сообщение(описание) коммита
  - `git push` - отправить изменения в удалённый репозиторий(сайт github)

</v-clicks>

---
layout: two-cols
---

# GIT

### При выполнении ДЗ №2

<v-clicks depth="2">

- создать репозиторий на сайте github.com(**один раз** для проекта)
- создать репозиторий на компьютере(**один раз** для проекта)
  - `git init`
  - `git remote add origin https://github.com/username/repo.git`
    - эта ссылка будет при создании репозитория на github.com, username - имя пользователя на github.com, repo - название репозитория

</v-clicks>

::right::
### При выполнении всех ДЗ
<v-clicks depth="2">

- сделать ДЗ(файл `homework_X.py`)
  - в нем напишите python код
- проверить состояние репозитория
  - `git status`
- добавить изменения
  - `git add .`
- создать коммит
  - `git commit -m "First commit"`
- отправить изменения на github
  - `git push origin main`

</v-clicks>

---

## Принципы ООП

- Наследование(это основной принцип)
- Полиморфизм
- Инкапсуляция
- Абстракция

---

## Наследование

Наследование — это механизм, позволяющий создать новый класс на основе существующего (родительского) класса. Новый класс наследует **свойства** и **методы** родительского класса, что позволяет уменьшить дублирование кода и упрощает его модификацию. 

```python
class Car:
  def drive(self):
    print("Driving ...")

class Bus(Car):
  pass

bus = Bus()
bus.drive() # Driving ...
```

Класс `Car` является **родительским** классом, **суперклассом**, а класс `Bus` является **потомком**, **дочерним**, **подклассом** класса `Car`.

---

## Наследование

При наследовании классов в Python иногда используют `super()` для вызова родительского метода. Часто это используется в методе `__init__` для инициализации родительского класса.

```python
class Car:
  def __init__(self, model):
    self.model = model

class Bus(Car):
  def __init__(self, model, seats):
    super().__init__(model)
    self.seats = seats

bus = Bus("Toyota", 30)
print("Модель автобуса:", bus.model) # Toyota
print("Количество мест в автобусе:", bus.seats) # 30
```
---

## Наследование

В Python используют `type()` для определения класса объекта, но `type()` не учитывает наследование. Также `isinstance()` может показать, является ли объект экземпляром определенного класса или подкласса.

```python
class Car:
  pass

class Bus(Car):
  pass

car = Car()
bus = Bus()

print(type(car)) # <class '__main__.Car'>
print(type(bus)) # <class '__main__.Bus'>
print(isinstance(car, Car)) # True - да, это экземпляр Car
print(isinstance(bus, Car)) # True - да, это экземпляр подкласса Car
print(isinstance(bus, Bus)) # True - да, это экземпляр Bus
```

---
layout: two-cols
---

## Полиморфизм

Полиморфизм — это способность объектов разных классов реагировать на одинаковые сообщения (методы) по-разному. Это позволяет использовать один и тот же интерфейс для различных базовых форм (типов) данных. В Python полиморфизм реализуется через переопределение методов в подклассах.

Каждый объект в списке cars имеет свой метод drive(), но он вызывается в разных контекстах и выполняет различные действия.
::right::

```python
class Car:
  def drive(self):
    print("Driving")

class Bus(Car):
  def drive(self):
    print("Driving a bus")

class Truck(Car):
  def drive(self):
    print("Driving a truck")

cars = [Car(), Bus(), Truck()]
for car in cars:
  car.drive() 
# Driving, Driving a bus, Driving a truck
```

---

## GIT

Порядок выполнения действий и команд в проекте:

1. `git init` - инициализация репозитория
2. создание и заполнения `.gitignore`. Если этот шаг пропустить или выполнить позже, лишние файлы будут добавлены в репозиторий
3. `git add .` - добавление изменений(любых)
4. `git commit -m "commit message"` - сохранение изменений, коммит
5. `git push` - отправка изменений на github

---