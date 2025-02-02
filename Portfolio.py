import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Yedu Krishnan - Portfolio", page_icon="🎯", layout="wide")

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home",  
    "💼 Work Experience",  
    "📂 Projects",  
    "🎓 Education",  
    "🏆 Certifications & Achievements"
])

# Home Page
if page == "🏠 Home":
    st.title("👋 Yedu Krishnan")
    st.markdown("### 📊 Data Scientist | 📈 Analyst | 💻 Developer")
    st.write("""
    Master’s graduate in Data Science with expertise in Python, SQL, Power BI, and data analysis. 
    Experienced in ETL pipelines, visualization, machine learning, and cloud computing.
    """)
    
    st.markdown("---")
    st.subheader("🛠️ Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**💻 Programming Languages:** Python, R, SQL, Java, C++, Bash")
        st.markdown("**📊 Data Analytics & Visualization:** Power BI, Tableau, Databricks, Dashboards")
        st.markdown("**🤖 Machine Learning:** Regression, Random Forest, SVM, KNN, Prophet, Forecasting")

    with col2:
        st.markdown("**☁️ Cloud & DevOps:** AWS Lambda, Azure, Docker, CI/CD Pipelines")
        st.markdown("**🗄️ Databases:** SQL Server, MySQL, PostgreSQL, AWS S3, DynamoDB")
        st.markdown("**🗣️ Soft Skills:** Problem-solving, Data Storytelling, Communication, Team Collaboration")

    
    st.markdown("---")
    st.subheader("📞 Contact")

    st.write("📍 **Location:** Calgary, AB")  
    st.write("📧 **Email:** edchris215@gmail.com")  

    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/yedu-krishnan215/) "
        "[![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github)](https://github.com/Ed-Chris)"
    )


# Work Experience Page
elif page == "💼 Work Experience":
    st.title("💼 Work Experience")

    # Links
    col1, col2 = st.columns(2)
    with col1:
        st.page_link("https://labour-market-and-wage-data-visualizations-gbkzvysesfg86lm3xkw.streamlit.app/", label="🌐 Live Application", icon="🌍")
    with col2:
        st.page_link("https://github.com/Ed-Chris/Labour-Market-and-Wage-Data-Visualizations", label="📂 GitHub Repository", icon="💻")

    # Job 1
    st.subheader("🧑‍💻 **Data Scientist Intern** - TOSSA Sustainability Services Inc.")
    st.write("📅 **May 2024 – Aug 2024**")
    with st.expander("View Details"):
        st.write("""
        - ⚡ **Engineered** an ETL pipeline that automated **daily retrieval and cleaning** of 100k+ rows of data from Stats Canada, integrating **GitHub Actions** for CI/CD.
        - 📊 **Developed and implemented** 11 **Power BI visualizations**, uncovering male and female participation rates across industries and identifying wage disparities.
        - 🌍 **Created and deployed** a **Streamlit website** replicating Power BI’s functionality for interactive data visualization.
        - 🔍 **Built a machine learning model** using Prophet to forecast **gender participation rates and pay gaps**, predicting a **32.6% reduction by 2033**.
        """)

    # Job 2
    st.subheader("📊 **Data Analyst** - Tata Consultancy Services")
    st.write("📅 **Sep 2021 – Aug 2023**")
    with st.expander("View Details"):
        st.write("""  
        - 🛠 **Utilized** MS SQL Server for **sales data analysis**, cleaned and analyzed data in **Excel**, and presented insights via **Power BI**.
        - 🔍 **Identified and rectified** four major data issues, uncovering insights about products and warranty sales.
        - 📈 **Rectified 90%** of one year’s data within four months using **advanced SQL**, demonstrating strong analytical and problem-solving skills.
        - 🗂 **Leveraged Excel functions** like **VLOOKUP** and SQL for **data validation**, resolving duplicates and inaccuracies, ensuring data integrity.
        - ☁ **Gained expertise** in **Azure DevOps and Kubernetes**, improving **Agile software development** and project delivery timelines.
        """)

    # Job 3
    st.subheader("🖥️ **Developer & Support Engineer** - Tata Consultancy Services")
    st.write("📅 **Feb 2021 – Aug 2021**")
    with st.expander("View Details"):
        st.write("""  
        - 🏗 **Developed microservices** in **Java** to **automate daily data processing** for 250 customers, reducing execution time from hours to minutes.
        - 🛠 **Managed and resolved** 10+ daily incident tickets using **ServiceNow, AppDynamics, Grafana, and Azure**, reducing website downtime.
        - 📢 **Led customer migration** to new tiers and programs, improving system reliability and customer satisfaction.
        - ⚙ **Enhanced API and microservice efficiency** using **MS Azure Insights & Blob Storage**, providing **L2 support** in an **Agile Scrum** environment.
        """)


# Projects Page
elif page == "📂 Projects":
    st.header("📂 Projects")
    st.subheader("Daily Stock Price Prediction with Databricks")
    st.write("Jan 2025 – Present")
    st.write("""
    - **Automated** a predictive pipeline in **Databricks** to forecast next-day closing prices for **AAPL** and **NVDA** using **LSTM models**.
    - Integrated **yFinance API** for real-time stock data ingestion and **Spark** for large-scale data handling.
    - Designed **interactive dashboards** with **Plotly** to visualize predictions vs. actual stock prices.
    - Implementing **Databricks Jobs** for seamless end-to-end automation of data ingestion, model execution, and database updates.
    """)

    st.subheader("Stock Price Predictor using LSTM hosted on AWS")
    st.markdown("[🌐 Visit the application](https://stockpredictor-wbptabbzh6qfrmr2no8js4.streamlit.app/)", unsafe_allow_html=True)
    st.write("Feb 2024 – Mar 2024")
    st.write("""
    - Developed a **Deep Learning-based** stock price prediction model using **LSTM**.
    - Integrated **Streamlit, Docker, and AWS** for a dynamic frontend and ML-driven backend.
    - Optimized the model, reducing computational time from **3 minutes to 15 seconds** (**92% efficiency increase**).
    """)
    st.markdown("[📂 GitHub Repository](https://github.com/Ed-Chris/Stock_Predictor)", unsafe_allow_html=True)

    st.subheader("Decoding Dermatology Diseases with Machine Learning")
    st.write("Feb 2024 – Mar 2024")
    st.write("""
    - Built ML models for **six erythemato-squamous diseases** using a dataset of **366 instances and 34 features**.
    - Achieved highest accuracy with **Random Forest and SVC** after feature selection and tuning.
    """)
    st.markdown("[📂 GitHub Repository](https://github.com/Ed-Chris/Decoding-Dermatology-diseases-through-Machine-Learning)", unsafe_allow_html=True)

    st.subheader("Exploratory Data Analysis on Rock Music")
    st.markdown("[📖 Notion](https://defiant-sunday-6a0.notion.site/Musicality-Popularity-of-Rock-songs-from-1950-to-2020-fb66240e6c174b5b890420b5dc0ce488?pvs=4) | [▶️ YouTube](https://www.youtube.com/watch?v=j3PU_fxkwss)", unsafe_allow_html=True)
    st.write("Jan 2023 – Feb 2024")
    st.write("""
    - Analyzed a **5400-record** rock music dataset, revealing **key correlations between loudness, energy, and musical key**.
    - Used **K-means clustering** to uncover hidden patterns in musical attributes.
    """)
    st.markdown("[📂 GitHub Repository](https://github.com/Ed-Chris/Musicality-and-Popularity-of-Rock-songs)", unsafe_allow_html=True)

    st.subheader("Energy Nexus: Energy Production, Consumption, and Temperature Change")
    st.write("Jan 2024 – Present")
    st.write("""
    - Explored **global energy trends** and their impact on **CO₂ emissions** using statistical analysis.
    - Developed **interactive visualizations** with **Seaborn, Pandas, and Plotly**.
    """)
    st.markdown("[📂 GitHub Repository](https://github.com/Ed-Chris/Temperature-Gas-Emissions-Analysis-with-Energy-variables-using-SQL)", unsafe_allow_html=True)

    st.subheader("Fuel Efficiency Regression Model")
    st.write("Jan 2024 – Present")
    st.write("""
    - Built a **multiple linear regression model** to analyze key factors affecting **vehicle fuel efficiency**.
    - Applied **Box-Cox transformation** and interaction models for improved accuracy.
    """)
    st.markdown("[📂 GitHub Repository](https://github.com/Ed-Chris/Fuel-Efficiency-Regression-Model)", unsafe_allow_html=True)

    st.subheader("Statistical Analysis of CPI and Income")
    st.write("Jan 2024 – Present")
    st.write("""
    - Investigated **Consumer Price Index (CPI)** trends and their impact on **income disparities**.
    - Applied **linear regression and bootstrap methods** to predict future income levels.
    """)
    st.markdown("[📂 GitHub Repository](https://github.com/Ed-Chris/Statistical-Analysis-of-CPI-and-Income)", unsafe_allow_html=True)

    st.subheader("Have Canadian Earnings Kept Pace with the Cost of Living?")
    st.write("1981 – 2021")
    st.write("""
    - Analyzed **inflation vs. income trends** in Canada using **22 datasets**.
    - Developed interactive charts with **Matplotlib, Seaborn, and Plotly**.
    """)
    st.markdown("[📂 GitHub Repository](https://github.com/Ed-Chris/Income-Vs-CPI-Data-Visualization)", unsafe_allow_html=True)

# Education Page
elif page == "🎓 Education":
    st.title("Education 🎓")

    st.write("## Master's in Data Science")
    st.write("📍 University of Calgary |  Sep 2023 - Sep 2024")
    st.write("Focus Areas: Machine Learning, Data Visualization, Big Data Analytics")

    st.write("---")

    st.write("## Bachelor's in  Electrical and Electronics Engineering")
    st.write("📍 APJ Abdul Kalam Technological University |  Aug 2016 - Aug 2020")
    st.write("Relevant Courses: Statistics, Programming, Database Systems")

# Certifications & Achievements Page
elif page == "🏆 Certifications & Achievements":
    st.title("🏆 Certifications & Achievements")

    # Certifications Section
    st.markdown("## 📜 Certifications")
    st.markdown("""
    - **Certification in Applied Optimization for Wireless, Machine Learning, and Big Data** (NPTEL)
    """)

    # Achievements Section
    st.markdown("## 🌟 Achievements")
    st.markdown("""
    - **Talent Development-Elevate Wings Award** – Tata Consultancy Services  
    - **On The Spot Award** for critical contributions – Tata Consultancy Services  
    - **Co-Founder** of College Music Band (RITM)  
    - **Scholarship** for Top 3 admissions at APJ Abdul Kalam Technological University  
    """)

