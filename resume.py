import streamlit as st
from PIL import Image
from pathlib import Path

#get the current directory path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#print(current_dir)
css_file = current_dir/"style.css"
#print(css_file)
profile_photo = current_dir/"assets"/"profile-pic.png"
resume = current_dir/"assets"/"Manan Shah Resume.pdf"
word_resume = current_dir/"assets"/"Manan Resume.docx"

#General Information
page_title = "Digital CV | Manan Shah"
page_icon = ":wave:"
name = "Manan Shah"
description = """
Senior Consultant specializing in leading cross-functional teams across FMCG, Supply Chain and Financial Services domain
to help clients implement data-driven analytical solutions.
"""
email = "shah.a.manan@gmail.com"
phone = 'Contact : +91-9699288283'
social_media = {
    'Linkedin':'https://www.linkedin.com/in/mananshah096/',
    'Github':'https://github.com/mananashah007'
}
st.set_page_config(page_title=page_title, page_icon=page_icon)

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}<style>",unsafe_allow_html=True)
with open(resume,'rb') as f:
    pdf = f.read()
profile_pic = Image.open(profile_photo)

## --- MAIN SECTION ---
col1, col2 = st.columns(2,gap='small')
with col1:
    st.image(profile_pic, width=300)
    st.subheader('Education')
    st.write('Bachelor of Engineering in Electronics and Telecommunications')
    st.write('University of Mumbai')
    st.write('08/2014 - 06/2018')
    st.write('GPA : 8.52/10')
with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label=" 📄 Download Resume",
        data = pdf,
        file_name='manan_shah.pdf',
        mime='application/octet-stream')
    st.write(email)
    for key in social_media.keys():
        st.write(f'[{key}]({social_media[key]})')
    st.write(phone)

## --- SKILLS ---
st.write('\n')
st.subheader('Skills')
st.write("""
- 👩‍💻 Programming: Python, SQL, Pyspark, Streamlit
- 📊 Data Visulization: MS Excel, PowerBi
- 📚 Modeling & AI: Statistical modeling, Predictive modeling, Generative AI
- 🗄️ Databases: Postgres, MySQL, Microsoft Server
""")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write( "**Senior Consultant | Ernst & Young**")
st.write("08/2023 - Present")
st.write(
    """
- ► Conducted in-depth consultations and meetings with clients to gain a comprehensive understanding of their specific business challenges and objectives.
- ► Leveraged advanced AI tools and frameworks, including Langchain, OpenAI, and Streamlit, to develop a suite of bespoke applications.
- ► Designed and built customer servicing automation applications, streamlining client interactions, and enhancing overall customer experience.
- ► Developed AI-powered solutions for Management Information System (MIS) reporting automation, significantly reducing manual effort and errors in reporting processes.
"""
)

# --- JOB 2
st.write('\n')
st.write( "**Consultant 2 | Fractal Analytics**")
st.write("04/2019 - 08/2023")
st.write(
    """
- ► Deciphered the search algorithm of online retailers for a Consumer-Packaged Goods client, identifying key search rank drivers to optimize digital advertisement spends, improve organic search rank, increase conversion rate of the products.  
- ► Led cross-functional teams in the development and execution of revenue management initiatives, ensuring alignment with the business objective
- ► Developed a media attribution model using Python and Pyspark to calculate the return on investment of digital campaigns, optimize the cost-per-click spends for keywords and products to help clients' digital commerce team enhance their digital marketing strategy.
- ► Managed a team of 3 members to develop pricing and promotion strategies in the space of Strategic Revenue Management utilizing regression analysis, calculating pricing and promotion elasticities, ROI on promotions, competition brand impact, and sales drivers, resulting in an incremental profit of over $4 million.
"""
)

# --- JOB 3
st.write('\n')
st.write( "**Associate Procurement Analyst | Zycus Infotech**")
st.write("08/2018 - 04/2019")
st.write(
    """
- ► Gathered and translated client business requirements into a data enrichment project focused on spend analysis to enable better sourcing and supplier decisions.
- ► Collaborated closely with internal technical teams to perform User Acceptance Testing (UAT) on an internal tool, ensuring that the tool met client expectations and was ready for implementation.
- ► Partnered with cross-functional teams to align business objectives, ensure timely delivery, and drive successful project outcomes.
"""
)

# -- ACADEMIC PROJECTS
st.write('\n')
st.subheader('Academic Projects')
st.write('- **Ecommerce Website Analysis**')
st.write(
    """
- • Analyzed product sales, refunds, and e-commerce website traffic using SQL queries to identify business opportunities and quantify company growth. 
- • Conducted funnel analysis to identify areas for website improvement based on click-through and bounce rates. 
- • Performed A/B testing on landing pages and analyzed results to optimize website performance. 
- • Analyzed user journeys on the website to understand user behavior and improve website usability.
""")
st.write("Link to project : https://github.com/mananashah007/Ecommerce-Perfomance-Analysis")
st.write('\n')
st.write('- **Case study on a telecommuication company with Declining profits**')
st.write(
    """
- • Conducted market research and root cause analysis to address declining profits for the client.
- • Analyzed historical data to understand consumer behavior and changes in market demand, presenting actionable insights to stakeholders.
- • Developed a proposal based on data-driven insights and presented it to stakeholders to address declining profits.
""")
st.write('\n')
st.write('**Fake and Real Disaster tweets classification**')
st.write(
    """
- • Extracted, cleaned and stored fake and real disaster tweets scrapped from twitter users.
- • Using XGBoost model, created a classification model to identify real and fake tweets from this data.
""")
st.write('Link to project : https://github.com/mananashah007/Fake-Real-Disaster-Tweets')


# -- AWARDS & HONORS
st.write('\n')
st.subheader('Awards and Recognition')
st.write('- **BEST UPCOMING CONSULTANT** - For exceptional team leadership skills')
st.write('- **GOOD SAMARITAN** - For assisting multiple clients & teams')
st.write('- **KAIZEN** - For showing continuous efficiency and successful delivery of project')
st.write('- **SPOT** - For going above and beyond in project delivery and execution')









