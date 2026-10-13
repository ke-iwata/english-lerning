/* Business English 30 — site script (no build step) */
(function (global) {
  'use strict';

  var REPO_URL = 'https://github.com/ke-iwata/english-lerning';
  var STORAGE_KEY = 'be30.done';
  var SECTIONS = [
    { name: 'Warm-up', min: 3 },
    { name: 'Vocabulary & Idioms', min: 7 },
    { name: 'Key Expressions', min: 7 },
    { name: 'Role-play', min: 10 },
    { name: 'Wrap-up', min: 3 }
  ];

  // ---------- storage (best effort) ----------
  function loadDone() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }
  function saveDone(obj) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(obj)); } catch (e) { /* ignore */ }
  }

  // ---------- helpers ----------
  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === 'class') node.className = attrs[k];
        else if (k === 'text') node.textContent = attrs[k];
        else if (k === 'html') node.innerHTML = attrs[k];
        else node.setAttribute(k, attrs[k]);
      });
    }
    (children || []).forEach(function (c) { if (c) node.appendChild(c); });
    return node;
  }
  function fetchJSON(url) { return fetch(url).then(function (r) { if (!r.ok) throw new Error(r.status + ' ' + url); return r.json(); }); }
  function fetchText(url) { return fetch(url).then(function (r) { if (!r.ok) throw new Error(r.status + ' ' + url); return r.text(); }); }
  function getParam(name) { return new URLSearchParams(location.search).get(name); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }

  function wireCopyButtons(root) {
    (root || document).querySelectorAll('[data-copy], [data-copy-target]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var text;
        var targetId = btn.getAttribute('data-copy-target');
        if (targetId) text = document.getElementById(targetId).textContent;
        else text = btn.parentNode.querySelector('span').textContent;
        var done = function () { btn.textContent = 'コピーしました'; setTimeout(function () { btn.textContent = 'コピー'; }, 1500); };
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, done);
        else done();
      });
    });
  }

  // ---------- index page ----------
  function renderIndex() {
    wireCopyButtons();
    var root = document.getElementById('levels');
    fetchJSON('lessons/index.json').then(function (data) {
      var done = loadDone();
      root.innerHTML = '';
      data.levels.forEach(function (lv) {
        var lessons = data.lessons.filter(function (l) { return l.level === lv.level; });
        var list = el('div', { class: 'lesson-list' }, lessons.map(function (l) {
          var isDone = !!done[l.id];
          return el('a', { class: 'lesson-card l' + l.level + (isDone ? ' done' : ''), href: 'lesson.html?id=' + l.id }, [
            el('div', { class: 'num', text: l.id }),
            el('div', { class: 'meta' }, [
              el('p', { class: 'title', text: l.title }),
              el('p', { class: 'title-en', text: l.title_en }),
              el('p', { class: 'cando', text: l.can_do })
            ]),
            isDone ? el('span', { class: 'check', text: '✓' }) : null
          ]);
        }));
        root.appendChild(el('div', { class: 'level', id: 'level-' + lv.level }, [
          el('div', { class: 'level-head' }, [
            el('span', { class: 'tag-level l' + lv.level, text: 'Level ' + lv.level }),
            el('h3', { text: lv.name + ' / ' + lv.name_en }),
            el('span', { class: 'cefr', text: '目安: CEFR ' + lv.cefr })
          ]),
          el('p', { class: 'level-desc', text: lv.description }),
          list
        ]));
      });

      var total = data.lessons.length;
      var count = data.lessons.filter(function (l) { return done[l.id]; }).length;
      if (count > 0) {
        var sec = document.getElementById('progress-section');
        sec.hidden = false;
        document.getElementById('progress-fill').style.width = Math.round(count / total * 100) + '%';
        document.getElementById('progress-text').textContent = count + ' / ' + total + ' レッスン完了';
      }
    }).catch(function (err) {
      root.innerHTML = '<p class="error">レッスン一覧を読み込めませんでした: ' + err.message + '</p>';
    });
  }

  // ---------- lesson page ----------
  function stripFrontMatter(md) {
    return md.replace(/^---[\s\S]*?\n---\s*\n/, '');
  }

  function renderLesson() {
    wireCopyButtons();
    var id = getParam('id') || '01';
    var content = document.getElementById('content');

    fetchJSON('lessons/index.json').then(function (data) {
      var idx = data.lessons.findIndex(function (l) { return l.id === id; });
      if (idx < 0) throw new Error('Lesson ' + id + ' は見つかりません');
      var lesson = data.lessons[idx];
      var prev = data.lessons[idx - 1];
      var next = data.lessons[idx + 1];

      document.title = 'Lesson ' + lesson.id + ': ' + lesson.title + ' — Business English 30';
      document.getElementById('level-tag').innerHTML = '<span class="tag-level l' + lesson.level + '">Level ' + lesson.level + '</span>';
      document.getElementById('lesson-pos').textContent = 'Lesson ' + lesson.id + ' / ' + pad(data.lessons.length);
      document.getElementById('claude-cmd').textContent = 'Claude Code で始める: /lesson ' + lesson.id;
      document.getElementById('claude-cmd-raw').textContent = '/lesson ' + lesson.id;
      document.getElementById('source-link').href = REPO_URL + '/blob/main/lessons/' + lesson.file;

      var prevLink = document.getElementById('prev-link');
      var nextLink = document.getElementById('next-link');
      if (prev) { prevLink.href = 'lesson.html?id=' + prev.id; prevLink.textContent = '← ' + prev.id + ' ' + prev.title; }
      else prevLink.classList.add('disabled');
      if (next) { nextLink.href = 'lesson.html?id=' + next.id; nextLink.textContent = next.id + ' ' + next.title + ' →'; }
      else { nextLink.href = './#curriculum'; nextLink.textContent = 'カリキュラムへ →'; }

      // done toggle
      var doneBtn = document.getElementById('done-btn');
      function refreshDone() {
        var d = loadDone();
        doneBtn.classList.toggle('active', !!d[lesson.id]);
        doneBtn.textContent = d[lesson.id] ? '✓ 完了済み' : '✓ 完了にする';
      }
      doneBtn.addEventListener('click', function () {
        var d = loadDone();
        if (d[lesson.id]) delete d[lesson.id]; else d[lesson.id] = new Date().toISOString().slice(0, 10);
        saveDone(d);
        refreshDone();
      });
      refreshDone();

      return fetchText('lessons/' + lesson.file);
    }).then(function (md) {
      var html = marked.parse(stripFrontMatter(md), { gfm: true, breaks: true });
      content.innerHTML = html;
      // make task-list checkboxes interactive (self-check)
      content.querySelectorAll('input[type="checkbox"]').forEach(function (cb) { cb.disabled = false; });
      // open external links in new tab
      content.querySelectorAll('a[href^="http"]').forEach(function (a) { a.target = '_blank'; a.rel = 'noopener'; });
      if (location.hash) {
        var target = document.querySelector(location.hash);
        if (target) target.scrollIntoView();
      }
    }).catch(function (err) {
      content.innerHTML = '<p class="error">レッスンを読み込めませんでした: ' + err.message + '</p><p><a href="./">トップへ戻る</a></p>';
    });

    setupTimer();
  }

  // ---------- 30-minute timer ----------
  function setupTimer() {
    var btn = document.getElementById('timer-btn');
    var timeEl = document.getElementById('timer-time');
    var phaseEl = document.getElementById('timer-phase');
    var box = document.getElementById('timer');
    var total = SECTIONS.reduce(function (s, x) { return s + x.min; }, 0) * 60;
    var startAt = null, handle = null;

    function phaseAt(elapsed) {
      var acc = 0;
      for (var i = 0; i < SECTIONS.length; i++) {
        acc += SECTIONS[i].min * 60;
        if (elapsed < acc) return { s: SECTIONS[i], left: acc - elapsed, idx: i };
      }
      return null;
    }
    function tick() {
      var elapsed = Math.floor((Date.now() - startAt) / 1000);
      var remain = total - elapsed;
      var sign = remain < 0 ? '-' : '';
      var r = Math.abs(remain);
      timeEl.textContent = sign + pad(Math.floor(r / 60)) + ':' + pad(r % 60);
      var p = phaseAt(elapsed);
      if (p) {
        phaseEl.innerHTML = '<strong>' + (p.idx + 1) + '. ' + p.s.name + '</strong> あと ' + Math.ceil(p.left / 60) + ' 分';
        box.classList.remove('over');
      } else {
        phaseEl.innerHTML = '<strong>30分終了</strong> お疲れさまでした';
        box.classList.add('over');
      }
    }
    btn.addEventListener('click', function () {
      if (handle) {
        clearInterval(handle); handle = null; startAt = null;
        btn.textContent = '▶ 30分タイマー';
        timeEl.textContent = '30:00';
        phaseEl.textContent = 'Warm-up 3分 → 単語 7分 → 表現 7分 → ロールプレイ 10分 → まとめ 3分';
        box.classList.remove('over');
        return;
      }
      startAt = Date.now();
      btn.textContent = '■ リセット';
      tick();
      handle = setInterval(tick, 1000);
    });
  }

  global.BE30 = { renderIndex: renderIndex, renderLesson: renderLesson };
})(window);
