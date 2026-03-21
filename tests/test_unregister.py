from tests.conftest import client  # noqa: F401 – fixture registration


def test_unregister_success_returns_200(client):
    # Arrange — michael@mergington.edu is in Chess Club's initial participants
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{participant_email}")

    # Assert
    assert response.status_code == 200


def test_unregister_response_message_contains_email_and_activity(client):
    # Arrange — daniel@mergington.edu is in Chess Club's initial participants
    activity_name = "Chess Club"
    participant_email = "daniel@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{participant_email}")

    # Assert
    message = response.json()["message"]
    assert participant_email in message
    assert activity_name in message


def test_unregister_removes_participant_from_activity(client):
    # Arrange — emma@mergington.edu is in Programming Class's initial participants
    activity_name = "Programming Class"
    participant_email = "emma@mergington.edu"

    # Act
    client.delete(f"/activities/{activity_name}/participants/{participant_email}")

    # Assert
    activities = client.get("/activities").json()
    assert participant_email not in activities[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Nonexistent Club"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/x@mergington.edu")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_participant_not_in_activity(client):
    # Arrange — notamember@mergington.edu is not in Chess Club
    activity_name = "Chess Club"
    non_member_email = "notamember@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{non_member_email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
