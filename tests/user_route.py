from fastapi.testclient import TestClient

def test_create_user(client: TestClient):

  # engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

  # Base.metadata.create_all(engine)

  # with Session(engine) as session:
  #   def get_db_override():
  #     return session
    
    # app.dependency_overrides[get_db] = get_db_override

    new_user = {
      "username":"adex",
      "email": "adex@mail.com",
      "password": "adex123"
    }

    response = client.post(url="/user", json=new_user)


    assert response.status_code == 200
    
    #try recreatinig same user
    response = client.post(url="/user", json=new_user)
    assert response.status_code == 409

# def test_get_users(client: TestClient):
    