# -*- coding: utf-8 -*-
"""
Задание 17.5

Создать сопрограмму (coroutine) configure_router. Сопрограмма подключается
по SSH (с помощью netdev) к устройству и выполняет перечень команд
в конфигурационном режиме на основании переданных аргументов.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, должно
генерироваться исключение ValueError с информацией о том, какая ошибка возникла,
при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command" на устройстве 192.168.100.1

Параметры функции:

* device - словарь с параметрами подключения к устройству
* config_commands - список команд или одна команда (строка), которые надо выполнить

Функция возвращает строку с результатами выполнения команды. Пример вызова функции:

In [7]: asyncio.run(configure_router(devices[0], 'sh clock'))
Out[7]: 'conf t\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#sh clock\n*07:55:25.233 UTC Wed Sep 30 2020\nR1(config)#'

In [8]: print(asyncio.run(configure_router(devices[0], 'sh clock')))
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#sh clock
*07:55:35.427 UTC Wed Sep 30 2020
R1(config)#


In [9]: asyncio.run(configure_router(devices[0], 'shclock'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-9-bc449d292363> in <module>
----> 1 asyncio.run(configure_router(devices[0], 'shclock'))
...
ValueError: Команда "shclock" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1



Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"

Запустить сопрограмму и проверить, что она работает корректно одним из устройств
в файле devices_netmiko.yaml.

При необходимости, можно использовать функции из предыдущих заданий
и создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

