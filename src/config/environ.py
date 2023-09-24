from pathlib import Path
import environ


env = environ.Env()
env_file_path = '/home/tab/Documents/To-Do-App/.env'
env.read_env(env_file_path)
