from flask import request, url_for


def test_purchase_logout(client, captured_templates, mock_clubs, mock_competitions):
    """
    Test purchase and logout
    """

    booking_places = {
        "places": "3",
        "competition": "Competition 2",
        "club": "Premier club",
    }

    request1 = client.post("/purchasePlaces", data=booking_places)
    assert request1.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert int(context["club"]["points"]) == 4
    assert int(context["competitions"][1]["numberOfPlaces"]) == 10

    response = client.get("/logout")
    assert response.status_code == 302
    client.get(url_for("index"))
    assert request.path == url_for("index")
