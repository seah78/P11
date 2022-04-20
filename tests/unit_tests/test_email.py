

def test_email_valid(client, mock_clubs):
    """
    Test valid email
    """
    email = "club1@test.fr"
    test_log = client.post('/showSummary', data={'email': email})
    data = test_log.data.decode()
    assert "Points available" in data
    assert test_log.status_code == 200

def test_email_invalid(client, mock_clubs):
    """
    Test invalid email
    """
    email = "invalid@test.fr"
    test_log = client.post('/showSummary', data={'email': email})
    data = test_log.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert test_log.status_code == 200 

def test_email_blank(client, mock_clubs):
    """
    Test invalid email
    """
    email = ""
    test_log = client.post('/showSummary', data={'email': email})
    data = test_log.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data
    assert test_log.status_code == 200 