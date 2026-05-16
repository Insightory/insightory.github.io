---
layout: page
title: "오늘의 타로"
description: "당신의 오늘 운세를 타로로 찾아 드립니다"
permalink: /dailytarot/
---

<style>
/* ── Hero ─────────────────────────────────── */
.dt-hero {
  text-align: center;
  padding: 2.5rem 0 1rem;
}
.dt-hero-title {
  font-size: 1.75em;
  font-weight: 800;
  line-height: 1.5;
  background: linear-gradient(135deg, #c9a96e 0%, #f5e0a8 50%, #c9a96e 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.4rem;
  letter-spacing: -0.01em;
}
.dt-date-badge {
  display: inline-block;
  font-size: 0.9em;
  opacity: 0.65;
  border: 1px solid rgba(201,169,110,0.35);
  border-radius: 20px;
  padding: 3px 14px;
  margin-top: 0.4rem;
}

/* ── Yulha Image ──────────────────────────── */
.dt-yulha {
  text-align: center;
  margin: 0.5rem 0 1.5rem;
}
.dt-yulha img {
  max-width: 260px;
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 6px 24px rgba(0,0,0,0.35);
}

/* ── Fortune Table ───────────────────────── */
.fortune-wrap {
  margin: 1.5rem 0 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* 수직 중앙 정렬 */
  min-height: 200px; /* 필요 시 조정 */
}
.fortune-wrap { box-sizing: border-box; padding: 0 12px; }
.fortune-wrap h2 {
  text-align: center;
  font-size: 1.1em;
  opacity: 0.75;
  margin-bottom: 1rem;
  font-weight: 400;
}
.fortune-table {
  width: 100%;
  max-width: 520px;
  border-collapse: collapse;
  border-radius: 10px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.25);
  margin: 0 auto;
  table-layout: auto; /* 컨텐츠에 맞춰 컬럼 너비 조정 */
  overflow: visible; /* 잘림 방지 */
  box-sizing: border-box;
}
.fortune-table thead tr {
  background: linear-gradient(135deg, #2a1a4a, #4a2a8a);
}
.fortune-table th {
  color: #c9a96e;
  padding: 10px 6px;
  text-align: center;
  font-size: 1em;
  letter-spacing: 0.03em;
  border: none;
  white-space: normal;
  overflow-wrap: anywhere;
}
.fortune-table td {
  text-align: center;
  padding: 18px 8px;
  font-size: clamp(1.2rem, 3.5vw, 2.2em); /* 화면 크기에 따라 자동 축소 */
  font-weight: 800;
  color: var(--accent-color, #4fb1ba);
  background: rgba(74,42,138,0.08);
  border: 1px solid rgba(128,128,128,0.15);
}

@media (max-width: 420px) {
  .fortune-table td { padding: 12px 6px; font-size: 1.4em; }
  .fortune-table th { font-size: 0.92em; padding: 8px 6px; }
}
.fortune-caption {
  text-align: center;
  font-size: 0.82em;
  opacity: 0.5;
  margin-top: 0.6rem;
}
</style>

<!-- ① Hero -->
<div class="dt-hero">
  <div class="dt-hero-title">✨ 당신의 오늘 운세를<br/>타로로 찾아 드립니다 ✨</div>
</div>

<!-- ③ Yulha Image -->
<div class="dt-yulha">
  <img src="/assets/img/intro/yulha.jpg" alt="율하 타로 마스터" />
</div>

<!-- ④⑤⑥ Fortune Table -->
<div class="fortune-wrap">
  <h2>오늘 당신의 타로 번호</h2>
  <center>
  <table class="fortune-table">
    <thead>
      <tr>
        <th>연애운</th>
        <th>금전운</th>
        <th>건강운</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td id="love-num">–</td>
        <td id="money-num">–</td>
        <td id="health-num">–</td>
      </tr>
    </tbody>
  </table>
  </center>
</div>

<script>
// 오늘 날짜 전용 — 브라우저 ID 제거, 날짜만으로 시드 생성
(function () {
  function formatDateLabel(d){
    return d.getFullYear() + '년 ' + (d.getMonth() + 1) + '월 ' + d.getDate() + '일 운세';
  }

  const dateBadge = document.getElementById('dt-today-date');
  const today = new Date();

  // 문자열 -> 32bit 해시 (FNV-1a 변형)
  function xfnv1a(str) {
    let h = 2166136261 >>> 0;
    for (let i = 0; i < str.length; i++) {
      h ^= str.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    return h >>> 0;
  }

  // mulberry32 PRNG 생성기
  function mulberry32(a) {
    return function() {
      var t = a += 0x6D2B79F5;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // 날짜 문자열과 컬럼을 합쳐 난수 생성 (브라우저 ID 제거)
  function seededRandFor(dateStr, column) {
    const seedStr = dateStr + '|' + column;
    const seed = xfnv1a(seedStr);
    const rnd = mulberry32(seed);
    return rnd();
  }

  // 날짜 객체와 컬럼으로 카드 번호(2~79) 생성
  function getDailyCardForDate(dateObj, column) {
    const dateKey = dateObj.getFullYear() * 10000 + (dateObj.getMonth() + 1) * 100 + dateObj.getDate();
    const r = seededRandFor(String(dateKey), column);
    return Math.floor(r * 78) + 2; // 2~79
  }

  // 렌더(오늘 날짜 기준)
  document.getElementById('love-num').textContent = getDailyCardForDate(today, 1);
  document.getElementById('money-num').textContent = getDailyCardForDate(today, 2);
  document.getElementById('health-num').textContent = getDailyCardForDate(today, 3);
  dateBadge.textContent = formatDateLabel(today);
})();
</script>
