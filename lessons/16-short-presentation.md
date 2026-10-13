---
id: "16"
level: 3
title: 短いプレゼンテーション
title_en: Giving a Short Presentation
can_do: 導入・本論・まとめの構成で、3分程度のプレゼンができる
scenario: チームミーティングで、改善提案(キャッシュ導入)を3分でプレゼンする
---

# Lesson 16: 短いプレゼンテーション
## Giving a Short Presentation

> **Can-do:** 導入・本論・まとめの構成で、3分程度のプレゼンができる
> **Level:** 3 ・ **Time:** 30 min ・ **Scenario:** チームミーティングで、改善提案(キャッシュ導入)を3分でプレゼンする

<details>
<summary>講師用メモ (Tutor Notes)</summary>

- **このレッスンのゴール:** 「導入(テーマと 3 つのポイント)→ 本論(問題 → 提案 → コスト)→ まとめ(結論と依頼)」の型で、3 分の提案プレゼンを最後まで止まらずに言い切る。
- **進め方のポイント:** Lesson 14(データの説明)と Lesson 15(順序表現)の集大成。新しい表現は「つなぎ(signposting)」が中心なので、内容は Role-play の参考情報をそのまま使ってよい。学習者がメモを見ながらでもいいので、まず 1 回通しで 3 分測る。2 回目は導入とまとめだけ見ないで言わせる。
- **よく出るつまずき:**
  - 導入なしでいきなり本論に入る → 「今日は何の話? ポイントはいくつ?」と日本語で聞き、`Today I'd like to talk about ... I'll cover three points.` を言わせる
  - ポイント間のつなぎがなく、聞き手が今どこか分からない → `That brings me to my second point.` を各区切りで必ず言うルールにする
  - 「〜だと思います」ばかりで提案にならない → `I'd like to propose ...` / `This would reduce ...` の形に変換させる
  - 最後が `That's all.` で終わって依頼がない → 「結局、何をしてほしい?」と聞いて `I'd like to start next sprint.` まで言わせる
- **日本語ヒントの例:** 「テーマを一言で: Today I'd like to talk about ...」「次のポイントへ: That brings me to ...」「グラフを指して: As you can see, ...」「結論: The bottom line is ...」
- **余裕があれば:** Challenge で、別の提案(リンター導入、CI の高速化など)を同じ型で 2 分、メモなしでやる。
- **時間が足りなければ:** Variation B(1 分バージョン)を飛ばし、Model dialogue の Ken 役を 1 回通すだけにする。Quick check は 4 問。

</details>

## 1. Warm-up (3 min)

講師が質問し、学習者は 1〜2 文で答えます。前回(システムの説明)の復習から始めます。

1. (復習) Tell me the first three steps of your deploy process. Use "First", "Then", "After that".
2. When did you last give a presentation? What was it about?
3. What makes a presentation easy to follow?

<details><summary>例 / Sample answers</summary>

1. First, I open a PR. Then the CI runs the tests. After that, I merge to main.
2. Last month, at a team meeting. It was about our new logging tool.
3. A clear structure and simple slides. / Telling the main point first.

</details>

## 2. Vocabulary & Idioms (7 min)

### Words

| English | 日本語 | Example |
|---|---|---|
| overview | 概要 | Let me give you a quick overview first. |
| purpose | 目的 | The purpose of this proposal is to reduce latency. |
| benefit | 利点・メリット | The main benefit is faster response times. |
| drawback | 欠点・デメリット | One drawback is that the data can be slightly old. |
| estimate | 見積もり(する) | I estimate about two weeks of work. |
| implement | 実装する・導入する | We can implement this in the next sprint. |
| impact | 影響・効果 | The impact on the database would be small. |
| conclusion | 結論 | In conclusion, I recommend adding a cache. |

### Idioms & Collocations

| English | 日本語 | Example |
|---|---|---|
| in a nutshell | 一言で言うと | In a nutshell, we store popular data for five minutes. |
| as you can see | ご覧のとおり | As you can see, the response time went up in May. |
| the bottom line is ... | 要するに・結論としては | The bottom line is, we need a cache before summer. |
| go over ... | 〜をざっと説明する | Let me go over the three points quickly. |

**発音・使い方の注意:**
- `estimate` は動詞なら最後を /eɪt/(**ES**-ti-mate)、名詞なら /ət/(**ES**-ti-mət)。会議では `rough estimate`(ざっくりの見積もり)がよく出る。
- `benefit` と `merit`: 日本語の「メリット」は英語では `benefit` / `advantage` が普通。`drawback` / `downside` が「デメリット」。
- `in a nutshell` は要約の前に置くカジュアルめの決まり文句。クライアント向けなら `in short` / `to put it simply` が無難。

### Quick check

講師が日本語で言い、学習者が英語で即答します(5〜6問)。

- 「概要」 → overview
- 「一言で言うと」 → in a nutshell
- 「ご覧のとおり」 → as you can see
- 「欠点が一つあります」 → There is one drawback.
- 「2 週間と見積もっています」 → I estimate about two weeks.
- 「要するに、〜です」 → The bottom line is, ...

## 3. Key Expressions (7 min)

### Pattern 1: 導入 — Today I'd like to talk about ... / I'll cover three points: ...

- Today I'd like to talk about adding a cache to the product API.
- I'll cover three points: the problem, the proposal, and the cost.

### Pattern 2: つなぎ(signposting) — Let me start with ... / That brings me to ...

- Let me start with the problem.
- That brings me to my second point: the proposal.

### Pattern 3: データと提案 — As you can see, ... / I'd like to propose ... This would ...

- As you can see, the response time went up by 50% in two months.
- I'd like to propose a Redis cache. This would cut latency by roughly 40%.

### Pattern 4: まとめと依頼 — To sum up, ... / That's all from me. Any questions?

- To sum up, a cache makes the API faster at a small cost.
- That's all from me. Any questions?

**Drill:** 日本語を見て、英語で言ってみましょう。

1. 今日はデプロイの自動化についてお話しします。
2. 3 つのポイントを扱います: 現状の問題、提案、そしてコストです。
3. まず問題からお話しします。
4. ご覧のとおり、デプロイには毎回 40 分かかっています。
5. まとめると、自動化でデプロイ時間は 10 分に減ります。以上です。ご質問はありますか?

<details><summary>Answers</summary>

1. Today I'd like to talk about automating our deploys.
2. I'll cover three points: the current problem, the proposal, and the cost.
3. Let me start with the problem.
4. As you can see, each deploy takes 40 minutes.
5. To sum up, automation would cut deploy time to 10 minutes. That's all from me. Any questions?

</details>

### よくある間違い (Common mistakes)

| ✗ | ✓ | なぜ |
|---|---|---|
| Today, I will explain about the cache. | Today I'd like to **talk about** the cache. | explain about は誤り。プレゼンの導入は talk about が自然 |
| Please look this graph. | **Take a look at** this graph. / **As you can see**, ... | look の後は at が必要。決まり文句で言うと楽 |
| I think we should introduce cache. | I'd like to **propose a** cache. | 提案は propose / suggest で。cache は数えられる名詞 |
| Finally, I summarize. | **To sum up**, ... | 「まとめると」は決まり文句を使う |

## 4. Role-play (10 min)

### Scenario

週次のチームミーティングで、あなた(Ken)は「商品 API にキャッシュを導入する」改善提案を 3 分でプレゼンします。聞き手は PM の Sarah と同僚の Mike。スライドは 1 枚(Lesson 14 で使ったレスポンスタイムのグラフ)だけ。終わったら Sarah が来週のスプリント計画に入れるかを判断します。

参考情報(Ken が話す内容):
- 問題: 平均レスポンスタイムが 2 か月で 300ms → 450ms。リクエスト数は 20% 増。多くは同じ商品データの読み取り
- 提案: DB の前に Redis キャッシュを置き、人気の商品データを 5 分間保持する
- 効果: 小規模テストではレスポンスタイムが約 40% 減(約 270ms)。DB の負荷も減る
- 欠点: データが最大 5 分古くなる(商品価格なら許容範囲と考えるが、クライアントに確認したい)
- コスト: エンジニア 1 人で約 2 週間 + サーバー代が月 50 ドル程度
- 依頼: 次のスプリントから始めたい

### Roles

- **Ken (you):** 提案者。導入 → 問題 → 提案 → コスト → まとめ、の順で 3 分。質問が来ても構造を崩さない。
- **Sarah (tutor):** PM。時間に厳しい。コストと「クライアントへの影響」を気にする。
- **Mike (tutor):** 同僚エンジニア。技術的な細部(なぜ Redis か、欠点は何か)に興味があり、途中で質問することがある。

### Model dialogue

まず講師と一緒に読みます。次に学習者が Ken の行を、見ないで言ってみます(時間を測ります)。

**Sarah:** OK Ken, you have three minutes. Go ahead.
**Ken:** Thanks. Today I'd like to talk about adding a cache to the product API. I'll cover three points: the problem, the proposal, and the cost.
**Sarah:** Sounds good.
**Ken:** Let me start with the problem. As you can see on this chart, the average response time went up from 300 to 450 milliseconds in two months.
**Mike:** Is that because of more traffic?
**Ken:** Yes, mainly. We have about 20% more requests, and most of them read the same product data.
**Ken:** That brings me to my second point: the proposal. I'd like to propose a Redis cache in front of the database. In a nutshell, we store popular product data for five minutes.
**Sarah:** What's the benefit?
**Ken:** Based on a small test, this would cut the response time by roughly 40%, to about 270 milliseconds. It would also reduce the load on the database.
**Mike:** Any drawbacks?
**Ken:** One. The data can be up to five minutes old. For product prices, I think that's acceptable, but we should confirm with the client.
**Ken:** Finally, the cost. I estimate about two weeks for one engineer, plus around 50 dollars a month for the server.
**Sarah:** That's cheaper than I expected.
**Ken:** To sum up, a cache would make the API faster and reduce database load, for a small cost. The bottom line is, I'd like to start next sprint. That's all from me. Any questions?
**Sarah:** Thanks, Ken. That was clear. Let's talk about the timeline next.

### Your turn

モデル対話を参考に、自分の言葉で。講師は Sarah と Mike の 2 役をしながら、必要なら日本語でヒントを出します。

- **Variation A:** 内容は同じ。ただし Mike が 2 つ目のポイントの途中で **"Sorry, quick question — why Redis? Why not Memcached?"** と割り込む。Ken は一言で答えるか、**"Good question. I'll come to that at the end, if that's OK."** と後回しにして、構造を崩さずに続ける(最後に必ず答えること)。
- **Variation B:** 開始直前に Sarah が **"Sorry Ken, we're running late. Can you do it in one minute?"** と言う。Ken は「問題 → 提案 → 依頼」の 3 文程度に圧縮して 1 分で伝える。導入(I'd like to talk about ...)とまとめ(The bottom line is ...)は省かない。

### Challenge (余裕があれば)

別のテーマで同じ型のプレゼンを 2 分、メモなしでやってみましょう。テーマ例: リンターの導入、CI の高速化、週次ミーティングの短縮。講師は聞き手として最後に 1 つ質問します。

- Today I'd like to talk about speeding up our CI. I'll cover the problem, the fix, and the cost.
- To sum up, running tests in parallel would save 15 minutes per deploy.

## 5. Wrap-up (3 min)

### Self-check

- [ ] 導入で「テーマ + ポイントの数」を言えた
- [ ] ポイントの区切りで `Let me start with ... / That brings me to ...` と言えた
- [ ] データを示して `This would ...` で効果を言えた
- [ ] まとめで結論と依頼(何をしてほしいか)を言えた

### Homework

今日のプレゼンを自分の言葉で書き直し(200 語以内)、スマホで録音して 3 分以内に収まるか確認する。次回の Warm-up で導入の 2 文を見ないで言ってもらい、次回のレッスン(質疑応答)でこのプレゼンへの質問を受けます。

### Next lesson

**Lesson 17: 質疑応答に対応する** — 今日のプレゼンの後、Sarah とクライアントの Ms. Lee から質問を受けます。「答える・時間を稼ぐ・分からないと伝える・後で回答する」を使い分けます。
