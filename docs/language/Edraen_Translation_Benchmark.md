# EDRAEN TRANSLATION BENCHMARK

**Document:** Grammar Stress-Test Set  
**Version:** 1.0  
**Status:** Working test suite; examples test the current grammar and do not add new canon  
**Standard under test:** Edraen Standard v3.1

This benchmark tests whether the documented rules can be applied consistently to sentences that combine more than one grammatical feature. Supported examples use approved vocabulary and existing rules. An unresolved case is deliberately left untranslated rather than filled with guessed grammar.

## 1. Supported regression tests

| ID | English target | Edraen test sentence | Rule being tested |
|---|---|---|---|
| T01 | I like eating meat. | **AN LIRV LI DUV BAVR.** | Activity nominalization with LI + verb phrase |
| T02 | I like to eat meat. | **AN LIRV TO DUV BAVR.** | TO infinitive; contrast with T01 |
| T03 | I do not like eating meat. | **AN NU LIRV LI DUV BAVR.** | Negation of the main clause |
| T04 | I like not eating meat. | **AN LIRV LI NU DUV BAVR.** | Negation inside the activity phrase |
| T05 | I want you to eat meat. | **AN DERV THA ET DUV BAVR.** | THA + full clause when the second action has a different subject |
| T06 | I had eaten the food. | **AN DA PE DUV LI VEM.** | Past tense before completive aspect |
| T07 | I will still be standing. | **AN VA LO STIL DALK.** | Future, progressive aspect, and continuative adverb |
| T08 | The home was built by us. | **LI DOM DA RI DURN BY EN.** | Past tense, passive marker, and optional agent |
| T09 | Can you speak Edraen? | **HA ET TALR FARL EDRAEN?** | Yes/no question with ability verb |
| T10 | Why do you not remember? | **KU ET NU SAVN?** | Information question with negation |
| T11 | How many people are in the village? | **KAI MA DAN ES IN LI DARN?** | Quantity question |
| T12 | These good people are in the village. | **DE SETH DAN ES IN LI DARN.** | Plural demonstrative; MA is omitted because DE already marks plurality |
| T13 | I know where you live. | **AN FIRV KO ET GELR.** | Embedded question |
| T14 | I know that you are well. | **AN FIRV THA ET ES SETH.** | Content clause |
| T15 | The person who helps us. | **LI DAN TA GARN EN.** | Relative clause with the head noun as the missing participant |
| T16 | If you come, I will meet you. | **IF ET TERV, AN VA RAVN ET.** | Condition plus future result |
| T17 | Although the water is hot, I eat the food. | **ALTH LI VOR ES KETHR, AN DUV LI VEM.** | Concessive clause |
| T18 | I will send you an email. | **AN VA DARV NA SAVAT TO ET.** | Future marker, object, and recipient phrase |
| T19 | I do not have any money. | **AN NU HURV ANY MELK.** | Negation with ANY |
| T20 | There is a person in the home. | **ES NA DAN IN LI DOM.** | Existential statement |
| T21 | The person whom I remember. | **LI DAN TA AN SAVN.** | Relative clause with the head noun as the missing object |
| T22 | At 2:30. | **AT BI HURK AND TRI DEK MIRK.** | Clock-time expression and number composition |
| T23 | I gave the book to her. | **AN DA DOVR LI ZULR TO IR.** | Past tense, direct object, and recipient phrase with TO |
| T24 | The book I gave him is in the home. | **LI ZULR TA AN DA DOVR TO IR ES IN LI DOM.** | Relative clause with a missing object, recipient phrase, and locative predicate |
| T25 | I had not been helped by them. | **AN NU DA PE RI GARN BY UR.** | Negation, past-completive sequence, passive marker, and agent phrase

These are regression fixtures, not claims that every English nuance has a one-to-one Edraen equivalent. In particular, T01 and T02 are intentionally different: LI + verb phrase presents an activity as a noun-like concept; TO + verb phrase presents an action as a complement.

## 2. Unresolved stress tests

These targets expose combinations or distinctions that need an explicit decision before a reliable Edraen translation should be treated as standard.

| ID | English target | Why it is unresolved |
|---|---|---|
| U01 | If I had known, I would have come. | The standard defines past, completive aspect, and WO as hypothetical, but does not yet define a full counterfactual-past construction or its interpretation. |
| U02 | The person who said that you would come left. | This nests a content clause inside a relative clause and then adds past time; the individual clause types exist, but their nested combination has not been stress-tested. |
| U04 | I stopped eating meat. | The current infinitive and activity constructions do not yet specify which construction expresses stopping an activity, and no approved root meaning for “stop” should be presumed. |
| U05 | She said, “I will return tomorrow.” | Direct quotation is permitted in writing, but quotation boundaries, speaker-relative time words, and whether the quoted clause keeps its own tense reference need a formal example. |
| U06 | I might not have been able to go. | The modal, negation, completive aspect, and ability verb require a documented scope and ordering rule for stacked modality. |

Do not invent translations for U01–U06 during ordinary use. Resolve each by documenting a rule, adding a test sentence, and then adding the supported translation to Section 1.

## 3. How to use this benchmark

1. Check every Edraen token against the master dictionary or grammar-word ledger.
2. Check each word order against the Standard Grammar, not English word order.
3. Preserve the intended scope of negation, modality, and embedded clauses.
4. If a sentence needs a rule that is not documented, mark it unresolved instead of guessing.
5. When a rule is approved, add a regression example here and update the grammar, phrasebook, and audit script where appropriate.

A larger vocabulary is not a substitute for these tests. The goal is to make a new sentence translatable by rule, without inventing a meaning or grammar rule to rescue it.
