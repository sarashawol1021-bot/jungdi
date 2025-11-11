import streamlit as st
import pandas as pd
import os
import random

DATA_FILE = "scammers.csv"

# -----------------------------
# 데이터 파일 로드/저장 유틸
# -----------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
    else:
        df = pd.DataFrame(columns=["이름", "전화번호", "계좌번호"])
        df.to_csv(DATA_FILE, index=False)
    # 문자열로 변환 (NaN → 빈 문자열)
    for col in ["이름", "전화번호", "계좌번호"]:
        df[col] = df[col].astype(str).fillna("")
    return df

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="중고거래 사기방지 앱", page_icon="🕵️‍♀️", layout="centered")

st.title("🕵️‍♀️ 중고거래 사기피해 방지 앱")
st.caption("더치트 + AI 대화 분석 + 사용자 제보 기능 (프로토타입)")

menu = st.sidebar.selectbox("메뉴 선택", ["사기꾼 조회", "대화 분석", "사기꾼 등록"])

data = load_data()

# -----------------------------
# 1️⃣ 사기꾼 정보 조회
# -----------------------------
if menu == "사기꾼 조회":
    st.header("🔍 사기꾼 정보 조회")

    name = st.text_input("이름")
    phone = st.text_input("전화번호")
    account = st.text_input("계좌번호")

    if st.button("조회하기"):
        filtered = data[
            (data["이름"].str.contains(name, na=False)) |
            (data["전화번호"].str.contains(phone, na=False)) |
            (data["계좌번호"].str.contains(account, na=False))
        ]

        if not filtered.empty:
            st.error("⚠️ 등록된 사기 의심 인물이 있습니다!")
            st.dataframe(filtered)
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
            fake_score = random.randint(0, 100)
            if fake_score > 70:
                st.error(f"⚠️ 사기 위험도 {fake_score}% — 매우 위험한 패턴이 감지되었습니다.")
            elif fake_score > 40:
                st.warning(f"⚠️ 사기 위험도 {fake_score}% — 주의가 필요합니다.")
            else:
                st.success(f"✅ 사기 위험도 {fake_score}% — 비교적 안전한 거래로 보입니다.")

# -----------------------------
# 3️⃣ 사기꾼 등록
# -----------------------------
elif menu == "사기꾼 등록":
    st.header("📝 사기꾼 정보 제보하기")

    name = st.text_input("사기꾼 이름")
    phone = st.text_input("전화번호")
    account = st.text_input("계좌번호")

    if st.button("등록하기"):
        if not (name or phone or account):
            st.warning("최소한 하나의 정보를 입력해야 합니다.")
        else:
            new_data = pd.DataFrame([[name, phone, account]], columns=["이름", "전화번호", "계좌번호"])
            updated = pd.concat([data, new_data], ignore_index=True)
            save_data(updated)
            st.success("✅ 제보가 등록되었습니다! (감사합니다 🙏)")

