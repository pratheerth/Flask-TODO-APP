import pytest
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

from app import create_app
import routes

@pytest.fixture(autouse=True)
def setup_db():
    # Use in-memory TinyDB for isolation
    routes.db = TinyDB(storage=MemoryStorage)
    yield
    routes.db.close()

def get_client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_main_page_loads():
    client = get_client()
    response = client.get('/')
    assert response.status_code == 200


def test_add_task():
    client = get_client()
    response = client.post('/add', data={'title': 'New Task'}, follow_redirects=True)
    assert response.status_code == 200
    tasks = routes.db.all()
    assert any(t['title'] == 'New Task' for t in tasks)


def test_delete_task():
    client = get_client()
    # Insert a task directly
    routes.db.insert({'id': 1, 'title': 'To Delete', 'complete': False})
    response = client.post('/delete/1', follow_redirects=True)
    assert response.status_code == 200
    Task = Query()
    assert routes.db.search(Task.id == 1) == []
