---
name: review
description: これまでのレッスン記録(progress/log.md)をもとに、弱点の単語・表現を 10〜15 分で復習する。使い方 `/review`、`/review 03`(特定レッスンの復習)、`/review vocab`(単語だけ)。
---

# /review — 弱点に合わせた復習セッション

引数: `$ARGUMENTS`

## 準備(学習者には見せない)

1. `TUTOR_GUIDE.md` を読む(言語の使い分け、間違いの直し方に従う)。
2. `progress/log.md` を読み、完了したレッスンと、各回の `Weak vocabulary` / `To improve` を集める。
3. `lessons/index.json` と、復習対象のレッスンファイルを読む。
   - 引数にレッスン番号があればそのレッスンのみ。
   - 引数が空なら、完了済みレッスンのうち **直近 3 回** + 記録に弱点として繰り返し出ている項目。
   - 記録が空なら、「まだ記録がありません。まず `/lesson 01` から始めましょう」と伝えて終了。
   - 引数に `vocab` があれば Part 1 のみ、`roleplay` があれば Part 3 のみ。

## 進行(目安 10〜15 分、1 ターン 1 問)

- **Part 1: Vocabulary flash (約 5 分)** — 弱点の単語・イディオムを中心に 10 問。日本語→英語と英語→日本語を混ぜる。言えなかったものは例文つきでもう一度。
- **Part 2: Fix the mistake (約 4 分)** — 記録の `To improve` にある ✗ 文を、学習者自身に直してもらう(5 問程度)。
- **Part 3: Mini role-play (約 5 分)** — 復習対象レッスンの Scenario のうち 1 つを、短縮版(5〜6 往復)で行う。相手役は元のレッスンの Roles に従う。訂正は終わってからまとめて。

## 終了時

- 今日できるようになったこと・まだ怪しいものを 2〜3 点ずつ伝える。
- `progress/log.md` の末尾に、次の形式で追記する。

```markdown
## YYYY-MM-DD — Review (Lessons NN, NN, NN)

- **Now OK:** …
- **Still weak:** …
- **Next:** …
```
