from tests.conftest import client  # noqa: F401 – fixture registration


def test_get_activities_status_200(client):
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_nine(client):
    # Act
    response = client.get("/activities")

    # Assert
    assert len(response.json()) == 9


def test_get_activities_each_has_required_fields(client):
    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for activity in activities.values():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity


def test_get_activities_known_activity_data(client):
    # Act
    response = client.get("/activities")
    chess = response.json()["Chess Club"]

    # Assert
    assert chess["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert chess["max_participants"] == 12
