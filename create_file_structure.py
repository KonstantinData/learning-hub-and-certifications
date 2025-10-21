"""
Script: setup_learning_hub_structure.py
Purpose: Creates the folder structure for an existing repo 'learning-hub-and-certifications'
without duplicating the root folder.
Author: Konstantin Milonas
"""

import os

# Work inside the current directory (assuming you're already in the repo)
root = "."

folders = [
    "01_Active_Modules/DeepLearning.AI_Agentic_AI_Engineering",
    "01_Active_Modules/Tableau_Data_Analyst_Certification",
    "01_Active_Modules/Coursera_AI_for_Everyone",

    "02_Certificates/DeepLearning.AI",
    "02_Certificates/Google",
    "02_Certificates/Vanderbilt_University",
    "02_Certificates/Stanford_University",
    "02_Certificates/DataCamp",
    "02_Certificates/LinkedIn_Learning",
    "02_Certificates/Tableau",

    "03_Planned_Learning/AI_Agent_Systems",
    "03_Planned_Learning/Cloud_Data_Platforms"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

readme_content = """# 📘 Learning Hub & Certifications

This repository documents the continuous learning path of **Konstantin Milonas** in the fields of **Data Analytics, AI, MLOps, and Cloud Data Platforms**.

## Structure
1. **Active Modules** – Ongoing courses, certifications, and notes.
2. **Certificates** – Completed and verifiable training programs.
3. **Planned Learning** – Future topics and skill focus areas.

---

## 🚀 Current Focus
- Agentic AI Workflows (DeepLearning.AI)
- Tableau Certified Data Analyst
- Advanced Python & MLOps Foundations
- Responsible AI & Prompt Engineering

---

## 🧾 Certificate Overview

| Year | Provider | Certificate | Focus |
|------|-----------|-------------|--------|
| 2025 | DeepLearning.AI | AI Python for Beginners | Python, AI Fundamentals |
| 2025 | Google | AI Essentials | Responsible AI, LLMs |
| 2025 | Vanderbilt University | Advanced Prompt Engineering | LLM Orchestration |
| 2025 | Stanford University | Supervised Machine Learning | Regression, Classification |
| 2024 | DataCamp | Tableau Analytics Suite | Visualization, KPI Reporting |

---

> This repository reflects an evolving learning path – bridging Data Analytics, Business Understanding, and AI-Driven Decision-Making.
"""

readme_path = os.path.join(root, "README.md")

# Create README.md only if not already existing
if not os.path.exists(readme_path):
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✅ README.md created.")
else:
    print("ℹ️ README.md already exists — skipped creation.")

print("✅ Folder structure created inside the existing repo.")
