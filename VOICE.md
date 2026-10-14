# 音声でレッスンを受ける (Voice Mode)

Claude Code(デスクトップアプリ / CLI / VS Code 拡張)で、**自分は声で話し、講師の返答も声で聞く** 設定です。
仕組みは 2 つの組み合わせです。

| 方向 | 使うもの | 備考 |
|---|---|---|
| あなた → Claude(音声入力) | Claude Code 標準の **`/voice`**(音声ディクテーション) | claude.ai アカウントでのログインが必要。ローカルのマイクを使う |
| Claude → あなた(読み上げ) | このリポジトリの **Stop フック** + `scripts/speak.py` | macOS は標準の `say`(追加インストール不要)。英語は英語の声、日本語は日本語の声で読む |

## セットアップ(macOS、初回のみ)

1. リポジトリを clone して Claude Code を起動する

   ```bash
   git clone https://github.com/ke-iwata/english-lerning.git
   cd english-lerning
   claude
   ```

   起動時に、このリポジトリの `.claude/settings.json`(フックと許可設定)を信頼するか聞かれたら許可します。

2. 読み上げが鳴るか確認する(Claude Code の中で、または普通のターミナルで)

   ```
   !scripts/voice.sh test
   ```

   「Hi Ken, nice to meet you. 今日は自己紹介の練習をしましょう。」が英語・日本語の声で読まれれば OK。
   声が出ない場合は macOS の「システム設定 → アクセシビリティ → 読み上げコンテンツ」で英語(Samantha など)と日本語(Kyoko)の声がダウンロードされているか確認してください。

3. 音声入力をオンにする(Claude Code の中で)

   ```
   /voice tap
   ```

   - **tap モード**: Space を 1 回押して話し始め、もう 1 回押すと止まって自動送信(3 語以上のとき)。会話練習にはこれが楽です。
   - **hold モード**(既定): Space を押している間だけ録音。離すと文字になり、Enter で送信。`/voice hold` で切り替え。
   - `/voice off` でオフ。Esc で録音キャンセル。

   日本語で「ヒント」「もう一回」と言いたいときも、英語設定のままで大体通じます。日本語の認識精度を上げたい場合は、Claude Code の `language` 設定を `ja` にします(ただし英語の認識は英語設定の方が正確です)。

## レッスンを始める

```
/lesson 01 voice
```

`voice` を付けると、講師が `scripts/voice.sh on` を実行し、以後の返答が自動で読み上げられます。講師は音声用の話し方(短い文、表や記号を使わない)に切り替わります。

毎回 `voice` を付けるのが面倒なら、`progress/profile.md` の「進め方の希望」を `音声モード: on` にしてください。`/lesson` `/review` `/freetalk` すべてで読み上げが有効になります。

## レッスン中の操作

| したいこと | 方法 |
|---|---|
| 読み上げを途中で止める | `!scripts/voice.sh stop`(または Claude に「音声オフ」) |
| 読み上げをオフにする | Claude に「音声オフ」と言う(`scripts/voice.sh off`) |
| 読み上げをオンに戻す | Claude に「音声オン」と言う(`scripts/voice.sh on`) |
| もう一回聞きたい | 「もう一回」(講師がゆっくり言い直す) |
| 聞き取れたか自信がない | 「今のを書いて」(講師が文字でも示す) |
| ゆっくり話してほしい | 「ゆっくり」 |

## 声と速さを変える

環境変数で変えられます(`~/.zshrc` などに書いておく)。

```bash
export VOICE_EN=Samantha   # 英語の声。候補: say -v '?' | grep en_
export VOICE_JA=Kyoko      # 日本語の声
export VOICE_RATE=150      # 速さ(words per minute)。既定 165。初心者は 140〜150 が聞き取りやすい
```

より自然な声にしたい場合は、macOS の「読み上げコンテンツ」で Premium / Enhanced 版の声(例: Ava (Premium), Zoe (Premium))をダウンロードし、`VOICE_EN="Ava (Premium)"` のように指定します。

## Windows / Linux の場合

- **Windows**: PowerShell の System.Speech を使います(標準で英語の声あり。日本語の声は「設定 → 時刻と言語 → 音声認識」で追加)。`python3` が必要です。
- **Linux**: `espeak-ng` または `speech-dispatcher`(`spd-say`)をインストールしてください。

```bash
sudo apt install espeak-ng        # Debian / Ubuntu
```

`/voice`(音声入力)は Claude Code 側の機能なので OS を問わず使えますが、クラウドセッションや SSH 越しでは使えません(ローカルのマイクが必要)。

## 仕組み(カスタマイズしたい人向け)

- `.claude/settings.json` の `Stop` フックが、Claude の返答完了ごとに `scripts/speak-last.sh` を呼びます。
- `speak-last.sh` は `.claude/.voice-on` があるときだけ動き、フックの入力に含まれる `last_assistant_message` を `scripts/speak.py --clean-markdown` に渡します(Markdown の記号や表を読み上げ用に整形し、英語と日本語を分けてそれぞれの声で読む)。読み上げはバックグラウンドなので、次の入力をすぐ始められます。
- 読み上げを手動で試す: `python3 scripts/speak.py "Hello. こんにちは。"`。整形結果だけ見る: `VOICE_DRY_RUN=1 python3 scripts/speak.py --clean-markdown < file.md`。
