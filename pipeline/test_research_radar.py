from datetime import datetime, timezone
import re
import unittest

from build_research_radar import DescriptionParser, TITLE_PATTERNS, weekly


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


if __name__ == "__main__":
    unittest.main()
