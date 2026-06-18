def test_remove_participant_success(client):
    # Arrange
    activity = "Programming Class"
    email = "emma@mergington.edu"
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    activities_after = client.get("/activities").json()
    assert email not in activities_after[activity]["participants"]


def test_remove_participant_not_found_returns_400(client):
    # Arrange
    activity = "Programming Class"
    email = "nonexistent@mergington.edu"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 400
    assert "not found" in resp.json().get("detail", "").lower()
