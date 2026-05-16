---
layout: page
title: 타로 상담 예약
permalink: /reserve/
---

카카오톡의 챗봇을 통해서 언제든지 상담 예약을 남길 수 있습니다. <br/>
상담시간과 종류를 선택하고, 내담자와 상담 가능한 시간이 매치되는 경우 예약시간이 확정됩니다. <br/>
챗봇은 다음과 같은 상담 상품을 제공하고 있습니다. <br/>

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

<div id="reserve" class="tarot-reserve">
  <h2>율하타로 예약방식</h2>
  <ul>                                     
    <li><strong>전화예약</strong>: <a href="tel:01064973389" class="call-btn">클릭시 전화연결</a></li>  
    <li><strong>카톡상담</strong>: 카톡ID: <a href="#" onclick="openKakaoTalk(); return false;">yulhatarot </a></li>
    <li><strong>카카오 오픈채팅 예약</strong>: <a href="https://open.kakao.com/o/s6oJCqYh" class="kakao-btn">오픈채팅 입장</a> </li>
  </ul>

  <p style="opacity:.85; margin-top: 8px;">
    원하시면 <strong>질문 다듬기</strong>도 함께 도와드려요. “무엇을 물어야 할지”부터가 상담의 시작이니까요.
  </p>
</div>
> **✅ Admin (관리자용)**
> 
> "예약하기" 

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