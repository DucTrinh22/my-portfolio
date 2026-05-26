import streamlit as st
import base64
import os

# --- 1. CẤU HÌNH & TIỆN ÍCH ---
st.set_page_config(page_title="Hồ sơ Kỹ thuật | Trịnh Văn Đức", page_icon="🏗️", layout="wide")

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

def display_pdf(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf" style="border:none; border-radius:10px;"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.warning(f"Không tìm thấy file: {file_path}")

# --- 2. CSS CUSTOM (KẾT HỢP MARKDOWN STYLING) ---
st.markdown("""
<style>
    /* Google Font */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@300;400;700;900&display=swap');
    
    .stApp { background-color: #ffffff; }
    
    /* Cấu trúc Header */
    .header-box {
        background: #1a1a1a;
        color: white;
        padding: 50px;
        border-radius: 0 0 50px 50px;
        margin-bottom: 50px;
    }
    
    /* Làm nổi bật Markdown Container */
    .md-container {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid #1a1a1a;
        margin-bottom: 25px;
        font-family: 'Inter', sans-serif;
    }
    
    /* Style cho các Header của Markdown */
    .md-container h1, .md-container h2 { color: #1a1a1a; font-weight: 800; }
    .md-container code { background: #e9ecef; color: #d63384; padding: 2px 6px; border-radius: 4px; }
    
    /* Badge phong cách GitHub */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 5px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: bold;
        margin-right: 10px;
        background: #eee;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. PHẦN HEADER (HTML) ---
avatar_b64 = get_base64_image("images/avatar.png")
st.markdown(f"""
<div class="header-box">
    <table style="width:100%; border:none;">
        <tr>
            <td style="width:70%; border:none;">
                <h1 style="font-size: 50px; margin:0;">TRỊNH VĂN ĐỨC</h1>
                <p style="font-size: 20px; opacity:0.8;">Technical Specialist | BIM Expert | AI Researcher</p>
                <div style="margin-top:20px;">
                    <span class="badge" style="background:#0078d4; color:white;">#RevitBIM</span>
                    <span class="badge" style="background:#28a745; color:white;">#Python_AI</span>
                    <span class="badge" style="background:#ffc107; color:black;">#MEP_Design</span>
                </div>
            </td>
            <td style="width:30%; text-align:right; border:none;">
                <img src="data:image/png;base64,{avatar_b64}" style="width:180px; border-radius:20px; border:4px solid #333;">
            </td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# --- 4. NỘI DUNG CHÍNH (KẾT HỢP MARKDOWN) ---

col_main, col_side = st.columns([2, 1], gap="large")

with col_main:
    # Sử dụng Markdown bên trong các div HTML để tạo hiệu ứng "bọc" nội dung
    st.markdown('<div class="md-container">', unsafe_allow_html=True)
    st.markdown("""
    ## 🚀 Giới thiệu bản thân
    Nhân viên Kỹ thuật với nhiều năm kinh nghiệm chuyên sâu trong triển khai **bản vẽ kiến trúc** và **quản lý MEP**. 
    Thành thạo hệ sinh thái `BIM (Revit)`, `AutoCAD` và đang nghiên cứu ứng dụng `AI` trong kỹ thuật để tối ưu hóa 30% quy trình làm việc.
    
    - **Thế mạnh:** Sự tỉ mỉ, tư duy kỹ thuật chính xác, thích nghi nhanh với công nghệ mới.
    - **Mục tiêu:** Trở thành chuyên gia BIM hàng đầu, tích hợp trí tuệ nhân tạo vào thiết kế xây dựng.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="md-container">', unsafe_allow_html=True)
    st.markdown("""
    ## 💼 Kinh nghiệm chiến thực
    
    ### 🏗️ EnTech Co. | 2024 - 2025
    **Technical Management**
    - Quản lý thiết bị bếp công nghiệp & hệ thống MEP cho **Sân bay Long Thành**.
    - Phối hợp triển khai dự án khách sạn 5 sao: `New World`, `JW Marriott`.
    
    ### 🇦🇺 Mitek Co. | 2020 - 2023
    **Team Leader (Australia Project)**
    - Lãnh đạo nhóm 5 người triển khai hồ sơ kiến trúc nhà ở tại Úc.
    - Đảm bảo 100% bản vẽ tuân thủ nghiêm ngặt tiêu chuẩn xây dựng quốc tế.
    
    ### 🇯🇵 SolidLine Co. | 2016 - 2020
    **Japanese Technical Specialist**
    - Làm việc trực tiếp với khách hàng Nhật Bản qua `Skype`.
    - Hoàn thành chi tiết cấu tạo thép và kết cấu bao che phức tạp.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col_side:
    st.markdown('<div class="md-container" style="border-left: 8px solid #0078d4;">', unsafe_allow_html=True)
    st.markdown("""
    ## 🛠️ Kỹ năng
    - **BIM/CAD:** `Revit (Master)`, `AutoCAD`, `Navisworks`
    - **Programming:** `Python`, `C++`, `Dynamo`
    - **Language:** English (Tech), Japanese
    - **Soft Skills:** Quản lý nhóm, Giải quyết vấn đề
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="md-container" style="border-left: 8px solid #ffc107;">', unsafe_allow_html=True)
    st.markdown("""
    ## 📞 Liên hệ
    - **Phone:** 0337 842 819
    - **Email:** tvduc71374@gmail.com
    - **Địa chỉ:** Q. Tân Phú, TP. HCM
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PHẦN PDF (DỰ ÁN & PORTFOLIO) ---
st.markdown('<h2 style="text-align:center; margin-top:50px;">📂 HỒ SƠ NĂNG LỰC TRỰC TUYẾN</h2>', unsafe_allow_html=True)

tab_cv, tab_port = st.tabs(["📄 CHI TIẾT CV (PDF)", "📐 PORTFOLIO BẢN VẼ"])

with tab_cv:
    display_pdf("CV_TrinhVanDuc.pdf")

with tab_port:
    display_pdf("Portfolio_Architect.pdf")

# --- FOOTER ---
st.markdown("""
<div style="text-align:center; padding:50px; color:#888;">
    Built with ❤️ using Python, Streamlit & Markdown | 2025
</div>
""", unsafe_allow_html=True)