def test_purchase_two_competition(client, captured_templates, mock_competitions, mock_clubs):
    """ 
    Test purchase in two competition
    """
    first_booking_places = {'places': '1', 'competition': 'Competition 2', 'club': 'Troisième club'}
    second_booking_places = {'places': '2', 'competition': 'Competition 3', 'club': 'Troisième club'}

    request1 = client.post('/purchasePlaces', data=first_booking_places)
    assert request1.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert int(context['club']['points']) == 21
    assert int(context['competitions'][1]['numberOfPlaces']) == 12


    request_book = client.get('/book/Competition 3/Troisième club')
    assert request_book == 200
    assert len(captured_templates) == 2

    request2 = client.post('/purchasePlaces', data=second_booking_places)
    assert request2.status_code == 200
    assert len(captured_templates) == 3
    template, context = captured_templates[2]
    assert int(context['club']['points']) == 15
    assert int(context['competitions'][2]['numberOfPlaces']) == 19
    