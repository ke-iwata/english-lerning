---
id: "20"
level: 4
title: 障害・トラブルの報告
title_en: Reporting an Incident
can_do: 障害の影響・原因・対応・再発防止策を、落ち着いて構造的に報告できる
scenario: 本番障害の直後、SarahとMs. Leeに状況を報告し、質問に答える
---

# Lesson 20: 障害・トラブルの報告
## Reporting an Incident

> **Can-do:** 障害の影響・原因・対応・再発防止策を、落ち着いて構造的に報告できる
> **Level:** 4 ・ **Time:** 30 min ・ **Scenario:** 本番障害の直後、SarahとMs. Leeに状況を報告し、質問に答える

<details>
<summary>講師用メモ (Tutor Notes)</summary>

- **このレッスンのゴール:** 「影響 (Impact) → 原因 (Cause) → 対応 (Action) → 再発防止 (Prevention)」の 4 ブロックを、この順番で、謝罪より先に言えるようになる。
- **進め方のポイント:** 障害報告は「落ち着いて聞こえること」が最重要。早口になったら止めて、`First, the impact.` のように見出しを声に出してから話させる。クライアント役(Ms. Lee)は不安げに質問し、Ken が事実で安心させる流れを作る。
- **よく出るつまずき:**
  - 最初に謝ってしまい、事実が出てこない → 「謝罪は最後。まず時間と影響: From 10:05 to 10:45, ...」
  - 原因が分からないときに黙る → 「まだ確定していないなら正直に: We haven't confirmed the root cause yet. Our current hypothesis is ...」
  - 「直った」の言い方があいまい → 「As of now, the service is stable. と"現時点で"を付けましょう」
  - 数字が曖昧(many users)→ 「概数でも数字で: about 20% / roughly 1,200 payments」
- **日本語ヒントの例:** 「根本原因は〜でした: The root cause was ...」「ロールバックして〜に復旧: We rolled back ... and service was restored at ...」「再発防止のために: To prevent this, we'll ...」
- **余裕があれば:** Challenge の「メモなしで 60 秒サマリー」。さらに余裕があれば、同じ内容を Slack の 3 行アップデート(Impact / Status / Next update)として口頭で作らせる。
- **時間が足りなければ:** Variation B を飛ばし、Model dialogue を 2 回通す(2 回目は Ken の行を見ないで)。Quick check は 4 問で止める。

</details>

## 1. Warm-up (3 min)

講師が質問し、学習者は 1〜2 文で答えます。前回(コードレビュー)の表現を一つ思い出してから始めます。

1. Last time we practiced code reviews. How do you politely point out a problem in someone's code?
2. Have you ever had a production incident? What happened, in one sentence?
3. Who do you usually report to when something breaks?

<details><summary>例 / Sample answers</summary>

1. "One concern is the error handling. Have you considered adding a retry?"
2. Yes. A deploy broke the login API for about ten minutes.
3. I report to my tech lead first, and then the PM updates the client.

</details>

## 2. Vocabulary & Idioms (7 min)

### Words

| English | 日本語 | Example |
|---|---|---|
| outage | 障害・サービス停止 | We had a 40-minute outage this morning. |
| impact | 影響 | The impact was limited to the checkout page. |
| root cause | 根本原因 | The root cause was a bad config change. |
| affected | 影響を受けた | About 20% of users were affected. |
| mitigate | (影響を)抑える・軽減する | We mitigated the issue by scaling up the servers. |
| restore | 復旧する | Service was restored at 10:45 JST. |
| timeline | 時系列・経緯 | Let me walk you through the timeline. |
| postmortem | 事後検証(報告書) | We'll share the postmortem by Friday. |

### Idioms & Collocations

| English | 日本語 | Example |
|---|---|---|
| roll back | ロールバックする・前の状態に戻す | We rolled back the deploy within five minutes. |
| as of now | 現時点では | As of now, the service is stable. |
| keep you posted | 随時お知らせする | I'll keep you posted on the investigation. |
| put ... in place | (対策を)導入する・整備する | We've put an alert in place for this. |

**発音・使い方の注意:**
- `outage` は **OUT**-age(/ˈaʊtɪdʒ/)。`incident` は **IN**-ci-dent。どちらも最初にアクセント。
- `affect`(動詞: 影響する)と `effect`(名詞: 効果・影響)を混同しやすい。「影響を受けたユーザー」は `affected users`。
- `restore` は「サービスを復旧する」。`service was restored` と受け身で使うことが多い。「直した」= `fixed` よりも、報告では `restored` が落ち着いて聞こえる。
- `root cause` は常にセットで。`The cause was ...` でも通じるが、障害報告では `root cause` が定番。

### Quick check

講師が日本語で言い、学習者が英語で即答します(5〜6問)。

- 「根本原因」 → root cause
- 「現時点では安定しています」 → As of now, it's stable.
- 「約 2 割のユーザーが影響を受けました」 → About 20% of users were affected.
- 「デプロイをロールバックしました」 → We rolled back the deploy.
- 「随時お知らせします」 → I'll keep you posted.
- 「事後検証(報告書)」 → postmortem

## 3. Key Expressions (7 min)

### Pattern 1: 影響を先に言う — We had an outage from ... to ... It affected ...

- We had a 40-minute outage this morning. It affected about 20% of users.
- The checkout page was down from 10:05 to 10:45 JST. No data was lost.

### Pattern 2: 原因 — The root cause was ... / It was caused by ...

- The root cause was a config change in the load balancer.
- It was caused by a migration that locked the orders table.

### Pattern 3: 対応と現状 — We rolled back ... / Service was restored at ...

- We rolled back the deploy, and service was restored at 10:45.
- As of now, everything is stable, and we're monitoring closely.

### Pattern 4: 再発防止 — To prevent this, we'll ... / We're putting ... in place.

- To prevent this, we're adding a check to the deploy pipeline.
- We'll write a postmortem and share it by Friday.

**Drill:** 日本語を見て、英語で言ってみましょう。

1. 今朝、15 分間の障害がありました。ユーザーの約 1 割に影響しました。
2. 根本原因は、キャッシュサーバーのメモリ不足でした。
3. デプロイをロールバックし、9 時 20 分にサービスは復旧しました。
4. 現時点では安定していて、引き続き監視しています。
5. 再発防止のため、デプロイ前のチェックを追加します。

<details><summary>Answers</summary>

1. We had a 15-minute outage this morning. It affected about 10% of users.
2. The root cause was that the cache server ran out of memory.
3. We rolled back the deploy, and service was restored at 9:20.
4. As of now, it's stable, and we're still monitoring.
5. To prevent this, we'll add a check before each deploy.

</details>

### よくある間違い (Common mistakes)

| ✗ | ✓ | なぜ |
|---|---|---|
| I'm very sorry, it was my mistake ... (最初に謝る) | First, the impact: from 10:05 to 10:45, ... | 聞き手が最初に知りたいのは事実(時間・影響)。謝罪は最後に短く |
| The server was broken. | The API returned errors for 15 minutes. | 「壊れた」ではなく、何がどうなったかを具体的に |
| We will try not to happen again. | We'll add a check so this doesn't happen again. | `try not to happen` は文として成立しない。具体的な対策 + `so (that)` |
| Now it is OK. | As of now, the service is stable. | 「現時点で」を付けると、まだ監視中であることが伝わり信頼される |

## 4. Role-play (10 min)

### Scenario

今朝 10:05 JST から約 40 分間、決済 API がエラーを返しました。原因は、データベースのマイグレーションが orders テーブルを想定より長くロックしたことです。ロールバックで復旧済み。今は 11:30、PM の Sarah とクライアントの Ms. Lee との緊急オンライン会議で、Ken が状況を報告します。

### Roles

- **Ken (you):** 障害対応の担当者。事実は次のとおり。影響 = 決済失敗 約 1,200 件(チェックアウトの約 20%)、データ損失なし、失敗した顧客は再試行可能。原因 = マイグレーションによるテーブルロック。対応 = 10:40 にロールバック、10:45 に復旧。再発防止 = マイグレーションは営業時間外に実施、パイプラインにロック時間のチェックを追加。
- **Sarah (tutor):** PM。冷静で、事実と今後の予定を知りたい。
- **Ms. Lee (tutor):** クライアント。顧客への影響とデータの安全を心配している。少し不安げに質問する。

### Model dialogue

まず講師と一緒に読みます。次に学習者が Ken の行を、見ないで言ってみます。

**Sarah:** Thanks for joining on short notice, Ken. Can you give us a summary?
**Ken:** Sure. From 10:05 to 10:45 JST, the payment API returned errors. About 20% of checkouts failed.
**Ms. Lee:** Twenty percent? How many customers is that?
**Ken:** Roughly 1,200 payments. No data was lost, and those customers can simply retry.
**Sarah:** OK. What was the root cause?
**Ken:** A database migration locked the orders table longer than expected. That blocked all payment writes.
**Ms. Lee:** Why wasn't this caught before the release?
**Ken:** Fair question. We tested the migration, but on a much smaller dataset. That was our gap.
**Sarah:** How did you resolve it?
**Ken:** We rolled back the migration at 10:40, and service was restored by 10:45. As of now, it's stable.
**Ms. Lee:** What are you doing to prevent this from happening again?
**Ken:** Two things. We'll run migrations outside business hours, and we're adding a lock-time check to the pipeline.
**Sarah:** Sounds good. When can we see the postmortem?
**Ken:** I'll share a written report by tomorrow noon, and I'll keep you posted if anything changes.
**Ms. Lee:** Thank you, Ken. I appreciate the clear explanation.
**Ken:** Thank you. And I'm sorry for the trouble this caused your customers.

### Your turn

モデル対話を参考に、自分の言葉で。講師は Sarah と Ms. Lee の両方を演じながら、必要なら日本語でヒントを出します。

- **Variation A:** 同じ障害。ただし Ms. Lee が途中で **"Was any customer card data exposed?"** と聞いてくる(答え: カード情報は決済プロバイダ側にあり、自社では保持していない → No. We don't store card data. It's handled by the payment provider.)。さらに **"Can you compensate the affected customers?"** と聞かれるので、技術側で決められないことは Sarah に引き継ぐ(That's a business decision. Sarah, could we discuss that separately?)。
- **Variation B:** 障害は復旧したが、**根本原因がまだ確定していない**設定。Sarah が **"So you don't actually know the cause yet?"** と突っ込んでくる。正直に「未確定」と言い、現時点の仮説と、次の報告の時刻を約束する(We haven't confirmed it yet. Our current hypothesis is ... I'll update you by 2 p.m.)。

### Challenge (余裕があれば)

メモを見ずに、60 秒で障害サマリーを話してみましょう。順番は必ず Impact → Cause → Action → Prevention。講師は時間を計り、4 つのブロックが全部入っていたかをフィードバックします。

## 5. Wrap-up (3 min)

### Self-check

- [ ] 謝罪より先に、時間と影響(数字つき)を言えた
- [ ] 原因を `The root cause was ...` で一文で言えた
- [ ] 対応と現状を `rolled back` / `restored` / `as of now` で言えた
- [ ] 再発防止策を具体的に `To prevent this, we'll ...` で言えた

### Homework

過去に経験した(または想像上の)障害を一つ選び、Impact / Cause / Action / Prevention の 4 行で英語のメモを書く。各行 1〜2 文。次回の Warm-up で、見ないで 30 秒で話してもらいます。

### Next lesson

**Lesson 21: クライアントとの要件確認** — Ms. Lee の「レポート機能がほしい」というあいまいな要望を、質問を重ねて具体的な要件に落とし込みます。
