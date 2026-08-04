"""Row-schema equivalence tests for the Open Library scraper.

Relocated verbatim (assertions untouched) from metadatarr's
test_scrapers_migrated.py, keeping only the tests for the scraper that
lives in this package, re-pointed at pyopenlibrary.harvest.*. These lock
the exact flat-row shape the scraper emits (the contract the LeData
datasets depend on) against a realistic upstream sample, so a future
engine change can't silently alter the output schema.
"""
from __future__ import annotations

from harvestkit.engine import all_sources

from pyopenlibrary.harvest.openlibrary_books import OpenLibraryBooks


def test_openlibrary_map_row_schema():
    src = OpenLibraryBooks()
    doc = {
        "key": "/works/OL45804W",
        "title": "Fantastic Mr Fox",
        "subtitle": "a story",
        "author_name": ["Roald Dahl"],
        "author_key": ["OL34184A"],
        "first_publish_year": 1970,
        "subject": [f"s{i}" for i in range(40)],
        "isbn": [f"isbn{i}" for i in range(9)],
        "publisher": [f"p{i}" for i in range(9)],
        "language": [f"l{i}" for i in range(20)],
        "number_of_pages_median": 96,
        "ebook_access": "borrowable",
        "has_fulltext": True,
        "edition_count": 120,
        "cover_i": 8739161,
    }
    row = src.map_row(doc)
    assert row["olid"] == "OL45804W"
    assert row["title"] == "Fantastic Mr Fox"
    assert row["authors"] == ["Roald Dahl"]
    # truncation contracts preserved from the original scraper
    assert len(row["subjects"]) == 30
    assert len(row["isbn_10"]) == 5
    assert row["isbn_13"] == []
    assert len(row["publisher"]) == 5
    assert len(row["language"]) == 10
    assert row["has_fulltext"] is True
    assert set(row) == {
        "olid", "title", "subtitle", "authors", "author_key",
        "first_publish_year", "subjects", "isbn_10", "isbn_13", "publisher",
        "language", "number_of_pages_median", "ebook_access", "has_fulltext",
        "edition_count", "cover_i",
    }


def test_openlibrary_map_row_drops_records_without_olid():
    assert OpenLibraryBooks().map_row({"key": "", "title": "x"}) is None


def test_openlibrary_partitions_stable_and_seeded():
    parts = OpenLibraryBooks().partitions()
    assert parts[0] == {"subject": "fiction"}
    assert len(parts) == 64
    assert all(set(p) == {"subject"} for p in parts)


def test_openlibrary_scraper_is_registered():
    reg = all_sources()
    assert reg.get("openlibrary_books") is OpenLibraryBooks
