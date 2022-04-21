class TestPurchasePlaces:
    booking_places_lower_value = {'places': '4', 'competition': 'Competition 2', 'club': 'Troisième club'}
    booking_places_higher_value = {'places': '14', 'competition': 'Competition 2', 'club': 'Premier club'}
    booking_places_more_than_12 = {'places': '13', 'competition': 'Competition 1', 'club': 'Premier club'}
    booking_places = {'places': '4', 'competition': 'Competition 1', 'club': 'Troisième club'}
    booking_places_not_have_enought_points = {'places': '4', 'competition': 'Competition 1', 'club': 'Deuxième club'}
    

    @staticmethod
    def _test_request(request, captured_templates):
        request = request
        assert request.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        return template, context

    def test_valid_purchase(self, client, mock_clubs, mock_competitions, captured_templates):
        """
        Test valid purchase
        """
        request = client.post('/purchasePlaces', data=self.booking_places_lower_value)
        data = request.data.decode()
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        assert 'Great-booking complete' in data
        assert request.status_code == 200

    def test_invalid_purchase(self, client, mock_clubs, mock_competitions, captured_templates):
        """
        Test invalid purchase
        """
        request = client.post('/purchasePlaces', data=self.booking_places_higher_value)
        data = request.data.decode()
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        assert 'Specify a lower value' in data
        assert request.status_code == 200
        
    def test_purchase_less_than_12(self, client, mock_clubs, mock_competitions, captured_templates):
        """
        Test purchase less than 12
        """
        request = client.post('/purchasePlaces', data=self.booking_places_more_than_12)
        data = request.data.decode()
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"        
        assert 'Specify a value less than or equal to 12' in data
        assert request.status_code == 200
        
        
    def test_no_purchase_in_finish_competition(self, client, mock_clubs, mock_competitions, captured_templates):
        """
        Test purchase in finish competition
        """
        request = client.get('/book/Competition 1/Premier club')
        data = request.data.decode()
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        assert "This competition is finished" in data
        assert request.status_code == 200
        
    def test_purchase_in_valid_competition(self, client, mock_clubs, mock_competitions, captured_templates):
        """
        Test purchase in finish competition
        """
        request = client.get('/book/Competition 2/Premier club')
        data = request.data.decode()
        template, context = self._test_request(request, captured_templates)
        assert template.name == "booking.html"
        assert request.status_code == 200
        
    def test_purchase_bad_competition(self, client, mock_clubs, mock_competitions, captured_templates):
        """
        Test purchase in finish competition
        """
        request = client.get('/book/Competition 3/Premier club')
        data = request.data.decode()
        template, context = captured_templates[0]
        assert len(captured_templates) == 1
        assert template.name == "welcome.html"
        assert "Something went wrong-please try again" in data
        
        
    def test_updating_points_after_purchase(self, client, mock_clubs, mock_competitions, captured_templates):
        """ 
        Test updating points after purchase
        """
        request = client.post('/purchasePlaces', data=self.booking_places)
        data = request.data.decode()
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        assert 'Points available: 12' in data # Mock with 24 points, expected result 12
        assert request.status_code == 200

    def test_purchase_not_have_enought_points(self, client, mock_clubs, mock_competitions, captured_templates):
        """
        Test purchase not have enought points
        """
        request = client.post('/purchasePlaces', data=self.booking_places_not_have_enought_points)
        data = request.data.decode()
        template, context = self._test_request(request, captured_templates)
        assert template.name == "welcome.html"
        assert 'You do not have enough points. The transaction is aborted.' in data
        assert request.status_code == 200
