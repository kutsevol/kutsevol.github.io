:title: Virtualenv in Python
:date: 2017-01-23
:modified: 2017-02-14
:author: Artur K.
:category: Development
:tags: virtualenv, python
:slug: virtualenv

.. figure:: /images/python-virtualenv.jpg
    :height: 400px
    :width: 750px
    :scale: 35%
    :align: left
    :alt: Python Virtualenv

----

Официальная документация по `Virtualenv <https://virtualenv.pypa.io/en/stable/>`_

**Virtualenv** - инструмент для создания изолированного окружения *Python*.
Это окружение можно использовать для проверки новых версий ваших программ, новых
версий пакетов, которые используются или просто в качестве песочницы для новых
пакетов. Кроме того, **virtualenv** можно использовать в качестве рабочего места в
случаях, если нет возможности копировать файлы в site-packages по какой-либо
причине.

**Virtualenv** решает ряд проблем:

- Создание новой изолированной среды для проекта *Python*;
- Возможность загрузки пакетов без привилегий  *admin/sudo*;
- Простая и быстрая упаковка приложения;
- Создание списка зависимостей одного проекта (с помощью *pip*);
- Быстрое восстановление зависимостей с помощью файла требований (с помощью *pip*);
- Портативность между системами.

=============
**Установка**
=============

Предварительно необходимо установить *pip* и *setuptools*.

Для **Python 3**:

.. code::

    sudo aptitude install python3-pip python3-setuptools

Для **Python 2**:

.. code::

    sudo aptitude install python-pip python-setuptools

Далее отличия будут только в *pip*. Для **Python 3** - *pip3*, для
**Python 2** - *pip*.
Далее рассмотрим на примере *pip3*.

Установка **virtualenv**:

.. code:: bash

    sudo pip3 install virtualenv

Для большего комфорта работы с *virtualenv* создано расширение, которое делает все
манипуляции с окруженем еще проще. Установка *virtualenvwrapper*:

.. code::

    sudo pip3 install virtualenvwrapper

В *~/.bashrc* дописываем:

.. code::

    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh

Создаем новое окружение:

.. code::

    mkvirtualenv env-name

Просмотреть список окружений:

.. code::

    workon

Поменять окружение:

.. code::

    workon env-name

Выход из окружения:

.. code::

    deactivate

Удалить окружение:

.. code::

    rmvirtualenv env-name

Находясь в одном из окружений, можно ставить пакеты через *pip*, как обычно.
Для примера выбран пакет - *flask*:

.. code::

    pip3 install flask

*Requirements.txt* - файл с описанием зависимостей, позволяет установить все
необходимые зависимости за один раз вот таким образом:

.. code::

    pip3 install -r requirements.txt


Создать такой файл можно следующим образом:

.. code::

    pip3 freeze > requirements.txt

----

P.S.
Иногда возникают ситуации, что необходимо использовать **virtualenv/virtualenvwrapper**
для разных веток (2.x и 3.x) *Python*.

Одно из простых решений - использовать `pyenv <{filename}pyenv.rst>`_.

----

======================
**Список источников:**
======================

- `Памятка по virtualenv и изолированным проектам на *Python* <http://eax.me/python-virtualenv/>`_
- `Python и окружение virtualenv <http://proft.me/2010/04/3/python-i-okruzhenie-virtualenv/>`_
