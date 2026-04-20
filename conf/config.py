import yaml


class Settings:
    def __init__(self):
        with open("config.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        self.DATABASE_URL = config['database']['url']


settings = Settings()