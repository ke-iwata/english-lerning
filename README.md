# Business English 30

中学英語レベルから、ビジネスで使える英語へ。
**1 回 30 分・全 24 レッスン** の講師付き 1on1 英会話テキストと、それを **Claude Code で実践レッスンとして使う** ための仕組みです。

- 📖 サイト: https://ke-iwata.github.io/english-lerning/
- 🎓 対象: 中学英語が多少身についている社会人(例文・ロールプレイは IT 企業のバックエンドエンジニアを想定)
- 🎯 目標: 会議・報告・依頼・交渉・面接など、ビジネスに必要な英語力

## レッスンの構成(すべて共通・30 分)

| 時間 | セクション | 内容 |
|---|---|---|
| 3 分 | Warm-up | 復習質問 + 今日のテーマの質問 |
| 7 分 | Vocabulary & Idioms | 単語 8 + イディオム 4、発音・使い方の注意、Quick check |
| 7 分 | Key Expressions | 表現パターン 3〜4、ドリル、よくある間違い |
| 10 分 | Role-play | 場面設定 → モデル対話 → 自分の言葉で(予想外の一言つき) |
| 3 分 | Wrap-up | Self-check、宿題、次回予告 |

## カリキュラム

| Level | テーマ | レッスン |
|---|---|---|
| 1 基礎固め (A2) | まず止まらずに話す | 01 自己紹介 / 02 会社と仕事 / 03 スモールトーク / 04 数字・時間・日付 / 05 丁寧な依頼 / 06 聞き返し |
| 2 職場の日常 (A2+–B1) | 毎日の仕事のやりとり | 07 日程調整 / 08 進捗報告 / 09 意見・賛成・反対 / 10 問題の説明と相談 / 11 メールとチャット / 12 電話・オンライン会議 |
| 3 会議とプレゼン (B1) | 構造的に話す | 13 会議の進行 / 14 データと傾向 / 15 手順・仕組みの説明 / 16 短いプレゼン / 17 質疑応答 / 18 提案と交渉 |
| 4 実践 (B1+–B2) | 実戦場面 | 19 フィードバック(コードレビュー) / 20 障害報告 / 21 要件確認 / 22 英語面接 / 23 懇親会 / 24 総合演習 |

## Claude と声でレッスンする(Claude アプリの音声モード)

1. `python3 scripts/build_pack.py`(またはサイトからダウンロード)で `dist/claude-project/` の教材ファイルを用意
2. Claude アプリで Project を作り、instructions に `00-project-instructions.md` を貼り、knowledge にレッスンファイルをアップロード
3. Project 内のチャットで `Lesson 01` と送り、音声モードに入る。あとは声で会話
4. 終わったら「記録を作って」→ 記録をコピー → Claude Code で `/log`(保存・コミット・次回用 progress-pack 生成)

手順の詳細とトラブル対処は [`VOICE.md`](VOICE.md)。

## Claude Code でレッスンする(テキスト中心)

```bash
git clone https://github.com/ke-iwata/english-lerning.git
cd english-lerning
claude
```

Claude Code の中で:

```
/lesson 01          # Lesson 01 を 30 分の対話レッスンとして進行
/lesson             # 記録をもとに次のレッスンを自動で選ぶ
/lesson 05 roleplay # ロールプレイだけやる
/review             # これまでの弱点を 10〜15 分で復習
/freetalk 出張      # テキストを離れて自由会話(テーマは省略可)
/log                # Claude アプリ(音声モード)でやったレッスンの記録を取り込む
```

Claude は `TUTOR_GUIDE.md` の講師プロトコルに従って、英語で質問し、詰まったら日本語でヒントを出し、ロールプレイの相手役を務め、最後にフィードバックをします。
レッスン中はいつでも日本語で「ヒント」「もう一回」「日本語で」「スキップ」「終了」と言えます([チートシート](prompts/cheat-sheet.md))。

Claude Code 内でも `/voice tap`(音声入力)と `/lesson 01 voice`(返答の読み上げ)で声のレッスンができます([`VOICE.md`](VOICE.md) の「別の方法」)。

### レッスン記録は git に積み上がる

レッスンが終わると、Claude が記録を書いてコミットします。次回はその記録を読んでから始めるので、前回の弱点や宿題を踏まえた連続したレッスンになります。

```
progress/profile.md                      学習者プロファイル(自分で編集して OK。仕事や使う技術を書いておくとロールプレイが自分仕様になる)
progress/log.md                          一覧表
progress/sessions/2026-10-14-lesson-01.md   各回の詳細(良かった点・直す点・弱い単語・宿題・次回)
```

### Claude Code 以外(claude.ai のチャットなど)で使う

各レッスンページの **「Claude 用プロンプトをコピー」** を押すと、講師プロンプトとレッスン本文がまとめてコピーされます。claude.ai に貼り付ければ同じレッスンができます。詳しくは [`prompts/README.md`](prompts/README.md)。

## サイトをローカルで見る

ビルド不要です。

```bash
python3 -m http.server 8000
# http://localhost:8000/ を開く
```

## GitHub Pages で公開する

1. GitHub のリポジトリ設定 → **Pages** → **Build and deployment** の Source を **GitHub Actions** にする
2. `main` ブランチに push すると `.github/workflows/pages.yml` がデプロイする(手動実行も可)

## レッスンを追加・修正する

- ルールと雛形: [`lessons/AUTHORING.md`](lessons/AUTHORING.md)
- 講師の振る舞い: [`TUTOR_GUIDE.md`](TUTOR_GUIDE.md)、音声モード: [`VOICE.md`](VOICE.md)
- 一覧への登録: [`lessons/index.json`](lessons/index.json)
- チェック: `python3 scripts/check_lessons.py`

## ライセンス

MIT
