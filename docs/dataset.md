# Dataset

## What this repo produces

`pyopenlibrary` harvests book records from Open Library. It queries the `/search.json` endpoint across 60+ subject seeds and deduplicates rows by Open Library work ID (OLID). The output is one JSONL file where each row is a distinct book work.

## Dataset format

One row per book work. Each row is a JSON object with these fields:

| Field | Type | Description |
| --- | --- | --- |
| `olid` | string | Open Library work identifier, with the `/works/` prefix removed. |
| `title` | string or null | Book title. |
| `subtitle` | string or null | Book subtitle. |
| `authors` | list of strings | Author names. |
| `author_key` | list of strings | Open Library author identifiers. |
| `first_publish_year` | integer or null | First known publication year. |
| `subjects` | list of strings | Up to 30 subject headings. |
| `isbn_10` | list of strings | Up to 5 ISBN-10 values. |
| `isbn_13` | list of strings | Reserved for ISBN-13 values (currently empty). |
| `publisher` | list of strings | Up to 5 publisher names. |
| `language` | list of strings | Up to 10 language codes. |
| `number_of_pages_median` | integer or null | Median page count across editions. |
| `ebook_access` | string or null | Ebook availability level, for example `borrowable`. |
| `has_fulltext` | boolean | Whether a full-text scan exists. |
| `edition_count` | integer or null | Number of known editions. |
| `cover_i` | integer or null | Open Library cover image identifier. |

## How to generate it

Install the package and run the harvester:

```bash
pip install pyopenlibrary
pyopenlibrary-harvest openlibrary_books \
  --output ~/.cache/metadatarr/scrapers/
```

The harvest is resumable. You can stop it with Ctrl-C and rerun the same command to continue from the last checkpoint.

## Worth publishing on Hugging Face?

Yes. Open Library data is openly licensed and the dataset provides a large bibliographic catalog with authors, subjects, ISBNs, and edition metadata. It is useful for retrieval and recommendation research.

## ML tasks served

- Book recommendation and retrieval.
- Subject and genre classification.
- Citation and ISBN matching.
- Named entity recognition on titles and author names.
- Language identification and catalog enrichment.
