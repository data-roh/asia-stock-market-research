import unittest

from audit_research_sources import category, sources
from verify_research_updates import (
    canonical_url,
    classify,
    official_host,
    title_matches,
    verification_candidates,
    verification_summary,
)


class ResearchRadarVerificationTests(unittest.TestCase):
    def test_canonical_url_removes_tracking_and_fragment(self):
        self.assertEqual(
            canonical_url("https://www.aqr.com/insights/test/?utm_source=email&id=4#top"),
            "https://www.aqr.com/insights/test?id=4",
        )

    def test_official_host_accepts_subdomains_but_not_lookalikes(self):
        domains = ["aqr.com"]
        self.assertTrue(official_host("https://research.aqr.com/article", domains))
        self.assertFalse(official_host("https://aqr.com.example.org/article", domains))

    def test_title_matching_tolerates_publisher_suffix(self):
        self.assertTrue(title_matches("Rates and Markets", "Rates and Markets | AQR"))
        self.assertFalse(title_matches("Rates and Markets", "Hiring Research Analysts"))

    def test_empty_verification_run_is_recorded_as_a_completed_zero_candidate_run(self):
        run = verification_summary([], "2026-11-09T00:17:00+00:00")
        self.assertEqual(run["completedAt"], "2026-11-09T00:17:00+00:00")
        self.assertEqual(run["candidateCount"], 0)
        self.assertEqual(run["verifiedNewCount"], 0)
        self.assertEqual(run["needsReviewCount"], 0)

    def test_verification_summary_counts_only_current_run_candidates(self):
        candidates = [
            {"verification": {"status": "VERIFIED_NEW"}},
            {"verification": {"status": "POSSIBLE_NEW"}},
        ]
        run = verification_summary(candidates, "2026-11-09T00:17:00+00:00")
        self.assertEqual(run["candidateCount"], 2)
        self.assertEqual(run["verifiedNewCount"], 1)
        self.assertEqual(run["needsReviewCount"], 1)

    def test_only_persisted_phase_one_candidates_are_verified(self):
        source = {"aqr": {}}
        item = {"key": "new-article", "sourceId": "aqr"}
        old_state = {"items": [item]}
        pending_state = {**old_state, "pendingVerificationKeys": ["new-article"]}
        self.assertEqual(verification_candidates(old_state, source), [])
        self.assertEqual(verification_candidates(pending_state, source), [item])

    def test_asia_classification_returns_bounded_score_and_content_type(self):
        topics, regions, relevance, reason, content_type = classify(
            "Japan equity outlook", "A review of Japanese market flows and valuations."
        )
        self.assertIn("Equities", topics)
        self.assertIn("Japan", regions)
        self.assertGreaterEqual(relevance, 40)
        self.assertLessEqual(relevance, 100)
        self.assertTrue(reason)
        self.assertEqual(content_type, "Outlook")

    def test_source_audit_covers_every_library_source(self):
        source_rows = sources()
        self.assertEqual(len(source_rows), 45)
        self.assertEqual(len({source["id"] for source in source_rows}), 45)
        self.assertEqual(
            {source["id"] for source in source_rows if source["id"] in {"aqr", "citadel", "man", "apollo", "oaktree-memos"}},
            {"aqr", "citadel", "man", "apollo", "oaktree-memos"},
        )

    def test_source_classes_use_expected_labels(self):
        row = {
            "rss_available": "no",
            "access_restriction": "none observed",
            "article_url_visible": "yes",
            "javascript_required": "unknown",
        }
        self.assertEqual(category(row), "B")
        row["access_restriction"] = "HTTP 403"
        row["article_url_visible"] = "unknown"
        self.assertEqual(category(row), "E")


if __name__ == "__main__":
    unittest.main()
