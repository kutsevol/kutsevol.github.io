:title: Ansible Introduction. Part 2
:date: 2017-02-20
:modified: 2017-02-21
:author: Artur K.
:category: Administration
:tags: ansible, python, linux
:slug: ansible_cont

.. figure:: /images/ansible-header-2.jpg
    :height: 375px
    :width: 800px
    :scale: 75%
    :align: center
    :alt: Ansible

.. contents:: **Содержание**
   :depth: 3

----

В `предыдущей статье <{filename}ansible_introduction.rst>`_ рассмотрели основные
задачи и принципы работы, как работает **Ansible** его установка и настройка, а
также рассмотрели примеры простых задач, которые можно решать с помощью него.

=============================
**Управление конфигурациями**
=============================

--------------
**Playbooks**
--------------

Исполнение *Playbooks* - одна из основных задач **Ansible**. *Playbooks* содержат
списки задач. Каждая задача внутри **Ansible** использует кусок кода-модуля.
*Playbooks* описываются в формате *YAML*.

Чтобы выполнить сценарий используется команда ansible-playbook со следующим
синтаксисом:

.. code::

    ansible-playbook <имя_файла_сценария.yml> ... [другие параметры]

--------
**YAML**
--------

Для **Ansible** практически каждый *YAML* файл начинается со списка. Каждый
элемент списка - список пар "ключ-значение", часто называемая словарем.

Все *YAML* файлы должны начинаться с "---". Это часть формата *YAML* и означает
начало документа.

Все члены списка должны находится с одинаковым отступом от начала строки, и
должны начинаться с пробела или "-". Комментарии начинаются с "#".

Например:

.. code::

    ---
    # Message
    - Hosting
    – Cloud

Словарь представлен в виде "ключ" (двоеточие и пробел) "значение":

.. code::

    ---
    # Message
    site: site_test
    blog: blog_test

При необходимости словари могут быть представлены в сокращенной форме:

.. code::

    ---
    # Comment
    {site: site_test, blog: blog_test}

Можно указать логические значение (истина/ложь) так:

.. code::

    ---
    need_access: no
    use_service: yes
    file_conf: TRUE
    read_value: True
    kill_process: false

Целиком *YAML*-файл будет выглядеть так:

.. code::

    ---
    # About blog
    site: site_test
    blog: blog_test
    must_read: True
    themes:
        - hosting
        - cloud
        - it
        - geeks
    brands:
        - blog_test
        - blog_test_cloud

Для переменных **Ansible** используют "{{ var }}". Если значение после двоеточия
начинается с "{", то *YAML* будет думать, что это словарь.

Для использования переменных нужно заключить скобки в кавычки:

.. code::

    word: "{{ variable }}"

-----------------------
**Написание playbooks**
-----------------------

*Playbooks* может состоять из списка обсуживаемых серверов, переменных
пользователя, задач, обработчиков (handlers) и т.д. Большинство настроек
конфигурации можно переопределить в *playbook*. Каждый *playbook* состоит из одного
или более действий (игры) в списке.

Цель игры - связать группу хостов с предопределенными ролями, представленными
как вызов задач **Ansible**.

В качестве примера рассматривается процесс установки *nginx*.
Создадим директорию, где будут хранится *playbooks*:

.. code::

    mkdir ~/ansible/playbooks

Создадим файл *setup_nginx.yml* в директории *playbooks* со следующим содержанием:

.. code::

    ---
    - hosts: dbservers
      tasks:

      - name: Install nginx package
        apt: name=nginx update_cache=yes
        sudo: yes

      - name: Starting nginx service
        service: name=nginx state=started
        sudo: yes

Рассмотрим подробнее содержимое:

- **hosts:** Список хостов или группа, на которой вы запускаете задачу. Это поле обязательное и каждый *playbook* должен иметь его, за исключением ролей. Если указана хост-группа, сначала **Ansible** ее ищет в *playbook*, а затем в файле *inventory*. Узнать, на каких хостах будет происходить работа, можно командой: *ansible-playbook --list-host*, где – путь к вашему *playbook (playbooks/setup_nginx.yml)*.
- **tasks:** Задачи. Все *playbooks* содержат задачи. Задача — это список действий, которые вы хотите выполнить. Поле задачи содержит имя задачи (справочная информация о задаче для пользователя *playbook*), модуль, который должен быть выполнен и аргументы, требуемые для модуля. Параметр «name» опциональный, но рекомендуемый.

Также в сценарии перед непосредственным описанием задачи могут указыватся
следующие параметры или группы параметров:

- **gather_facts** - собирать или нет информацию о хостах перед выполнением задач, по умолчанию - да;
- **vars** - в нем указываются различные переменные, которые будут использованы при выполнении сценария;
- **connection** - можно указать метод соединения с хостами: *pure ssh*, *paramiko*, *fireball*, *chroot*, *jail*, *local*, *accelerate* (применимо также для выполнения отдельного модуля);
- **sudo** - после установления соединения выполнять задачу с привелегиями другого пользователя, по умолчанию другой пользователь - *root*;
- **sudo_user** - в сочетании с предыдущим параметром можно указать с привелегиями какого именно пользователя будет выполнена задача;
- **vars_prompt** - перед выполнением *playbook'a* **Ansible** в интерактивном режиме, может уточнить указанные в этом разделе параметры;
- **remote_user** (в предыдущих версиях - просто *user*) - имя пользователя для авторизации на удаленном хосте.

----------------
**Шаблонизация**
----------------

В **Ansible** используется шаблонизатор `Jinja2 <http://jinja.pocoo.org/>`_.

~~~~~~~~~~~~~~~~~~~~~
**Стандартные циклы**
~~~~~~~~~~~~~~~~~~~~~

Пример сценария в yml-файле:

.. code::

    ---
    - hosts: all
    user: ubuntu

    tasks:
    - name: Update apt cache
      apt: update_cache=yes
      sudo: yes

    - name: Install required packages
      apt: name={{ item }}
      sudo: yes
      with_items:
        - nginx
        - postgresql

Если необходимо установить несколько пакетов при этом с одинаковыми настройками
- используется шаблонизатор и параметр *with_items*. На каждой итерации *item* принимает
следующее значение, указанное в *with_items*.

Задача запускается один раз, но *apt* вызывается для всех указанных пакетов.
Можно так же использовать *with_items* как словарь вместо строк:

.. code::

    with_items:
    – {name: 'httpd', state: 'latest'}
    – {name: 'htop', state: 'absent'}

~~~~~~~~~~~~~~~~~~~
**Вложенные циклы**
~~~~~~~~~~~~~~~~~~~

Вложенные циклы полезны, когда необходимо выполнить несколько операций над
одним и тем же ресурсом. Например, если вы хотите предоставить доступ ко множеству
баз данных для пользователей MySQL.

.. code::

    ---
    - hosts: experiments
        remote_user: root
        tasks:
        - name: give users access to multiple databases
            mysql_user: name={{ item[0] }} priv={{ item[1]}}.*:ALL append_privs=yes password=pass login_user=root login_password=root
        with_nested:
        - ['alexey', 'alexander']
        - ['clientdb', 'providerdb']

В приведенном примере используется модуль mysql_user для установки прав на базы данных и
используем вложенные циклы с двумя спискми: список пользователей и список базы данных.
**Ansible** запустит модуль *mysql_user* для пользователей *alexey*, даст права
на все указанные во втором списке базы данных, затем запустит для пользователей
*alexander* и так же даст права.

~~~~~~~~~~~~~~~~~~~~~~~~~
**Циклы по подэлементам**
~~~~~~~~~~~~~~~~~~~~~~~~~

В предыдущем примере назначали все указанные БД всем указанным пользователям.
Но если для каждого пользователя нужно назначить свой специфический набор баз данных?
Для это нам нужны циклы по подэлементам.

.. code::

    ---
    - hosts: experiments
        remote_user: root
        vars:
        users:
            - name: alexey
              database:
              - clientdb
              - providerdb
            - name: alexander
              database:
              - providerdb
      tasks:
        – name: give users access to multiple databases
        mysql_user: name={{ item.0.name }} priv={{ item.1 }}.*:ALL append_privs=yes password=pass login_user=root login_password=root
        with_subelements:
        - users
        - database

Cоздали словари, которые состоят из имен пользователей и имен баз данных.
Вместо добавления данных пользователей в *playbook* можно вынести их в отдельный
файл переменных и включить в *playbook*. **Ansible** пройдется по словарю используя
переменную *item*. **Ansible** назначает численные значения ключам, представленным
конструкцией *with_subelements*, начиная с 0. В словаре 0 имя — пара «ключ-значения»,
поэтому для обращения по имени пользователя мы используем item.0.name.
*Dictionary* — простой список, поэтому для обращения используем item.1.

---------------------------------
**Обработчик событий (Handlers)**
---------------------------------

**Ansible** не просто выполняет задачи в указанном порядке, но и проверяет их
состояние на наличие изменений. Если при выполнении сценария требовалось,
например, добавить строку в конфигурационный файл, и в результате выполнения
он изменился (необходимой строки действительно не было), то **Ansible** может
выполнить специальную задачу, описанную как обработчик события (*handler*).
Если при выполнении строка уже была в конфигурационном файле, то обработчик
выполнен не будет. Обработчики событий описываются в конце сценария; в описании
задачи они указываются через параметр *notify*.

Пример:

.. code:: yaml

    ---
    - hosts: webservers
      vars:
        max_clients: 200

    tasks:
      # сгенерируем файл конфигурации на основе шаблона
      # и укажем, что требуется выполнить задачу “restart apache”
      # если файл изменился
    - name: write the apache config file
      template: src=/srv/httpd.j2 dest=/etc/httpd.conf
      notify:
      - restart apache

    - name: ensure apache is running
      service: name=httpd state=started

    # раздел описания обработчиков
    handlers:
      - name: restart apache
        # используем модуль service для перезапуска веб-сервера
        service: name=httpd state=restarted

-----------------------
**Контроль выполнения**
-----------------------

Допустим, что при выполнении сценария нам нужно проверять определённые
переменные или состояния и, в зависимости от них, выполнять или не выполнять
какие-либо задачи. Для этого можно использовать оператор *“when”*:

.. code::

    tasks:
      # сохраняем файл шаблона и сохраняем результат задачи
      # в переменную last_result
    - template: src=/templates/foo.j2 dest=/etc/foo.conf
      register: last_result
      # проверяем переменную last_result.changed и если она имеет
      # значение true - задача будет выполнена, иначе - будет пропущена
    - command: echo 'the file has changed'
      when: last_result.changed

.. code::

    ---
    - hosts: experiments
        remote_user: root
        tasks:

        - name: Testing user sudo privilege
            command: /usr/bin/sudo -v
            register: sudo_response
            ignore_errors: yes

        - name: Stop if Users doesn`t have sudo privilege
            fail: msg="User doesn`t have sudo privilege"
            when: sudo_response.rc == 1

В примере выше запускаем команду на сервере */usr/bin/sudo -v* и сохранили ее вывод
в переменную через *register*. В переменной был захвачен вывод *stdout* и *stderr*
(rc, return code). Во второй задаче проверяем *return code* переменной и если ошибка возникла -
должны завершить исполнение *playbook* c выводом сообщения.

Для сравнения в условиях в **Ansible** можно использовать **==** (равно), **!=** (не равно),
**>** (больше), **<** (меньше), **>=** (больше равно), **<=** (меньше равно).

Если необходимо проверить, есть ли в переменной символ или строка, используйте операторы **in** и **not**.

.. code::

    - name: Querying rpm list for httpd package
        shell: rpm -qa | grep httpd
        register: httpd_rpm

    - name: Check if httpd rpm is installed on the remote host
        debug: msg="httpd is installed on the remote host"
        when: "'httpd-2.2.27–1.2.x86_64' in httpd_rpm.stdout"

    – name: Check if httpd rpm is not installed on the remote host
        debug: msg="httpd is not installed on the remote host"
        when: not 'httpd-2.2.27.1.2.x86_64' in httpd_rpm.stdout

Можно задавать несколько условий, используя операторы **and** (и) и **or** (или).

.. code::

    – name: Check if httpd rpm is installed on the remote host
        debug: msg="httpd is installed on the remote host"
        when: "'httpd-2.2.27–1.2.x86_64' in httpd_rpm.stdout and
        'httpd-tools-2.2.27–1.2.x86–64' in httpd_rpm.stdout"

Также можно проверить логическое значение переменной. Давайте сделаем *backup*,
если в переменной backup установлено *true*:

.. code::

    – name: Rsync
        shell: /usr/bin/rsync -ra /home /backup/{{ inventory_hostname }}
        sudo: yes
        when: backup

Ansible позволяет в условии использовать информацию о том, была ли уже определена
переменная. Для этого используйте *when*: *var is not define* (где *var* — имя переменной, *is not define* – еще не была определена, *is defined* – уже была определена).

--------------------------------------
**Делегирование задачи другому хосту**
--------------------------------------

Иногда требуется выполнить задачу на определённом узле, но в контексте другого
узла. Например, во время обновления узла может возникнуть необходимость отключить
для него мониторинг, находящийся на отдельном сервере. Для этого используется
управляющая директива *delegate_to*. Приведём пример:

.. code::

    - name: disable nagios alerts for this host webserver service
    nagios: action=disable_alerts host={{inventory_hostname}} services=dnsserver
    delegate_to: mon_host.example.com

Результатом выполнения этой задачи будет отключение сообщений для сервиса
dnsserver в Nagios.

-----------
**Отладка**
-----------

При запуске *playbook* можно увидеть примерно следующий вывод в терминале:

.. figure:: /images/ansible-playbook.jpg
    :height: 836px
    :width: 1000px
    :scale: 75%
    :align: center
    :alt: Ansible playbook

**Gathering facts** - это первая задача по умолчанию в любом playbook. Задача
собирает полезные метаданные о серверах в форме переменных, которые могут
использоваться в *playbook* в дальнейшем. Например, такими переменными могут быть
*ip-адрес*, архитектура OC и имя хоста.

Можно посмотреть эти переменные, используя команду:

.. code::

    ansible -m setup experiments

где experiments - название секции в вашем *inventory*.

Или записать все в файл:

.. code::

    ansible -m setup experiments >> facts

Ниже в выводе указаны задачи **TASK**, согласно ходу выполнения plyabook:
установка nginx, запуск сервиса.

Одно из ключевых свойств систем **Ansible**: **Идемпотентность** (операция, которая
если применяется к любому значению несколько раз - всегда получается то же значение,
как и при однократном применении). Большинство систем управления конфигурациями
следуют этому принципу и применяют его на инфраструктуру.

Секция **PLAY RECAP** ниже в выводе. Параметр **changed** показывает, сколько раз
в задачах менялось состояние сервера. **ok** - количество исполняемых задач вместе
с **Gathering facts**.

Для исправления ошибок при исполнении *playbook* - есть 3 уровня вывода отладочной
информации (verbose):

**-v** вывод базовой информации:

.. code::

    ansible-playbook playbooks/setup_nginx.yml -v

**-vv** более подробный вывод:

.. code::

    ansible-playbook playbooks/setup_nginx.yml -vv

**-vvv** самый подробный вывод. В этом выводе указаны SSH-команды, которые
**Ansible** использует для создания временных файлов на удаленном хосте для запуска
скрипта удаленно.

.. code::

    ansible-playbook playbooks/setup_nginx.yml -vvv

Можно выводить любые переменные **Ansible** для отладки. Для этого необходимо добавить
в *playbok* следующую секцию:

.. code::

    - name: Debug
        debug: msg={{ ansible_distribution }}

При запуске *playbook* вы увидите вывод этой переменной. Каждая переменная
**Ansible** начинается с префикса **ansible_**.

.. figure:: /images/ansible-debug-variable.jpg
    :height: 480px
    :width: 1000px
    :scale: 75%
    :align: center
    :alt: Ansible debug variable

Для того чтобы посмотреть на все задачи, выполняющиеся в *playbook*. Она
особенно полезна, когда есть несколько *playbook*, исполняющих другие *playbook*.

.. code::

    ansible-playbook playbooks/setup_nginx.yml --list-tasks

.. figure:: /images/ansible-list-tasks.jpg
    :height: 334px
    :width: 1000px
    :scale: 75%
    :align: center
    :alt: Ansible list tasks

Можно исполнить конкретную задачу из *playbook*:

.. code::

    ansible-playbook playbooks/setup_nginx.yml --start-at-task="Debug"

.. figure:: /images/ansible-run-once-task.jpg
    :height: 570px
    :width: 1000px
    :scale: 75%
    :align: center
    :alt: Ansible run once task

====================================
**Повторное использование playbook**
====================================

Если задача или набор задач часто используется - есть смысл оформить ее в виде
отдельного файла, который можно будет использовать в других *playbook*.

Создадим директорию для повторно используемых задач:

.. code::

    mkdir ~/ansible/playbooks/tasks

Создадим задачу обновления ОС в файле ~/ansible/playbooks/tasks/**os_update.yml**:

.. code::

    ---
    # Update and upgrade apt-based linux
    - name: Update and upgrade apt-based Linux
        apt: update-cache=yes state=latest
        sudo: yes

Теперь можно включить секцию обновления ОС в ~/ansible/playbooks/**setup_nginx.yml**:

.. code::

    ---
    - hosts: experiments
        remote_user: root
        tasks:

        - include: tasks/os_update.yml

        - name: Install nginx package
            apt: name=nginx update_cache=yes
            sudo: yes

        - name: Starting nginx service
            service: name=nginx state=started
            sudo: yes

Теперь до установки *nginx* *Ubuntu* на обслуживаемых серверах из *Inventory* будет обновлена.
Стоит и установку *nginx* (~/ansible/playbooks/tasks/**pkg_nginx_install.yml**)
вынести в отдельную задачу, если часто устанавливаете *nginx*.

.. code::

    ---
    # Install NGINX package
        - name: Install nginx package
            apt: name=nginx update_cache=yes
            sudo: yes

        - name: Starting nginx service
            service: name=nginx state=started
            sudo: yes

В результате наш playbook станет совсем простым:

.. code::

    ---
        - hosts: experiments
            remote_user: root
            tasks:

            - include: tasks/os_update.yml
            - include: tasks/pkg_nginx_install.yml

=====================
**Список источников**
=====================

- Официальная документация по `Ansible <http://docs.ansible.com/ansible/index.html>`_
- `Система управления Ansible <https://habrahabr.ru/company/selectel/blog/196620/>`_
- `Ansible - давайте попробуем <https://habrahabr.ru/company/express42/blog/254959/>`_
- `Администрирование Ansible <https://habrahabr.ru/post/195048/>`_
- `Автоматизируем и ускоряем процесс настройки облачных серверов с Ansible. Часть 1: Введение <https://habrahabr.ru/company/infobox/blog/249143/>`_
- `Автоматизируем и ускоряем процесс настройки облачных серверов с Ansible. Часть 2: вывод, отладка, и повторное использование playbook <https://habrahabr.ru/company/infobox/blog/250115/>`_
