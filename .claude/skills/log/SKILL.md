---
name: log
description: Claude アプリ(音声モード)で行ったレッスンの記録を取り込む。クリップボードまたは貼り付けた記録テキストを progress/sessions/ に保存し、log.md と profile.md を更新して commit し、Project 用の progress-pack を再生成する。使い方 `/log`(クリップボードから)、`/log` の後に記録を貼り付け。
---

# /log — Claude アプリでのレッスン記録を取り込む

引数: `$ARGUMENTS`

音声モードのレッスン(Claude アプリ)の終わりに「記録を作って」と言って出力された記録を、このリポジトリに保存します。

## 手順

1. 記録テキストを取得する。
   - `$ARGUMENTS` に記録らしいテキスト(`# YYYY-MM-DD — Lesson NN` や `## Good` を含む)があればそれを使う。
   - なければ、macOS では `pbpaste`、Linux では `xclip -o` または `wl-paste`、Windows では `powershell Get-Clipboard` でクリップボードを読む。記録らしいテキストでなければ、「Claude アプリで出力された記録を貼り付けてください」と言って待つ。
2. 記録を解析する: 日付(なければ今日 `date +%Y-%m-%d`)、種別(Lesson NN / Review / Free Talk)、タイトル。`lessons/index.json` で番号とタイトルを照合する。
3. `progress/sessions/TEMPLATE.md` の形式に整えて `progress/sessions/YYYY-MM-DD-lesson-NN.md`(Review は `-review`、Free Talk は `-freetalk`)に保存する。同名があれば `-2` を付ける。内容は貼り付けられた記録を尊重し、勝手に要約しない。
4. `progress/log.md` の表の末尾に 1 行追記する: `| YYYY-MM-DD | Lesson NN | タイトル | yes または partial | Next の内容 |`
5. `progress/profile.md` を更新する: 「繰り返し出る弱点」「定着した表現」「本人について」に記録から分かることを追記(本人が書いた部分は消さない)。
6. `python3 scripts/build_pack.py` を実行し、`dist/claude-project/progress-pack.md` を再生成する。
7. `git add progress && git commit -m "Lesson NN の記録を追加 (YYYY-MM-DD)"`。「push しておきますか?」と一度だけ聞き、はいなら `git push`。
8. 最後に伝えること: 保存したファイル名、次回のレッスン番号、そして「Claude アプリの Project の progress-pack.md を `dist/claude-project/progress-pack.md` で差し替えると、次回のレッスンに今日の記録が反映されます」の一言。
