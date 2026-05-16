---
layout: page
title: "가격 소개"
description: "타로 상담 가격 소개"
permalink: /price/
---

## 상품 구조
<div style="display: grid; grid-template-columns: 1fr; gap: 16px; align-items: stretch; margin-top: 20px; margin-bottom: 30px;">

  <!-- 10분 체험 -->
  <div style="border: 1px solid rgba(128,128,128,0.3); border-radius: 8px; padding: 16px 20px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
      <h3 style="margin: 0;">10분 체험</h3>
      <span style="font-size: 1.1em; font-weight: bold; color: var(--accent-color, #4fb1ba);">12,000원</span>
    </div>
    <p style="font-size: 0.9em; margin: 0; opacity: 0.85;">간단하고 빠르게 현재 상황에 대한 조언과 통찰을 얻고 싶을 때 추천합니다.</p>
  </div>

  <!-- 20분 상담 -->
  <div style="border: 1px solid rgba(128,128,128,0.3); border-radius: 8px; padding: 16px 20px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
      <h3 style="margin: 0;">20분 상담</h3>
      <span style="font-size: 1.1em; font-weight: bold; color: var(--accent-color, #4fb1ba);">24,000원</span>
    </div>
    <p style="font-size: 0.9em; margin: 0; opacity: 0.85;">기본적인 타로 상담으로 한 가지 주제에 대해 심층적인 리딩이 가능합니다.</p>
  </div>

  <!-- 40분 상담 -->
  <div style="border: 1px solid rgba(128,128,128,0.3); border-radius: 8px; padding: 16px 20px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
      <h3 style="margin: 0;">40분 상담</h3>
      <span style="font-size: 1.1em; font-weight: bold; color: var(--accent-color, #4fb1ba);">46,000원</span>
    </div>
    <p style="font-size: 0.9em; margin: 0; opacity: 0.85;">두 가지 이상의 주제를 다루거나, 더 깊고 자세한 이야기를 나누고 싶을 때 좋습니다.</p>
  </div>

  <!-- 60분 상담 -->
  <div style="border: 1px solid rgba(128,128,128,0.3); border-radius: 8px; padding: 16px 20px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
      <h3 style="margin: 0;">60분 상담</h3>
      <span style="font-size: 1.1em; font-weight: bold; color: var(--accent-color, #4fb1ba);">69,000원</span>
    </div>
    <p style="font-size: 0.9em; margin: 0; opacity: 0.85;">충분한 시간 동안 편안한 대화 및 종합적인 심도 있는 분석을 원하실 때 추천합니다.</p>
  </div>

</div>


## 상담 방법
* 전화 상담
* 채팅 상담
* 방문 상담

## 상담 예약
* 전화: <a href="tel:01064973389" class="call-btn">010-6497-3389</a>
* 이메일: <a href="mailto:yulha3389@gmail.com?subject=율하타로상담예약">타로이메일상담</a>
* 카카오톡ID: <a href="#" onclick="openKakaoTalk(); return false;">yulhatarot</a>
* 카카오 오픈채팅: <a href="https://open.kakao.com/o/s6oJCqYh" class="kakao-btn">오픈 채팅 입장 </a>
* 방문 상담: 대면 상담을 통해 빠르게 흐름을 잡고 싶은 분께 추천 (카톡으로 문의) 

<!-- div style="margin-top: 0.5rem; margin-bottom: 1rem;">
  <iframe
    src="https://maps.google.com/maps?q=%EC%88%98%EC%9B%90%EC%97%AD&t=m&z=16&output=embed&iwloc=near"
    width="100%"
    height="300"
    style="border: none; border-radius: 8px; display: block;"
    allowfullscreen=""
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
    title="율하타로 위치">
  </iframe>
</div  -->

<script>
function openKakaoTalk() {
  var deepLink  = 'kakaotalk://friend/add?id=yulhatarot';
  var fallback  = 'https://open.kakao.com/o/s6oJCqYh';
  var isMobile  = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

  // PC: 딥링크 불필요 → 오픈채팅 바로 열기
  if (!isMobile) {
    window.open(fallback, '_blank');
    return;
  }

  // 모바일: 1500ms 안에 앱이 열리지 않으면(blur 없음) 폴백 실행
  var timer = setTimeout(function () {
    window.location.href = fallback;
  }, 1500);

  // 앱이 실행되면 브라우저가 blur → 타이머 취소
  window.addEventListener('blur', function onBlur() {
    clearTimeout(timer);
    window.removeEventListener('blur', onBlur);
  });

  // 딥링크 시도
  window.location.href = deepLink;
}
</script>
