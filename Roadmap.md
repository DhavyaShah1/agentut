# AI / ML / Data Career Roadmap — July to December 2026
### Target: Internship-ready and earning by December 31, 2026

**Your starting point:** 5th-semester (3rd-year) engineering student · Python basics, DSA theory, supervised ML theory, unsupervised ML in progress · pandas/numpy/matplotlib · one project (Customer Churn — logistic regression + XGBoost) · India market · 25 hrs/week (3 hrs weekdays, 5 hrs weekends) ≈ 600 hours over 6 months.

**Lucky timing:** this semester your college is teaching DBMS, Data Analytics, ML, and GenAI/Agentic AI. That's almost exactly this roadmap's core. Let college give you the theory pass; use your 25 hrs/week to turn it into things you've actually built and can defend in an interview.

**Working assumption:** since you're still in 6th semester (Jan–May 2027) after Dec 31, this plan targets remote or part-time internships — the realistic path for a full-time student — not on-campus placement drives (those hire for summer 2027). Say so if that's wrong.

---

## 1. The Strategy

Build one deep shared foundation for three months. Branch into your preferred roles (AI Engineer, ML Engineer, Data Engineer) for three more. Stay naturally eligible for Data Science, Analytics, and Applied AI throughout, because the foundation overlaps almost entirely with those too.

**Why not go deep on all six from month one:** a Data Engineer's core stack (SQL, orchestration, warehousing, Spark) and an AI Engineer's core stack (LLMs, RAG, agents) are genuinely different specializations once you get past the fundamentals. Splitting 25 hrs/week six ways from day one means shallow everywhere in December. Splitting it two ways — foundation, then two or three specializations — means genuinely competitive somewhere.

**DSA is not a "month."** It's a standing weekly habit from July through December, 2–3 hrs/week, because it's a skill built by spaced repetition, not by cramming. You don't need FAANG-level DSA for these roles — you need to comfortably clear a screening round. Real Indian ML/AI internship postings researched for this plan list "Data Structures" as a named skill tag, so it's not optional, but it's also not the main event — your projects are.

---

## 2. Where the Market Actually Is (July 2026)

**AI Engineer:** the hottest-growing title in tech right now — postings up roughly 143% year-over-year. The role has shifted from "someone who fine-tunes models" to someone who ships full AI-powered products: APIs, RAG, agents, deployment, cost/latency tradeoffs. Employers increasingly want strong software engineering fundamentals (APIs, system design basics, reliability) *plus* GenAI fluency — not GenAI knowledge alone.

**ML Engineer:** classical ML mastery (ensembles, regularization, evaluation metrics) is table stakes; what differentiates candidates now is being comfortable taking a model from notebook to a deployed, monitored service (Docker, an API layer, basic cloud).

**Data Engineer:** India has an enormous, still-growing shortage — one report puts open positions above 36,000. The bar is narrower than people think: real SQL fluency, comfort reading someone else's schema, and depth in *one* cloud/orchestrator beats broad shallow tool-collecting. Fresher full-time pay at GCCs/product companies: roughly ₹6–14 LPA. PySpark + one of (Azure/AWS/GCP) + Snowflake or BigQuery + dbt is the current default stack.

**Data Analyst / Data Scientist:** NASSCOM projects India will need over 1–1.3 million data professionals by 2026. This is the most accessible entry point of the six — Excel (XLOOKUP, Power Query), SQL, Python, and Power BI or Tableau, plus the ability to explain findings in plain business language. Fresher pay: roughly ₹4–6.5 LPA, reaching ₹6–9 LPA with a strong SQL+Python+PowerBI portfolio.

**The GCC wave (this matters a lot for you specifically):** Global Capability Centres (in-house tech centers for global companies) are now India's biggest tech hiring engine — bigger than IT services firms. Roughly 64% of new GCC roles created in 2026 require AI, data science, or automation skills, and AI/Data roles are GCCs' fastest-growing function (+38% YoY). Critically: a majority of GCCs say they're increasing *fresher* hiring, often through hackathons and internship pipelines rather than traditional recruiting. This is a real, current channel for someone in your position — not just a campus-placement thing.

### The 6-months-out signal
Agentic AI is the clearest growth curve in the entire field. Gartner projects 40% of enterprise applications will include task-specific AI agents by end of 2026, up from under 5% in 2025. The global AI agent market is projected to grow from ~$7.8B (2025) to ~$52.6B by 2030. Over half of Indian GCCs already report investing in agentic AI, and the large majority are scaling generative AI projects. Model Context Protocol (MCP) — the open standard for connecting AI models to tools and data — has gone from Anthropic-specific to industry-wide, now under Linux Foundation stewardship and supported by essentially every major agent framework. By December, "I built a RAG app" will be a common portfolio line; "I built something agentic that uses tools" will still stand out.

**Framework consensus for 2026:** PyTorch is the default recommendation for students and new projects (85% of DL research papers, the Hugging Face ecosystem, and most GenAI tooling are PyTorch-first); TensorFlow still matters for enterprise/mobile deployment but isn't where you should start. For agents: CrewAI has the gentlest learning curve (a working prototype in an afternoon) and LangGraph is the production-grade standard for anything needing state, branching, or reliability — learning both, in that order, is a sound path.

---

## 3. What This Means For Your Plan

- **SQL is your highest-ROI single skill.** It's the one thing every one of your six target roles uses daily, and your DBMS course gives you a head start most self-taught learners don't get. Push it past "theory" into real fluency early.
- **Your existing churn project is a liability until you can defend it.** Interviewers will ask "why XGBoost over Random Forest," "how did you handle class imbalance," "what does this confusion matrix actually tell you." A project you can't explain line-by-line is worse than no project — it signals AI-generated work the moment you're probed. Fix this in month 1, not month 5.
- **Agentic AI is your differentiator, not a nice-to-have.** It's rare among entry-level candidates, it's exactly what GCCs and startups are scrambling to hire for, and your college course gives you a running start. Weight your project time toward it.
- **Deep learning math gets fixed early, deliberately.** You said DL math is still hard — that's exactly the thing that becomes a wall once you start transformers/attention in month 3. Front-load it in months 1–2 with visual/intuitive resources, not textbook derivations.

---

## 4. Complete Skill Checklist

### Programming & Software Engineering
- [ ] Python: OOP (classes, inheritance), exceptions, file I/O, comprehensions, virtual environments
- [ ] Writing modular, readable code (not notebook spaghetti)
- [ ] Git & GitHub: branches, commits, PRs, a genuinely clean profile
- [ ] REST API basics: consuming and building simple APIs (requests, Flask/FastAPI)
- [ ] DSA: arrays, strings, hashmaps, recursion, sorting/searching, basic trees, basic graphs, Big-O — target 120–150 problems (Easy/Medium) by December

### SQL & Databases
- [ ] Core: SELECT, WHERE, GROUP BY, all JOIN types, subqueries
- [ ] Intermediate/advanced: window functions (RANK, ROW_NUMBER, LAG/LEAD), CTEs, query optimization basics
- [ ] Hands-on with a real database (PostgreSQL or MySQL), not just theory
- [ ] Comfortable reading and explaining someone else's messy 100+ line query

### Math for ML/DL
- [ ] Linear algebra & probability/stats for classical ML (you're already fairly solid here)
- [ ] Deep learning math: backpropagation and chain rule intuition — visually, not just formulas
- [ ] Attention mechanism intuition (needed before transformers make sense)
- [ ] Core stats for DS/DA: hypothesis testing, distributions, confidence intervals, correlation vs. causation

### Classical ML (deepen, don't relearn)
- [ ] Finish unsupervised ML course (clustering, PCA/dimensionality reduction, anomaly detection)
- [ ] Ensemble methods: bagging vs. boosting, why XGBoost works
- [ ] Regularization (L1/L2), hyperparameter tuning (GridSearch/RandomSearch/Optuna)
- [ ] Imbalanced data handling (SMOTE, class weights) — directly relevant to your churn project
- [ ] Evaluation metrics beyond accuracy: precision/recall/F1/ROC-AUC, confusion matrix interpretation

### Deep Learning
- [ ] Neural network fundamentals: forward/backward pass, activation functions, loss functions
- [ ] PyTorch: tensors, autograd, building/training a model from scratch
- [ ] CNNs (light touch — you're not targeting computer vision specifically)
- [ ] Transformers & self-attention (this is the one that matters most for your GenAI track)

### Generative AI
- [ ] How LLMs work at an applied level: tokenization, embeddings, context windows
- [ ] Prompt engineering: few-shot, chain-of-thought, system prompts
- [ ] Using LLM APIs programmatically (OpenAI, Anthropic, or Hugging Face/Ollama for local models)
- [ ] RAG: vector databases (Chroma/FAISS to start; Pinecone/Weaviate are the production names), chunking strategy, retrieval pipelines
- [ ] Fine-tuning concepts (LoRA/QLoRA) — conceptual understanding, not required to actually fine-tune

### Agentic AI
- [ ] What makes a system "agentic" (plans, uses tools, observes, adjusts) vs. a plain LLM call
- [ ] Build a first agent with CrewAI (fastest path to something working)
- [ ] Build a second, more controlled agent with LangGraph (state, branching, retries)
- [ ] MCP (Model Context Protocol) — what it is and why it's become the standard for connecting agents to tools/data

### Data Engineering
- [ ] ETL vs. ELT concepts
- [ ] Orchestration basics (Airflow — still the industry default)
- [ ] PySpark fundamentals (dominant in Indian data engineering job postings)
- [ ] One cloud platform in depth (AWS recommended — broadest adoption in Indian startups; Azure is stronger in enterprise/legacy shops)
- [ ] Data warehousing basics: star schema, one of Snowflake/BigQuery/Redshift

### MLOps / Deployment
- [ ] Serving a model via FastAPI (preferred over Flask for new projects in 2026)
- [ ] Docker: containerizing an app
- [ ] Basic experiment tracking (MLflow or Weights & Biases)
- [ ] Deploying to a free-tier host (Render, Railway, or Hugging Face Spaces for GenAI demos)

### Career Skills
- [ ] Resume tailored to AI/ML/Data roles with quantified project outcomes
- [ ] GitHub with pinned, well-documented repos (clear problem → approach → result in every README)
- [ ] LinkedIn profile optimized for recruiter search
- [ ] Comfortable explaining every project end-to-end, unscripted

---

## 5. Month-by-Month Roadmap

*Indian college exam calendars vary — swap any "new content" week below for a revision-only week whenever your mid-sems/end-sems actually land, and slide that week's content forward. Buffer is loosely built into September and November for this reason.*

### July — Foundation Sprint
| Area | Hrs/wk |
|---|---|
| SQL fundamentals | 5 |
| Python (OOP, Git/GitHub) | 4 |
| DSA (arrays, strings, hashmaps) | 3 |
| Finish unsupervised ML course | 3 |
| DL math intuition (visual resources) | 3 |
| Rebuild churn project (deep understanding) | 4 |

**By end of month:** write 20+ SQL queries with joins from scratch without looking things up · explain backpropagation in your own words · churn project rebuild underway, and you can justify every choice in it.

### August — Deepen ML, Start PyTorch
| Area | Hrs/wk |
|---|---|
| SQL (window functions, CTEs) + practice problems | 4 |
| Classical ML deepening (imbalance, tuning, metrics) | 4 |
| DSA (sorting, recursion, intro trees) | 3 |
| PyTorch fundamentals | 4 |
| Finish + deploy churn project | 5 |

**By end of month:** churn project live (simple deployment) and interview-defensible · trained a basic neural net in PyTorch from scratch · comfortable with SQL window functions.

### September — Deep Learning Core + Data Engineering Project Begins
| Area | Hrs/wk |
|---|---|
| Transformers/attention intuition | 4 |
| Data engineering project (ETL → Postgres) | 6 |
| DSA (trees, graph basics) | 3 |
| GenAI fundamentals (tokenization, embeddings, first API calls) | 4 |
| Resume v1 + LinkedIn setup | — |

*Mid-sem exams likely land here — prioritize revision over new content if they clash.*

**By end of month:** data pipeline project functional end-to-end · can explain self-attention at a working level · made your first programmatic LLM API calls.

### October — RAG + Start Applying
| Area | Hrs/wk |
|---|---|
| RAG project (vector DB, embeddings, chunking) | 6 |
| Docker + AWS basics | 4 |
| Polish + document data engineering project | 3 |
| DSA (medium problems) | 3 |
| **Start applying** (Internshala, LinkedIn, Wellfound) | 3 |

**By end of month:** RAG app deployed (HF Spaces/Streamlit Cloud) · first internship applications sent — don't wait until "fully ready."

### November — Agentic AI + Applications Ramp Up
| Area | Hrs/wk |
|---|---|
| Agentic AI: CrewAI first, then LangGraph | 6 |
| MCP conceptual understanding + one integration | 2 |
| Applications (10–15/week) + hackathons (Unstop) | 4 |
| Mock interviews (technical + behavioral) | 3 |

*End-sem exams may land here too — same rule: revision takes priority.*

**By end of month:** agentic project live · 40+ cumulative applications sent · 3–4 mock interviews done.

### December — Final Push
| Area | Hrs/wk |
|---|---|
| Polish all project READMEs + portfolio | 4 |
| Heavy interview prep (DSA patterns, SQL, ML/DL concepts, project stories) | 6 |
| Continued applications + follow-ups | 4 |
| Mock interviews | 3 |

**Target:** offer in hand by Dec 31, or at minimum an active interview pipeline built from six months of real, defensible work.

---

## 6. Project Portfolio

Four to five well-built projects beat nine shallow ones. This set cross-covers all six target roles without spreading you too thin:

| # | Project | Demonstrates | Supports |
|---|---|---|---|
| 1 | Customer Churn (rebuilt from scratch understanding) | EDA, classical ML, imbalanced data, basic deployment | Data Science, Analytics, ML Engineer |
| 2 | End-to-end data pipeline (public API/dataset → ETL → Postgres → dashboard) | SQL, Python, orchestration, warehousing basics | Data Engineer, Analytics |
| 3 | Deep learning project (PyTorch, transfer learning) | Neural nets, framework fluency | ML Engineer, AI Engineer |
| 4 | RAG application (chat over a custom document set) | LLMs, embeddings, vector DB, prompt engineering | AI Engineer, Applied AI |
| 5 | AI agent (tool-using, e.g. a research or automation assistant) | Agent frameworks, MCP | AI Engineer, Applied AI |

Deploy every one of them somewhere live (even a free-tier host) — a GitHub link with a working demo attached is worth far more than a notebook.

---

## 7. Application Strategy (India)

**Portals:** Internshala (the default for Indian internships, strong remote/WFH filter), LinkedIn, Naukri, Wellfound/AngelList India (startups), Unstop and Devfolio (hackathons — a genuine hiring channel, not just competition), Cutshort, Instahyre.

**Don't ignore GCCs.** Companies like Walmart Global Tech, Target India, JPMorgan, Goldman Sachs, and hundreds of others run large India-based tech centers that are actively expanding fresher/intern hiring, often through hackathons rather than formal drives. Worth tracking their career pages directly alongside the portals above.

**Realistic stipend range:** roughly ₹5,000–25,000/month depending on company stage, with real postings researched for this plan showing ₹7,500–15,000/month as a reasonable benchmark for a solid remote ML/AI internship. Some early-stage startups offer unpaid internships — avoid these where you have alternatives, since your goal is specifically to *start earning*.

**Timing:** start applying in October once your baseline portfolio (projects 1–3) is ready. Don't wait for "complete." Application-to-offer cycles take weeks; the more cycles you run before December, the better your odds by the 31st.

**Track everything** — a simple spreadsheet (company, role, date applied, status, follow-up date) prevents the process from becoming a blur by month 5.

---

## 8. Resources

**Deep learning math/intuition:** 3Blue1Brown's neural network series (YouTube, visual) · Andrej Karpathy's "Neural Networks: Zero to Hero" (build backprop and a GPT from scratch) · StatQuest for stats and ML explained simply

**PyTorch:** official PyTorch tutorials (pytorch.org)

**SQL:** Mode Analytics SQL tutorial (free, structured) · LeetCode SQL 50 · StrataScratch (realistic interview-style questions)

**DSA:** NeetCode (roadmap + explained solutions) · Striver's A2Z DSA course (widely used in India) · GeeksforGeeks

**GenAI/RAG:** DeepLearning.AI's short courses (many specifically on RAG, LangChain, prompt engineering) · LangChain and LlamaIndex official docs

**Agentic AI:** CrewAI docs (fastest starting point) · LangGraph official tutorials · docs.claude.com for Anthropic's tool-use/MCP documentation

**Data Engineering:** Airflow official docs · a free-tier PostgreSQL setup for practice

---

## 9. Long Term: Toward the Startup

Nothing in this roadmap is wasted on the startup goal, even though it's framed around an internship. SQL and data engineering teach you how real systems hold up under messy data. Classical ML and deep learning teach you what's actually happening inside the models you'd be building a product around. AI and agentic engineering teach you how to ship AI *products*, not just AI experiments — which is the exact skill gap most technical co-founders have. The internship itself will teach you things no amount of self-study can: how real teams scope work, review code, and ship under deadlines. Treat the next six months as the technical foundation you'll eventually build on, not just a credential to collect.

---

## 10. Weekly Rhythm

Different skills have different practice shapes. Some want small daily doses (spaced repetition — DSA). Some want long uninterrupted blocks (flow-state work — projects, a genuinely new complex concept). Trying to slice everything into every single day fragments your attention and kills the deep-work items. This rhythm stays constant July–December; only the *content* of the rotating focus block changes month to month per Section 5.

**Weekdays (3 hrs) — daily anchor + one rotating focus**
- 45 min–1 hr: DSA, every day, non-negotiable
- ~2 hrs: one focus block, alternating — Mon/Wed/Fri new concept for the month, Tue/Thu project work

**Weekends (5 hrs/day) — the deep blocks**
- One real 2–3 hr sitting on SQL (new topic, not review) — SQL lives mostly here since it's modular and your DBMS course gives ambient weekday exposure
- The other big chunk: project sprints (debugging/building need the longer canvas)
- ~15 min: check progress against the week's milestone, set next week's focus

**Decay check:** one random weekday, solve one SQL problem cold (no notes) before starting DSA — not a study session, just an early warning if something's slipping.

## 11. How to Validate You Actually Know It

The real test is three questions: can you do it **cold** (no notes/Google/AI), on something **slightly different** from what you practiced, and **explain it to someone else** in plain words? Failing any of the three means you've recognized it, not learned it.

- **DSA:** unseen problems, timed, no hints. A monthly LeetCode/HackerRank contest as a gut-check.
- **SQL:** an unfamiliar schema, not your own practice one — StrataScratch and LeetCode SQL are built for this.
- **ML theory:** the Feynman test — explain *why* (e.g. why XGBoost beats a single tree) with zero jargon, as if to a smart 12-year-old.
- **Projects:** rebuild the core pipeline from memory, no old code open. Defend every choice under questioning. Extend it with one new feature on the spot.
- **GenAI/agentic:** deliberately break something and fix it — following a tutorial proves you can follow instructions, debugging a silent failure proves you understand it.
- **Cross-cutting:** mock interviews, a hackathon entry, posting a project publicly and taking questions. Self-review has blind spots that outside pressure exposes.
