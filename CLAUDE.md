# Regles Obligatoires - A Respecter Dans Toutes Les Sessions

## REGLE 1 - Zero tirets longs
**JAMAIS** utiliser le caractere em dash (--), en dash (-) ou double tiret (--)
dans TOUT ce que Claude produit: texte visible, commentaires de code, JavaScript,
templates, fichiers de config, articles, memoires. Remplacer par: virgule,
deux-points, ou point. Cette regle s applique dans tous les projets, toutes
les sessions, Claude Code et Claude Chat.

## REGLE 2 - Toutes les langues
**TOUTE** modification de contenu ou de lien doit etre faite dans les 4 langues:
Francais (defaut, racine /), English (/en/), Espanol (/es/), Arabe (/ar/).
Ne jamais modifier une langue sans faire la meme chose dans les 3 autres.

---

# Real Estate Website Automation Workflow

## Project Overview
Personal real estate broker website for **georgesmatar.ca** - automated content publishing system where user provides Word documents and Claude handles all website updates.

**Owner:** George Smatar  
**Email:** georgesmatar92@gmail.com  
**Publishing Frequency:** 3 articles per week  
**Tech Stack:** Hugo (static site generator) + GitHub Pages + Custom Domain

---

## Core Philosophy
**User's Role:** Write articles in Word, provide property listings, send to Claude  
**Claude's Role:** Convert everything, push to GitHub, deploy to live website  
**Goal:** Minimize user's technical workload to near zero

---

## Workflow Process

### Article Publishing Workflow (Most Common Task)

**Input:** Microsoft Word document (.docx)  
**Output:** Live article on georgesmatar.ca with auto-sourced photos

**Steps Claude Executes Automatically:**
1. ✅ Read the Word document provided
2. ✅ Extract content and images using `/anthropic-skills:docx`
3. ✅ **Extract keywords from article content** (title, headings, key phrases)
4. ✅ **Search & download photos automatically:**
   - Query Unsplash API for relevant images
   - Query Pexels API for fallback images
   - Query Pixabay API for additional options
   - Query Wikimedia Commons for educational content
   - Select best matches (high quality, relevant, licensed for reuse)
5. ✅ **Optimize images for web** (resize, compress, convert to WebP)
6. ✅ Convert to Markdown format for Hugo
7. ✅ **Place images strategically** in article (after intro, between sections, before conclusion)
8. ✅ Create frontmatter (title, date, tags, categories)
9. ✅ Push to GitHub repository `/content/articles/` with all images
10. ✅ GitHub Pages auto-deploys (website updates in 2-3 minutes)
11. ✅ Confirm to user: "Article live at [URL]" + list of photos added

### Property Listing Workflow

**Input:** Property details + photos (can be in Word doc or email)  
**Output:** Dedicated property page on website

**Steps Claude Executes:**
1. ✅ Extract property info (price, beds, baths, description, address)
2. ✅ Process property images
3. ✅ Create property listing page
4. ✅ Push to GitHub `/content/listings/`
5. ✅ Auto-deploy
6. ✅ Generate property URL

---

## User Handoff Instructions

When the user sends you anything, assume this workflow:

### **Receiving an Article**
```
User sends: "Here's my article.docx"
Your action: 
  1. Read the .docx file using /anthropic-skills:docx
  2. Extract all text, existing images, and article metadata
  3. Extract 3-5 KEYWORDS from article (title + main topics)
  4. SEARCH & DOWNLOAD PHOTOS AUTOMATICALLY:
     - Use Unsplash API: search with keywords → download top 2-3 images
     - Use Pexels API: search with keywords → download 1-2 images
     - Use Pixabay API: search with keywords → download 1-2 images
     - Use Wikimedia Commons: search with keywords for educational content
     - Prioritize: high quality + relevant + different perspectives
     - Skip: watermarked, low resolution, or unsuitable images
  5. Optimize all photos (resize to max 1200px width, compress to <500KB)
  6. Save photos to /static/images/articles/[article-slug]/
  7. Convert to Markdown with Hugo frontmatter
  8. INSERT IMAGES strategically in markdown:
     - After intro paragraph (featured image)
     - Between major sections (supporting images)
     - Before conclusion (summary/conclusion image)
  9. Create file: /content/articles/[slug].md
  10. Commit to GitHub with message: "Article: [title] + [# of images] photos"
  11. Confirm deployment with photo count and sources
```

### **Receiving Property Listing**
```
User sends: Property details (Word doc or text)
Your action:
  1. Extract all property information
  2. Process images
  3. Create listing file: /content/listings/[address].md
  4. Commit to GitHub
  5. Send user the live URL
```

### **Receiving Bulk Updates**
```
User sends: Multiple articles + listings
Your action:
  1. Process each item separately
  2. Batch commit to GitHub
  3. Summarize all changes to user
  4. Provide links to all new content
```

---

## GitHub Repository Structure

```
georgesmatar-website/
├── content/
│   ├── articles/           # Blog posts (publish 3x/week)
│   │   └── *.md
│   ├── listings/           # Property listings
│   │   └── *.md
│   ├── _index.md           # Homepage
│   └── about.md            # About the broker
├── static/
│   ├── images/
│   │   ├── articles/       # Article images
│   │   └── listings/       # Property photos
│   └── favicon.ico
├── config.toml             # Hugo configuration
├── themes/                 # Website theme
└── README.md
```

---

## Automatic Photo Discovery & APIs

**Enabled Services (Free Tier):**
- **Unsplash API** - https://unsplash.com/api
- **Pexels API** - https://www.pexels.com/api/
- **Pixabay API** - https://pixabay.com/api/
- **Wikimedia Commons API** - https://commons.wikimedia.org/wiki/Special:ApiSandbox

**Photo Priority Order:**
1. Unsplash (primary - highest quality)
2. Pexels (secondary - good quality)
3. Pixabay (tertiary - reliable)
4. Wikimedia Commons (educational content)

**Image Selection Criteria:**
- ✅ **Quality:** Minimum 1920x1080px resolution
- ✅ **Relevance:** Matches article keywords/topic
- ✅ **License:** Free for reuse (CC0, CC-BY, Public Domain)
- ✅ **Diversity:** Different photographers/perspectives
- ✅ **Real Estate Focus:** Prefer interior/exterior/property-related

**Image Processing:**
- Resize to max 1200px width (maintain aspect ratio)
- Compress to <500KB using WebP or optimized JPEG
- Add alt text (extracted from article context)
- Rename with SEO-friendly format: `[article-slug]-[image-number].webp`

---

## Skills to Use

| Task | Skill | When |
|------|-------|------|
| Read Word documents | `/anthropic-skills:docx` | Whenever user provides .docx |
| Manage GitHub | Git + Bash | Commit, push, check status |
| Search APIs | WebFetch/Bash | Call Unsplash, Pexels, Pixabay, Wikimedia APIs |
| Handle images | Standard tools | Optimize, compress, rename images |
| Create/update content | Edit tool | Markdown files with image embeds |

---

## Content Guidelines for User

### Article Format (What User Should Know)
- **Title:** Clear, SEO-friendly
- **Length:** 800-1500 words typical
- **Format:** Any structure (listicle, guide, market analysis)
- **Images:** Include where helpful
- **Real estate focus:** Market trends, buying tips, local insights

### Listing Format (What User Should Provide)
- **Address**
- **Price**
- **Beds/Baths/Sqft**
- **Description** (why it's special)
- **Photos** (3-10 images)
- **Highlights** (bullet points)

---

## GitHub Commit Message Template

```
Article: [Title] - [Date]
or
Listing: [Address] - [Date]
or
Update: [What changed]
```

---

## Automation Behaviors

**When article is received:**
- ✅ Auto-extract keywords from content
- ✅ Auto-search Unsplash, Pexels, Pixabay, Wikimedia APIs
- ✅ Auto-download best-matching images (4-8 images per article)
- ✅ Auto-optimize images (resize, compress, convert to WebP)
- ✅ Auto-convert Word → Markdown
- ✅ Auto-place images strategically throughout article
- ✅ Auto-commit to GitHub with image count
- ✅ Auto-deploy (GitHub Pages handles this)
- ✅ Auto-notify user of live URL + photos added

**When listing is received:**
- ✅ Same as article process
- ✅ Search for listing-type photos (property, interior, exterior)
- ✅ Generate property-specific features
- ✅ Add to listings index
- ✅ Include downloaded images in listing

---

## Important Constraints & Preferences

1. **Always ask before:** Deleting anything, modifying homepage without approval, changing design
2. **Never:** Commit without clear message, push untested changes, lose images, commit API keys to code
3. **Default behavior:** If user sends Word doc → process it → push to GitHub (no approval needed)
4. **Error handling:** If conversion fails, show user the Word doc content and ask clarification
5. **API Keys:** Always store in GitHub Secrets or environment variables, never in code
6. **Image Attribution:** Ensure proper licensing/attribution for Wikimedia Commons images

---

## Setting Up Photo API Keys (One-Time Setup)

**Step 1: Create Free Accounts**
- Unsplash: Visit https://unsplash.com/api/register
- Pexels: Visit https://www.pexels.com/api/
- Pixabay: Visit https://pixabay.com/api/
- Wikimedia Commons: No registration needed

**Step 2: Get API Keys**
- Copy your API key from each service
- Keep them secure (never share or commit)

**Step 3: Store in GitHub Repository**
- Go to GitHub repo settings → Secrets and variables → Actions
- Add secrets:
  - `UNSPLASH_API_KEY`: [your key]
  - `PEXELS_API_KEY`: [your key]
  - `PIXABAY_API_KEY`: [your key]

**Step 4: Claude Code reads from environment**
- Access via: `$env:UNSPLASH_API_KEY` (PowerShell) or `$UNSPLASH_API_KEY` (Bash)
- Automatic in GitHub Actions workflows

**Note:** Free tier limits are generous (50-200 requests/hour) — enough for 3 articles/week

---

## Required Credentials & Access

**GitHub:**
- **Repository:** `georgesmatar/georgesmatar-website`
- **Domain:** georgesmatar.ca (already pointing to GitHub Pages)
- **GitHub Pages:** Auto-deploys from main branch

**Photo API Keys (Free Tier - No Payment Required):**
- **Unsplash API Key:** [Store in .env or GitHub Secrets]
  - Get at: https://unsplash.com/api/register
  - Free tier: 50 requests/hour
- **Pexels API Key:** [Store in .env or GitHub Secrets]
  - Get at: https://www.pexels.com/api/
  - Free tier: 200 requests/hour
- **Pixabay API Key:** [Store in .env or GitHub Secrets]
  - Get at: https://pixabay.com/api/
  - Free tier: 50 requests/hour
- **Wikimedia Commons:** No API key needed (public)
  - Access at: https://commons.wikimedia.org/wiki/Special:ApiSandbox

**Setup Instructions:**
1. Create free accounts at Unsplash, Pexels, Pixabay
2. Generate API keys
3. Store keys in GitHub Secrets (never commit to code)
4. Claude Code reads from environment variables

---

## Contact Information for Admin Tasks

- **Email:** georgesmatar92@gmail.com
- **GitHub:** [User's GitHub username]
- **Domain Registrar:** [Where georgesmatar.ca is registered]

---

## Performance Targets

- **Per article:** 15-20 minutes (includes auto-photo search + download + optimization)
  - Photo search & download: 5-7 minutes
  - Image optimization: 2-3 minutes
  - Markdown conversion: 2-3 minutes
  - GitHub push & deploy: 2-3 minutes
- **Per listing:** 20-25 minutes (more complex with property photos)
- **Website load time:** <2 seconds (Hugo static = fast, even with optimized images)
- **Uptime:** 99.9% (GitHub Pages reliability)
- **API Reliability:** 99%+ (Unsplash, Pexels, Pixabay, Wikimedia)

---

## FAQ for Claude

**Q: User sends a Word doc. What do I do?**  
A: Extract keywords → Search APIs for photos → Download/optimize → Convert to Markdown → Add images → Push to GitHub → Done. No approval needed.

**Q: User sends multiple files at once?**  
A: Process each independently (search photos for each, optimize, add to content), batch commit with summary.

**Q: What if photo search returns no results?**  
A: Try alternative keywords, fallback to different API (Pexels → Pixabay), or proceed without adding photos if absolutely necessary (rare).

**Q: Image sizes too large?**  
A: Resize to max 1200px width, compress to <500KB. Convert to WebP for best compression.

**Q: Article already has images - what do I do?**  
A: Keep user's images + add supplementary photos from APIs. Mix both for best results.

**Q: How many photos per article?**  
A: 4-8 photos depending on article length. 1 featured image (top) + 1-2 per major section + 1 before conclusion.

**Q: Which API to prioritize?**  
A: Unsplash first (best quality) → Pexels → Pixabay → Wikimedia Commons (educational).

**Q: What about licensing/attribution?**  
A: All four sources provide free-to-use images (CC0/CC-BY). Wikimedia Commons requires minimal attribution in image alt text.

**Q: Article has formatting I can't preserve in Markdown?**  
A: Use HTML in Markdown, or ask user to simplify.

**Q: Website not updating after push?**  
A: GitHub Pages might need 2-3 minutes. Check GitHub Actions. If still broken, troubleshoot.

**Q: API rate limits exceeded?**  
A: Wait 1 hour for limit reset, or use fallback API. Log the error and notify user.

---

## Future Enhancements (Out of Scope Now)

- SEO optimization automation
- Social media auto-posting (LinkedIn, Instagram)
- Email newsletter integration
- Advanced analytics dashboard
- MLS API integration for auto-listing updates
- AI-powered photo caption generation
- Automatic article summarization for social media

---

---

## Automatic Photo Workflow Summary

**You send:** Article in Word format  
**Claude Code does:**
1. Reads your article
2. Extracts keywords (title, topics, themes)
3. Searches 4 photo websites simultaneously
4. Downloads best matching photos (4-8 per article)
5. Optimizes images for web speed
6. Inserts images throughout article
7. Pushes everything to GitHub
8. Website updates automatically in 2-3 minutes

**Result:** Professional article with beautiful, relevant photos - all automatic! ✨

---

**Last Updated:** 2026-05-18 (Updated with Automatic Photo Discovery)  
**Status:** Ready for production with auto-photo feature  
**Next Steps:** Get API keys + User provides first article → Full automation begins!
