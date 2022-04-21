from flask import request, url_for


def test_request_index(client, captured_templates):
    """
    Test url '/'
    """
    response = client.get("/")
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "index.html"


def test_request_logout(client, captured_templates):
    """
    Test url '/lougout'
    """
    response = client.get("/logout")
    assert response.status_code == 302
    client.get(url_for("index"))
    assert request.path == url_for("index")


def test_request_clubsboard(client, captured_templates):
    """
    Test url '/clubsBoard'
    """
    response = client.get("/clubsBoard")
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "clubsboard.html"
