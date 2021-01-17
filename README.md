# GetNYTHeadlineWidth
Compiles the width of the New York Times main headline. Run with script.py and launchd.

`script.py` adds title, link, and fontsize to `.csv` file if the data are new. `get_nyt_data.py` actually scrapes the data, and `nytHeadlines.plist` sets up launchd to run `script.py` every ten seconds.
