:title: Pyenv. Python manager version
:date: 2017-04-07
:modified: 2017-04-21
:author: Artur K.
:category: Development
:tags: virtualenv, python, pyenv
:slug: pyenv

.. figure:: /images/python-pyenv.jpg
    :height: 180px
    :width: 180px
    :scale: 100%
    :align: left
    :alt: Pyenv

----

**Pyenv** lets you easily switch between multiple versions of Python. It's simple,
unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

Сегодня речь пойдет о таком инструменте, как - `Pyenv <https://github.com/pyenv/pyenv>`_.
Данный скрипт удобный менеджер версий для языка **Python**.

**Pyenv** можно установить либо вручную, либо используя `автоматический скрипт <https://github.com/pyenv/pyenv-installer>`_ от
того же автора.

Рассмотрим автоматическую установку.

.. code::

    curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

После этого появится сообщение о том, что необходимо добавить следующие строки
кода в *.profile* / *.bash_profile* / *.bashrc* для того, чтобы автоматически обнаруживать **Pyenv**.

.. code::

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

Перед тем как устанавливать определенную версию **Python**, необходимо
предварительно установить все зависимости:

.. code::

    sudo apt-get install build-essential python-dev libreadline-dev
    libbz2-dev libssl-dev libsqlite3-dev libxslt1-dev libxml2-dev git

Для того, чтобы установить определенную версию **Python** необходимо выполнить
следующие команды:

.. code::

    pyenv install 2.7.11

Для просмотра всех установленных версий **Python** необходимо:

.. code::

    pyenv versions

Чтобы переключиться на версию:

.. code::

    pyenv local 2.7.11

Создаем отдельное виртуальное окружение **Python** 2.7.11 и переключаемся на него:

.. code::

    pyenv virtualenv 2.7.11 virtual_env_name

    Активировать виртуальное окружение (необходимо выполнять в директории проекта
    для которого создано виртуальное окружение):
    pyenv local virtual_env_name

После выполнения команды *python local* в директории, где была выполнена команда - создается файл
*.python-version*. Используется для "трекинга" версий **Python**.

Удаление виртуального окружения осуществляется следующей командой:

.. code::

    pyenv uninstall virtual_env_name

Список команд **pyenv** можно увидеть следующим образом:

.. code::

    pyenv commands

Мануал по каждой команде:

.. code::

    pyenv local --help

----

======================
**Список источников:**
======================

- `Менеджер версий Python <https://habrahabr.ru/post/203516/>`_
- `Pyenv: удобный менеджер версий Python <https://khashtamov.com/2015/12/pyenv-python/>`_
