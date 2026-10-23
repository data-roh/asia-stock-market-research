from datetime import date, datetime, timezone
import re
import unittest

from build_research_radar import DescriptionParser, TITLE_PATTERNS, observed_star_growth, weekly


class ResearchRadarTests(unittest.TestCase):
    def test_excerpt_comes_from_publisher_metadata(self):
        parser = DescriptionParser()
        parser.feed('<meta property="og:description" content="A report on market liquidity.">')
        self.assertEqual(parser.description, "A report on market liquidity.")

    def test_market_microstructure_excludes_materials_papers(self):
        pattern = TITLE_PATTERNS["market microstructure"]
        self.assertIsNone(re.search(pattern, "Heat Treatment on Microstructure of Al-Mg-Si Alloys", re.I))
        self.assertIsNotNone(re.search(pattern, "Liquidity in Limit Order Books", re.I))

    def test_weekly_uses_completed_hong_kong_week(self):
        # Monday 00:30 UTC is already Monday morning in Hong Kong.
        now = datetime(2026, 10, 19, 0, 30, tzinfo=timezone.utc)
        data = {
            "institutional": [
                {"id": "last-week", "publishedAt": "2026-10-18T15:30:00+00:00"},
                {"id": "this-week", "publishedAt": "2026-10-18T16:30:00+00:00"},
            ],
            "ssrn": [{"id": "paper", "indexedAt": "2026-10-16T10:00:00+00:00"}],
            "github": [{"id": "gain", "stars7d": 10}, {"id": "loss", "stars7d": -2}],
        }
        result = weekly(now, data)
        self.assertEqual(result["start"], "2026-10-12")
        self.assertEqual(result["institutionalIds"], ["last-week"])
        self.assertEqual(result["ssrnIds"], ["paper"])
        self.assertEqual(result["githubIds"], ["gain"])

    def test_first_week_shows_tracked_repositories_without_growth(self):
        data = {"institutional": [], "ssrn": [], "github": [{"id": "new", "stars7d": None}]}
        result = weekly(datetime(2026, 10, 19, tzinfo=timezone.utc), data)
        self.assertEqual(result["githubIds"], ["new"])

    def test_star_growth_requires_exact_fresh_snapshots(self):
        history = [
            {"date": "2026-10-16", "stars": 100},
            {"date": "2026-10-23", "stars": 125},
        ]
        self.assertEqual(observed_star_growth(history, date(2026, 10, 23)), 25)
        self.assertIsNone(observed_star_growth(history[:-1], date(2026, 10, 23)))
        self.assertIsNone(observed_star_growth(history, date(2026, 10, 24)))


if __name__ == "__main__":
    unittest.main()
