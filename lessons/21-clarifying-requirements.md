---
id: "21"
level: 4
title: クライアントとの要件確認
title_en: Clarifying Requirements with a Client
can_do: あいまいな要望を具体的な要件に落とし込むための質問ができ、認識のずれを確認できる
scenario: Ms. Leeの「レポート機能がほしい」という要望を、質問を重ねて具体化する
---

# Lesson 21: クライアントとの要件確認
## Clarifying Requirements with a Client

> **Can-do:** あいまいな要望を具体的な要件に落とし込むための質問ができ、認識のずれを確認できる
> **Level:** 4 ・ **Time:** 30 min ・ **Scenario:** Ms. Leeの「レポート機能がほしい」という要望を、質問を重ねて具体化する

<details>
<summary>講師用メモ (Tutor Notes)</summary>

- **このレッスンのゴール:** あいまいな要望に対して、「背景 (Why) → 具体化 (What exactly) → 確認 (Is that right?) → 優先順位 (Must-have?)」の 4 種類の質問を順に出せるようになる。
- **進め方のポイント:** Lesson 06 の「聞き返し」との違いを意識させる。今回は聞き取れなかったのではなく、相手自身も細かく決めていないことを一緒に決めていく会話。Ms. Lee 役はわざと抽象的に答え、Ken が 2〜3 回掘り下げるまで具体的なことを言わない。
- **よく出るつまずき:**
  - いきなり技術的な質問(Which database?)をしてしまう → 「まず目的を: What problem are you trying to solve?」
  - 相手の言葉をそのまま繰り返すだけで具体化できない → 「選択肢を出して聞く: Do you mean A or B?」
  - 確認のフレーズが出ない → 「So, just to confirm, ... Is that right?」
  - "I'm not sure. What do you recommend?" と返されて固まる → 「提案してよい: I'd recommend starting with ... because ...」
- **日本語ヒントの例:** 「"それは〜という意味ですか、それとも〜?" は When you say ..., do you mean ... or ...?」「"必須ですか、あれば嬉しいですか?" は Is that a must-have or a nice-to-have?」
- **余裕があれば:** Challenge の「会話の最後に 4 点の要件サマリーを口頭で言う」。できる人には、Lesson 11 で学んだメールの型で、確認メールの本文を口頭で組み立てさせる。
- **時間が足りなければ:** Variation B を飛ばす。Pattern 4 は例文を読むだけにして Drill の 5 番を省く。

</details>

## 1. Warm-up (3 min)

講師が質問し、学習者は 1〜2 文で答えます。前回(障害報告)の宿題から始めます。

1. Last time, your homework was a four-line incident memo. Tell me the impact and the root cause in two sentences.
2. Have you ever received a vague request from a client or a PM? What was it?
3. What do you usually do when a request is not clear?

<details><summary>例 / Sample answers</summary>

1. The login API was down for ten minutes. The root cause was an expired certificate.
2. Yes. Someone asked us to "make the dashboard faster," but didn't say which page.
3. I usually ask what they want to achieve, and then I write it down and confirm.

</details>

## 2. Vocabulary & Idioms (7 min)

### Words

| English | 日本語 | Example |
|---|---|---|
| requirement | 要件 | Let's write down the requirements before we estimate. |
| scope | 範囲(スコープ) | Mobile support is out of scope for this phase. |
| assumption | 前提・仮定 | My assumption is that only admins will use this. |
| use case | 利用場面・ユースケース | What's the main use case for this report? |
| stakeholder | 関係者・利害関係者 | Who are the stakeholders for this feature? |
| constraint | 制約 | The main constraint is the two-month deadline. |
| priority | 優先順位 | Which of these has the highest priority? |
| mockup | 画面のラフ案・モックアップ | Could you share a mockup of the screen? |

### Idioms & Collocations

| English | 日本語 | Example |
|---|---|---|
| must-have / nice-to-have | 必須 / あれば嬉しい | Is the export a must-have or a nice-to-have? |
| walk me through ... | 〜を順を追って説明する | Could you walk me through how you'd use it? |
| be on the same page | 認識が合っている | Let me make sure we're on the same page. |
| narrow down | 絞り込む | Let's narrow down the list to three items. |

**発音・使い方の注意:**
- `requirement` は re-**QUIRE**-ment。`priority` は pri-**OR**-i-ty。どちらも 2 音節目にアクセント。
- `scope` は「範囲」。「今回はやらない」は `out of scope`、「含める」は `in scope`。`scope creep`(要件がだんだん膨らむこと)も現場でよく聞く。
- `assumption` は「自分がそう思っている前提」。「〜という前提で進めていいですか?」は `Can I assume that ...?` が便利。
- `must-have` と `nice-to-have` は名詞として使う(It's a must-have.)。

### Quick check

講師が日本語で言い、学習者が英語で即答します(5〜6問)。

- 「要件」 → requirement
- 「今回の範囲外です」 → That's out of scope for this phase.
- 「それは必須ですか、あれば嬉しいですか?」 → Is that a must-have or a nice-to-have?
- 「順を追って説明してもらえますか?」 → Could you walk me through it?
- 「認識を合わせましょう」 → Let's make sure we're on the same page.
- 「3 つに絞り込みましょう」 → Let's narrow it down to three.

## 3. Key Expressions (7 min)

### Pattern 1: 背景・目的を聞く — What problem are you trying to solve? / Could you walk me through ...?

- What problem are you trying to solve with this report?
- Could you walk me through how your team would use it?

### Pattern 2: あいまいな言葉を具体化する — When you say "...", do you mean A or B?

- When you say "report," do you mean a dashboard or a downloadable file?
- When you say "real time," is a five-minute delay acceptable?

### Pattern 3: 認識を確認する — So, just to confirm, ... Is that right?

- So, just to confirm, you need a weekly CSV sent by email. Is that right?
- Let me make sure we're on the same page: only admins can see it, correct?

### Pattern 4: 優先順位を決める — Which of these is a must-have? / If we had to pick one, ...?

- Which of these three is a must-have for the first release?
- If we had to pick one, which would you choose: speed or detail?

**Drill:** 日本語を見て、英語で言ってみましょう。

1. このレポートで、どんな問題を解決したいのですか?
2. 「レポート」というのは、画面で見るものですか、それともダウンロードするファイルですか?
3. 確認ですが、毎週月曜に CSV が届けばよい、ということで合っていますか?
4. この中で、最初のリリースに必須なのはどれですか?
5. モバイル対応は今回の範囲外、という前提で進めてよいですか?

<details><summary>Answers</summary>

1. What problem are you trying to solve with this report?
2. When you say "report," do you mean something on screen, or a downloadable file?
3. So, just to confirm, you need a CSV every Monday. Is that right?
4. Which of these is a must-have for the first release?
5. Can I assume that mobile support is out of scope this time?

</details>

### よくある間違い (Common mistakes)

| ✗ | ✓ | なぜ |
|---|---|---|
| Which database do you want? (最初の質問) | What problem are you trying to solve? | 技術の話より先に目的を聞く。クライアントは DB を選べない |
| You mean report? | When you say "report," do you mean a dashboard or a file? | 繰り返すだけでは具体化しない。選択肢を出して聞く |
| I understand. (本当は不明なまま) | So, just to confirm, ... Is that right? | 「分かった」で終わらせず、自分の言葉で言い直して確認する |
| Everything is important? | Which one is a must-have for the first release? | `Everything` と聞くと `Yes` しか返ってこない。範囲を区切って聞く |

## 4. Role-play (10 min)

### Scenario

クライアントの Ms. Lee から「管理画面にレポート機能がほしい」というメールが届きました。詳細は書かれていません。今日はオンラインで 15 分の要件確認ミーティング。Ken は質問を重ねて、最初のリリースで作るものを決めます。

### Roles

- **Ken (you):** Sakura Tech のバックエンドエンジニア。開発期間は 1 か月しかない。聞き出したいこと: 誰が使うか、何のデータか、どのくらいの頻度か、画面かファイルか、必須機能はどれか。
- **Ms. Lee (tutor):** クライアント企業の運用マネージャー。本当の目的は「毎週月曜の社内会議で、先週の売上と返金の件数を上司に見せること」。ただし最初は "a report feature" としか言わない。Ken が掘り下げると少しずつ具体的に答える。

### Model dialogue

まず講師と一緒に読みます。次に学習者が Ken の行を、見ないで言ってみます。

**Ms. Lee:** Thanks for making time, Ken. As I wrote, we'd like a report feature in the admin panel.
**Ken:** Happy to help. Before we get into details, what problem are you trying to solve?
**Ms. Lee:** Every Monday, I have to show last week's numbers to my manager. Right now I do it by hand.
**Ken:** I see. Could you walk me through what you do by hand now?
**Ms. Lee:** I export orders, count the sales and refunds in a spreadsheet, and paste them into a slide.
**Ken:** Got it. So the key numbers are weekly sales and refunds. Is there anything else?
**Ms. Lee:** Maybe the top five products. But that's less important.
**Ken:** OK. When you say "report," do you mean a page in the admin panel, or a file you can download?
**Ms. Lee:** Hmm, both would be nice.
**Ken:** Understood. If we had to pick one for the first release, which would help you more?
**Ms. Lee:** The downloadable file, I think. I need to put it in a slide anyway.
**Ken:** That makes sense. Is the top-five list a must-have or a nice-to-have?
**Ms. Lee:** Nice-to-have. The totals are the must-have.
**Ken:** So, just to confirm: a weekly CSV with sales and refund totals, downloadable from the admin panel. Is that right?
**Ms. Lee:** Yes, exactly. And it should only be visible to managers.
**Ken:** Good point, I'll add that. I'll send a short summary today so we're on the same page.

### Your turn

モデル対話を参考に、自分の言葉で。講師は Ms. Lee 役をしながら、必要なら日本語でヒントを出します。

- **Variation A:** 要望は「通知機能がほしい (We want notifications.)」。Ken が「何の通知か」「誰に」「メールかアプリ内か」を掘り下げる。ところが Ms. Lee は途中で **"I'm not sure. What would you recommend?"** と聞き返してくる。Ken は一つ提案し、理由を添える(I'd recommend starting with email, because ...)。
- **Variation B:** 要望は「検索を速くしてほしい (Search is too slow.)」。Ken が「どの画面か」「何秒くらいか」「どのくらいのデータ量か」を確認する。合意できたと思った最後に Ms. Lee が **"Oh, and it needs to work on the mobile app too."** と追加してくる。Ken はスコープを確認し、今回に含めるか次のフェーズにするかを提案する。

### Challenge (余裕があれば)

会話の最後に、決まった要件を 4 点にまとめて口頭で言ってみましょう(誰が / 何を / いつ・どの頻度で / 必須か)。

- Let me summarize. One, managers only. Two, weekly sales and refund totals. Three, a CSV download every Monday. Four, the top-five list is a nice-to-have for later.

## 5. Wrap-up (3 min)

### Self-check

- [ ] 技術の話の前に、目的 (What problem ...?) を聞けた
- [ ] あいまいな言葉を `When you say ..., do you mean A or B?` で具体化できた
- [ ] 決まったことを `So, just to confirm, ...` で言い直して確認できた
- [ ] `must-have / nice-to-have` で優先順位を聞けた

### Homework

自分の仕事で最近あったあいまいな要望(または「ダッシュボードを改善して」のような想像上の要望)を一つ選び、Pattern 1〜4 の質問を 1 つずつ、合計 4 つ英語で書く。次回の Warm-up で聞かせてもらいます。

### Next lesson

**Lesson 22: 英語での面接** — 外資系 IT 企業の一次面接を想定し、経歴・強み・実績・志望動機を STAR 法を使って具体的に話します。
