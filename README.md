# pyopenlibrary

Open Library book catalog bulk harvester grouped onto the
[harvestkit](https://github.com/LeMetadatarr/harvestkit) resumable-harvest
engine. Extracted from [metadatarr](https://github.com/TigreGotico/metadatarr)'s
scraper collection into its own standalone package.

## Sources

| Scraper | Registry name | Source |
| --- | --- | --- |
| `openlibrary_books` | `openlibrary_books` | Open Library `/search.json`, 60+ subject seeds |

## Install

```bash
pip install pyopenlibrary
# or, for the HuggingFace publisher (via harvestkit):
pip install "pyopenlibrary[hf]"
# or, for Cloudflare-guarded sources:
pip install "pyopenlibrary[stealth]"
```

## Usage

```bash
# list every registered scraper
pyopenlibrary-harvest --list

# harvest one source (resumable — safe to Ctrl-C and rerun)
pyopenlibrary-harvest openlibrary_books --output ~/.cache/metadatarr/scrapers/
```

Every scraper is a `harvestkit.engine.Source` subclass: checkpoint/dedup/
pagination/throttle are handled by the shared engine, each module only
answers `initial_cursor()` and `fetch(cursor)`. See
[harvestkit](https://github.com/LeMetadatarr/harvestkit) for the full engine
API.

## License

Apache-2.0
