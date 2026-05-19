# FOI Agent Webinar — companion site

A small static site that runs alongside a public sector webinar on building a
declarative Freedom of Information (FOI) agent in Microsoft Copilot Agent
Builder.

## Pages

- `index.html` — overview, the three-stage FOI process, why Copilot fits stages 1 and 3.
- `build.html` — step-by-step build guide for Agent Builder, with copy-ready prompts.
- `resources.html` — guidance links, prompt pack, sample requests, and FAQ.

## Local preview

The site is plain HTML/CSS/JS with no build step. Open `index.html` directly,
or run any static server, for example:

```powershell
# from the repo root
python -m http.server 8080
```

Then browse to <http://localhost:8080>.

## Deploy to GitHub Pages

1. Push this repo to GitHub.
2. In the repo, go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch `main` and folder `/ (root)`. Save.
5. GitHub will publish the site at `https://<user-or-org>.github.io/<repo-name>/`.

A `.nojekyll` file is included so GitHub Pages serves the `assets/` folder
without running Jekyll.

## Structure

```
.
├── index.html
├── build.html
├── resources.html
├── assets/
│   ├── css/styles.css
│   └── js/main.js
├── .nojekyll
└── README.md
```

## Customising for your sector

The content is written for a general UK public sector audience. To tailor it
for a specific department (police force, council, HMRC, NHS trust, etc.):

- Swap the guidance links on `resources.html` for your sector regulator.
- Update the sample FOI requests with scenarios your team actually sees.
- Adjust the agent instructions on `build.html` to reference your internal FOI
  policy and tone of voice.
