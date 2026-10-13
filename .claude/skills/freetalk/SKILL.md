---
name: freetalk
description: テキストを使わない 15〜20 分の自由英会話。記録にある弱点を自然に練習させ、終了後に記録を保存してコミットする。使い方 `/freetalk`、`/freetalk 出張の予定`(テーマ指定)。
---

# /freetalk — 自由会話セッション

引数(テーマ、省略可): `$ARGUMENTS`

## 準備(学習者には見せない)

1. `TUTOR_GUIDE.md` と `prompts/free-talk.md` を読む。
2. `progress/profile.md` と、`progress/sessions/` の直近 3 ファイル(ファイル名の日付順)を読む。
3. テーマが空なら、記録にある学習者の興味・仕事の話題から 2〜3 案を出して選んでもらう。

## 進行

`prompts/free-talk.md` の「ルール」に従う。1 ターン 1 質問、英語が基本、会話中は訂正しない。
15〜20 往復、または学習者の「終了」で Wrap-up へ。

## 終了時(記録の保存とコミット)

1. `prompts/free-talk.md` の Wrap-up に従ってフィードバックを行う。
2. `progress/sessions/YYYY-MM-DD-freetalk.md` に記録を書く(日付は `date +%Y-%m-%d`。同日に複数回あれば `-2` を付ける)。
3. `progress/log.md` の表の末尾に 1 行追記: `| YYYY-MM-DD | Free Talk | テーマ | yes | … |`
4. `progress/profile.md` の「繰り返し出る弱点」「定着した表現」「本人について」を必要に応じて更新する(追記中心。本人が書いた部分は消さない)。
5. 次のコマンドでコミットする: `git add progress && git commit -m "Free talk の記録を追加 (YYYY-MM-DD)"`。
6. 「push しておきますか?」と一度だけ聞き、はいなら `git push`。
