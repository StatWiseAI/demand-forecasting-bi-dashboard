# Deployment Checklist

## 1. Pre-publish quality control
- [ ] confirm one official KPI set across report, slides, README, and dashboard
- [ ] remove all local absolute file paths
- [ ] remove notebook outputs and large binary clutter
- [ ] verify dataset file name and sheet names
- [ ] export screenshots for README and landing page
- [ ] ensure no secrets or credentials are committed

## 2. GitHub repository checklist
- [ ] create public repository with a professional name
- [ ] push clean notebook, app, src, docs, report, and slides
- [ ] add repository description and topics
- [ ] add LICENSE, .gitignore, and requirements.txt
- [ ] update README with live links once deployed
- [ ] create v1.0 release tag

## 3. Streamlit deployment checklist
- [ ] confirm entry point is `app/app.py`
- [ ] keep model and processed data loading lightweight
- [ ] use caching for data and model loads
- [ ] test locally before pushing
- [ ] deploy from GitHub on Streamlit Community Cloud
- [ ] verify all pages load correctly
- [ ] add dashboard URL to README and GitHub Pages

## 4. Render deployment checklist
- [ ] only use if you want a generic web-service deployment path
- [ ] add start command and runtime specification
- [ ] ensure ephemeral filesystem is not used for permanent storage
- [ ] avoid heavy startup logic because free services spin down on idle
- [ ] test cold-start behavior and external file access

## 5. GitHub Pages deployment checklist
- [ ] add `docs/index.html` or configure a Pages publishing branch
- [ ] enable Pages in repository settings
- [ ] verify assets and links resolve correctly
- [ ] add live dashboard, report, slides, and GitHub links
- [ ] optionally connect a custom domain

## 6. Final professional polish
- [ ] use consistent terminology: forecasting, decision support, operational impact
- [ ] add a concise architecture diagram
- [ ] include 3-5 clean screenshots
- [ ] add an executive summary paragraph for recruiters and stakeholders
- [ ] publish the project link on LinkedIn and CV
