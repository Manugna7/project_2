import streamlit as st
import pandas as pd
from datetime import date


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="KKR & KSR | Attendance Tracker",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

if "student" not in st.session_state:
    st.session_state.student = {
        "name": "",
        "roll_no": "",
        "branch": "CSE",
        "year": "1st Year",
        "section": "A"
    }

if "subjects" not in st.session_state:
    st.session_state.subjects = []

if "attendance" not in st.session_state:
    st.session_state.attendance = {}


# ============================================================
# DARK PROFESSIONAL THEME
# ============================================================

st.markdown("""
<style>

/* ============================================================
   MAIN APP
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at top right,
            #312e81 0%,
            #111827 35%,
            #020617 100%
        );

    color: #ffffff !important;
}


/* ============================================================
   MAIN CONTENT
   ============================================================ */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #020617 0%,
            #111827 55%,
            #1e1b4b 100%
        );

    border-right: 1px solid #334155;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}


/* ============================================================
   COLLEGE HEADER
   ============================================================ */

.college-name {
    background:
        linear-gradient(
            135deg,
            #312e81,
            #4f46e5,
            #7c3aed
        );

    color: #ffffff !important;

    padding: 24px 25px;

    border-radius: 20px;

    font-size: 20px;

    font-weight: 800;

    text-align: center;

    margin-bottom: 35px;

    border: 1px solid #818cf8;

    box-shadow:
        0 12px 35px rgba(79, 70, 229, 0.35);
}


/* ============================================================
   WELCOME TITLE
   ============================================================ */

.main-title {
    color: #ffffff !important;

    font-size: 40px;

    font-weight: 900;

    line-height: 1.2;

    margin-bottom: 8px;
}


/* ============================================================
   SUBTITLE
   ============================================================ */

.subtitle {
    color: #cbd5e1 !important;

    font-size: 17px;

    font-weight: 500;

    margin-bottom: 30px;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: #ffffff !important;

    font-size: 25px;

    font-weight: 800;

    margin-top: 30px;

    margin-bottom: 18px;
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

[data-testid="stMetric"] {

    background: #ffffff !important;

    border: 2px solid #6366f1 !important;

    border-radius: 18px !important;

    padding: 20px !important;

    min-height: 125px;

    box-shadow:
        0 10px 25px rgba(0, 0, 0, 0.35);
}


/* Metric label */

[data-testid="stMetricLabel"] {
    color: #334155 !important;
}

[data-testid="stMetricLabel"] p {
    color: #334155 !important;

    font-size: 15px !important;

    font-weight: 800 !important;
}


/* Metric value */

[data-testid="stMetricValue"] {
    color: #111827 !important;

    font-size: 32px !important;

    font-weight: 900 !important;
}


/* ============================================================
   NORMAL TEXT
   ============================================================ */

.stMarkdown {
    color: #ffffff !important;
}

.stMarkdown p {
    color: #e2e8f0 !important;
}


/* ============================================================
   HEADINGS
   ============================================================ */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #ffffff !important;
}


/* ============================================================
   FORMS
   ============================================================ */

[data-testid="stForm"] {

    background:
        linear-gradient(
            135deg,
            #111827,
            #172033
        );

    padding: 25px;

    border-radius: 18px;

    border: 1px solid #475569;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.30);
}


/* ============================================================
   INPUT LABELS
   ============================================================ */

.stTextInput label,
.stSelectbox label,
.stDateInput label,
.stRadio label {
    color: #ffffff !important;

    font-weight: 700 !important;
}


/* ============================================================
   TEXT INPUT
   ============================================================ */

.stTextInput input {

    background: #ffffff !important;

    color: #111827 !important;

    border: 2px solid #475569 !important;

    border-radius: 10px !important;
}

.stTextInput input:focus {

    border: 2px solid #818cf8 !important;

    box-shadow:
        0 0 12px rgba(99, 102, 241, 0.45);
}


/* ============================================================
   SELECT BOX
   ============================================================ */

div[data-baseweb="select"] > div {

    background: #ffffff !important;

    color: #111827 !important;

    border: 2px solid #475569 !important;

    border-radius: 10px !important;
}

div[data-baseweb="select"] span {
    color: #111827 !important;
}


/* ============================================================
   DATE INPUT
   ============================================================ */

[data-testid="stDateInput"] input {

    background: #ffffff !important;

    color: #111827 !important;

    border: 2px solid #475569 !important;

    border-radius: 10px !important;
}


/* ============================================================
   RADIO BUTTON
   ============================================================ */

.stRadio label {
    color: #ffffff !important;
}

.stRadio div[role="radiogroup"] {
    color: #ffffff !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        ) !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 10px !important;

    min-height: 44px;

    font-size: 15px;

    font-weight: 800;

    box-shadow:
        0 6px 18px rgba(79, 70, 229, 0.35);

    transition: 0.2s ease;
}


.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6
        ) !important;

    color: #ffffff !important;

    transform: translateY(-2px);

    box-shadow:
        0 8px 22px rgba(99, 102, 241, 0.45);
}


/* ============================================================
   DOWNLOAD BUTTON
   ============================================================ */

.stDownloadButton > button {

    background:
        linear-gradient(
            135deg,
            #059669,
            #10b981
        ) !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 10px !important;

    min-height: 44px;

    font-weight: 800;
}


/* ============================================================
   INFO / WARNING / SUCCESS BOXES
   ============================================================ */

[data-testid="stAlert"] {

    border-radius: 14px !important;

    color: #ffffff !important;
}


/* General info */

[data-testid="stAlert"][kind="info"] {

    background: #172554 !important;

    border: 1px solid #3b82f6 !important;
}


/* Success */

[data-testid="stAlert"][kind="success"] {

    background: #052e16 !important;

    border: 1px solid #22c55e !important;
}


/* Warning */

[data-testid="stAlert"][kind="warning"] {

    background: #422006 !important;

    border: 1px solid #f59e0b !important;
}


/* Error */

[data-testid="stAlert"][kind="error"] {

    background: #450a0a !important;

    border: 1px solid #ef4444 !important;
}


/* Alert text */

[data-testid="stAlert"] p {
    color: #ffffff !important;
}


/* ============================================================
   PROFILE CARD
   ============================================================ */

.info-card {

    background:
        linear-gradient(
            135deg,
            #111827,
            #1e1b4b
        );

    color: #ffffff !important;

    padding: 25px;

    border-radius: 18px;

    border: 1px solid #6366f1;

    box-shadow:
        0 10px 25px rgba(0, 0, 0, 0.30);
}


.info-card h3 {
    color: #ffffff !important;

    margin-top: 0;
}


.info-card b {
    color: #a5b4fc !important;
}


/* ============================================================
   SUBJECT CARDS
   ============================================================ */

.subject-card {

    background:
        linear-gradient(
            135deg,
            #111827,
            #1e293b
        );

    border: 1px solid #475569;

    border-radius: 15px;

    padding: 18px;

    color: #ffffff !important;

    margin-bottom: 12px;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {

    background: #ffffff !important;

    border-radius: 14px !important;

    border: 2px solid #6366f1 !important;

    overflow: hidden;
}


/* ============================================================
   CAPTION
   ============================================================ */

[data-testid="stCaptionContainer"] {
    color: #94a3b8 !important;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

hr {
    border-color: #334155 !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align: center;

    color: #94a3b8 !important;

    padding: 35px 0 10px;

    font-size: 13px;
}


/* ============================================================
   SIDEBAR RADIO
   ============================================================ */

[data-testid="stSidebar"] [role="radiogroup"] label {
    color: #ffffff !important;
}


/* ============================================================
   SIDEBAR CAPTION
   ============================================================ */

[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #cbd5e1 !important;
}


/* ============================================================
   SCROLLBAR
   ============================================================ */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #020617;
}

::-webkit-scrollbar-thumb {
    background: #4f46e5;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNCTIONS
# ============================================================

def attendance_percentage(subject):

    record = st.session_state.attendance.get(
        subject,
        {
            "conducted": 0,
            "present": 0
        }
    )

    if record["conducted"] == 0:
        return 0.0

    return (
        record["present"] /
        record["conducted"]
    ) * 100


def overall_attendance():

    total_conducted = sum(
        data["conducted"]
        for data in st.session_state.attendance.values()
    )

    total_present = sum(
        data["present"]
        for data in st.session_state.attendance.values()
    )

    if total_conducted == 0:
        return 0.0, 0, 0

    percentage = (
        total_present /
        total_conducted
    ) * 100

    return percentage, total_present, total_conducted


def attendance_status(percentage):

    if percentage >= 75:
        return "Good"

    elif percentage >= 65:
        return "Warning"

    else:
        return "Low"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎓 Attendance Tracker")

    st.caption(
        "KKR & KSR Institute of Technology and Sciences"
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Student Profile",
            "Manage Subjects",
            "Mark Attendance",
            "Attendance Report"
        ]
    )

    st.divider()

    st.markdown("### 📌 Quick Guide")

    st.write("1. Create your student profile")
    st.write("2. Add your subjects")
    st.write("3. Mark daily attendance")
    st.write("4. Check attendance percentage")
    st.write("5. Download your report")

    st.divider()

    st.caption(
        "Student Attendance Management System"
    )


# ============================================================
# COLLEGE HEADER
# ============================================================

st.markdown(
    """
    <div class="college-name">
        🎓 KKR & KSR INSTITUTE OF TECHNOLOGY AND SCIENCES
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    percentage, present, conducted = overall_attendance()

    student_name = (
        st.session_state.student["name"]
        or "Student"
    )


    # --------------------------------------------------------
    # WELCOME
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="main-title">
            Welcome, {student_name} 👋
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            Track your classes, subjects and attendance easily.
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # METRIC CARDS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "📊 Overall Attendance",
            f"{percentage:.1f}%"
        )


    with col2:

        st.metric(
            "✅ Classes Present",
            present
        )


    with col3:

        st.metric(
            "📚 Classes Conducted",
            conducted
        )


    with col4:

        st.metric(
            "📖 Total Subjects",
            len(st.session_state.subjects)
        )


    # --------------------------------------------------------
    # ATTENDANCE OVERVIEW
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📈 Attendance Overview</div>',
        unsafe_allow_html=True
    )


    if not st.session_state.subjects:

        st.info(
            "No subjects added yet. "
            "Go to 'Manage Subjects' and add your subjects."
        )

    else:

        rows = []


        for subject in st.session_state.subjects:

            record = st.session_state.attendance.get(
                subject,
                {
                    "conducted": 0,
                    "present": 0
                }
            )


            conducted_count = record["conducted"]

            present_count = record["present"]

            absent_count = (
                conducted_count -
                present_count
            )

            percentage = attendance_percentage(
                subject
            )


            rows.append(
                {
                    "Subject": subject,
                    "Present": present_count,
                    "Conducted": conducted_count,
                    "Absent": absent_count,
                    "Attendance": f"{percentage:.1f}%",
                    "Status": attendance_status(
                        percentage
                    )
                }
            )


        df = pd.DataFrame(rows)


        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


        # ----------------------------------------------------
        # CHART
        # ----------------------------------------------------

        st.markdown(
            "#### 📊 Subject-wise Attendance"
        )


        chart_data = pd.DataFrame(
            {
                "Subject": [
                    row["Subject"]
                    for row in rows
                ],

                "Attendance %": [
                    float(
                        row["Attendance"].replace(
                            "%",
                            ""
                        )
                    )

                    for row in rows
                ]
            }
        )


        chart_data = chart_data.set_index(
            "Subject"
        )


        st.bar_chart(
            chart_data
        )


# ============================================================
# STUDENT PROFILE
# ============================================================

elif page == "Student Profile":

    st.markdown(
        '<div class="section-title">👤 Student Profile</div>',
        unsafe_allow_html=True
    )


    with st.form("student_profile_form"):

        col1, col2 = st.columns(2)


        # ----------------------------------------------------
        # LEFT COLUMN
        # ----------------------------------------------------

        with col1:

            name = st.text_input(
                "Student Name",
                value=st.session_state.student["name"],
                placeholder="Enter your full name"
            )


            roll_no = st.text_input(
                "Roll Number",
                value=st.session_state.student["roll_no"],
                placeholder="Example: 24JR1A0501"
            )


            branches = [
                "CSE",
                "CSE-AIML",
                "CSE-DS",
                "ECE",
                "EEE",
                "ME",
                "CE"
            ]


            branch = st.selectbox(
                "Branch",
                branches,
                index=branches.index(
                    st.session_state.student["branch"]
                )
            )


        # ----------------------------------------------------
        # RIGHT COLUMN
        # ----------------------------------------------------

        with col2:

            years = [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year"
            ]


            year = st.selectbox(
                "Academic Year",
                years,
                index=years.index(
                    st.session_state.student["year"]
                )
            )


            sections = [
                "A",
                "B",
                "C",
                "D",
                "E"
            ]


            section = st.selectbox(
                "Section",
                sections,
                index=sections.index(
                    st.session_state.student["section"]
                )
            )


            st.date_input(
                "Profile Date",
                value=date.today(),
                disabled=True
            )


        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        submitted = st.form_submit_button(
            "💾 Save Student Profile",
            use_container_width=True
        )


        if submitted:

            if not name.strip():

                st.error(
                    "Please enter the student name."
                )

            elif not roll_no.strip():

                st.error(
                    "Please enter the roll number."
                )

            else:

                st.session_state.student = {

                    "name": name.strip(),

                    "roll_no": roll_no.strip().upper(),

                    "branch": branch,

                    "year": year,

                    "section": section
                }


                st.success(
                    "Student profile saved successfully!"
                )


    # --------------------------------------------------------
    # CURRENT PROFILE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📋 Current Profile</div>',
        unsafe_allow_html=True
    )


    profile = st.session_state.student


    st.markdown(
        f"""
        <div class="info-card">

            <h3>
                {profile["name"] or "Student Name not added"}
            </h3>

            <b>Roll Number:</b>
            {profile["roll_no"] or "Not added"}

            <br><br>

            <b>Branch:</b>
            {profile["branch"]}

            <br><br>

            <b>Academic Year:</b>
            {profile["year"]}

            <br><br>

            <b>Section:</b>
            {profile["section"]}

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MANAGE SUBJECTS
# ============================================================

elif page == "Manage Subjects":

    st.markdown(
        '<div class="section-title">📚 Manage Subjects</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # ADD SUBJECT
    # --------------------------------------------------------

    with st.form(
        "add_subject_form",
        clear_on_submit=True
    ):

        subject_name = st.text_input(
            "Subject Name",
            placeholder="Example: Data Structures"
        )


        submitted = st.form_submit_button(
            "➕ Add Subject",
            use_container_width=True
        )


        if submitted:

            clean_name = subject_name.strip()


            if not clean_name:

                st.error(
                    "Please enter a subject name."
                )


            elif clean_name in st.session_state.subjects:

                st.warning(
                    "This subject already exists."
                )


            else:

                st.session_state.subjects.append(
                    clean_name
                )


                st.session_state.attendance[
                    clean_name
                ] = {
                    "conducted": 0,
                    "present": 0
                }


                st.success(
                    f"{clean_name} added successfully!"
                )


    # --------------------------------------------------------
    # SUBJECT LIST
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📖 Your Subjects</div>',
        unsafe_allow_html=True
    )


    if not st.session_state.subjects:

        st.info(
            "No subjects added yet."
        )


    else:

        for index, subject in enumerate(
            st.session_state.subjects
        ):

            col1, col2 = st.columns(
                [5, 1]
            )


            with col1:

                percentage = attendance_percentage(
                    subject
                )


                st.markdown(
                    f"""
                    <div class="subject-card">
                        <h3>📖 {subject}</h3>
                        <p>
                            Current attendance:
                            <b>{percentage:.1f}%</b>
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with col2:

                st.write("")


                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{index}"
                ):

                    del st.session_state.subjects[
                        index
                    ]


                    st.session_state.attendance.pop(
                        subject,
                        None
                    )


                    st.rerun()


# ============================================================
# MARK ATTENDANCE
# ============================================================

elif page == "Mark Attendance":

    st.markdown(
        '<div class="section-title">✅ Mark Attendance</div>',
        unsafe_allow_html=True
    )


    if not st.session_state.subjects:

        st.warning(
            "Please add subjects before marking attendance."
        )


    else:

        # ----------------------------------------------------
        # SELECT SUBJECT
        # ----------------------------------------------------

        selected_subject = st.selectbox(
            "Select Subject",
            st.session_state.subjects
        )


        # ----------------------------------------------------
        # ATTENDANCE FORM
        # ----------------------------------------------------

        with st.form("attendance_form"):

            attendance_date = st.date_input(
                "Class Date",
                value=date.today(),
                max_value=date.today()
            )


            status = st.radio(
                "Attendance Status",
                [
                    "Present",
                    "Absent"
                ],
                horizontal=True
            )


            submitted = st.form_submit_button(
                "💾 Save Attendance",
                use_container_width=True
            )


            if submitted:

                record = (
                    st.session_state.attendance[
                        selected_subject
                    ]
                )


                record["conducted"] += 1


                if status == "Present":

                    record["present"] += 1


                st.session_state.attendance[
                    selected_subject
                ] = record


                percentage = attendance_percentage(
                    selected_subject
                )


                st.success(
                    f"Attendance saved for "
                    f"{selected_subject} on "
                    f"{attendance_date.strftime('%d-%m-%Y')}."
                )


                st.info(
                    f"Current attendance: "
                    f"{percentage:.1f}%"
                )


        # ----------------------------------------------------
        # STATISTICS
        # ----------------------------------------------------

        record = st.session_state.attendance[
            selected_subject
        ]


        percentage = attendance_percentage(
            selected_subject
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "✅ Present",
                record["present"]
            )


        with col2:

            st.metric(
                "❌ Absent",
                record["conducted"] -
                record["present"]
            )


        with col3:

            st.metric(
                "📊 Attendance",
                f"{percentage:.1f}%"
            )


# ============================================================
# ATTENDANCE REPORT
# ============================================================

elif page == "Attendance Report":

    st.markdown(
        '<div class="section-title">📄 Attendance Report</div>',
        unsafe_allow_html=True
    )


    if not st.session_state.subjects:

        st.info(
            "No attendance data available yet."
        )


    else:

        report_rows = []


        # ----------------------------------------------------
        # CREATE REPORT
        # ----------------------------------------------------

        for subject in st.session_state.subjects:

            record = st.session_state.attendance.get(
                subject,
                {
                    "conducted": 0,
                    "present": 0
                }
            )


            conducted = record["conducted"]

            present = record["present"]

            absent = (
                conducted -
                present
            )


            percentage = attendance_percentage(
                subject
            )


            report_rows.append(
                {
                    "Subject": subject,

                    "Classes Conducted": conducted,

                    "Present": present,

                    "Absent": absent,

                    "Attendance %": round(
                        percentage,
                        2
                    ),

                    "Status": attendance_status(
                        percentage
                    )
                }
            )


        report_df = pd.DataFrame(
            report_rows
        )


        # ----------------------------------------------------
        # REPORT TABLE
        # ----------------------------------------------------

        st.dataframe(
            report_df,
            use_container_width=True,
            hide_index=True
        )


        # ----------------------------------------------------
        # OVERALL SUMMARY
        # ----------------------------------------------------

        overall, total_present, total_conducted = (
            overall_attendance()
        )


        st.markdown(
            '<div class="section-title">📊 Overall Summary</div>',
            unsafe_allow_html=True
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "✅ Total Present",
                total_present
            )


        with col2:

            st.metric(
                "📚 Total Classes",
                total_conducted
            )


        with col3:

            st.metric(
                "📊 Overall Attendance",
                f"{overall:.2f}%"
            )


        # ----------------------------------------------------
        # DOWNLOAD REPORT
        # ----------------------------------------------------

        csv_data = report_df.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(
            "⬇️ Download Attendance Report",
            data=csv_data,
            file_name="attendance_report.csv",
            mime="text/csv",
            use_container_width=True
        )


        # ----------------------------------------------------
        # ATTENDANCE MESSAGE
        # ----------------------------------------------------

        if overall >= 75:

            st.success(
                f"Your overall attendance is "
                f"{overall:.2f}%."
            )


        elif overall > 0:

            st.warning(
                f"Your overall attendance is "
                f"{overall:.2f}%. "
                f"Please monitor your attendance regularly."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        KKR & KSR Institute of Technology and Sciences
        • Student Attendance Tracker
    </div>
    """,
    unsafe_allow_html=True
)