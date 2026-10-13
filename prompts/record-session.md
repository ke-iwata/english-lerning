# レッスン記録プロンプト (Record Session)

レッスン終了時に記録を残すためのプロンプトです。
Claude Code の `/lesson` `/review` `/freetalk` は、このプロンプトの内容を自動で行い、git commit まで実行します。
claude.ai のチャットで Claude が記録を出さなかったとき、または途中で終わったときに貼り付けてください。

---

今日のレッスンはここまでにします。これまでの会話をもとに、次の 2 つを出力してください。

## 1. レッスン記録(Markdown のコードブロックで)

```markdown
# YYYY-MM-DD — Lesson NN: タイトル

- **Completed:** yes / partial(どこまで)
- **Sections:** Warm-up ✓ / Vocabulary ✓ / Key Expressions ✓ / Role-play ✓(Variation A, B)/ Wrap-up ✓

## Good
- (私の実際の発話を引用して 2〜3 点)

## To improve
- ✗ … → ✓ …(理由を一言)

## Weak vocabulary
- (出てこなかった・間違えた単語や表現)

## Learner notes
- (私の仕事・興味・話したがったことなど、次回に活かせる情報)

## Homework
- …

## Next
- Lesson NN(または Review NN)、次回の Warm-up で聞くこと
```

## 2. プロフィールの更新案

`progress/profile.md` に追記・修正すべき点があれば、箇条書きで(例: 「冠詞の抜けが 3 回連続で出ている」「本人の担当は決済基盤ではなく検索 API」)。なければ「更新なし」。

---

## 保存とコミット(ユーザーが手動で行う場合)

```bash
# 記録を保存
cat > progress/sessions/$(date +%Y-%m-%d)-lesson-NN.md   # 上の記録を貼り付けて Ctrl-D
# profile.md を必要に応じて編集
git add progress
git commit -m "Lesson NN の記録を追加 ($(date +%Y-%m-%d))"
git push
```
