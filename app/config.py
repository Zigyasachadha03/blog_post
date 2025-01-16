from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    database_username: str
    database_password: str
    database_port: int
    database_name: str
    database_host: str


    class Config():
        env_file = '.env'

settings = Setting()
