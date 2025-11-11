import streamlit as st
import random

# -----------------------------
# 샘플 사기꾼 데이터 (나중에 CSV로 교체 가능)
# -----------------------------
scammer_data = [
    {"name": "김사기", "phone": "010-1111-2222", "account": "국민 123456-12-123456"},
    {"name": "이사기", "phone": "010-3333-4444", "account": "신한 111-222-333333"},
    {"name": "박사기", "phone": "010-5555-6666", "account": "농협 999-8888-777777"},
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="중고거래 사기방지 앱", page_icon="🕵️‍♀️", layout="centered")

st.title("🕵️‍♀️ 중고거래 사기피해 방지 앱")
st.caption("더치트 + AI 대화 분석 기능 (프로토타입)")

menu = st.sidebar.selectbox("메뉴 선택", ["사기꾼 조회", "대화 분석"])

# -----------------------------
# 1️⃣ 사기꾼 정보 조회
# -----------------------------
if menu == "사기꾼 조회":
    st.header("🔍 사기꾼 정보 조회")

    name = st.text_input("이름")
    phone = st.text_input("전화번호")
    account = st.text_input("계좌번호")

    if st.button("조회하기"):
        results = []
        for scammer in scammer_data:
            if (name and name in scammer["name"]) or \
               (phone and phone in scammer["phone"]) or \
               (account and account in scammer["account"]):
                results.append(scammer)

        if results:
            st.error("⚠️ 사기 의심 인물 발견!")
            for scammer in results:
                st.write(f"- 이름: {scammer['name']}")
                st.write(f"- 전화번호: {scammer['phone']}")
                st.write(f"- 계좌번호: {scammer['account']}")
                st.write("---")
        else:
            st.success("✅ 등록된 사기꾼 정보가 없습니다.")

# -----------------------------
# 2️⃣ 대화 분석 (AI 흉내)
# -----------------------------
elif menu == "대화 분석":
    st.header("🤖 AI 대화 분석기")
    chat_text = st.text_area("사기 의심 거래자와의 대화 내용을 붙여넣으세요", height=200)

    if st.button("AI로 분석하기"):
        if not chat_text.strip():
            st.warning("대화 내용을 입력해주세요!")
        else:
            # 여기서 나중에 실제 OpenAI API 연결 가능
            fake_score = random.randint(0, 100)
            if fake_score > 70:
                st.error(f"⚠️ 사기 위험도 {fake_score}% — 매우 위험한 패턴이 감지되었습니다.")
            elif fake_score > 40:
                st.warning(f"⚠️ 사기 위험도 {fake_score}% — 주의가 필요합니다.")
            else:
                st.success(f"✅ 사기 위험도 {fake_score}% — 비교적 안전한 거래로 보입니다.")
