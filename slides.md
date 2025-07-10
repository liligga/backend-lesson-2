---
theme: seriph
background: https://cover.sli.dev
title: Урок 2
---

# Добро пожаловать

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