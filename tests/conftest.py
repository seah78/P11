import pytest
import server
from flask import template_rendered

@pytest.fixture
def app():
    app = server.app
    app.config.update(({'TESTING': True}))
    yield app
    
@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
        
@pytest.fixture
def mock_clubs(mocker):
    data = [
        {
            "name": "Premier club",
            "email": "club1@test.fr",
            "points": "13"
        },
        {
            "name": "Deuxième club",
            "email": "club2@test.fr",
            "points": "4"
        },
        {
            "name": "Troisième club",
            "email": "club3@test.fr",
            "points": "24"
        }
    ]
    mocker.patch.object(server, 'clubs', data)
    
@pytest.fixture
def mock_competitions(mocker):
    data = [
        {
            "name": "Competition 1",
            "date": "2022-03-20 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Competition 2",
            "date": "2022-05-22 10:00:00",
            "numberOfPlaces": "13"
        }
    ]
    mocker.patch.object(server, 'competitions', data)

@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)