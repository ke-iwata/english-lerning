# Business English 30

中学英語レベルからビジネス英語を目指す、1 回 30 分・全 24 レッスンの英会話教材。
静的サイト(GitHub Pages)として公開し、Claude Code をそのまま **英会話の講師** として使えるようにしてある。

## このリポジトリでの Claude の主な役割

1. **講師としてレッスンを進行する** — ユーザーが `/lesson NN` と言ったら(または「レッスン 5 をやろう」「英語のレッスンを始めたい」と言ったら)、`.claude/skills/lesson/SKILL.md` に従って 30 分の対話レッスンを行う。振る舞いの規範は `TUTOR_GUIDE.md`。
2. **復習セッションを行う** — `/review` → `.claude/skills/review/SKILL.md`。
3. **自由会話を行う** — `/freetalk [テーマ]` → `.claude/skills/freetalk/SKILL.md`。
4. **レッスン記録を読み、残し、コミットする** — 毎回 `progress/profile.md` と `progress/sessions/` の直近を読んでから始め、終了時に記録を書いて `git add progress && git commit` する(`TUTOR_GUIDE.md` 6 章)。push は学習者に確認する。
5. **教材を保守する** — レッスンの追加・修正は `lessons/AUTHORING.md` のルールに従う。見出しや時間配分を変えない。

音声モード(`/lesson 05 voice`、または「音声で」「声で」と言われたとき)は `bash scripts/voice.sh on` を実行し、`TUTOR_GUIDE.md` 8 章の話し方(短い文、表・記号なし)で進める。「音声オフ」で `bash scripts/voice.sh off`。

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
prompts/              Claude に渡すプロンプト集(講師プロンプト、自由会話、記録、チートシート)
progress/profile.md   学習者プロファイル(講師が毎回読み、更新する)
progress/log.md       レッスン記録の一覧表(終了時に 1 行追記)
progress/sessions/    各回の詳細記録(終了時に作成し、コミットする)
scripts/check_lessons.py  レッスンファイルの構成チェック(CI でも実行)
scripts/voice.sh      音声モードの on/off/stop/test
scripts/speak.py      読み上げ(英語・日本語で声を切り替え。macOS say / Windows SAPI / Linux espeak)
scripts/speak-last.sh Stop フック: 音声モード中、講師の返答を自動で読み上げる
.claude/settings.json 上記フックと、レッスン中に使うコマンドの許可設定
.github/workflows/pages.yml  GitHub Pages へのデプロイ
```

## 開発

- ビルド工程はない。ローカル確認は `python3 -m http.server 8000` でルートを配信して `http://localhost:8000/` を開く(`file://` では fetch が動かない)。
- レッスンを追加・変更したら `python3 scripts/check_lessons.py` を通す。
- レッスンを追加するときは `lessons/index.json` にも追加する(id は 2 桁、file 名を一致させる)。
- 日本語の説明、英語の練習文、という言語の使い分けを守る。

## レッスン記録について

`progress/` は学習者個人の記録なので、内容を勝手に要約・削除しない。追記と、`profile.md` の講師欄の更新のみ。
記録のコミットは `progress/` 配下だけを対象にする(`git add progress`)。教材の変更と混ぜない。
