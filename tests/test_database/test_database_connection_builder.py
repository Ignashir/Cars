import pytest

from infrastructure.persistence.connection import DataBaseConnectionBuilder


@pytest.fixture
def get_database_builder():
    return (DataBaseConnectionBuilder.builder()
            .set_username("username")
            .set_password("password")
            .set_hostname("hostname")
            .set_database("database")
            .set_port("0000"))

@pytest.fixture
def get_database_config_from_env():
    return DataBaseConnectionBuilder.build_from_env(".env.test")


def test_url_creation_builder(get_database_builder):
    assert "mysql+aiomysql://username:password@hostname:0000/database" == get_database_builder._get_url()


def test_url_creation_from_env(get_database_config_from_env):
    assert "mysql+aiomysql://root_password:password@hostname:0000/database" == get_database_config_from_env._get_url()
