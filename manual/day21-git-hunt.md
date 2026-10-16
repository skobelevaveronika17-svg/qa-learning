# 1
$ git status
On branch main
Your branch is up to date with 'origin/main'.

# 2
$ git add .
$ git commit -m "fix"
[main 4c1e2a9] fix
 3 files changed, 41 insertions(+)
 create mode 100644 tests/test_login.py
 create mode 100644 .env
 create mode 100644 .idea/workspace.xml


# 3
$ git push
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:team/autotests.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally.

# 4
$ git push --force
+ 9b2f7d1...4c1e2a9 main -> main (forced update)

# 5 — позже, новая задача
$ git switch -c feature/cart-tests
Switched to a new branch 'feature/cart-tests'
$ git commit -am "cart tests"
$ git switch main
$ git merge feature/cart-tests
CONFLICT (content): Merge conflict in tests/conftest.py
Automatic merge failed; fix conflicts and then commit the result.
$ git add .
$ git commit -m "merge"

# 6 — содержимое tests/conftest.py после этого
BASE_URL = "https://stage.shop.ru"
<<<<<<< HEAD
TIMEOUT = 10
=======
TIMEOUT = 30
>>>>>>> feature/cart-tests
> 
блок 2 - Коммит прямо в main — блок 1 показал «On branch main» - В main попадает непроверенный код, без ревью. Сломать main — сломать работу всей команде - Сначала ветка: git switch -c feature/login-tests
пароль скорее всего в файле .env
блок 2 - В коммит попали .env и .idea/ - .env — файл с паролями и ключами, теперь он виден всем, у кого есть доступ, и остаётся в истории навсегда. .idea/ — личные настройки PyCharm, мешают другим - Добавить их в .gitignore. Перед коммитом — git status, а не вслепую git add. Пароль от стенда теперь надо менять
блок 3 - Сообщение коммита «fix» - Через месяц никто не поймёт, что исправлено и зачем - «Добавлены тесты формы входа: пустые поля и неверный пароль»
блок 3-4 - Git отказал в push: на сервере есть чужие коммиты. Олег сделал push --force - Force перезаписал main на сервере его версией. Чужие коммиты коллег пропали с сервера - Прочитать hint: git pull, решить конфликты, если будут, потом git push. Force в общую ветку — никогда
блок 5 - Git сообщил о конфликте, Олег сразу сделал add и commit - Конфликт не решён, а закоммичен как есть - Открыть файл, выбрать правильный вариант, удалить маркеры, потом add и commit
блок 6 - В conftest.py остались маркеры <<<<<<<, =======, >>>>>>> - Это не Python. Все тесты команды падают с ошибкой синтаксиса — следствие ошибки 5 - Оставить одну строку TIMEOUT = ... — какую именно, спросить у автора второй ветки, а не угадывать