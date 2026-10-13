---
id: "15"
level: 3
title: 手順やシステムの仕組みを説明する
title_en: Explaining a Process or System
can_do: システムの構成や処理の流れを、順序を示す表現を使って分かりやすく説明できる
scenario: 新しく入ったMikeに、決済処理の流れとデプロイ手順を説明する
---

# Lesson 15: 手順やシステムの仕組みを説明する
## Explaining a Process or System

> **Can-do:** システムの構成や処理の流れを、順序を示す表現を使って分かりやすく説明できる
> **Level:** 3 ・ **Time:** 30 min ・ **Scenario:** 新しく入ったMikeに、決済処理の流れとデプロイ手順を説明する

<details>
<summary>講師用メモ (Tutor Notes)</summary>

- **このレッスンのゴール:** 「First → Then → After that → Finally」の順序表現と、「X は Y に〜を送る / X が〜を担当する」の構成説明を組み合わせて、5〜6 ステップの処理の流れを止まらずに説明できるようになる。
- **進め方のポイント:** エンジニアにとって最も得意な話題なので、内容よりも「順序の接続詞」と「確認の一言(Does that make sense?)」に集中させる。長い説明を一気に言おうとして崩れるので、「1 ステップ = 1 文」をルールにする。Role-play では講師(Mike 役)が「分かったふり」をせず、曖昧なところを突っ込む。
- **よく出るつまずき:**
  - 全部 `and then, and then` でつなぐ → `After that` / `Once ...` / `Finally` を混ぜるようヒント
  - 主語が抜ける(日本語の癖) → 「誰が(何が)やるの?」と聞いて `The payment service validates ...` と主語を言わせる
  - `if` と `when` の混同 → 「毎回必ず起きる → when / once」「起きるかもしれない → if」
  - 説明が長くなり相手を置いてきぼりにする → 3 ステップごとに `Does that make sense so far?` を入れるルールにする
- **日本語ヒントの例:** 「最初は? → First, ...」「その次は? → Then / After that, ...」「それが終わったら? → Once that's done, ...」「失敗したら? → If it fails, ...」「ここまで OK? → Does that make sense so far?」
- **余裕があれば:** Challenge で、学習者が自分の実際の担当システムを図なしで説明し、講師が "Where does X go?" "What if Y is down?" と質問する。
- **時間が足りなければ:** Role-play を決済フロー(Model dialogue の前半)だけにして、デプロイ手順(Variation B)は宿題に回す。

</details>

## 1. Warm-up (3 min)

講師が質問し、学習者は 1〜2 文で答えます。前回(データと傾向)の復習から始めます。

1. (復習) Tell me one number that changed at work recently. Did it go up or down, and why?
2. When a new engineer joins your team, who explains the system? How long does it take?
3. What do you do first when you deploy to production?

<details><summary>例 / Sample answers</summary>

1. The number of daily users went up by about 10% because of a campaign.
2. Usually a senior engineer explains it. It takes about a week to understand everything.
3. First, I check that all the tests pass. Then I create a release tag.

</details>

## 2. Vocabulary & Idioms (7 min)

### Words

| English | 日本語 | Example |
|---|---|---|
| step | 手順・ステップ | The deploy process has five steps. |
| component | 構成要素・コンポーネント | The system has three main components. |
| request | リクエスト・要求 | The client sends a request to the API gateway. |
| validate | 検証する | The service validates the input first. |
| queue | キュー・待ち行列 | The event goes into a queue. |
| trigger | きっかけになる・起動する | A merge to main triggers the CI pipeline. |
| pipeline | パイプライン(一連の処理) | The pipeline runs tests and builds the image. |
| roll back | ロールバックする・元に戻す | If something breaks, we roll back to the previous version. |

### Idioms & Collocations

| English | 日本語 | Example |
|---|---|---|
| go through ... | 〜を通る・〜を経る | Every request goes through the gateway. |
| be responsible for ... | 〜を担当する・〜の役割を持つ | This service is responsible for payments. |
| in case of ... | 〜の場合(に備えて) | In case of an error, the job retries three times. |
| end up (with) ... | 最終的に〜になる | If it fails twice, we end up with a manual check. |

**発音・使い方の注意:**
- `queue` は「キュー」と 1 音節 (/kjuː/)。`validate` のアクセントは前 (**VAL**-i-date)。`component` は 2 音節目 (com-**PO**-nent)。
- `be responsible for` は人にも物にも使える。Lesson 01 の `be in charge of` は主に人。システムの役割なら `responsible for` か `handles`(例: This service handles payments.)が自然。
- `in case of + 名詞`(In case of failure)、`in case + 文`(in case it fails)。`if` と違い「備えて」のニュアンス。

### Quick check

講師が日本語で言い、学習者が英語で即答します(5〜6問)。

- 「検証する」 → validate
- 「リクエストはゲートウェイを通ります」 → The request goes through the gateway.
- 「このサービスは決済を担当しています」 → This service is responsible for payments.
- 「マージするとパイプラインが起動します」 → A merge triggers the pipeline.
- 「ロールバックする」 → roll back
- 「エラーの場合は」 → in case of an error

## 3. Key Expressions (7 min)

### Pattern 1: 順序を示す — First, ... / Then, ... / After that, ... / Finally, ...

- First, the client sends a request to the API gateway.
- After that, the payment service validates the request. Finally, it saves the result.

### Pattern 2: 構成と役割 — X is responsible for ... / X sends ... to Y

- The gateway is responsible for authentication.
- The payment service sends the result to the notification service.

### Pattern 3: 条件と完了 — Once ..., ... / If ..., ...

- Once the tests pass, the pipeline builds a Docker image.
- If the payment provider times out, we retry up to three times.

### Pattern 4: 理解を確認する — Does that make sense so far? / Let me know if ...

- Does that make sense so far?
- Let me know if I'm going too fast.

**Drill:** 日本語を見て、英語で言ってみましょう。

1. まず、クライアントがゲートウェイにリクエストを送ります。
2. その後、決済サービスが入力を検証します。
3. ゲートウェイは認証を担当しています。
4. テストが通ったら、パイプラインがイメージをビルドします。
5. もし決済に失敗したら、3 回までリトライします。ここまで大丈夫ですか?

<details><summary>Answers</summary>

1. First, the client sends a request to the gateway.
2. After that, the payment service validates the input.
3. The gateway is responsible for authentication.
4. Once the tests pass, the pipeline builds the image.
5. If the payment fails, we retry up to three times. Does that make sense so far?

</details>

### よくある間違い (Common mistakes)

| ✗ | ✓ | なぜ |
|---|---|---|
| And then validate. And then save. | **Then the service validates** the input. **After that, it saves** it. | 主語が必要。接続詞も and then ばかりにしない |
| When the payment fails, we retry. | **If** the payment fails, we retry. | 「毎回必ず起きる」なら when、「起きるかもしれない」なら if |
| The request is go through the gateway. | The request **goes** through the gateway. | 受け身ではない。be 動詞を入れない |
| Do you understand? | **Does that make sense?** | "Do you understand?" は上から目線に聞こえることがある |

## 4. Role-play (10 min)

### Scenario

US チームから Mike が、今週あなた(Ken)のチームに異動してきました。Mike はフロントエンド出身で、決済システムはまだ知りません。今日のオンボーディングで、(1) 決済処理の流れ、(2) 本番へのデプロイ手順を 10 分で説明します。図は共有せず、口頭だけで伝えます。

参考情報(Ken が説明する内容):
- 決済フロー: クライアント → API ゲートウェイ(認証)→ 決済サービス(入力を検証)→ 外部の決済プロバイダーを呼ぶ → 結果を DB に保存 → イベントをキューに入れる → 通知サービスがメールを送る
- デプロイ手順: PR を作る → CI がテスト実行 → main にマージ → パイプラインがイメージをビルド → ステージングに自動デプロイ → PM が承認 → 本番へ → 問題があればロールバック

### Roles

- **Ken (you):** チームのバックエンドエンジニア(決済担当)。順序を示しながら、1 ステップ 1 文で説明し、途中で理解を確認する。
- **Mike (tutor):** 新メンバー。やる気はあるが、バックエンド用語に不慣れ。分からないところは遠慮なく質問し、「失敗したらどうなるの?」と気にする。

### Model dialogue

まず講師と一緒に読みます。次に学習者が Ken の行を、見ないで言ってみます。

**Mike:** Thanks for doing this, Ken. Can you walk me through the payment flow?
**Ken:** Sure. There are four main components: the gateway, the payment service, the database, and the notification service.
**Mike:** OK, got it.
**Ken:** First, the client sends a request to the API gateway. The gateway is responsible for authentication.
**Mike:** So every request goes through the gateway?
**Ken:** Yes, every request. Then, the payment service validates the input. After that, it calls the external payment provider.
**Mike:** What if the provider is slow?
**Ken:** Good question. If the provider times out, we retry up to three times. Does that make sense so far?
**Mike:** Yes, that's clear.
**Ken:** Once the payment succeeds, the service saves the result in the database. Finally, it puts an event in a queue.
**Mike:** And who reads the queue?
**Ken:** The notification service. It's responsible for sending the email to the customer.
**Mike:** Nice. And what about deploying? How do I get my code to production?
**Ken:** It's simple. First, you open a PR, and the CI runs the tests. Once the tests pass and someone approves, you merge to main.
**Mike:** Then it goes to production automatically?
**Ken:** Not yet. The pipeline builds an image and deploys it to staging. After that, Sarah approves, and then it goes to production.
**Mike:** And in case of a problem?
**Ken:** We roll back to the previous version. It takes about two minutes. Let me know if you want to try a deploy together tomorrow.

### Your turn

モデル対話を参考に、自分の言葉で。講師は Mike 役をしながら、必要なら日本語でヒントを出します。

- **Variation A:** 決済フローの説明。ただし Mike は途中で **"Wait, where do the logs go? How do I debug if something fails?"** と、Ken が用意していなかった質問をしてくる。Ken は「それは後で説明する」と流れに戻すか、1〜2 文で簡単に答えてから続ける(例: Each service sends logs to the central logging tool. I'll show you later.)。
- **Variation B:** デプロイ手順の説明。Mike は前のチームで別のツールを使っていて、**"In my old team, we deployed straight to production. Why do you need staging?"** と理由を聞いてくる。Ken は手順だけでなく「なぜそうしているか」を 1〜2 文で説明する。

### Challenge (余裕があれば)

自分の実際の担当システム(または好きな Web サービス)の処理の流れを、図なしで 1 分で説明してください。講師は "What happens if X is down?" "Which component handles Y?" と質問します。

- First, the user uploads a file. The upload service stores it and puts a job in the queue.
- Once the worker picks up the job, it resizes the image and saves it.

## 5. Wrap-up (3 min)

### Self-check

- [ ] First / Then / After that / Finally を使って、5 ステップ以上の流れを説明できた
- [ ] 各ステップに主語(どのコンポーネントが)を付けて言えた
- [ ] Once / If を使って、完了条件や失敗時の動きを説明できた
- [ ] 途中で "Does that make sense so far?" と理解を確認できた

### Homework

自分の担当システムの処理の流れを 5〜6 ステップで英語で書き(1 ステップ 1 文)、声に出して 3 回読む。次回の Warm-up で、最初の 3 ステップを見ないで言ってもらいます。

### Next lesson

**Lesson 16: 短いプレゼンテーション** — 「導入・本論・まとめ」の型で、キャッシュ導入の改善提案を 3 分でプレゼンします。今日の順序表現と前回のデータ表現がそのまま使えます。
