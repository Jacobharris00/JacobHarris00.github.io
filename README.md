# Jacob Harris — Aerospace Engineering Portfolio

Responsive, dependency-free HTML/CSS portfolio using the selected Modern Engineering design and supplied engineering project imagery. No build step or deployment is configured.

## Preview

Open `index.html` directly in a browser. For an HTTP preview serving **only website assets**, run:

```sh
python3 tools/preview.py
```

Open localhost port 8000 in your development browser. This local preview deliberately denies access to engineering source documents.

## Structure

- `index.html`: homepage, featured projects, additional FEMAP coursework, About and Contact.
- `projects/`: three project pages with source-supported summaries.
- `assets/`: shared stylesheet and selected project images.
- `PersonalPortfolio/`: original source materials, unchanged; not public website downloads.
- `docs/content-sources.md`: exact source mapping, limitations, and missing information.
- `_config.yml`: excludes source materials from standard GitHub Pages/Jekyll output.

Source workbooks were inspected without recalculating formulas. Engineering calculations were not independently validated. Jacob Harris has confirmed he is the sole editor of the TMAD workbook. Broader team roles and final results remain qualified where evidence is incomplete. The eVTOL workbook does not explicitly name Maelstrom; confirm that association before publication.

## Before publishing

Review the initial design, content, source mapping, and public-release suitability. Supply contact details and clarify outstanding project contributions. Standard GitHub Pages/Jekyll must retain `_config.yml` exclusions; do not add `.nojekyll`. A custom static deployment must publish only `index.html`, `projects/`, and `assets/`, not the whole checkout. Site exclusions do not make committed repository files private.

No files have been pushed and nothing has been deployed by this task.
