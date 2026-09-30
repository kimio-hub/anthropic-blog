# Writing the article

The style works because the writing does most of the explaining. Draft the text before the page.

## Reading promise

Write one sentence the reader should be able to say after reading: an explanation they can repeat or a
judgement they can make. Deliver something useful in the first screen: the question, why it matters to
this reader, and what the piece offers. No sweeping "in today's fast-moving world" openings.

## Pick a narrative skeleton

These are scalable spines, not fixed heading lists.

| Content | Progression | The reader leaves with |
|---|---|---|
| Explaining a complex issue | Question → one concrete case → minimal mechanism → what changes it → consequences → limits | A model to think with |
| Engineering lesson | Judgement up front → terms and scope → building blocks → patterns compared on the same axes → operating advice → appendix | Grounds for choosing an approach |
| Research finding | Phenomenon → prior expectation → evidence → mechanism → counter-examples and limits → open questions | The finding and how strong the evidence is |
| Interactive explainer | Open question → concrete case taught step by step → invite the reader to change assumptions → findings one by one → limits and method | A mechanism they have tried themselves |
| Announcement | What changes and for whom → how it works → what it does not do → how to use it | Enough to act |

Patterns seen across the source posts that are worth borrowing:

- **Summary first** for long research posts: 3–5 bullets, each a complete claim with its key number.
- **Run-in leads** to structure method sections: "**What we measured.**", "**What we found.**",
  "**Why measure X?**", "**What you can do today.**"
- **Findings as claims**: "Finding 2: Bottlenecks — The remaining time concentrates in review.",
  with the kicker in grey and the claim in ink.
- **Limits in the body, not only in a footnote**: a "Limitations" section and, when useful, "What would
  change our conclusion".
- **Credit and provenance at the end**: acknowledgements in small italic, footnotes, citation block,
  version and date for living pieces ("v1.0, September 2026").

## Sections and headings

- Order sections by what the reader must understand first. Each section answers one question.
- Headings are either a question the section genuinely answers or a claim the section supports.
  "Cite claims, not documents" beats "Methodology". Avoid a page of "Background / Method / Results".
- Keep heading levels shallow: h2 for sections, h3 for sub-points, h4 rarely.
- If you only read the title, headings and figure captions, you should get the argument.

## Paragraphs and sentences

- One paragraph, one recognisable move. Lead with the informative sentence, then the reason or evidence.
- Concrete subjects and verbs: "Reviewers had to re-check every citation" beats "This had a significant
  impact on overall efficiency."
- Name a term once, define it by what it does, then keep the same word; do not rotate synonyms.
- Transitions carry real questions: once it is faster, who catches the errors? When the total grows,
  where do the gains go?
- Numbers travel with their comparison and condition ("from 18% to 86% of claims, with a one-minute
  limit"). No false precision; no causal language for correlations.
- Mark the status of every claim: measured, inferred, assumed (scenario), or recommended.
- Cut: praise words (revolutionary, groundbreaking), stacked adjectives, rhetorical triplets, "It is
  important to note that", and paragraphs that only restate the previous one.
- Use one concrete case through the whole piece instead of a new metaphor per section.

## Writing in Chinese

- Keep natural Chinese syntax; do not mirror English clause order. Prefer short clauses joined by
  commas and real connectives (因为、所以、但、于是) over chains of "的".
- Avoid slogan rhythm (排比口号), one-sentence paragraphs used for drama, and translationese such as
  "对……进行了……", "作为一个……", "值得注意的是".
- Numbers and units: Arabic numerals, "24 周", "1.4 倍", "58%". Percentage points: "上升 3.9 个百分点".
  A space between Chinese and Latin words or numbers is common and fine; be consistent.
- Punctuation: full-width in Chinese text (，。：；？！), 「」 or “” consistently, 《》 for titles.
  Emphasis uses 着重号 via `<em>` (the CSS renders dots), not bold everywhere.
- Headings can be questions (「AI 能让一个研究项目快多少？」) or claims (「最快的环节，决定不了项目有多快。」).

### Example: generic vs concrete opening (no data assumed)

Generic:

> 在人工智能快速发展的今天，阅读方式正在经历前所未有的变革，智能工具为知识工作带来了无限可能。

Concrete:

> 读完一篇论文的摘要，你通常还不能判断它是否值得精读。你需要知道实验比较了什么、结论依赖哪些条件，以及它与你的问题有什么关系。
>
> 阅读助手可以帮你定位这些信息。但如果答案没有指向原文，它也会增加一项工作：核对助手究竟说对了没有。这篇文章从一次论文筛选开始，解释怎样把检索、判断和核对安排在同一条流程里。

Possible headings: 「先找到支持结论的实验」「每个回答都需要一条回到原文的路」「何时应该停止追问」.
(These illustrate style only; they are not research findings.)

## Plan figures with the text

For each important figure, write a short storyboard before drawing (full template in `figures.md`):
reader question, the sentence before, encoding, the sentence after, data status, text fallback. Simple
posts do not need a separate planning table; complex explainers do.

Captions say what to notice and the condition it depends on. Factual figures carry units, time range,
source and baseline; illustrative ones say "illustrative" inside the figure.

## Endings

Land on the action or open question the evidence supports. Say what new evidence would change the
conclusion. Put method details, sources, acknowledgements and version history where readers can find
them. Avoid "the future is full of possibilities".

## Before delivering

- Reading only title, dek, headings and captions, can you retell the argument? Does the first screen
  give a reason to keep reading?
- Does the concrete case actually explain the mechanism? Does every section add information?
- Do figure titles, units, baselines and sources match the text? Are scenario outputs tied to their
  assumptions?
- Is every placeholder (template text, `data-sample` numbers, "Your Name") replaced or removed?
- For restyling jobs: are all claims and numbers unchanged?
