# Preprocessing

Runs minimal preprocessing on the business description section of the annual filings.
- Removes newline markers, such as "\n"
- Removes redundant, non-informative words such as "Overview", "Table of Contents", "Description of Major Subsidiaries"
- Removes the word "General" if it appears at the beginning of the document
- Replaces running whitespaces with a single space