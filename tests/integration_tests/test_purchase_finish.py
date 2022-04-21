def test_purchase_finish(client, captured_templates, mock_competitions, mock_clubs):
    """ 
    Test purchase and finish competition
    """
    first_booking_places = {'places': '8', 'competition': 'Competition 3', 'club': 'Troisième club'}

    request1 = client.post('/purchasePlaces', data=first_booking_places)
    assert request1.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert int(context['club']['points']) == 24
    assert int(context['competitions'][1]['numberOfPlaces']) == 13


    request_book = client.get('/book/Competition 1/Premier club')
    assert request_book == 200
    assert len(captured_templates) == 2

    
    request2 = client.get('/book/Competition 1/Premier club')
    data = request2.data.decode()
    template, context = captured_templates[2]
    assert template.name == "welcome.html"
    assert "This competition is finished" in data
    assert request2.status_code == 200




