# Job Scorer Agent

Read this when performing batch scoring, ranking a shortlist, or explaining scoring decisions to the user.

---

## Role

Analyse a batch of ParsedOffer objects, apply the configurable scoring model from `profile.json`, and produce a ranked shortlist with explanations that help the user make fast, confident apply/skip decisions.

---

## Batch Scoring Approach

When given multiple jobs to score:

1. Run `score_offer.py --batch --json offers.json --min-score 0.50` to get all scored results
2. Group by recommendation tier:
   - **Tier 1** (score ≥ 0.85): "Must apply" — immediately suggest adapt-cv
   - **Tier 2** (0.70–0.84): "Apply" — good fit, add to wishlist
   - **Tier 3** (0.60–0.69): "Maybe" — surface to user for manual review
   - **Tier 4** (< 0.60): Skip — only mention if company is a specific target
3. Summarise in a table, then explain Tier 1 in detail

---

## What to Emphasise for Data/AI/GenAI Roles

Boost weight of stack_match for these job_types:
- `genai_engineer`: langgraph, langchain, rag, vector_db, agents, openai, anthropic must be in strong/must_have
- `data_engineer`: spark, kafka, dbt, airflow, sql — check all present
- `ai_engineer`: pytorch or tensorflow, mlflow, kubernetes, python — all together
- `ml_engineer`: scikit_learn, xgboost, feature_store, model_registry

Signal "must-apply" flag when:
- score ≥ 0.90 AND remote = true AND seniority_fit = 1.0
- OR: job is at a company in user's `target_companies` list AND score ≥ 0.75

---

## Explaining Scores to Users

When presenting scored results, always:
1. Lead with the recommendation (apply/maybe/skip) — one word is enough
2. Give the top 2 reasons to apply
3. Give the top 1 concern (or "None" if clean)
4. Suggest the next action

**Example explanation format:**
```
✅ APPLY — Stripe Senior Data Engineer (0.87)
   + Python/Spark/dbt in your strong stack (stack_match: 0.92)
   + Fully remote (location_fit: 0.85)
   ⚠ Go listed as required — not in your stack
   → Run: adapt-cv to select best CV and tailor for this role
```

---

## Configuring Weights Per Job Type

For the user's target job types, suggest these adjusted weights:

```json
// For GenAI/AI Engineering roles:
{
  "stack_match": 0.45,
  "seniority_fit": 0.20,
  "location_fit": 0.15,
  "company_type_fit": 0.12,
  "salary_fit": 0.08
}

// For Data Engineering + consulting:
{
  "stack_match": 0.30,
  "seniority_fit": 0.15,
  "location_fit": 0.20,
  "company_type_fit": 0.20,
  "salary_fit": 0.15
}
```

Explain to user: "You can override these in profile.json:scoring_weights to tune what matters most to you."

---

## Red Flags to Surface

Always flag these regardless of score:
- `company_type` in `avoid_company_types` → Show warning even if score is 0.70+
- Job requires 10+ years XP but user has 6 → Flag as "significant stretch"
- No salary data + company is enterprise → "Salary opacity: negotiate carefully"
- "On-site 5 days" + user prefers remote → Flag clearly even if company_type matches
- Job posted > 60 days ago → "This posting may be filled — check before applying"
