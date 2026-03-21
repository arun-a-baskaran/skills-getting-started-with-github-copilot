from tests.conftest import client  # noqa: F401 – fixture registration


def test_signup_success_returns_200(client):
    # Arrange
    activity_name = "Chess Club"
    new_email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": new_email})

    # Assert
    assert response.status_code == 200


def test_signup_response_message_contains_email_and_activity(client):
    # Arrange
    activity_name = "Programming Class"
    new_email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": new_email})

    # Assert
    message = response.json()["message"]
    assert new_email in message
    assert activity_name in message


def test_signup_adds_participant_to_activity(client):
    # Arrange
    activity_name = "Drama Club"
    new_email = "newstudent@mergington.edu"

    # Act
    client.post(f"/activities/{activity_name}/signup", params={"email": new_email})

    # Assert
    activities = client.get("/activities").json()
    assert new_email in activities[activity_name]["participants"]


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Nonexistent Club"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": "x@mergington.edu"})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_if_already_signed_up(client):
    # Arrange — michael@mergington.edu is already in Chess Club's initial participants
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": existing_email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"
