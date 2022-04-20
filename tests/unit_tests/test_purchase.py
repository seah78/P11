class TestPurchasePlaces:
    booking_places_lower_value = {'places': '12', 'competition': 'Competition 2', 'club': 'Premier club'}
    booking_places_higher_value = {'places': '14', 'competition': 'Competition 2', 'club': 'Premier club'}
    booking_places_more_than_12 = {'places': '13', 'competition': 'Competition 1', 'club': 'Premier club'}

    def test_valid_purchase(self, client, mock_clubs, mock_competitions):
        """
        Test valid purchase
        """
        request = client.post('/purchasePlaces', data=self.booking_places_lower_value)
        data = request.data.decode()
        assert 'Great-booking complete' in data
        assert request.status_code == 200

    def test_invalid_purchase(self, client, mock_clubs, mock_competitions):
        """
        Test invalid purchase
        """
        request = client.post('/purchasePlaces', data=self.booking_places_higher_value)
        data = request.data.decode()
        assert 'Specify a lower value' in data
        assert request.status_code == 200
        
    def test_purchase_less_than_12(self, client, mock_clubs, mock_competitions):
        """
        Test purchase less than 12
        """
        request = client.post('/purchasePlaces', data=self.booking_places_more_than_12)
        data = request.data.decode()
        assert 'Specify a value less than or equal to 12' in data
        assert request.status_code == 200
        
        
    def test_no_puchase_in_finish_competition(self, client, mock_clubs, mock_competitions):
        """
        Test purchase in finish competition
        """
        request = client.get('/book/Competition 1/Premier club')
        data = request.data.decode()
        assert "This competition is finished" in data
        assert request.status_code == 200
