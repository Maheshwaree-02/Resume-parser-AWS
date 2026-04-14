import streamlit as st
import boto3
import time

# AWS Config
REGION = "eu-north-1"
BUCKET_NAME = "resume-parser-bucket-xyz"
TABLE_NAME = "ResumeParsedData"

# Initialize clients
s3 = boto3.client('s3', region_name=REGION)
dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table(TABLE_NAME)

# Page config
st.set_page_config(page_title="Resume Parser", layout="wide")

# ----------- CUSTOM CSS (PRO UI) -----------
st.markdown("""
<style>
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}
.title {
    font-size: 28px;
    font-weight: bold;
    color: #4CAF50;
}
.sub {
    font-size: 16px;
    color: #ccc;
}
</style>
""", unsafe_allow_html=True)

# ----------- HEADER -----------
st.markdown('<div class="title">📄 AI Resume Parser Dashboard</div>', unsafe_allow_html=True)
st.write("Upload resumes and view structured candidate data")

st.divider()

# ----------- UPLOAD SECTION -----------
st.subheader("📤 Upload Resume")

uploaded_file = st.file_uploader("Upload a .txt resume", type=["txt"])

if uploaded_file:
    file_name = uploaded_file.name
    s3.upload_fileobj(uploaded_file, BUCKET_NAME, f"resumes/{file_name}")
    st.success("✅ Uploaded successfully! Processing...")
    time.sleep(3)

st.divider()

# ----------- SEARCH BAR -----------
search = st.text_input("🔍 Search by skill (e.g. Python, AWS)")

# ----------- FETCH DATA -----------
response = table.scan()
items = response.get('Items', [])

# Sort latest first
items = sorted(items, key=lambda x: x.get('uploaded_at', ''), reverse=True)

# Filter search
if search:
    items = [i for i in items if search.lower() in " ".join(i.get('skills', [])).lower()]

# ----------- DISPLAY CARDS -----------
st.subheader("📊 Parsed Resumes")

if not items:
    st.warning("No resumes found")
else:
    for item in items:
        skills = item.get('skills', [])
        
        st.markdown(f"""
        <div class="card">
            <h3>👤 {item.get('name', 'Unknown')}</h3>
            <p class="sub">📧 {item.get('email', 'N/A')}</p>
            <p><b>🛠 Skills:</b> {", ".join(skills)}</p>
            <p class="sub">📁 {item.get('file_name')}</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("🔍 View Key Phrases"):
            st.write(item.get('key_phrases', []))