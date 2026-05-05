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

/* ── Shuffle Stage ────────────────────────── */
.shuffle-stage {
  position: relative;
  width: 100%;
  height: 180px;
  margin: 2rem auto 1.5rem;
  max-width: 420px;
  overflow: visible;
}
.tarot-card {
  position: absolute;
  width: 65px;
  height: 108px;
  left: 50%;
  top: 50%;
  margin-left: -32px;
  margin-top: -54px;
  border-radius: 7px;
  border: 2px solid #c9a96e;
  box-shadow: 0 4px 14px rgba(0,0,0,0.45);
  background: linear-gradient(160deg, #1e103a 0%, #3a1a72 60%, #1e103a 100%);
  cursor: pointer;
  transform-origin: center bottom;
}
/* Card inner pattern */
.tarot-card::before {
  content: '✦';
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2em;
  color: rgba(201,169,110,0.5);
}
.tarot-card::after {
  content: '';
  position: absolute;
  inset: 5px;
  border: 1px solid rgba(201,169,110,0.3);
  border-radius: 4px;
}

/* Individual card animations */
@keyframes fan-c1 {
  0%,100% { transform: translateX(0) translateY(0) rotate(0deg); z-index:1; }
  40%,60% { transform: translateX(-145px) translateY(10px) rotate(-25deg); z-index:1; }
}
@keyframes fan-c2 {
  0%,100% { transform: translateX(0) translateY(0) rotate(0deg); z-index:2; }
  40%,60% { transform: translateX(-95px) translateY(5px) rotate(-15deg); z-index:2; }
}
@keyframes fan-c3 {
  0%,100% { transform: translateX(0) translateY(0) rotate(0deg); z-index:3; }
  40%,60% { transform: translateX(-45px) translateY(2px) rotate(-7deg); z-index:3; }
}
@keyframes fan-c4 {
  0%,100% { transform: translateX(0) translateY(0) rotate(0deg); z-index:4; }
  40%,60% { transform: translateX(0px) translateY(-5px) rotate(0deg); z-index:4; }
}
@keyframes fan-c5 {
  0%,100% { transform: translateX(0) translateY(0) rotate(0deg); z-index:3; }
  40%,60% { transform: translateX(45px) translateY(2px) rotate(7deg); z-index:3; }
}
@keyframes fan-c6 {
  0%,100% { transform: translateX(0) translateY(0) rotate(0deg); z-index:2; }
  40%,60% { transform: translateX(95px) translateY(5px) rotate(15deg); z-index:2; }
}
@keyframes fan-c7 {
  0%,100% { transform: translateX(0) translateY(0) rotate(0deg); z-index:1; }
  40%,60% { transform: translateX(145px) translateY(10px) rotate(25deg); z-index:1; }
}

#tc1 { animation: fan-c1 3.2s ease-in-out infinite; }
#tc2 { animation: fan-c2 3.2s ease-in-out infinite 0.05s; }
#tc3 { animation: fan-c3 3.2s ease-in-out infinite 0.1s; }
#tc4 { animation: fan-c4 3.2s ease-in-out infinite 0.15s; }
#tc5 { animation: fan-c5 3.2s ease-in-out infinite 0.1s; }
#tc6 { animation: fan-c6 3.2s ease-in-out infinite 0.05s; }
#tc7 { animation: fan-c7 3.2s ease-in-out infinite 0s; }

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
}
.fortune-wrap h2 {
  text-align: center;
  font-size: 1.1em;
  opacity: 0.75;
  margin-bottom: 1rem;
  font-weight: 400;
}
.fortune-table {
  width: 100%;
  border-collapse: collapse;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0,0,0,0.25);
}
.fortune-table thead tr {
  background: linear-gradient(135deg, #2a1a4a, #4a2a8a);
}
.fortune-table th {
  color: #c9a96e;
  padding: 14px 8px;
  text-align: center;
  font-size: 1em;
  letter-spacing: 0.03em;
  border: none;
}
.fortune-table td {
  text-align: center;
  padding: 22px 8px;
  font-size: 2.2em;
  font-weight: 800;
  color: var(--accent-color, #4fb1ba);
  background: rgba(74,42,138,0.08);
  border: 1px solid rgba(128,128,128,0.15);
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
  <div class="dt-date-badge" id="dt-today-date">로딩 중…</div>
</div>

<!-- ② Card Shuffle Animation -->
<div class="shuffle-stage">
  <div class="tarot-card" id="tc1"></div>
  <div class="tarot-card" id="tc2"></div>
  <div class="tarot-card" id="tc3"></div>
  <div class="tarot-card" id="tc4"></div>
  <div class="tarot-card" id="tc5"></div>
  <div class="tarot-card" id="tc6"></div>
  <div class="tarot-card" id="tc7"></div>
</div>

<!-- ③ Yulha Image -->
<div class="dt-yulha">
  <img src="/assets/img/intro/yulha.jpg" alt="율하 타로 마스터" />
</div>

<!-- ④⑤⑥ Fortune Table -->
<div class="fortune-wrap">
  <h2>오늘 당신의 타로 번호</h2>
  <table class="fortune-table">
    <thead>
      <tr>
        <th>💕 연애운</th>
        <th>💰 금전운</th>
        <th>💪 건강운</th>
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
</div>

<script>
// ── 오늘 날짜 표시 ────────────────────────
(function () {
  const d = new Date();
  const label = d.getFullYear() + '년 ' +
                (d.getMonth() + 1) + '월 ' +
                d.getDate() + '일 운세';
  document.getElementById('dt-today-date').textContent = label;
})();

// ── 날짜 기반 시드 PRNG ──────────────────
// 같은 날짜 → 항상 같은 숫자 (2~79)
function seededRand(seed) {
  // 간단한 mulberry32 변형
  seed = seed ^ 0xdeadbeef;
  seed = Math.imul(seed ^ (seed >>> 16), 0x45d9f3b);
  seed = Math.imul(seed ^ (seed >>> 16), 0x45d9f3b);
  seed = seed ^ (seed >>> 16);
  // 0~1 사이 양수값
  return (seed >>> 0) / 4294967296;
}

function getDailyCard(column) {
  const d = new Date();
  // 날짜를 정수 시드로 변환: YYYYMMDD + column offset
  const dateInt = d.getFullYear() * 10000 +
                  (d.getMonth() + 1) * 100 +
                  d.getDate();
  const seed = dateInt + column * 9973; // 소수로 column 분리
  return Math.floor(seededRand(seed) * 78) + 2; // 2~79
}

document.getElementById('love-num').textContent   = getDailyCard(1);
document.getElementById('money-num').textContent  = getDailyCard(2);
document.getElementById('health-num').textContent = getDailyCard(3);
</script>
