from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import dotenv_values
from typing import Any, Self


class DataBaseConnectionBuilder:
    def __init__(self, params: dict[str, Any]):
        self._connection_config = params

    @staticmethod
    def __read_connection_config_from_dotenv(env_path: str) -> dict[str, Any]:
        return dotenv_values(env_path)

    def set_username(self, new_username: str) -> Self:
        self._connection_config['ROOT_PASSWORD'] = new_username
        return self

    def set_password(self, new_password: str) -> Self:
        self._connection_config['PASSWORD'] = new_password
        return self

    def set_database(self, new_database: str) -> Self:
        self._connection_config['DATABASE'] = new_database
        return self

    def set_port(self, new_port: str) -> Self:
        self._connection_config['TCP_PORT'] = new_port
        return self

    def set_hostname(self, new_hostname: str) -> Self:
        self._connection_config['HOSTNAME'] = new_hostname
        return self

    @classmethod
    def builder(cls) -> Self:
        return cls({})

    @classmethod
    def build_from_env(cls, env_path: str) -> Self:
        return cls(DataBaseConnectionBuilder.__read_connection_config_from_dotenv(env_path))

    def _get_url(self) -> str:
        return (f"mysql+aiomysql://{self._connection_config['ROOT_PASSWORD']}:"
                f"{self._connection_config['PASSWORD']}@{self._connection_config['HOSTNAME']}:"
                f"{self._connection_config['TCP_PORT']}/{self._connection_config['DATABASE']}")

    def get_engine(self) -> Any:
        return create_async_engine(self._get_url(), echo=True)

    def get_session(self) -> Any:
        return sessionmaker(self.get_engine(), expire_on_commit=False, class_=AsyncSession)

    @staticmethod
    def get_base() -> Any:
        return declarative_base()
