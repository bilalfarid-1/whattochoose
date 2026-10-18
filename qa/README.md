# QA & SDET Engineering Suite (JobPulse System Under Test)

[![Interactive Dashboard](https://img.shields.io/badge/Dashboard-30__Day__QA__Roadmap__Pro.html-blue.svg)](30_Day_QA_Roadmap_Pro.html)
[![Curriculum](https://img.shields.io/badge/Curriculum-60%20Days%20Complete-success.svg)](30_day_job_ready_qa_roadmap.md)
[![SUT Contract](https://img.shields.io/badge/SUT%20Contract-20%20Operations-orange.svg)](jobpulse_sut_contract.md)
[![Interview Handbook](https://img.shields.io/badge/Interview%20Handbook-35%20Technical%20Q%26As-purple.svg)](qa_interview_handbook.md)
[![AI Mentor](https://img.shields.io/badge/AI%20Mentor-%2Fqa--sprint-brightgreen.svg)](skill/SKILL.md)

Welcome to the **QA & SDET Engineering Suite**. This directory contains the complete, production-grade quality engineering curriculum, test design matrices, automation frameworks, interview defense handbooks, and interactive dashboards designed to take an aspiring engineer from manual QA fundamentals to a verifiable, full-stack SDET.

All exercises and automation suites in this curriculum are grounded in **[JobPulse](../backend)**, our production-style multi-tenant FastAPI backend service.

---

## 🏛️ Suite File Map & Navigation

Every asset in this suite is self-contained and locally accessible:

| Asset | File | Description |
| :--- | :--- | :--- |
| 🖥️ **Master Dashboard** | [`30_Day_QA_Roadmap_Pro.html`](30_Day_QA_Roadmap_Pro.html) | Standalone interactive dashboard covering all 60 days, 5 subtasks per day, 9 weekly strategy banners, and 1-click prompt copiers. Double-click to open in any browser. |
| 📋 **SUT Contract** | [`jobpulse_sut_contract.md`](jobpulse_sut_contract.md) | Authoritative operational specification for JobPulse: all 20 REST operations across 13 path templates, auth semantics, and multi-tenant BOLA policies. |
| 📅 **Core 30-Day Roadmap** | [`30_day_job_ready_qa_roadmap.md`](30_day_job_ready_qa_roadmap.md) | Foundational 30-day curriculum: STLC, EP/BVA, Postman, Python/pytest, SQL verification, multi-user authorization, Playwright UI, and CI/CD (108–112 focused hours). |
| 🚀 **Days 31–60 Extension** | [`days_31_60_qa_automation_extension.md`](days_31_60_qa_automation_extension.md) | Advanced SDET depth: API maintainability, contract validation, Playwright Trace diagnostics, BOLA hardening, CI reporting, and 4 specialization tracks. |
| 🎤 **Interview Handbook** | [`qa_interview_handbook.md`](qa_interview_handbook.md) | 35 technical questions with model answers, STAR behavioral stories, BOLA defense, and flaky test triage rubrics. |
| 📊 **Market Research** | [`qa_sdet_market_analysis.md`](qa_sdet_market_analysis.md) | Empirical labor market research synthesizing hiring requirements, AI testing transitions, and skill lifecycle data. |
| 🤖 **AI Mentor System Prompt** | [`skill/SKILL.md`](skill/SKILL.md) | Autonomous prompt configuring ChatGPT or Antigravity into Lead SDET, Adversarial QA, or Socratic Interviewer modes. |
| 📈 **Progress Tracker** | [`skill/progress_tracker.md`](skill/progress_tracker.md) | 60-day tabular progress tracker recording completion dates, deliverables, and bug counts. |
| 🗄️ **Legacy Redirect** | [`30_day_qa_sdet_hands_on_roadmap.md`](30_day_qa_sdet_hands_on_roadmap.md) | Redirect-style stub preserving backward compatibility with legacy links. |

---

## ⚙️ The System Under Test (JobPulse)

All test design, exploratory charters, Postman collections, Pytest suites, and Playwright UI scripts target the **JobPulse API** located in [`../backend`](../backend).

### SUT Specifications
* **Runtime:** Python 3.12 + FastAPI + Uvicorn
* **Database:** SQLite (local development) / PostgreSQL 16 (containerized) via SQLAlchemy 2.0 & Alembic
* **Authentication:** OAuth2 Password Bearer flow returning signed JWTs (`/api/v1/auth/token`) + standard JSON login (`/api/v1/auth/login`)
* **Security Model:** Strict multi-tenant row-level ownership. When User B queries User A's application, the API returns `HTTP 404 Not Found` (non-disclosing policy to prevent resource enumeration).

To boot the SUT for testing:
```bash
cd ../backend
pip install -r requirements.txt
alembic upgrade head
python -m uvicorn app.main:app --reload --port 8000
```
Swagger UI will be live at `http://127.0.0.1:8000/docs`.

---

## ⏱️ The 4-Hour Daily Operating Routine

Every standard study day is structured into 5 disciplined blocks:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE 4-HOUR STUDY BLOCK                          │
├──────────────┬──────────────┬──────────────────┬──────────────┬────────┤
│ Learn (45m)  │ Practice (45m)│   Build (105m)   │ Explain (30m)│Commit  │
│ Deep Concept │ Micro-drills │ Production Code  │ Socratic QA  │(15m)   │
└──────────────┴──────────────┴──────────────────┴──────────────┴────────┘
```

1. **Learn (45m):** Study official documentation (ISTQB CTFL syllabus, RFC 9110 HTTP specs, Pytest fixtures, Playwright locators).
2. **Practice (45m):** Targeted micro-drills against JobPulse endpoints or database tables.
3. **Build (105m):** Author production-grade test artifacts (test matrices, Postman JSON, Pytest files, Playwright scripts).
4. **Explain (30m):** Closed-book oral defense or chat interview drill using [`qa_interview_handbook.md`](qa_interview_handbook.md).
5. **Commit (15m):** Git commit with conventional commit format, check off subtasks in [`30_Day_QA_Roadmap_Pro.html`](30_Day_QA_Roadmap_Pro.html), and export JSON progress backup.

---

## 🤖 The 2-Tool Workflow (Dashboard + AI Chat)

You only need **two tools** to execute this curriculum:
1. **In Browser:** Open [`30_Day_QA_Roadmap_Pro.html`](30_Day_QA_Roadmap_Pro.html) to view the roadmap, track your subtasks, and click the 1-click prompt copiers.
2. **In Chat (ChatGPT or Antigravity):** Paste prompts to trigger `/qa-sprint`. The AI will guide your study, audit your deliverables against [`jobpulse_sut_contract.md`](jobpulse_sut_contract.md), and conduct mock interviews.

If you are giving this repository to an AI assistant, provide it with the system prompt in [`skill/SKILL.md`](skill/SKILL.md).
