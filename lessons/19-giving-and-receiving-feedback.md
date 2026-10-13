---
id: "19"
level: 4
title: フィードバックを与える・受ける(コードレビュー)
title_en: Giving and Receiving Feedback
can_do: 相手を傷つけずに改善点を伝え、自分へのフィードバックには前向きに応答できる
scenario: Mikeのプルリクエストをレビューし、自分のPRへの指摘にも対応する
---

# Lesson 19: フィードバックを与える・受ける(コードレビュー)
## Giving and Receiving Feedback

> **Can-do:** 相手を傷つけずに改善点を伝え、自分へのフィードバックには前向きに応答できる
> **Level:** 4 ・ **Time:** 30 min ・ **Scenario:** Mikeのプルリクエストをレビューし、自分のPRへの指摘にも対応する

<details>
<summary>講師用メモ (Tutor Notes)</summary>

- **このレッスンのゴール:** 「良い点 → 懸念 → 提案」の順で指摘を言えること。そして指摘を受けたら「受け止める → 対応を言う」か「理由を添えてやわらかく反論する」のどちらかができること。
- **進め方のポイント:** Level 4 なので、文法の正しさより「トーン」に集中する。命令形(Change this.)が出たら、その場で提案形(I'd suggest ...)に言い直させる。反論の練習では、Mike 役は一度は引かずに "Why?" と理由を求める。
- **よく出るつまずき:**
  - 指摘がきつくなる(You should ... / This is wrong.)→ 「提案の形にしてみましょう: I'd suggest ... / Have you considered ...?」
  - 反論できずに全部 OK と言ってしまう → 「納得していないなら理由を言いましょう: I see your point, but ... because ...」
  - 褒め言葉がゼロで指摘だけになる → 「まず良いところを一言: Nice work on the tests.」
  - 指摘の重さが伝わらない → 「必須なら This is a blocker. 細かいだけなら Nitpick: と頭に付けましょう」
- **日本語ヒントの例:** 「"気になる点が一つ" は One concern is ...」「"〜に移したらどうでしょう" は I'd suggest moving ...」「"もっともです" は Fair point.」
- **余裕があれば:** Challenge で、非同期(PR コメント欄)向けの 3 文コメントを声に出して作らせる。書き言葉と話し言葉の違い(コメントは主語を省きやすい)も触れる。
- **時間が足りなければ:** Variation B を飛ばす。Quick check は 3 問に減らし、Drill は 1・2・5 だけにする。

</details>

## 1. Warm-up (3 min)

講師が質問し、学習者は 1〜2 文で答えます。前回(交渉)の表現を思い出すところから始めます。

1. Last time we practiced negotiating. How would you suggest an alternative plan? (代替案を出すときの言い方を一つ)
2. When did you last review someone's code? What was the PR about?
3. How do you feel when someone leaves many comments on your code?

<details><summary>例 / Sample answers</summary>

1. "What if we release the basic version first?" / "How about we move the deadline by one week?"
2. Yesterday. It was a PR that added pagination to the order list API.
3. Honestly, a little nervous at first, but it usually helps me.

</details>

## 2. Vocabulary & Idioms (7 min)

### Words

| English | 日本語 | Example |
|---|---|---|
| suggestion | 提案 | Just a suggestion, but we could cache this result. |
| readable | 読みやすい | Shorter functions make the code more readable. |
| edge case | 境界条件・特殊なケース | What happens in the edge case where the list is empty? |
| maintainable | 保守しやすい | A smaller class is easier to keep maintainable. |
| nitpick | 細かい指摘(本質的でない) | Nitpick: there's a typo in this comment. |
| refactor | リファクタリングする・整理し直す | I'd refactor this into two smaller functions. |
| blocker | マージを止めるべき問題 | This isn't a blocker, but please take a look. |
| concern | 懸念・気になる点 | My main concern is performance on large tables. |

### Idioms & Collocations

| English | 日本語 | Example |
|---|---|---|
| Have you considered ...? | 〜は検討しましたか? | Have you considered using a map here? |
| fair point | もっともな指摘ですね | Fair point. I'll update the error message. |
| nice catch | よく気づきましたね | Nice catch! I missed that null check. |
| address a comment | 指摘に対応する | I've addressed all your comments. Could you take another look? |

**発音・使い方の注意:**
- `nitpick`(または短く `nit`)は、PR コメントの冒頭に付けて「細かい話ですが」と合図する言葉。これがあると相手は優先度を判断しやすい。逆に必須の修正なら `This is a blocker.` とはっきり言う。
- `consider` の後は動名詞: Have you considered **using** ...?(✗ to use)。
- `concern` は "I'm concerned about X." か "One concern is X." が自然。`I have a concern.` は少し堅く聞こえる。
- `address` は「住所」ではなく、ここでは「(指摘・問題に)対応する」。`address the feedback / the issue` のように使う。

### Quick check

講師が日本語で言い、学習者が英語で即答します(5〜6問)。

- 「境界条件」 → edge case
- 「これはブロッカーではありません」 → This isn't a blocker.
- 「〜は検討しましたか?」 → Have you considered ...?
- 「よく気づきましたね」 → Nice catch.
- 「もっともな指摘です」 → Fair point.
- 「指摘にはすべて対応しました」 → I've addressed all the comments.

## 3. Key Expressions (7 min)

### Pattern 1: 良い点 → 懸念 — This looks good overall. One concern is ...

- This looks good overall. One concern is the retry logic.
- Nice work on the tests. One small thing: the variable names are a bit unclear.

### Pattern 2: 命令ではなく提案 — I'd suggest ... / It might be cleaner to ...

- I'd suggest moving this check into the service layer.
- It might be cleaner to return early here.

### Pattern 3: 質問の形で指摘する — Have you considered ...? / Is there a reason ...?

- Have you considered handling the empty-list case?
- Is there a reason we don't use the existing helper?

### Pattern 4: 受け止める・やわらかく反論する — Fair point. I'll ... / I see your point, but ...

- Fair point. I'll add a test for that.
- I see your point, but I kept it simple on purpose. Here's why.

**Drill:** 日本語を見て、英語で言ってみましょう。

1. 全体的には良さそうです。一つ気になるのはエラー処理です。
2. この処理をヘルパー関数に移すことを提案します。
3. タイムアウトのケースは検討しましたか?
4. ここで既存のライブラリを使わない理由は何かありますか?
5. もっともな指摘です。ログのメッセージを直します。

<details><summary>Answers</summary>

1. This looks good overall. One concern is the error handling.
2. I'd suggest moving this logic into a helper function.
3. Have you considered the timeout case?
4. Is there a reason we don't use the existing library here?
5. Fair point. I'll fix the log message.

</details>

### よくある間違い (Common mistakes)

| ✗ | ✓ | なぜ |
|---|---|---|
| You should change this. | I'd suggest changing this. / Could we change this? | `You should` は命令に近く聞こえる。提案か質問の形にする |
| This code is bad. | This part is a bit hard to follow. | 人やコードを「評価」せず、「何が難しいか」を具体的に言う |
| OK, I will do. (本当は納得していない) | I see your point, but I'd keep it as is because ... | 納得していないのに従うと認識のずれが残る。理由を添えて反論してよい |
| I will fix. | I'll fix it. / I'll fix that. | `fix` は目的語が必要。`it / that` を落とさない |

## 4. Role-play (10 min)

### Scenario

今日はレビューの「与える側」と「受ける側」を両方やります。前半は、Ken が Mike の PR(注文一覧 API へのページネーション追加)をレビューします。後半は、Mike が Ken の PR(決済のリトライ処理)にコメントしてきます。どちらもビデオ通話でのペアレビューです。

### Roles

- **Ken (you):** Sakura Tech のバックエンドエンジニア。Mike の PR には「ページサイズに上限がない」「ソート処理が 2 か所に重複している」という懸念がある。自分の PR ではリトライ回数を 5 回にしているが、それは決済プロバイダの推奨値に合わせたという明確な理由がある。
- **Mike (tutor):** US チームの同僚エンジニア。率直でフレンドリー。筋の通った指摘には素直だが、理由がある場合は簡単には譲らない。

### Model dialogue

まず講師と一緒に読みます。次に学習者が Ken の行を、見ないで言ってみます。

**Mike:** Hey Ken, thanks for picking up my PR. Any thoughts?
**Ken:** Sure. Overall it looks good, and the tests are really nice. I have two small concerns.
**Mike:** Go ahead.
**Ken:** First, there's no upper limit on the page size. Have you considered capping it at 100?
**Mike:** Fair point. Someone could request a million rows. I'll add a limit.
**Ken:** Great. Second, the sorting logic appears in two places. I'd suggest moving it into a helper.
**Mike:** Hmm, is that a blocker? I was planning to clean that up later.
**Ken:** Not a blocker. But it's a quick change, so I'd do it now if possible.
**Mike:** OK, that makes sense. I'll address both and re-request a review.
**Ken:** Thanks. By the way, did you get a chance to look at my retry PR?
**Mike:** I did. One thing: five retries feels like a lot. Why not three?
**Ken:** I see your point, but the payment provider recommends five. I'll add a comment explaining that.
**Mike:** Nice, that would help. Also, nitpick: there's a typo in the log message.
**Ken:** Nice catch. I'll fix that too.
**Mike:** Cool. Then I'm happy to approve once that's in.
**Ken:** Perfect. I'll push the changes in ten minutes.

### Your turn

モデル対話を参考に、自分の言葉で。講師は Mike 役をしながら、必要なら日本語でヒントを出します。

- **Variation A:** Ken が Mike の新しい PR(キャッシュ層の追加)をレビューする。懸念は「キャッシュの有効期限が設定されていない」こと。ところが Mike は **"I don't think that's necessary. The cache is read-only."** と反対してくる。Ken は、なぜそれでも必要か(例: 古いデータが残り続ける)を説明するか、納得したなら理由を添えて引き下がる。
- **Variation B:** 相手は Mike ではなく PM の **Sarah**。Ken の PR の説明文を読んで **"Sorry, I don't follow. What does 'idempotent' mean for the user?"** と聞いてくる。専門用語を使わずに、ユーザーにとっての意味(同じ注文が二重に作られない、など)を 2 文で説明する。

### Challenge (余裕があれば)

同期のレビューではなく、PR のコメント欄に「書く」つもりで、3 文のコメントを口頭で組み立ててみましょう。「良い点 → 懸念 → 提案」の順で。

- Nice work on the pagination. One concern: there's no upper limit on page size. I'd suggest capping it at 100 so a single request can't load the whole table.

## 5. Wrap-up (3 min)

### Self-check

- [ ] 「良い点」を一言添えてから指摘を始められた
- [ ] 命令形ではなく `I'd suggest ...` / `Have you considered ...?` で指摘できた
- [ ] 指摘の重さを `blocker` / `nitpick` で伝え分けられた
- [ ] 受けた指摘に `Fair point.` か `I see your point, but ...` で応答できた

### Homework

実際の(または想像上の)PR に対して、英語のレビューコメントを 3 つ書く。Pattern 1〜3 をそれぞれ 1 回ずつ使うこと。次回の Warm-up で読み上げてもらいます。

### Next lesson

**Lesson 20: 障害・トラブルの報告** — 本番障害の直後に、影響・原因・対応・再発防止策を、落ち着いて構造的に PM とクライアントへ報告します。
