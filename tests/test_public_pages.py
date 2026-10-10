from __future__ import annotations

import os
import unittest
from contextlib import ExitStack
from unittest.mock import patch

import httpx
from fastapi.testclient import TestClient


class PublicPagesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(
            patch.dict(
                os.environ,
                {
                    "APP_ENV": "test",
                    "APP_COMPONENT": "api",
                    "APP_HOST": "127.0.0.1",
                    "APP_PORT": "8787",
                    "CODE_HOTRELOAD": "false",
                    "SERVICE_READINESS_TIMEOUT": "60",
                    "PULL_SECRETS_FROM_VAULT": "false",
                    "PERFORMANCE_SERVICE_BASE_URL": "https://performance.test",
                    "PYTHON_DOTENV_DISABLED": "1",
                },
            ),
        )

        from app.api.rest import init_api

        self.rework = {
            "rework_id": 1,
            "rework_name": "Test Rework",
            "mode": 0,
            "rx": 0,
            "updated_at": 0,
        }
        self.backend_requests = []
        backend = httpx.AsyncClient(
            transport=httpx.MockTransport(self.backend_response)
        )
        self.stack.enter_context(
            patch("app.services.http.ServiceHTTP", return_value=backend)
        )
        self.client = self.stack.enter_context(TestClient(init_api()))

    def backend_response(self, request: httpx.Request) -> httpx.Response:
        self.backend_requests.append(request.url.path)
        payloads = {
            "/api/v1/reworks": [self.rework],
            "/api/v1/reworks/1": self.rework,
            "/api/v1/reworks/users/7": {
                "user_id": 7,
                "user_name": "Test User",
                "country": "DE",
                "reworks": [self.rework],
            },
            "/api/v1/reworks/1/users/7/stats": {
                "user_id": 7,
                "user_name": "Test User",
                "country": "DE",
                "new_pp": 1200,
                "old_pp": 1000,
                "new_rank": 2,
                "old_rank": 3,
            },
        }
        if request.url.path not in payloads:
            raise AssertionError(f"Unexpected backend request: {request.url}")
        return httpx.Response(200, json=payloads[request.url.path])

    def assert_page(self, path: str, template: str, title: str):
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.headers["content-type"].startswith("text/html"))
        self.assertEqual(response.template.name, template)
        self.assertIn(f"<title>{title} | Akatsuki Rework</title>", response.text)
        self.assertEqual(response.context["request"].url.path, path.split("?")[0])
        self.assertIn("Test Rework", response.text)
        return response

    def test_homepage(self) -> None:
        self.assert_page("/", "homepage.html", "Home")

    def test_login(self) -> None:
        self.assert_page("/auth/login", "login.html", "Login")

    def test_leaderboard(self) -> None:
        response = self.assert_page(
            "/rework/1/leaderboard?page=2",
            "rework.html",
            "Test Rework",
        )
        self.assertEqual(response.context["page_num"], 2)

    def test_authenticated_queue(self) -> None:
        self.client.cookies.update({"user_id": "7", "session_token": "test-session"})
        response = self.assert_page(
            "/rework/1/queue", "queue.html", "Test Rework Queue"
        )
        self.assertEqual(response.context["user"].id, 7)
        self.assertIn('value="test-session"', response.text)

    def test_profile(self) -> None:
        response = self.assert_page(
            "/rework/1/users/7",
            "profile.html",
            "Test User's Profile (Test Rework)",
        )
        self.assertEqual(response.context["user_data"].user_id, 7)
        self.assertIn("1,200", response.text)

    def test_anonymous_queue_redirects_to_login(self) -> None:
        response = self.client.get("/rework/1/queue", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["location"], "/auth/login")
        self.assertNotIn("/api/v1/reworks/1", self.backend_requests)

    def test_leaderboard_without_page_redirects(self) -> None:
        response = self.client.get("/rework/1/leaderboard", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["location"], "/rework/1/leaderboard?page=1")


if __name__ == "__main__":
    unittest.main()
