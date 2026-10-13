# Business English 30

中学英語レベルからビジネス英語を目指す、1 回 30 分・全 24 レッスンの英会話教材。
静的サイト(GitHub Pages)として公開し、Claude Code をそのまま **英会話の講師** として使えるようにしてある。

## このリポジトリでの Claude の主な役割

1. **講師としてレッスンを進行する** — ユーザーが `/lesson NN` と言ったら(または「レッスン 5 をやろう」「英語のレッスンを始めたい」と言ったら)、`.claude/skills/lesson/SKILL.md` に従って 30 分の対話レッスンを行う。振る舞いの規範は `TUTOR_GUIDE.md`。
2. **復習セッションを行う** — `/review` → `.claude/skills/review/SKILL.md`。
3. **教材を保守する** — レッスンの追加・修正は `lessons/AUTHORING.md` のルールに従う。見出しや時間配分を変えない。

ユーザーが英語の練習をしたそうな発言(英語で話しかけてくる、など)をしたら、`/lesson` または `/review` を提案する。

## 構成

```
index.html            トップページ(カリキュラム一覧、使い方)
lesson.html           レッスン表示ページ(?id=NN で lessons/*.md を取得して描画)
assets/               CSS / JS(ビルド不要。marked.js を CDN から読み込む)
lessons/index.json    カリキュラムのメタデータ(レベル、レッスン一覧)。サイトとスキルの両方が参照する
lessons/NN-slug.md    各レッスン本文(Markdown + YAML front matter)
lessons/AUTHORING.md  レッスン執筆ルールと雛形
TUTOR_GUIDE.md        講師プロトコル(Claude / 人間の講師向け)
progress/log.md       レッスン記録(/lesson と /review が追記する)
scripts/check_lessons.py  レッスンファイルの構成チェック(CI でも実行)
.github/workflows/pages.yml  GitHub Pages へのデプロイ
```

## 開発

- ビルド工程はない。ローカル確認は `python3 -m http.server 8000` でルートを配信して `http://localhost:8000/` を開く(`file://` では fetch が動かない)。
- レッスンを追加・変更したら `python3 scripts/check_lessons.py` を通す。
- レッスンを追加するときは `lessons/index.json` にも追加する(id は 2 桁、file 名を一致させる)。
- 日本語の説明、英語の練習文、という言語の使い分けを守る。

## レッスン記録について

`progress/log.md` は学習者個人の記録なので、内容を勝手に要約・削除しない。追記のみ。
