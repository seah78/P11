from flask import request, url_for

def test_login_logout(client, mock_clubs, captured_templates):
    email = "club1@test.fr"
    test_log = client.post('/showSummary', data={'email': email})
    data = test_log.data.decode()
    assert "Points available" in data
    assert test_log.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert context['club']['email'] == "club1@test.fr"
    
    response = client.get('/logout')
    assert response.status_code == 302
    client.get(url_for('index'))
    assert request.path == url_for('index')