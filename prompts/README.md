# プロンプト集 (Prompts)

Claude にレッスンをしてもらうときのプロンプトをまとめています。
Claude Code を使う場合は `/lesson` `/review` `/freetalk` スキルがこれらを自動で読むので、**ユーザーが自分で貼り付ける必要はありません**。
claude.ai のチャットやアプリ(音声入力が使えるので会話練習に向いています)など、Claude Code 以外で使うときは、ここのプロンプトをコピーして貼り付けます。

| ファイル | 用途 | 使う人 |
|---|---|---|
| [`tutor-system-prompt.md`](tutor-system-prompt.md) | 講師役 Claude の基本プロンプト。レッスン本文と記録を差し込んで使う | Claude Code(自動)/ チャット(手動) |
| [`lesson-start.md`](lesson-start.md) | レッスン開始時にユーザーが送る指示の例 | ユーザー |
| [`cheat-sheet.md`](cheat-sheet.md) | レッスン中に使える一言(ヒント・もう一回・日本語で…)と、英語で言いたいときの表現 | ユーザー |
| [`free-talk.md`](free-talk.md) | テキストから離れて自由会話をするときのプロンプト | Claude Code(`/freetalk`)/ チャット |
| [`record-session.md`](record-session.md) | レッスン終了時に記録を残させるプロンプト(Claude が記録を忘れたときにも使う) | Claude Code(自動)/ チャット |

## claude.ai のチャットで使う手順

1. 各レッスンページ(サイト)の **「Claude 用プロンプトをコピー」** ボタンを押す
   → 講師プロンプト + そのレッスンの本文がまとめてクリップボードに入ります
2. claude.ai で新しいチャットを開き、貼り付けて送信する
3. 前回までの記録を反映させたいときは、`progress/profile.md` と直近の `progress/sessions/*.md` の内容も続けて貼り付ける
4. レッスンが終わったら [`record-session.md`](record-session.md) を貼り付けて記録を書いてもらい、その内容を `progress/sessions/` に保存してコミットする

## Claude Code で使う手順

```
/lesson 03        # Lesson 03 を開始(記録の読み込み・レッスン進行・記録の保存とコミットまで自動)
/lesson           # 記録から次のレッスンを自動選択
/review           # 弱点の復習
/freetalk 出張    # テーマを決めて自由会話(テーマ省略可)
```

レッスン後の記録は `progress/` に保存され、Claude が自動で git commit します(push は確認してから)。
次回のレッスンでは、講師がその記録を読んでから始めます。
