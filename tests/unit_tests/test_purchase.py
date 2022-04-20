class TestPurchasePlaces:
    booking_places_lower_value = {'places': '12', 'competition': 'Competition 2', 'club': 'Premier club'}
    booking_places_higher_value = {'places': '14', 'competition': 'Competition 2', 'club': 'Premier club'}


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