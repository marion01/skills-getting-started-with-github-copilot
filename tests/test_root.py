def test_root_redirects_to_static_index(client):
    # Arrange: (handled by fixtures)

    # Act
    resp = client.get("/", follow_redirects=False)

    # Assert
    assert resp.status_code == 307
    assert resp.headers.get("location") == "/static/index.html"
