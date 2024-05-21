# **Development environment setup**


## Prerequisites:

- Direnv and Pyenv installed in your system. Ensure shell hooks are installed before proceeding! Alternatives are possible, see below.

- Install python binaries with pyenv (see Install python binaries and poetry in Details section).

- Copy and .envrc.example in equivalent .envrc (which are NOT versioned as they may contain secrets).

- Run direnv allow (needed each time you modify .envrc).

- cd && cd - && poetry install



# **Details**

Install python binaries and poetry
Installation in one line: 

        export NEEDED_VER=`head -1 .python-version`
        mkdir /tmp/t ; cd /tmp/t ; pyenv install $NEEDED_VER ; pyenv local 3.12.1; pip install -U pip poetry
        
Explanation:
We user a temporary folder from where to:

1. install needed python version (whatever version needed from .python-version)
2. point to the newly installed binaries
3. Upgrade pip to latest version and install latest version of poetry
4. ONLY ONCE per system (not per binaries) set poetry to create virtualenvens in a local .venv folder: poetry config virtualenvs.in-project true


Now you should have a fully working environment

# **Sample Images:**

![Screenshot from 2024-05-21 18-33-45](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/4df99821-f604-4a8f-9ce0-36ec485ed0d8)
![Screenshot from 2024-05-21 18-33-53](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/ffcd9227-f416-4425-b65c-ae287d0737d7)
![Screenshot from 2024-05-21 18-33-31](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/edfb417f-b009-4742-99bd-8ece9e05f8c2)
![Screenshot from 2024-05-21 18-32-34](https://github.com/TaleeBarbieri/Django-To-Do/assets/115103838/fd3ab8f3-463f-4591-9c19-7678babafb96)
