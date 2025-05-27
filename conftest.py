from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from database.db_config import Base, get_db
import pytest
from sqlalchemy.pool import StaticPool
from main import app
from fastapi.testclient import TestClient
from schema.user import (
  CreateUser
)

@pytest.fixture(name="session")
def create_session_fixture():
  engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
  Base.metadata.create_all(engine)

  with Session(engine) as session:
    yield session
  

@pytest.fixture(name="client")
def create_client(session:Session):

  def get_db_override():
    yield session

  app.dependency_overrides[get_db] = get_db_override

  client = TestClient(app)

  yield client

  app.dependency_overrides.clear()

@pytest.fixture(name="new_user")
def create_fake_user():
  new_user = CreateUser(username="adex", email="adex@mail.com", password="adex123")

  return new_user