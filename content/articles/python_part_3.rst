:title: Python_Mutable
:date: 2017-05-28
:modified: 2017-05-28
:author: Artur K.
:category: Programming
:tags: python, linux
:slug: python_3
:status: draft

python tricks:
- enumerate
- zip
- x,y = y,x
- dict.get()
- for - else
- with
- try-except-else-finally


----

=======================================
**Ошибки во время выполнения программ**
=======================================

**Не работает функция print**

Пример кода:

.. code::

    print "Hello, world!"

Ошибка:

.. code::

    SyntaxError: invalid syntax

Решение:

Код написан для *python2*, а запускается в *python3*. Чтобы заработал в *python3*,
необходимо добавить скобки для функции *print*.
