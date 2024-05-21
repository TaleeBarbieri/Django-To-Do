Development environment setup


Prerequisites

direnv and pyenv installed in your system. Ensure shell hooks are installed before proceeding! Alternatives are possible, see below.

Install python binaries with pyenv (see Install python binaries and poetry in Details section).
Create an empty postgres database (eg. "krm3").
Copy .env.example and .envrc.example in equivalent .env and .envrc (which are NOT versioned as they may contain secrets).
Amend local .env (and .envrc as needed). Most importantly set the KRM3_DATABASE_URL pointing to you database.
Run direnv allow (needed each time you modify .envrc or you want to reload the .env).
cd && cd - && poetry install



Now you should have a fully working environment

![Screenshot from 2024-05-21 18-33-45](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/4df99821-f604-4a8f-9ce0-36ec485ed0d8)
![Screenshot from 2024-05-21 18-33-53](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/ffcd9227-f416-4425-b65c-ae287d0737d7)
![Screenshot from 2024-05-21 18-33-31](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/edfb417f-b009-4742-99bd-8ece9e05f8c2)
![Screenshot from 2024-05-21 18-32-34](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/fd3ab8f3-463f-4591-9c19-7678babafb96)
