# Content sources and review notes

All source materials remain byte-for-byte unchanged under `PersonalPortfolio/`. No original report or workbook is linked from the website. Selected standalone images and two unchanged workbook-embedded images are copied to `assets/images/`.

| Website use | Source | Evidence and limits |
| --- | --- | --- |
| Hero and STOL lead image | `SeniorDesign/Hybrid3view/OrthoView.webp` | Original CAD rendering; no invented specifications. |
| STOL gallery | `SeniorDesign/Hybrid3view/TopView.webp`, `SideView.webp`, `FrontView.webp` | Original CAD views. Bottom view is retained in the source folder. |
| STOL methods and scope | `SeniorDesign/AIAA Hybrid-Electric STOL SeniorDesign.xlsx` | Lift/flap calculations, weight/CG cases, static/braking gear loads and geometry. Notes flag gear layout assumptions as provisional; no final numerical performance claimed. Individual ownership is pending. |
| BANSHEE card and lead image | `BANSHEE_Sinch/SaddleBraceFV.webp` | SolidWorks static Y-displacement figure credited to Jacob Harris. Original annotations, deformation-scale note, and educational watermark retained. |
| BANSHEE methods and results | `BANSHEE_Sinch/LoadsAnalysisCode.pdf`, `LoadsAnalysisResults.pdf` | Code listing identifies Jacob Harris. 1G/2G static and 2G landing cases; shear, bending, margins. Positive tabulated margins are qualified as modeled outputs, not test validation. Source code was inspected, not executed. |
| eVTOL card and CAD figure | `TMAD/EVTOL Fuselage Stress Analysis.xlsx`, `xl/media/image3.png` | Embedded side-view CAD figure extracted unchanged. |
| eVTOL shear-force figure | Same workbook, `xl/media/image7.png` | Static fuselage analysis credited to Jacob Harris; Simcenter NASTRAN output, educational watermark retained. |
| eVTOL methods | Same workbook | Point/distributed loads, bending, shear, margins, 3G landing and coordinated-turn studies. Jacob Harris confirmed in chat that he owns the workbook and is its sole editor. This establishes workbook responsibility, not authorship of every embedded image or the wider aircraft design. Workbook formulas were inspected, not recalculated or independently validated. The workbook does not explicitly identify the project as Maelstrom; association remains pending. |
| Additional coursework summary | `FEA/FusDummyFrameFEA.pdf`, introduction and conclusion | ARO4080 report authored by Jacob Harris, California State Polytechnic University Pomona. FEMAP model, CBAR/CROD/CQUAD4 idealization, floor/strut/frame load paths and reaction balance. Kept separate from aircraft project claims. |

Three `.url` files in `BANSHEE_Sinch/` are external image shortcuts, not embedded images. They were not fetched or republished. Full aircraft BANSHEE imagery is not available locally. No additional awards, flight-test results, or professional achievements were established.

## Still needed

- Confirm TMAD workbook belongs to Maelstrom eVTOL.
- Confirm individual contributions to the STOL team project and any eVTOL responsibilities beyond the workbook.
- Final requirements/specifications and validation evidence, if appropriate for public release.
- Public contact information, résumé, education details, and optional full-aircraft BANSHEE imagery.

## Publication boundary

`_config.yml` excludes `PersonalPortfolio`, `docs`, and the README from standard GitHub Pages/Jekyll output. Do not add `.nojekyll` or upload the entire checkout as a static Pages artifact: that would bypass these exclusions. A custom deployment must use an explicit allowlist containing only `index.html`, `projects/`, and `assets/`. Publication is not performed by this task. Exclusion from site output does not change the visibility of files already committed to the GitHub repository.
