from datetime import date
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "static" / "data" / "market_summary.json"


def build_market_summary() -> dict[str, object]:
    return {
        "title": "Asia Market Pulse",
        "as_of": date.today().isoformat(),
        "is_demo": True,
        "source": "Illustrative sample data",
        "markets": [
            {"country": "Korea", "index": "KOSPI 200", "return_1w": 1.8, "breadth": 63.0},
            {"country": "Japan", "index": "Nikkei 225", "return_1w": -0.5, "breadth": 47.0},
            {"country": "Taiwan", "index": "TWSE 50", "return_1w": 2.4, "breadth": 68.0},
            {"country": "China", "index": "CSI 300", "return_1w": -1.2, "breadth": 42.0},
            {"country": "Hong Kong", "index": "Hang Seng", "return_1w": 0.7, "breadth": 54.0},
        ],
    }


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(build_market_summary(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(OUTPUT_PATH.resolve())


if __name__ == "__main__":
    main()