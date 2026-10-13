---
id: "10"
level: 2
title: 問題を説明して助けを求める
title_en: Explaining a Problem and Asking for Help
can_do: 技術的な問題の状況・試したこと・欲しい助けを、順序立てて説明できる
scenario: デプロイがうまくいかず、先輩エンジニアのMikeに相談する
---

# Lesson 10: 問題を説明して助けを求める
## Explaining a Problem and Asking for Help

> **Can-do:** 技術的な問題の状況・試したこと・欲しい助けを、順序立てて説明できる
> **Level:** 2 ・ **Time:** 30 min ・ **Scenario:** デプロイがうまくいかず、先輩エンジニアのMikeに相談する

<details>
<summary>講師用メモ (Tutor Notes)</summary>

- **このレッスンのゴール:** 「問題(何が起きている)→ 状況の絞り込み(どこで・いつ起きる)→ 試したこと → 欲しい助け」の順で、相手が質問しなくても状況が伝わる説明ができる。
- **進め方のポイント:** 日本人エンジニアは「結論の前に経緯を全部話す」か、逆に「エラーが出ます」だけで止まるかの両極になりやすい。今日の 4 パターンの順番そのものが「相談のテンプレート」だと伝える。Role-play では Mike が「最後に成功してから何を変えた?」など、準備していない質問を必ず投げる。
- **よく出るつまずき:**
  - 「動かない」を ✗ It is not work と言う → "It doesn't work." / "It's not working."
  - 試したことで主語と過去形が抜ける(✗ tried restart but not work)→ "I tried restarting, but it didn't work."
  - 「エラーが出る」→ "I'm getting an error." の形を口癖にする
  - 「教えてください」を ✗ Please teach me と言う → "Could you help me with this?" / "Could you show me how?"
- **日本語ヒントの例:** 「まず何が起きてるか一言: I'm having a problem with ...」「どこでは動いて、どこで失敗する? It works ..., but it fails ...」「試したことは? I've tried ..., but ...」「何をしてほしい? Could you take a look?」
- **余裕があれば:** Challenge の「Slack 用 3 文まとめ」。できる人には、Mike の質問に対して "I haven't checked that yet. Let me check." と正直に答える練習(知ったかぶりをしない)を重点的に。
- **時間が足りなければ:** Quick check を 3 問に減らし、Variation B を省略。Challenge は宿題に回す。

</details>

## 1. Warm-up (3 min)

講師が質問し、学習者は 1〜2 文で答えます。短くて OK。完璧でなくて OK。

1. Last time we practiced opinions. What do you think about remote work? Give one reason. (前回の復習: 意見 + 理由)
2. When did you last get stuck on a technical problem? What was it? (最近、技術的な問題で詰まったのはいつ?)
3. Who do you usually ask for help at work? (職場で困ったとき、誰に聞きますか?)

<details><summary>例 / Sample answers</summary>

1. I think remote work is good, because I can focus better.
2. Last week. A test failed only in CI, not on my laptop.
3. I usually ask a senior engineer on my team. Sometimes I ask in Slack.

</details>

## 2. Vocabulary & Idioms (7 min)

### Words

| English | 日本語 | Example |
|---|---|---|
| issue | 問題・不具合 | I'm having an issue with the deploy script. |
| error message | エラーメッセージ | The error message says "connection refused". |
| log | ログ | I checked the logs, but I found nothing useful. |
| cause | 原因 | I don't know the cause yet. |
| environment | 環境 | It works in my local environment. |
| reproduce | 再現する | I can reproduce it every time on staging. |
| workaround | 回避策 | Is there a workaround for now? |
| config | 設定(configuration の略) | I think the config file is wrong. |

### Idioms & Collocations

| English | 日本語 | Example |
|---|---|---|
| run into (a problem) | (問題に)ぶつかる | I ran into a problem with the deploy. |
| be stuck on ... | 〜で行き詰まっている | I've been stuck on this for two hours. |
| figure out | 解明する・突き止める | I can't figure out why it fails. |
| look into | 調べる | Could you look into the logs with me? |

**発音・使い方の注意:**
- 「動かない」は "It doesn't work." が万能。✗ It is not work. ✗ It doesn't working.
- 症状は現在形(It fails on staging.)、試したことは現在完了(I've tried restarting.)。時制で「今の状態」と「これまでやったこと」が伝わる。
- 「エラーが出る」は "I'm getting an error." が定番。✗ Error is happen.
- `issue` は **IS**-shoo(「イシュー」)、`reproduce` は re-pro-**DUCE**。`log` は複数形 logs で使うことが多い。

### Quick check

講師が日本語で言い、学習者が英語で即答します(5〜6問)。

- 「デプロイで問題にぶつかりました」 → I ran into a problem with the deploy.
- 「2時間詰まっています」 → I've been stuck on this for two hours.
- 「原因が分かりません」 → I can't figure out the cause.
- 「ステージングで再現します」 → I can reproduce it on staging.
- 「回避策」 → workaround
- 「エラーが出ます」 → I'm getting an error.

## 3. Key Expressions (7 min)

### Pattern 1: 問題を言う — I'm having a problem with ... / I'm getting an error when ...

- I'm having a problem with the deploy to staging.
- I'm getting a timeout error when I run the migration.

### Pattern 2: 状況を絞る — It works ..., but it fails ... / It happens only when ...

- It works locally, but it fails on staging.
- It happens only when the database is under load.

### Pattern 3: 試したこと — I've tried ..., but ... / So far, I've checked ...

- I've tried restarting the service, but it didn't help.
- So far, I've checked the logs and the config file.

### Pattern 4: 助けを求める — Do you have a minute? / Could you take a look? / Any idea what's causing this?

- Do you have a minute? Could you take a look at this error?
- Do you have any idea what's causing this?

**Drill:** 日本語を見て、英語で言ってみましょう。

1. ステージングへのデプロイで問題が起きています。
2. ローカルでは動くのですが、ステージングでは失敗します。
3. サービスの再起動は試しましたが、効きませんでした。
4. 今のところ、ログと設定ファイルは確認しました。
5. 少し時間ありますか? 何が原因か、心当たりはありますか?

<details><summary>Answers</summary>

1. I'm having a problem with the deploy to staging.
2. It works locally, but it fails on staging.
3. I've tried restarting the service, but it didn't help.
4. So far, I've checked the logs and the config file.
5. Do you have a minute? Any idea what's causing this?

</details>

### よくある間違い (Common mistakes)

| ✗ | ✓ | なぜ |
|---|---|---|
| The deploy is not success. | The deploy **failed**. / The deploy **isn't working**. | success は名詞。動詞 fail か、work を使う |
| I tried to restart but not work. | I tried restarting, but it **didn't work**. | 主語と did が抜けやすい。「〜してみた」は try + -ing |
| Error is happen. | I'm getting an error. / An error occurs. | happen の形が崩れがち。get an error で覚える |
| Please teach me how to fix it. | Could you **help me** with this? / Could you **show me** how to fix it? | teach は「科目を教える」。助けは help、やり方は show |

## 4. Role-play (10 min)

### Scenario

あなた(Ken)は決済 API の新バージョンを staging にデプロイしていますが、2 時間前から失敗し続けています。リリースは明日。US チームの先輩エンジニア Mike がオンラインなので、Slack で声をかけて短い通話に切り替えました。

### Roles

- **Ken (you):** staging にデプロイすると、サービスが起動直後に落ちる。ローカルでは動く。ログには DB 接続時に "connection refused" とある。サービスの再起動とイメージの再ビルドは試した。直前の変更で、DB ホスト用の環境変数を 1 つ追加した(staging に設定し忘れている可能性あり)。
- **Mike (tutor):** 先輩エンジニア。親切だが、答えを言う前に質問して状況を把握するタイプ。「最後に成功したデプロイから何を変えた?」など、Ken が準備していない質問もする。

### Model dialogue

まず講師と一緒に読みます。次に学習者が Ken の行を、見ないで言ってみます。

**Ken:** Hi Mike, do you have a minute? I'm stuck on a deploy problem.
**Mike:** Sure, what's going on?
**Ken:** I'm having a problem with the deploy to staging. The service starts, then crashes right away.
**Mike:** OK. Does it work locally?
**Ken:** Yes, it works locally. It fails only on staging.
**Mike:** What does the error message say?
**Ken:** The log says "connection refused" when it connects to the database.
**Mike:** Hmm. What have you tried so far?
**Ken:** I've tried restarting the service and rebuilding the image, but it didn't help.
**Mike:** Got it. What changed since the last successful deploy?
**Ken:** Good question. I added a new environment variable for the DB host... Oh, maybe it's not set on staging.
**Mike:** That's probably it. Let's look into the staging config together.
**Ken:** Thanks, Mike. I really appreciate it.

### Your turn

モデル対話を参考に、自分の言葉で。講師は Mike 役をしながら、必要なら日本語でヒントを出します。

- **Variation A:** 問題を変えます。**テストがローカルでは通るのに CI では落ちる**。Ken は問題・状況・試したことを順に説明する。Mike は **"Which version of Go does CI use? Did you check that?"** と聞いてきますが、Ken はまだ確認していません。知ったかぶりせず **"I haven't checked that yet. Let me check."** と正直に答えて、次の一手を決める。
- **Variation B:** Mike は忙しく、最初に **"I'm in the middle of something. Can it wait an hour?"** と言います。Ken は「リリースが明日」という緊急度を伝えて、5 分だけ時間をもらうか、ヒントだけもらうかをお願いする。さらに Mike が **"Have you asked in #platform-support yet? Can you send me the log first?"** と聞いてくるので、それに答えて次のアクションを合意する。

### Challenge (余裕があれば)

同じ問題を、Slack の **#backend** チャンネルに投稿する 3 文のメッセージとして口頭で言う。「何が起きているか・試したこと・何をしてほしいか」の順で。

- 例: Deploy to staging is failing with "connection refused" on DB connect. I've tried restarting and rebuilding the image. Could someone check the staging DB config with me?
- ヒント: Slack では "Hi" や "I'm writing to" は不要。いきなり本題で OK。

## 5. Wrap-up (3 min)

### Self-check

- [ ] I'm having a problem with ... / I'm getting an error when ... で問題を言えた
- [ ] It works ..., but it fails ... で状況を絞って説明できた
- [ ] I've tried ..., but ... / So far, I've checked ... で試したことを言えた
- [ ] Do you have a minute? / Could you take a look? で助けを求められた

### Homework

最近実際に詰まった問題を 1 つ選び、「問題・試したこと・欲しい助け」の 3 文を英語で書いて、声に出して 3 回読む。次回の Warm-up で、見ないで言ってもらいます。

### Next lesson

**Lesson 11: ビジネスメールとチャットの基本** — クライアントの Ms. Lee からのメールを読んで要点をつかみ、「件名・書き出し・用件・結び」の型で返信を組み立てます。
