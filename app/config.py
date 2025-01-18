from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    database_username: str
    database_password: str
    database_port: int
    database_name: str
    database_host: str
    secret_key: str
    algorithm: str
    access_expires_in_minutes: int


    class Config():
        env_file = '.env'

settings = Setting()
