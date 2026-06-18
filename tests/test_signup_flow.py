def test_signup_adds_participant_when_not_registered(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")
    activities_after = client.get("/activities").json()
    assert email in activities_after[activity]["participants"]


def test_signup_existing_returns_400(client):
    # Arrange
    activity = "Chess Club"
    existing = "michael@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": existing})

    # Assert
    assert resp.status_code == 400
    assert "already" in resp.json().get("detail", "").lower()
