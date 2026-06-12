"""Mock in-memory data for the eLearning analytics dashboard."""

from __future__ import annotations

from typing import Any

ADMIN_KPIS = {
    "total_enrollments": 1150,
    "active_students": 930,
    "completion_rate": 76.8,
    "dropout_rate": 6.1,
    "total_learning_hours": 28450,
    "active_courses": 14,
    "license_usage": 84.7,
}

ENROLLMENT_DATA = [
    {"month": "Jan", "enrolled": 120, "active": 94, "completed": 70},
    {"month": "Feb", "enrolled": 135, "active": 101, "completed": 76},
    {"month": "Mar", "enrolled": 140, "active": 110, "completed": 82},
    {"month": "Apr", "enrolled": 152, "active": 118, "completed": 90},
    {"month": "May", "enrolled": 160, "active": 125, "completed": 98},
    {"month": "Jun", "enrolled": 172, "active": 136, "completed": 108},
    {"month": "Jul", "enrolled": 182, "active": 143, "completed": 116},
    {"month": "Aug", "enrolled": 189, "active": 152, "completed": 124},
]

COURSE_COMPLETION = [
    {"course": "Ballet Basics", "completion": 78},
    {"course": "Hip Hop I", "completion": 65},
    {"course": "Contemporary", "completion": 82},
    {"course": "Jazz Dance", "completion": 71},
    {"course": "Salsa & Latin", "completion": 55},
]

LICENSE_UTILIZATION = [
    {"resource": "Student Seats", "used": 847, "total": 1000, "unit": ""},
    {"resource": "Instructor Seats", "used": 38, "total": 50, "unit": ""},
    {"resource": "Storage", "used": 720, "total": 1000, "unit": "GB"},
    {"resource": "Live Sessions", "used": 142, "total": 200, "unit": ""},
]

DAILY_LEARNING_HOURS = [
    {"day": "Mon", "hours": 4200},
    {"day": "Tue", "hours": 4300},
    {"day": "Wed", "hours": 4050},
    {"day": "Thu", "hours": 4150},
    {"day": "Fri", "hours": 3900},
    {"day": "Sat", "hours": 4500},
    {"day": "Sun", "hours": 3350},
]

AT_RISK = [
    {"id": "S-204", "name": "Aarav Singh", "course": "Hip Hop I", "last_active": "2 days ago", "progress": 41, "risk": "High"},
    {"id": "S-219", "name": "Mia Patel", "course": "Jazz Dance", "last_active": "4 days ago", "progress": 36, "risk": "High"},
    {"id": "S-231", "name": "Noah Davis", "course": "Salsa & Latin", "last_active": "3 days ago", "progress": 48, "risk": "Medium"},
    {"id": "S-244", "name": "Anaya Shah", "course": "Ballet Basics", "last_active": "1 day ago", "progress": 59, "risk": "Medium"},
    {"id": "S-252", "name": "Liam Brown", "course": "Contemporary", "last_active": "6 days ago", "progress": 29, "risk": "High"},
    {"id": "S-266", "name": "Kiara Mehta", "course": "Jazz Dance", "last_active": "2 days ago", "progress": 62, "risk": "Low"},
    {"id": "S-278", "name": "Ishaan Verma", "course": "Hip Hop I", "last_active": "5 days ago", "progress": 53, "risk": "Medium"},
    {"id": "S-289", "name": "Riya Nair", "course": "Salsa & Latin", "last_active": "2 days ago", "progress": 67, "risk": "Low"},
]

RECENT_ENROLLMENTS = [
    {"id": "E-9001", "name": "Zara Khan", "course": "Ballet Basics", "date": "2026-05-28", "status": "Active"},
    {"id": "E-9002", "name": "Ethan Moore", "course": "Contemporary", "date": "2026-05-29", "status": "Pending"},
    {"id": "E-9003", "name": "Sana Iyer", "course": "Jazz Dance", "date": "2026-05-30", "status": "Active"},
    {"id": "E-9004", "name": "Mateo Clark", "course": "Hip Hop I", "date": "2026-06-01", "status": "Onboarding"},
    {"id": "E-9005", "name": "Priya Rao", "course": "Salsa & Latin", "date": "2026-06-02", "status": "Active"},
]

ENROLLMENT_FUNNEL = [
    {"stage": "Visited Site", "count": 4800},
    {"stage": "Started Signup", "count": 2950},
    {"stage": "Completed Signup", "count": 1620},
    {"stage": "Made Payment", "count": 1150},
    {"stage": "Onboarding", "count": 930},
]

DROPOUT_REASONS = [
    {"reason": "Cost", "value": 38},
    {"reason": "Time", "value": 25},
    {"reason": "Interest", "value": 17},
    {"reason": "Difficulty", "value": 12},
    {"reason": "Technical", "value": 8},
]

PENDING_INVITATIONS = [
    {"name": "Arjun Menon", "email": "arjun.menon@example.com", "course": "Contemporary", "sent_on": "2026-06-02"},
    {"name": "Emily Reed", "email": "emily.reed@example.com", "course": "Ballet Basics", "sent_on": "2026-06-03"},
    {"name": "Devika Sen", "email": "devika.sen@example.com", "course": "Hip Hop I", "sent_on": "2026-06-04"},
]

LICENSE_ROI = {
    "cost_per_student": 12.40,
    "revenue_per_user": 89.50,
    "roi_multiplier": 3.2,
    "unused_seat_cost": 186,
}

SEAT_USAGE_OVER_TIME = [
    {"month": "Mar", "used": 620},
    {"month": "Apr", "used": 688},
    {"month": "May", "used": 735},
    {"month": "Jun", "used": 776},
    {"month": "Jul", "used": 812},
    {"month": "Aug", "used": 847},
]

STORAGE_BREAKDOWN = [
    {"name": "Video", "value": 480},
    {"name": "Assignments", "value": 120},
    {"name": "Uploads", "value": 80},
    {"name": "System", "value": 40},
]

FEATURE_ADOPTION = [
    {"feature": "Video Lessons", "value": 94},
    {"feature": "Quizzes", "value": 88},
    {"feature": "Live Sessions", "value": 71},
    {"feature": "Peer Reviews", "value": 64},
    {"feature": "Discussion Boards", "value": 76},
]

LICENSE_PLANS = [
    {"plan": "Student Pro", "seats": 1000, "unit_price": 4.80, "monthly_cost": 4800},
    {"plan": "Instructor Pro", "seats": 50, "unit_price": 18.00, "monthly_cost": 900},
    {"plan": "Storage Add-on", "seats": 1, "unit_price": 288.00, "monthly_cost": 288},
    {"plan": "Live Session Pack", "seats": 200, "unit_price": 0.50, "monthly_cost": 100},
]

PLAGIARISM_FLAGS = [
    {"student": "Mia Patel", "course": "Jazz Dance", "assignment": "Theory Reflection 4", "similarity": 84},
    {"student": "Aarav Singh", "course": "Hip Hop I", "assignment": "Routine Notes", "similarity": 71},
    {"student": "Anaya Shah", "course": "Ballet Basics", "assignment": "Technique Essay", "similarity": 67},
]

HONOR_CODE_VIOLATIONS = [
    {"student": "Noah Davis", "type": "Unauthorized collaboration", "date": "2026-05-21", "status": "Open"},
    {"student": "Liam Brown", "type": "Repeated late submissions", "date": "2026-05-24", "status": "Reviewed"},
    {"student": "Ishaan Verma", "type": "Exam conduct warning", "date": "2026-05-31", "status": "Resolved"},
]

COURSES = [
    {
        "id": "C-101",
        "name": "Ballet Basics",
        "category": "Classical",
        "instructor": "Elena Ross",
        "students": 42,
        "avg_grade": 76,
        "rating": 4.5,
        "completion": 78,
        "duration": "10 weeks",
        "modules": [
            {"name": "Posture", "completion": 92},
            {"name": "Footwork", "completion": 85},
            {"name": "Turns", "completion": 74},
            {"name": "Stage Presence", "completion": 61},
        ],
        "grade_distribution": {"A": 8, "B": 16, "C": 11, "D": 5, "F": 2},
        "weekly_enrollment": [8, 10, 7, 9, 8],
        "top_performers": ["Sonia Paul", "Ravi Das", "Nina George", "Aditi Jain"],
    },
    {
        "id": "C-102",
        "name": "Hip Hop I",
        "category": "Street",
        "instructor": "Marcus Lee",
        "students": 36,
        "avg_grade": 69,
        "rating": 4.2,
        "completion": 65,
        "duration": "8 weeks",
        "modules": [
            {"name": "Groove Basics", "completion": 81},
            {"name": "Isolation", "completion": 66},
            {"name": "Freestyle", "completion": 58},
            {"name": "Battle Drill", "completion": 52},
        ],
        "grade_distribution": {"A": 5, "B": 12, "C": 10, "D": 6, "F": 3},
        "weekly_enrollment": [7, 8, 6, 9, 6],
        "top_performers": ["Raj Nair", "Tina Roy", "Neil Shah", "Ava Cruz"],
    },
    {
        "id": "C-103",
        "name": "Contemporary",
        "category": "Modern",
        "instructor": "Leah Brooks",
        "students": 31,
        "avg_grade": 83,
        "rating": 4.7,
        "completion": 82,
        "duration": "12 weeks",
        "modules": [
            {"name": "Flow", "completion": 88},
            {"name": "Partner Work", "completion": 79},
            {"name": "Improvisation", "completion": 84},
            {"name": "Final Piece", "completion": 73},
        ],
        "grade_distribution": {"A": 11, "B": 13, "C": 5, "D": 2, "F": 0},
        "weekly_enrollment": [6, 7, 5, 8, 5],
        "top_performers": ["Maya Gill", "Om Verma", "Lina Hart", "Aman Sethi"],
    },
    {
        "id": "C-104",
        "name": "Jazz Dance",
        "category": "Rhythm",
        "instructor": "Oliver Reid",
        "students": 28,
        "avg_grade": 71,
        "rating": 4.3,
        "completion": 71,
        "duration": "9 weeks",
        "modules": [
            {"name": "Warmups", "completion": 95},
            {"name": "Combinations", "completion": 74},
            {"name": "Expression", "completion": 63},
            {"name": "Performance", "completion": 54},
        ],
        "grade_distribution": {"A": 4, "B": 10, "C": 8, "D": 4, "F": 2},
        "weekly_enrollment": [5, 5, 6, 6, 6],
        "top_performers": ["Rhea Jain", "Cole Park", "Tara Bose", "Milan Shah"],
    },
    {
        "id": "C-105",
        "name": "Salsa & Latin",
        "category": "Latin",
        "instructor": "Diego Mora",
        "students": 24,
        "avg_grade": 66,
        "rating": 4.1,
        "completion": 55,
        "duration": "8 weeks",
        "modules": [
            {"name": "Timing", "completion": 69},
            {"name": "Partner Frame", "completion": 62},
            {"name": "Turns", "completion": 51},
            {"name": "Routine", "completion": 44},
        ],
        "grade_distribution": {"A": 3, "B": 7, "C": 7, "D": 5, "F": 2},
        "weekly_enrollment": [4, 5, 4, 5, 6],
        "top_performers": ["Ira Khan", "Drew Cole", "Lia Pinto", "Vik Tan"],
    },
    {
        "id": "C-106",
        "name": "Technique Lab",
        "category": "Skills",
        "instructor": "Priya Menon",
        "students": 19,
        "avg_grade": 80,
        "rating": 4.6,
        "completion": 74,
        "duration": "6 weeks",
        "modules": [
            {"name": "Flexibility", "completion": 82},
            {"name": "Core", "completion": 79},
            {"name": "Precision", "completion": 71},
            {"name": "Evaluation", "completion": 64},
        ],
        "grade_distribution": {"A": 6, "B": 8, "C": 3, "D": 2, "F": 0},
        "weekly_enrollment": [3, 4, 4, 4, 4],
        "top_performers": ["Nia Lee", "Jay Rao", "Ari Sen", "Moe Clark"],
    },
]

STUDENTS = [
    {
        "id": "S-001",
        "name": "Ava Sharma",
        "course": "Ballet Basics",
        "progress": 83,
        "grade": 88,
        "streak": 16,
        "joined": "2026-01-10",
        "status": "Active",
        "risk": "Low",
        "skills": [82, 78, 75, 80, 84],
        "grade_trend": [74, 77, 80, 84, 88],
        "activity": ["Completed Module 4", "Submitted Quiz 2", "Attended live session"],
    },
    {
        "id": "S-002",
        "name": "Ryan Gupta",
        "course": "Ballet Basics",
        "progress": 67,
        "grade": 74,
        "streak": 9,
        "joined": "2026-01-11",
        "status": "Active",
        "risk": "Medium",
        "skills": [66, 70, 62, 68, 72],
        "grade_trend": [68, 69, 70, 72, 74],
        "activity": ["Missed live session", "Retook Quiz 2", "Completed assignment"],
    },
    {
        "id": "S-003",
        "name": "Noah Iyer",
        "course": "Hip Hop I",
        "progress": 49,
        "grade": 61,
        "streak": 4,
        "joined": "2026-01-15",
        "status": "At Risk",
        "risk": "High",
        "skills": [58, 61, 55, 52, 59],
        "grade_trend": [63, 62, 60, 60, 61],
        "activity": ["No activity for 3 days", "Late assignment"],
    },
    {
        "id": "S-004",
        "name": "Mia Verma",
        "course": "Hip Hop I",
        "progress": 72,
        "grade": 78,
        "streak": 11,
        "joined": "2026-01-17",
        "status": "Active",
        "risk": "Low",
        "skills": [76, 73, 74, 71, 79],
        "grade_trend": [70, 72, 74, 76, 78],
        "activity": ["Perfect attendance", "Completed challenge"],
    },
    {
        "id": "S-005",
        "name": "Liam Dsouza",
        "course": "Contemporary",
        "progress": 58,
        "grade": 69,
        "streak": 6,
        "joined": "2026-01-19",
        "status": "At Risk",
        "risk": "Medium",
        "skills": [62, 64, 61, 59, 60],
        "grade_trend": [66, 67, 67, 68, 69],
        "activity": ["Low quiz score", "Requested help"],
    },
    {
        "id": "S-006",
        "name": "Sana Thomas",
        "course": "Contemporary",
        "progress": 91,
        "grade": 93,
        "streak": 22,
        "joined": "2026-01-20",
        "status": "Active",
        "risk": "Low",
        "skills": [91, 90, 88, 92, 95],
        "grade_trend": [86, 88, 90, 92, 93],
        "activity": ["Top performer", "Mentored peers"],
    },
    {
        "id": "S-007",
        "name": "Arjun Kapoor",
        "course": "Jazz Dance",
        "progress": 64,
        "grade": 72,
        "streak": 7,
        "joined": "2026-02-01",
        "status": "Active",
        "risk": "Medium",
        "skills": [70, 68, 67, 66, 71],
        "grade_trend": [67, 69, 70, 71, 72],
        "activity": ["Completed module 5"],
    },
    {
        "id": "S-008",
        "name": "Riya Bose",
        "course": "Jazz Dance",
        "progress": 39,
        "grade": 54,
        "streak": 2,
        "joined": "2026-02-04",
        "status": "At Risk",
        "risk": "High",
        "skills": [52, 55, 49, 48, 53],
        "grade_trend": [60, 58, 56, 55, 54],
        "activity": ["Missed 2 deadlines"],
    },
    {
        "id": "S-009",
        "name": "Ishaan Rao",
        "course": "Salsa & Latin",
        "progress": 74,
        "grade": 77,
        "streak": 10,
        "joined": "2026-02-11",
        "status": "Active",
        "risk": "Low",
        "skills": [75, 72, 74, 76, 78],
        "grade_trend": [70, 72, 74, 75, 77],
        "activity": ["Completed live workshop"],
    },
    {
        "id": "S-010",
        "name": "Kiara Nair",
        "course": "Salsa & Latin",
        "progress": 52,
        "grade": 63,
        "streak": 3,
        "joined": "2026-02-15",
        "status": "Inactive",
        "risk": "Medium",
        "skills": [61, 59, 57, 58, 62],
        "grade_trend": [64, 64, 63, 63, 63],
        "activity": ["Dormant this week"],
    },
    {
        "id": "S-011",
        "name": "Dev Malhotra",
        "course": "Technique Lab",
        "progress": 87,
        "grade": 89,
        "streak": 14,
        "joined": "2026-02-20",
        "status": "Active",
        "risk": "Low",
        "skills": [88, 85, 87, 86, 90],
        "grade_trend": [80, 83, 85, 87, 89],
        "activity": ["New personal best"],
    },
    {
        "id": "S-012",
        "name": "Nina George",
        "course": "Technique Lab",
        "progress": 61,
        "grade": 70,
        "streak": 5,
        "joined": "2026-02-23",
        "status": "Active",
        "risk": "Low",
        "skills": [69, 66, 64, 63, 67],
        "grade_trend": [65, 67, 68, 69, 70],
        "activity": ["Completed extra practice"],
    },
]

GRADEBOOK = {
    "C-101": [
        {"student": "Ava Sharma", "quiz1": 85, "quiz2": 88, "midterm": 86, "attendance": 96, "letter": "A", "status": "On Track"},
        {"student": "Ryan Gupta", "quiz1": 71, "quiz2": 74, "midterm": 73, "attendance": 88, "letter": "B", "status": "On Track"},
        {"student": "Noah Iyer", "quiz1": 62, "quiz2": 58, "midterm": 61, "attendance": 69, "letter": "D", "status": "At Risk"},
    ],
    "C-103": [
        {"student": "Sana Thomas", "quiz1": 92, "quiz2": 94, "midterm": 93, "attendance": 98, "letter": "A", "status": "On Track"},
        {"student": "Liam Dsouza", "quiz1": 68, "quiz2": 70, "midterm": 69, "attendance": 82, "letter": "C", "status": "At Risk"},
        {"student": "Nina George", "quiz1": 72, "quiz2": 71, "midterm": 70, "attendance": 86, "letter": "B", "status": "On Track"},
    ],
    "C-104": [
        {"student": "Arjun Kapoor", "quiz1": 73, "quiz2": 70, "midterm": 72, "attendance": 84, "letter": "B", "status": "On Track"},
        {"student": "Riya Bose", "quiz1": 55, "quiz2": 53, "midterm": 54, "attendance": 64, "letter": "F", "status": "At Risk"},
    ],
}

ASSESSMENTS = {
    "Week 4 Quiz": {
        "avg_attempts": 2.4,
        "flagged": 9,
        "pass_rate": 62,
        "cohort_trend": [58, 60, 61, 62],
        "attempt_distribution": {"1": 12, "2": 15, "3": 8, "4+": 3},
        "score_distribution": {"90-100": 4, "75-89": 11, "60-74": 14, "<60": 9},
        "needs_help": ["Noah Iyer", "Riya Bose", "Liam Dsouza", "Kiara Nair"],
    },
    "Technique Test 2": {
        "avg_attempts": 3.1,
        "flagged": 12,
        "pass_rate": 57,
        "cohort_trend": [52, 54, 56, 57],
        "attempt_distribution": {"1": 8, "2": 10, "3": 12, "4+": 6},
        "score_distribution": {"90-100": 3, "75-89": 10, "60-74": 13, "<60": 10},
        "needs_help": ["Arjun Kapoor", "Ryan Gupta", "Noah Iyer", "Riya Bose"],
    },
    "Midterm Theory": {
        "avg_attempts": 1.8,
        "flagged": 5,
        "pass_rate": 79,
        "cohort_trend": [74, 75, 77, 79],
        "attempt_distribution": {"1": 24, "2": 9, "3": 2, "4+": 0},
        "score_distribution": {"90-100": 8, "75-89": 14, "60-74": 9, "<60": 4},
        "needs_help": ["Noah Iyer", "Riya Bose", "Kiara Nair"],
    },
}

INSTRUCTOR_KPIS = {
    "my_students": 101,
    "pending_reviews": 20,
    "class_avg_grade": 76,
    "at_risk": 5,
}

INSTRUCTOR_COURSE_CARDS = [
    {"name": "Ballet Basics - Cohort 7", "students": 42, "avg": 76, "pending": 12, "bottleneck": "Week 4 Quiz", "attempts": 2.4},
    {"name": "Contemporary Flow - Level 2", "students": 31, "avg": 83, "pending": 0, "bottleneck": "None", "attempts": 1.0},
    {"name": "Jazz Fundamentals", "students": 28, "avg": 69, "pending": 8, "bottleneck": "Technique Test 2", "attempts": 3.1},
]

SKILL_MASTERY = {
    "overall": 70,
    "strongest": "Posture",
    "most_improved": "Musicality",
    "focus": "Choreography",
    "skills": [
            {"name": "Posture", "level": 82, "badge": "Advanced", "tip": "Hold neutral spine in transitions."},
            {"name": "Footwork", "level": 74, "badge": "Intermediate", "tip": "Practice slow tempo drills daily."},
            {"name": "Musicality", "level": 69, "badge": "Intermediate", "tip": "Count beats out loud in rehearsal."},
            {"name": "Choreography", "level": 58, "badge": "Developing", "tip": "Chunk routines into 8-count blocks."},
            {"name": "Presence", "level": 67, "badge": "Intermediate", "tip": "Focus on eye-line with audience."},
    ],
        "history_vs_class": {
            "weeks": ["W1", "W2", "W3", "W4", "W5"],
            "you": [58, 61, 64, 67, 70],
            "class": [62, 63, 64, 65, 66],
    },
        "exercises": [
            "5-minute posture wall drill",
            "Footwork ladder x3 rounds",
            "Mirror rehearsal with counts",
            "Record and review one run-through",
    ],
        "next_milestone": 78,
}


LEADERBOARD = [
    {"rank": 1, "name": "Sana Thomas", "score": 980, "streak": 22},
    {"rank": 2, "name": "Ava Sharma", "score": 962, "streak": 16},
    {"rank": 3, "name": "Dev Malhotra", "score": 940, "streak": 14},
    {"rank": 4, "name": "Mia Verma", "score": 914, "streak": 11},
    {"rank": 5, "name": "Ishaan Rao", "score": 897, "streak": 10},
    {"rank": 6, "name": "Arjun Kapoor", "score": 881, "streak": 7},
    {"rank": 7, "name": "Noah Iyer", "score": 869, "streak": 4},
    {"rank": 8, "name": "Nina George", "score": 850, "streak": 5},
]

WEEKLY_PLAN = [
    {"type": "video", "task": "Ballet posture refresher", "day": "Mon", "done": True},
    {"type": "quiz", "task": "Technique Quiz 3", "day": "Tue", "done": True},
    {"type": "live", "task": "Live feedback circle", "day": "Wed", "done": False},
    {"type": "assignment", "task": "Routine breakdown upload", "day": "Thu", "done": False},
    {"type": "video", "task": "Footwork timing drill", "day": "Fri", "done": True},
    {"type": "quiz", "task": "Musicality checkpoint", "day": "Sat", "done": False},
    {"type": "live", "task": "Weekend jam session", "day": "Sun", "done": False},
]

UPCOMING_DEADLINES = [
    {"title": "Technique Test 2", "due": "2026-06-09", "priority": "High"},
    {"title": "Choreography Draft", "due": "2026-06-11", "priority": "Medium"},
    {"title": "Peer Feedback", "due": "2026-06-12", "priority": "Low"},
    {"title": "Live Performance Check", "due": "2026-06-14", "priority": "High"},
]

ACTIVITY_VS_CLASS_AVG = {
    "weeks": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
    "you": [3.5, 4.0, 5.2, 5.8, 6.0],
    "class_avg": [4.0, 4.3, 4.6, 4.9, 5.1],
}

DRILL_DATA = {
    "annual": {
        "2024": {
            "Q1": {
                "total": 245,
                "months": {
                    "Jan": [18, 21, 24, 25],
                    "Feb": [20, 22, 23, 26],
                    "Mar": [19, 21, 23, 28],
                },
            },
            "Q2": {
                "total": 286,
                "months": {
                    "Apr": [20, 22, 24, 26],
                    "May": [21, 24, 27, 29],
                    "Jun": [22, 25, 28, 28],
                },
            },
            "Q3": {
                "total": 302,
                "months": {
                    "Jul": [23, 25, 26, 28],
                    "Aug": [24, 26, 28, 29],
                    "Sep": [22, 24, 23, 24],
                },
            },
            "Q4": {
                "total": 317,
                "months": {
                    "Oct": [24, 26, 27, 28],
                    "Nov": [25, 27, 28, 29],
                    "Dec": [26, 28, 29, 30],
                },
            },
        }
    }
}


def get_student_by_id(student_id: str) -> dict[str, Any] | None:
    return next((student for student in STUDENTS if student["id"] == student_id), None)


def get_course_by_id(course_id: str) -> dict[str, Any] | None:
    return next((course for course in COURSES if course["id"] == course_id), None)


def get_gradebook_by_course(course_id: str) -> list[dict[str, Any]]:
    return GRADEBOOK.get(course_id, [])


def get_assessment_detail(name: str) -> dict[str, Any] | None:
    return ASSESSMENTS.get(name)


def get_drill(level: str, period: str | None) -> dict[str, Any]:
    year_data = DRILL_DATA["annual"]["2024"]

    if level == "annual":
        categories = ["Q1", "Q2", "Q3", "Q4"]
        values = [year_data[q]["total"] for q in categories]
        return {
            "label": "2024 Annual",
            "level": "Level 1",
            "next_level": "quarter",
            "categories": categories,
            "values": values,
        }

    if level == "quarter" and period in year_data:
        months = year_data[period]["months"]
        categories = list(months.keys())
        values = [sum(months[m]) for m in categories]
        return {
            "label": f"{period} 2024",
            "level": "Level 2",
            "next_level": "month",
            "categories": categories,
            "values": values,
        }

    if level == "month":
        for quarter, data in year_data.items():
            months = data["months"]
            if period in months:
                categories = ["Week 1", "Week 2", "Week 3", "Week 4"]
                values = months[period]
                return {
                    "label": period,
                    "level": "Level 3",
                    "next_level": None,
                    "categories": categories,
                    "values": values,
                    "quarter": quarter,
                }

    return get_drill("annual", None)