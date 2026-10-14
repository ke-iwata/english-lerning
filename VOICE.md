# 音声でレッスンを受ける (Voice Lessons)

**Claude アプリの音声モード**(声で話し、Claude が声で答える)で、Claude に講師をさせる手順です。
Claude アプリの Project に講師インストラクションとレッスン教材を入れ、その Project の中で音声モードを使います。

音声モードは iOS / Android / Claude Desktop / Web で使えます(公式: [Use voice mode](https://support.claude.com/en/articles/11101966-use-voice-mode))。スマホが一番快適です。Claude Code と Cowork には音声モードはなく、音声入力(ディクテーション)だけです。

## 1. 教材ファイルを用意する(初回のみ)

サイトからダウンロードするか、リポジトリで生成します。

- サイト: https://ke-iwata.github.io/english-lerning/#voice にダウンロードリンクがあります
- リポジトリ: `python3 scripts/build_pack.py` → `dist/claude-project/` に出力

| ファイル | 用途 |
|---|---|
| `00-project-instructions.md` | Project の **instructions** に貼る講師インストラクション(音声用の話し方ルール入り) |
| `01-curriculum.md` | レッスン一覧(Claude が番号からレッスンを探すため) |
| `level1-foundation.md` 〜 `level4-practice.md` | レッスン本文(Level ごと)。**Project knowledge にアップロード** |
| `lessons-all.md` | 全レッスン 1 ファイル版(Level 別の代わりに使ってもよい) |
| `progress-pack.md` | 学習者プロファイル + 直近の記録。**レッスンのたびに差し替える** |

## 2. Claude アプリで Project を作る(初回のみ)

1. claude.ai(または Claude Desktop / スマホアプリ)で **Projects → New Project**。名前は「Business English 30」など。
2. **Set project instructions** を開き、`00-project-instructions.md` の中身を貼り付けて保存。
3. 右側の **Project knowledge** に `01-curriculum.md`、`level1-foundation.md`〜`level4-practice.md`、`progress-pack.md` をアップロード。

Project の instructions と knowledge は、その Project 内のすべてのチャットに適用されます。Project ごとに独立したメモリがあり、有料プランでは Project 内の過去チャットを Claude が参照できます(公式: [Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)、[Memory](https://support.claude.com/en/articles/11817273))。

## 3. レッスンを受ける

1. Project の中で **新しいチャット** を開く。
2. 最初に、テキストで `Lesson 03` と送る(レッスンを確実に特定させるため。番号なしで「レッスン始めて」でも、記録から次を選びます)。
3. 入力欄の右の **音波アイコン** を押して音声モードに入る。Claude が Warm-up の質問から始めます。
4. あとは声で会話するだけ。詰まったら日本語で「ヒント」「もう一回」「日本語で」「ゆっくり」「終了」と言えば講師が対応します。
5. 声の種類と速さは、音声モード中の設定(スマホ)または Settings → General → Voice(デスクトップ / Web)で変えられます。英語で話す練習なので、Voice の Language は **English** のままで OK です(日本語の合図も通じます)。

音声モードはターン制(こちらが話し終わると Claude が答える)なので、言い終えたら少し間を置くか、騒がしい場所ではプッシュトゥトーク(押している間だけ録音)にしてください。

## 4. レッスン後: 記録を残す

音声モードを **Stop** で止めてから、テキストで `記録を作って` と送ります。Claude が決まった形式の記録(良かった点・直す点・弱い単語・宿題・次回)を出すので、それを **コピー** します。

次に、リポジトリで Claude Code を開き:

```
/log
```

クリップボードの記録を `progress/sessions/` に保存し、一覧と学習者プロファイルを更新し、`git commit` し、`dist/claude-project/progress-pack.md` を再生成します。最後に Project knowledge の `progress-pack.md` を新しいものに差し替えれば、次回のレッスンに今日の記録が反映されます(有料プランなら Project のメモリでも前回の内容は引き継がれますが、差し替えておくと確実です)。

Claude Code を使わない場合は、記録を `progress/sessions/YYYY-MM-DD-lesson-NN.md` として保存して commit してください([prompts/record-session.md](prompts/record-session.md) に手順)。

## 5. うまくいかないとき

| 症状 | 対処 |
|---|---|
| Claude がレッスンの内容を知らない | Project の中でチャットを始めているか確認。knowledge にレッスンファイルが入っているか確認。最初のメッセージでレッスン番号を送る |
| 一度に長く読み上げる | 「短くして。1 回に 1 つだけ聞いて」と言う。instructions が貼られているか確認 |
| 英語を聞き取ってもらえない | ゆっくり、文を短く。騒音が多い場所ではプッシュトゥトークに。Settings → Voice → Language が English か確認 |
| 日本語の合図が通じない | 「hint」「again」「in Japanese」「stop」でも通じます |
| 前回の内容を覚えていない | `/log` で progress-pack.md を再生成して Project knowledge を差し替える |

## 別の方法: Claude Code で読み上げる

Claude アプリの音声モードを使わず、Claude Code(デスクトップ / CLI)で `/lesson` を使いながら講師の返答を読み上げさせることもできます(音声入力は Claude Code の `/voice`、読み上げは macOS の `say` を Stop フックで鳴らす仕組み)。記録の保存とコミットが自動になる利点がありますが、会話の自然さは Claude アプリの音声モードの方が上です。

```
/voice tap          # Claude Code の音声入力(Space を押して話す)
/lesson 01 voice    # 返答を自動で読み上げ(scripts/voice.sh on)
```

声や速さは環境変数 `VOICE_EN`(既定 Samantha)、`VOICE_JA`(Kyoko)、`VOICE_RATE`(165)で変更。`scripts/voice.sh test` で動作確認、`scripts/voice.sh stop` で停止、Claude に「音声オフ」で解除。Windows は PowerShell の標準音声、Linux は `espeak-ng` を使います。
