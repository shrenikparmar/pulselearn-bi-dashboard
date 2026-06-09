import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ==========================================
# CENTRALIZED MOCK STORAGE ENGINE (data.py inline)
# ==========================================
MOCK_DATA = {
    "global_kpis": {
        "admin": {
            "total_enrollments": "1,150", "active_students": "930", "completion_rate": "76.8%", "dropout_rate": "6.1%",
            "learning_hours": "28,450", "active_courses": "14", "license_usage": "84.7%"
        },
        "instructor": {
            "my_students": 101, "pending_reviews": 20, "class_avg": "76%", "at_risk": 5
        },
        "learner": {
            "name": "Noah Iyer", "course": "Hip Hop I", "progress": "68%", "streak": "12 days", "hours": "24.5h", "rank": "#7"
        }
    },
    "courses": [
        {"id": "ballet", "name": "Ballet Basics", "cohort": "Cohort 7", "instructor": "Elena Ross", "students": 42, "avg_grade": "76%", "rating": 4.5, "duration": "10 weeks", "completion": 78, "category": "Classical", "bottleneck": "Week 4 Quiz (2.4x avg attempts)"},
        {"id": "hiphop", "name": "Hip Hop I", "cohort": "Cohort 1", "instructor": "Marcus Lee", "students": 36, "avg_grade": "69%", "rating": 4.2, "duration": "8 weeks", "completion": 65, "category": "Street", "bottleneck": "Technique Test 2 (3.1x avg attempts)"},
        {"id": "contemporary", "name": "Contemporary Flow", "cohort": "Level 2", "instructor": "Leah Brooks", "students": 31, "avg_grade": "83%", "rating": 4.7, "duration": "12 weeks", "completion": 82, "category": "Modern", "bottleneck": "No bottlenecks detected"},
        {"id": "jazz", "name": "Jazz Dance", "cohort": "Fundamentals", "instructor": "Oliver Reid", "students": 28, "avg_grade": "71%", "rating": 4.3, "duration": "9 weeks", "completion": 71, "category": "Rhythm", "bottleneck": "Technique Test 2 (1.8x)"},
        {"id": "salsa", "name": "Salsa & Latin", "cohort": "Beginners", "instructor": "Diego Mora", "students": 24, "avg_grade": "66%", "rating": 4.1, "duration": "8 weeks", "completion": 55, "category": "Latin", "bottleneck": "Choreography Draft (2.1x)"},
        {"id": "tech_lab", "name": "Technique Lab", "cohort": "Advanced", "instructor": "Priya Menon", "students": 19, "avg_grade": "80%", "rating": 4.6, "duration": "6 weeks", "completion": 74, "category": "Skills", "bottleneck": "None"}
    ],
    "students": [
        {"name": "Ava Sharma", "course": "Ballet Basics", "progress": 83, "grade": 85, "streak": "16 days", "joined": "2026-01-10", "status": "Active", "letter": "A", "q1": 85, "q2": 88, "midterm": 86, "attendance": 96},
        {"name": "Ryan Gupta", "course": "Ballet Basics", "progress": 67, "grade": 74, "streak": "9 days", "joined": "2026-01-11", "status": "Active", "letter": "B", "q1": 71, "q2": 74, "midterm": 73, "attendance": 88},
        {"name": "Noah Iyer", "course": "Hip Hop I", "progress": 49, "grade": 61, "streak": "4 days", "joined": "2026-01-15", "status": "At Risk", "letter": "D", "q1": 62, "q2": 58, "midterm": 61, "attendance": 69},
        {"name": "Mia Verma", "course": "Hip Hop I", "progress": 72, "grade": 78, "streak": "11 days", "joined": "2026-01-17", "status": "Active", "letter": "B", "q1": 75, "q2": 80, "midterm": 79, "attendance": 91},
        {"name": "Liam Brown", "course": "Contemporary", "progress": 58, "grade": 69, "streak": "6 days", "joined": "2026-01-19", "status": "At Risk", "letter": "C", "q1": 68, "q2": 70, "midterm": 69, "attendance": 74},
        {"name": "Sana Thomas", "course": "Contemporary", "progress": 91, "grade": 93, "streak": "22 days", "joined": "2026-01-20", "status": "Active", "letter": "A", "q1": 94, "q2": 92, "midterm": 93, "attendance": 98},
        {"name": "Arjun Kapoor", "course": "Jazz Dance", "progress": 64, "grade": 72, "streak": "7 days", "joined": "2026-02-01", "status": "Active", "letter": "B", "q1": 70, "q2": 71, "midterm": 75, "attendance": 85},
        {"name": "Riya Bose", "course": "Jazz Dance", "progress": 39, "grade": 54, "streak": "2 days", "joined": "2026-02-04", "status": "At Risk", "letter": "F", "q1": 55, "q2": 50, "midterm": 57, "attendance": 60},
        {"name": "Ishaan Rao", "course": "Salsa & Latin", "progress": 74, "grade": 77, "streak": "10 days", "joined": "2026-02-11", "status": "Active", "letter": "B", "q1": 76, "q2": 78, "midterm": 77, "attendance": 89},
        {"name": "Kiara Nair", "course": "Salsa & Latin", "progress": 52, "grade": 63, "streak": "3 days", "joined": "2026-02-15", "status": "Inactive", "letter": "D", "q1": 60, "q2": 62, "midterm": 67, "attendance": 65}
    ],
    "alerts": {
        "high": [
            {"name": "Aarav Singh", "course": "Hip Hop I", "meta": "Last active 2 days ago", "progress": 35},
            {"name": "Mia Patel", "course": "Jazz Dance", "meta": "Last active 4 days ago", "progress": 28},
            {"name": "Liam Brown", "course": "Contemporary", "meta": "Last active 6 days ago", "progress": 42}
        ],
        "medium": [
            {"name": "Noah Davis", "course": "Salsa & Latin", "meta": "Last active 3 days ago", "progress": 51},
            {"name": "Anaya Shah", "course": "Ballet Basics", "meta": "Last active 1 day ago", "progress": 60},
            {"name": "Ishaan Verma", "course": "Hip Hop I", "meta": "Last active 5 days ago", "progress": 48}
        ],
        "low": [
            {"name": "Kiara Mehta", "course": "Jazz Dance", "meta": "Last active 2 days ago", "progress": 68},
            {"name": "Riya Nair", "course": "Salsa & Latin", "meta": "Last active 2 days ago", "progress": 71}
        ],
        "plagiarism": [
            {"student": "Mia Patel", "course": "Jazz Dance", "assignment": "Theory Reflection 4", "match": "84%"},
            {"student": "Aarav Singh", "course": "Hip Hop I", "assignment": "Routine Notes", "match": "71%"},
            {"student": "Anaya Shah", "course": "Ballet Basics", "assignment": "Technique Essay", "match": "67%"}
        ],
        "violations": [
            {"student": "Noah Davis", "type": "Unauthorized collaboration", "date": "2026-05-21", "status": "Open"},
            {"student": "Liam Brown", "type": "Repeated late submissions", "date": "2026-05-24", "status": "Reviewed"},
            {"student": "Ishaan Verma", "type": "Exam conduct warning", "date": "2026-05-31", "status": "Resolved"}
        ]
    },
    "drilldown": {
        "annual": {"labels": ["Q1", "Q2", "Q3", "Q4"], "values": [420, 510, 640, 720]},
        "quarter": {
            "Q1": {"labels": ["Jan", "Feb", "Mar"], "values": [120, 140, 160]},
            "Q2": {"labels": ["Apr", "May", "Jun"], "values": [150, 175, 185]},
            "Q3": {"labels": ["Jul", "Aug", "Sep"], "values": [200, 210, 230]},
            "Q4": {"labels": ["Oct", "Nov", "Dec"], "values": [230, 240, 250]}
        },
        "month": {
            "May": {"labels": ["W1", "W2", "W3", "W4"], "values": [35, 42, 48, 50]},
            "Jun": {"labels": ["W1", "W2", "W3", "W4"], "values": [40, 45, 48, 52]}
        }
    }
}

# ==========================================
# VIEW CONTROLLER ROUTINGS
# ==========================================
@app.route('/')
@app.route('/admin/dashboard')
def admin_dashboard():
    fig_trend = px.line(df, x='Date', y='Enrollments', title='Enrollment Core Trend')
    fig_progress = px.bar(df, x='Course', y='Progress', title='Course Progress')
    enrollment_trend_json = fig_trend.to_json()
    course_progress_json = fig_progress.to_json()
    
    # Pass these exact variable names to your template
    return render_template(
        'admin/dashboard.html',
        enrollment_trend_graph=enrollment_trend_json,
        course_progress_graph=course_progress_json
    )

@app.route('/admin/enrollment')
def admin_enrollment():
    return render_template('admin/enrollment.html', data=MOCK_DATA)

@app.route('/admin/utilization')
def admin_utilization():
    return render_template('admin/utilization.html', data=MOCK_DATA)

@app.route('/admin/alerts')
def admin_alerts():
    return render_template('admin/alerts.html', data=MOCK_DATA)

@app.route('/admin/students')
def admin_students():
    return render_template('admin/students.html', data=MOCK_DATA)

@app.route('/admin/courses')
def admin_courses():
    return render_template('admin/courses.html', data=MOCK_DATA)

@app.route('/instructor')
def instructor_dashboard():
    return render_template('instructor/dashboard.html', data=MOCK_DATA)

@app.route('/instructor/gradebook')
def instructor_gradebook():
    return render_template('instructor/gradebook.html', data=MOCK_DATA)

@app.route('/learner')
def learner_dashboard():
    return render_template('learner/dashboard.html', data=MOCK_DATA)

# ==========================================
# REST API INTERFACES (Plotly Dynamic Engine)
# ==========================================
@app.route('/api/enrollment/drill')
def api_drilldown():
    level = request.args.get('level', 'annual')
    period = request.args.get('period', '')
    
    if level == 'annual':
        return jsonify(MOCK_DATA['drilldown']['annual'])
    elif level == 'quarter' and period in MOCK_DATA['drilldown']['quarter']:
        return jsonify(MOCK_DATA['drilldown']['quarter'][period])
    elif level == 'month' and period in MOCK_DATA['drilldown']['month']:
        return jsonify(MOCK_DATA['drilldown']['month'][period])
    return jsonify({"labels": [], "values": []})

@app.route('/api/students')
def api_students():
    return jsonify({"students": MOCK_DATA['students']})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
