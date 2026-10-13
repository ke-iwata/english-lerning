---
id: "14"
level: 3
title: データと傾向の説明
title_en: Describing Data and Trends
can_do: グラフや数値を使って、増減・変化・比較を説明し、原因に触れられる
scenario: APIのレスポンスタイムとエラー率の推移をSarahに説明する
---

# Lesson 14: データと傾向の説明
## Describing Data and Trends

> **Can-do:** グラフや数値を使って、増減・変化・比較を説明し、原因に触れられる
> **Level:** 3 ・ **Time:** 30 min ・ **Scenario:** APIのレスポンスタイムとエラー率の推移をSarahに説明する

<details>
<summary>講師用メモ (Tutor Notes)</summary>

- **このレッスンのゴール:** 「何が・どこから・どこまで・どう変わった・なぜ」を 1 セットで言えるようになる(例: The error rate went up from 0.1% to 2% on Tuesday because of a DB issue.)。
- **進め方のポイント:** 動詞(go up / drop / level off)と、程度の副詞(sharply / gradually / slightly)を分けて練習し、最後に合体させる。Role-play では講師が「グラフの形」を日本語で口頭描写し(「火曜に急に上がって、水曜にほぼ元に戻った」など)、学習者がそれを英語にする形にすると、画面共有がなくても成立する。
- **よく出るつまずき:**
  - `increase 20%` と by を落とす → 「20% 分 → by 20%」「20% に → to 20%」を日本語で対比させる
  - 「高くなった」を `became high` と言う → `went up` / `increased` にヒント
  - 原因を言うときに `because` の後が文にならない → `because of + 名詞` か `because + 主語 + 動詞` のどちらかに決めさせる
  - 数字の読み方で止まる(Lesson 04 の復習): 0.1% = zero point one percent、450ms = four hundred fifty milliseconds
- **日本語ヒントの例:** 「上がった? 下がった? → went up / went down」「どこからどこまで? → from A to B」「急に? ゆっくり? → sharply / gradually」「原因は? → This is because ...」
- **余裕があれば:** Challenge で、学習者が自分の担当システムの最近のメトリクスを 1 分で説明する。講師は "Compared to last month?" "What caused it?" と深掘りする。
- **時間が足りなければ:** Pattern 3(比較)を軽く触れるだけにし、Variation B を飛ばす。Quick check は 4 問に減らす。

</details>

## 1. Warm-up (3 min)

講師が質問し、学習者は 1〜2 文で答えます。前回(ミーティングの進行)の復習から始めます。

1. (復習) You are leading a meeting and Mike starts talking about something else. What do you say?
2. What metrics do you check every day? (response time, error rate, CPU ...?)
3. Did any number at work go up or down this week?

<details><summary>例 / Sample answers</summary>

1. "That's a good point, but let's get back to the release."
2. I check the error rate and the response time on the dashboard every morning.
3. Yes, the number of users went up a little after the campaign. / Not really, everything was stable.

</details>

## 2. Vocabulary & Idioms (7 min)

### Words

| English | 日本語 | Example |
|---|---|---|
| increase | 増加(する) | We saw a 20% increase in traffic last week. |
| decrease | 減少(する) | The error rate decreased after the fix. |
| spike | 急上昇・スパイク | There was a spike in errors on Tuesday night. |
| peak | ピーク・最高値 | The response time peaked at 800 milliseconds. |
| trend | 傾向 | The overall trend is going up slowly. |
| average | 平均(の) | The average response time is about 300 milliseconds. |
| steady | 安定した・一定の | Traffic has been steady since Wednesday. |
| roughly | おおよそ | Roughly 2% of requests failed during the spike. |

### Idioms & Collocations

| English | 日本語 | Example |
|---|---|---|
| go up / go down | 上がる / 下がる | CPU usage went up to 90% at noon. |
| level off | 横ばいになる | The error rate leveled off at 0.1%. |
| compared to ... | 〜と比べて | Compared to last month, latency is 30% higher. |
| due to ... | 〜が原因で | The spike was due to a database connection issue. |

**発音・使い方の注意:**
- `increase` / `decrease` は名詞なら前にアクセント (**IN**-crease)、動詞なら後ろ (in-**CREASE**)。迷ったら動詞は `go up / go down` を使えば安全。
- `by` と `to` を区別する: `increased **by** 20%`(20 ポイント分増えた)、`increased **to** 20%`(20% になった)。
- `due to` の後は名詞(the DB issue)。文を続けたいときは `because` + 主語 + 動詞。

### Quick check

講師が日本語で言い、学習者が英語で即答します(5〜6問)。

- 「急上昇(スパイク)」 → spike
- 「横ばいになった」 → leveled off
- 「平均レスポンスタイム」 → average response time
- 「先月と比べて」 → compared to last month
- 「DB の問題が原因で」 → due to a database issue
- 「エラー率が 2% まで上がった」 → The error rate went up to 2%.

## 3. Key Expressions (7 min)

### Pattern 1: 変化を言う — X went up / dropped from A to B.

- The response time went up from 300 to 450 milliseconds.
- The error rate dropped from 2% to 0.1% after the fix.

### Pattern 2: 変化の程度・速さ — sharply / gradually / slightly

- Traffic increased sharply on Tuesday night.
- Latency has been going up gradually over the last two weeks.

### Pattern 3: 比較 — compared to ... / twice as ... as ...

- Compared to last week, we have 15% more requests.
- The new endpoint is twice as fast as the old one.

### Pattern 4: 原因を言う — This is mainly because ... / The spike was caused by ...

- This is mainly because the connection pool was too small.
- The spike was caused by a batch job at 2 a.m.

**Drill:** 日本語を見て、英語で言ってみましょう。

1. エラー率は火曜日に 0.1% から 2% に上がりました。
2. その後、水曜日には 0.1% まで下がって、横ばいになりました。
3. レスポンスタイムはこの 2 週間でゆっくり上がっています。
4. 先月と比べて、リクエスト数はおよそ 20% 多いです。
5. 急上昇の原因は、深夜のバッチ処理でした。

<details><summary>Answers</summary>

1. The error rate went up from 0.1% to 2% on Tuesday.
2. After that, it dropped to 0.1% on Wednesday and leveled off.
3. The response time has been going up gradually over the last two weeks.
4. Compared to last month, we have roughly 20% more requests.
5. The spike was caused by a batch job late at night.

</details>

### よくある間違い (Common mistakes)

| ✗ | ✓ | なぜ |
|---|---|---|
| The error rate increased 20%. | The error rate increased **by** 20%. | 「〜分」増えたときは by が必要 |
| The response time became high. | The response time **went up**. | became high は不自然。変化は go up / increase で |
| It is increasing from last week. | It **has been** increasing **since** last week. | 「先週から今まで」は現在完了進行形 + since |
| The spike is because the batch job. | The spike was **due to** the batch job. | because の後は文、名詞なら due to / because of |

## 4. Role-play (10 min)

### Scenario

月曜の朝。PM の Sarah から「先週、API が遅かったとクライアントから言われた。何が起きていたの?」と Slack で聞かれ、10 分のオンライン通話で説明することになりました。手元のダッシュボードには次のデータがあります。

- レスポンスタイム(平均): 2 週間前 300ms → 先週 450ms(ゆっくり上昇中)
- エラー率: 普段 0.1%、火曜の夜に 2% まで急上昇、水曜の朝に 0.1% に戻って横ばい
- 原因: 火曜深夜のバッチ処理で DB の接続プールが足りなくなった。接続数を増やして解決済み
- リクエスト数: 先月比でおよそ 20% 増

### Roles

- **Ken (you):** バックエンドエンジニア。データを順番に説明し、原因と対策を伝える。専門用語は噛み砕く。
- **Sarah (tutor):** PM。技術には詳しくないので、分からない用語は遠慮なく聞き返す。クライアントに説明するために「結局、直ったのか」「また起きるのか」を知りたい。

### Model dialogue

まず講師と一緒に読みます。次に学習者が Ken の行を、見ないで言ってみます。

**Sarah:** Hi Ken. The client said the API was slow last week. What happened?
**Ken:** Sure, let me explain. There are two things: the response time and the error rate.
**Sarah:** OK, go ahead.
**Ken:** First, the average response time went up from 300 to 450 milliseconds over the last two weeks.
**Sarah:** That's a big change. Is that why the client noticed?
**Ken:** Partly. The main problem was the error rate. It spiked from 0.1% to 2% on Tuesday night.
**Sarah:** 2%? What caused that?
**Ken:** It was due to a batch job at 2 a.m. The database connection pool was too small, so some requests failed.
**Sarah:** I see. Is it fixed now?
**Ken:** Yes. We increased the pool size on Wednesday morning. The error rate dropped to 0.1% and leveled off.
**Sarah:** Good. And the response time? Is it still going up?
**Ken:** Slowly, yes. Compared to last month, we have roughly 20% more requests. That's the main reason.
**Sarah:** Will it get worse?
**Ken:** It might. I'd like to add a cache next month. I'll share a proposal on Thursday.
**Sarah:** Perfect. I'll tell the client the error issue is fixed and we're working on speed.

### Your turn

モデル対話を参考に、自分の言葉で。講師は Sarah 役をしながら、必要なら日本語でヒントを出します。

- **Variation A:** データは同じ。ただし Sarah が途中で **"Sorry, what do you mean by 'connection pool'? Explain it simply."** と聞き返してくる。Ken は専門用語を使わずに一言で説明する(例: It's the number of connections we can use at the same time.)。
- **Variation B:** 講師がダッシュボードの新しいグラフを **日本語で口頭描写** する(例:「CPU 使用率が先週の月曜から金曜まで毎日少しずつ上がって、金曜に 90% でピーク、週末に 40% まで下がった」)。Ken はそれを英語で説明し、Sarah は **"Is that normal? What's the usual number?"** と想定外の質問をしてくる。

### Challenge (余裕があれば)

自分の実際の担当システム(または最近見たグラフ)について、「何が・どこからどこまで・どう変わった・なぜ」を 1 分で説明してください。講師は "Compared to last month?" "Is that good or bad?" と深掘りします。

- Over the last month, the number of daily jobs went up from about 500 to 700.
- This is mainly because two new clients started using the batch API.

## 5. Wrap-up (3 min)

### Self-check

- [ ] 増減を `went up / dropped from A to B` の形で言えた
- [ ] `by` と `to` を正しく使い分けられた
- [ ] 変化の速さを `sharply / gradually` で表せた
- [ ] 原因を `due to ... / This is mainly because ...` で説明できた

### Homework

自分のダッシュボードから数字を 1 つ選び、「先週と比べてどう変わったか + 原因」を英語 3 文で書いて、声に出して読む。次回の Warm-up で、見ないで言ってもらいます。

### Next lesson

**Lesson 15: 手順やシステムの仕組みを説明する** — 決済処理の流れとデプロイ手順を、First / Then / After that などの順序の表現を使って、新しいメンバーに分かりやすく説明します。
