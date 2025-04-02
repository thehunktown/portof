import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# Page configuration
st.set_page_config(
    page_title="Ashutosh Mishra | AI Developer Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Lottie animation
@st.cache_data
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        st.warning(f"Error loading animation: {e}")
        return None

# Use a different, working Lottie animation
lottie_dev = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_tljjah3u.json")

# Custom dark theme styling
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .block-container {
            padding: 2rem;
        }
        .stButton>button {
            background-color: #007BFF;
            color: white;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Top-level horizontal navigation
st.markdown("""
    <style>
        .horizontal-nav {
            display: flex;
            gap: 2rem;
            padding-bottom: 1rem;
        }
        .horizontal-nav a {
            text-decoration: none;
            font-weight: bold;
            color: #1f77b4;
        }
    </style>
    <div class="horizontal-nav">
        <a href="#experience">Experience</a>
        <a href="#contact">Contact Us</a>
    </div>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Code - Navigation")
main_nav = st.sidebar.radio("Main Section", ["About", "Skills", "Data Handling", "Ai Code Crafting", "Profession Projects", "Weekend Projects", "DS Algo Craft", "AI"])

# Nested navigation if "AI" is selected
sub_nav = None
if main_nav == "AI":
    sub_nav = st.sidebar.radio("AI Topics", ["LLM Projects", "AI Agents", "Prompt Engineering"])

# Header with image and     
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://media.licdn.com/dms/image/v2/D4D03AQHn7p945b8qEQ/profile-displayphoto-shrink_400_400/B4DZQ5ioM2GgAg-/0/1736132167062?e=1749081600&v=beta&t=j3wbfn7WdVkLGZjHOVQ0P0yCMAnTT-fK9ga84xqLRDc", width=100)
with col2:
    st.markdown("""
    # Ashutosh Mishra
    ### AI & Backend Engineer
    """)

# About Me Section
if lottie_dev:
    st_lottie(lottie_dev, height=300)
else:
    st.info("Smart solutions come from smarter questions.")

st.markdown("""
## About Me
I'm an AI and backend developer with experience in building scalable systems using Python, Node.js, Django, NestJS, and more. I specialize in AI-driven applications, cloud solutions, and backend systems for automation and intelligence.

🔗 [Portfolio](https://devbyashu.com) | 📫 [Email](mailto:devbyashutosh@gmail.com) | 🔗 [LinkedIn](https://linkedin.com/in/devbyashu) | 🧑‍💻 [GitHub](https://github.com/thehunktown)
""")

# Main Navigation Content
if main_nav == "About":
    st.markdown("""
    ## Welcome to my portfolio! Please use the side navigation to explore.
    """)

elif main_nav == "Skills":
    st.markdown("""
    ## Skills
    - **Languages**: Python, JavaScript, TypeScript, Bash, SQL
    - **Frameworks**: Django, FastAPI, NestJS, Node.js, React
    - **AI & ML**: LLMs, LangChain, TensorFlow, scikit-learn, Milvus
    - **Databases**: PostgreSQL, MySQL, Redis, Neo4j
    - **Tools**: Docker, RabbitMQ, Celery, Git, MLFlow
    """)

elif main_nav == "Profession Projects":
    st.markdown("""
    ## Professional Projects

    ### 🏭 AI-Driven Manufacturing Workflow Automation
    Automated inventory and workflow using LangChain, NestJS, and LangGraph.

    ### 🏢 Customer On-boarding and Billing Portal
    Built a SaaS platform for user billing, vendor registration, and product recommendation.

    ### 💰 SIP/STP Automation System
    Real-time high-frequency mutual fund investment system with SEBI-compliant checks.

    ### 📐 AI-Powered Floor Plan Extractor
    Used TrOCR to extract structured JSON from PDFs, images, and canvas floor plans.

    ### 🛒 FimoDuck
    Multi-vendor e-commerce app with vendor KYC, payment system, and real-time dashboard.
    """)

elif main_nav == "Contact":
    st.markdown("""
    ## Contact Me
    Feel free to reach out for collaboration or opportunities!

    - 📧 Email: devbyashutosh@gmail.com
    - 🔗 LinkedIn: [linkedin.com/in/devbyashu](https://linkedin.com/in/devbyashu)
    - 🌐 Portfolio: [devbyashu.com](https://devbyashu.com)
    """)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Your Message")
    st.button("Send Message")

# AI Sub Navigation Content
elif main_nav == "AI" and sub_nav:
    st.markdown(f"## {sub_nav}")
    if sub_nav == "LLM Projects":
        st.write("Projects and experiments built using Large Language Models.")
    elif sub_nav == "AI Agents":
        st.write("Modular agents, LangGraph systems, and real-time orchestration tools.")
    elif sub_nav == "Prompt Engineering":
        st.write("Smart prompt strategies and prompt evaluation systems.")