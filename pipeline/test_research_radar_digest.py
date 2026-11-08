import unittest

from send_research_radar_digest import collect_ready_items, render_digest


class ResearchRadarDigestTests(unittest.TestCase):
    def setUp(self):
        self.item = {
            "id": "article-1",
            "title": "Japan equity outlook",
            "url": "https://aqr.com/article/japan-outlook",
            "sourceId": "aqr",
            "publishedAt": None,
            "verification": {"status": "VERIFIED_NEW", "confidence": "MEDIUM"},
            "asiaRelevance": 75,
            "researchPriority": 85,
            "topics": ["Equities", "Macro"],
            "excerpt": "Publisher description.",
        }

    def test_digest_only_includes_verified_articles_on_expected_domains(self):
        possible = {**self.item, "id": "possible", "verification": {"status": "POSSIBLE_NEW"}}
        outside = {**self.item, "id": "outside", "url": "https://aqr.com.attacker.example/article"}
        radar = {"institutional": [self.item, possible, outside]}
        result = collect_ready_items(radar, {"aqr": ["aqr.com"]}, set())
        self.assertEqual([item["id"] for item in result], ["article-1"])

    def test_sent_articles_are_excluded(self):
        result = collect_ready_items(
            {"institutional": [self.item]}, {"aqr": ["aqr.com"]}, {"article-1"}
        )
        self.assertEqual(result, [])

    def test_digest_has_plain_text_and_html_provenance(self):
        _, text, html = render_digest([self.item], "2026-11-08", {"sourceChecks": []})
        self.assertIn("Official source: https://aqr.com/article/japan-outlook", text)
        self.assertIn("Publisher description: Publisher description.", text)
        self.assertIn("https://aqr.com/article/japan-outlook", html)
        self.assertIn("Publisher descriptions are metadata", html)


if __name__ == "__main__":
    unittest.main()
