# Selma's Autobiography & Portfolio Streamlit App
import streamlit as st
import pandas as pd
import time
from PIL import Image

st.set_page_config(page_title="Selma's Portfolio", page_icon="🌟", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Portfolio", "Skills", "Contact", "Gallery"])

st.sidebar.image("gallery/pfp.jpg", width=200)
st.sidebar.markdown("**Selma JE.**\n3rd Year College IT Student | Ametuer Programmer")
st.sidebar.markdown("---")

if page == "About Me":
	st.title("👩‍💻 Selma's Autobiography")
	st.write("""
	Hi! I'm Selma, a passionate 3rd Year College IT student with a love for data, technology, and creative problem-solving.\n
	**Education:**
	- Bachelor of Science in Information Technology
	- 3rd Year, College
    
	**Hobbies:**
	- Fighting and Single-player Games
	- Reading and Collecting Books
	- Art and Music Appreciation
	""")
	st.success("Always learning, always growing!")
	st.progress(65)
	st.balloons()

elif page == "Portfolio":
	st.title("📁 Portfolio")
	st.write("Here are some of my favorite projects:")
	col1, col2 = st.columns(2)
	with col1:
		st.subheader("CourseCompanion")
		st.markdown("[View on GitHub](https://github.com/SecongKoylaaa/CSIT327-G6-Group12-CourseCompanion/tree/Selma)")
		st.write("A web app for students to organize courses, track deadlines, and access learning resources. Built with Django and React.")
	with col2:
		st.subheader("PURR")
		st.markdown("[View on GitHub](https://github.com/kiyoder/Purr/tree/selma)")
		st.write("A platform connecting pet adopters and shelters. Features pet profiles, search, and adoption workflow. Built with Flask and React.")
	st.markdown("---")
	st.write("### Project Table")
	df = pd.DataFrame({
		'Project': ['CourseCompanion', 'PURR'],
		'Type': ['Web App', 'Web App'],
		'Year': [2025, 2024],
		'Link': [
			'https://github.com/SecongKoylaaa/CSIT327-G6-Group12-CourseCompanion/tree/Selma',
			'https://github.com/kiyoder/Purr/tree/selma',
		]
	})
	st.dataframe(df)

elif page == "Skills":
	st.title("🛠️ Skills")
	st.write("A quick overview of my technical and soft skills:")
	st.markdown("**Programming:** Python, JavaScript, HTML/CSS, SQL")
	st.markdown("**Frameworks:** Streamlit, React")
	st.markdown("**Tools:** Git, VS Code, Jupyter, Figma")
	st.markdown("**Soft Skills:** Communication, Teamwork, Problem-solving")
	st.write("---")
	st.write("#### Skill Proficiency")
	st.progress(60)
	st.slider("Python", 0, 100, 60)
	st.slider("Data Analysis", 0, 100, 50)
	st.slider("Web Development", 0, 100, 40)

elif page == "Contact":
	st.title("📬 Contact Me")
	st.write("Feel free to reach out!")
	with st.form("contact_form"):
		name = st.text_input("Your Name")
		email = st.text_input("Your Email")
		message = st.text_area("Message")
		submitted = st.form_submit_button("Send")
		if submitted:
			with st.spinner("Sending message..."):
				time.sleep(1)
			st.success(f"Thank you, {name}! I'll get back to you soon.")

elif page == "Gallery":
	st.title("🖼️ Gallery")
	st.write("A glimpse into my interests side:")
	import os
	gallery_dir = "gallery"
	gallery_files = [f for f in os.listdir(gallery_dir) if f.lower().endswith((".jpg", ".jpeg", ".png")) and f != "pfp.jpg"]
	gallery_paths = [os.path.join(gallery_dir, f) for f in gallery_files]
	from PIL import Image
	if gallery_paths:
		col1, col2 = st.columns(2)
		for idx, (img_path, caption) in enumerate(zip(gallery_paths, gallery_files)):
			img = Image.open(img_path)
			width, height = img.size
			if idx % 2 == 0:
				with col1:
					st.image(img, caption=caption)
			else:
				with col2:
					st.image(img, caption=caption)
	else:
		st.info("No gallery images found.")
	st.write("---")
	st.info("More coming soon!")
