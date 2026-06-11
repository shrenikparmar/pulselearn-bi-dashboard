from __future__ import annotations

from flask import Flask, jsonify, redirect, render_template, request, url_for

from data import (
    ACTIVITY_VS_CLASS_AVG,
    ADMIN_KPIS,
    ASSESSMENTS,
    AT_RISK,
    COURSE_COMPLETION,
    COURSES,
    DAILY_LEARNING_HOURS,
    DROPOUT_REASONS,
    ENROLLMENT_DATA,
    ENROLLMENT_FUNNEL,
    FEATURE_ADOPTION,
    GRADEBOOK,
    HONOR_CODE_VIOLATIONS,
    INSTRUCTOR_COURSE_CARDS,
    INSTRUCTOR_KPIS,
    LEADERBOARD,
    LICENSE_PLANS,
    LICENSE_ROI,
    LICENSE_UTILIZATION,
    PENDING_INVITATIONS,
    PLAGIARISM_FLAGS,
    RECENT_ENROLLMENTS,
    SEAT_USAGE_OVER_TIME,
    SKILL_MASTERY,
    STORAGE_BREAKDOWN,
    STUDENTS,
    UPCOMING_DEADLINES,
    WEEKLY_PLAN,
    get_assessment_detail,
    get_course_by_id,
    get_drill,
    get_student_by_id,
)

app = Flask(__name__)


def role_context(role: str) -> dict:
    return {"role": role}


@app.route("/")
def home():
    return redirect(url_for("admin_dashboard"))


@app.route("/admin")
def admin_dashboard():
    return render_template(
        "admin/dashboard.html",
        **role_context("admin"),
        kpis=ADMIN_KPIS,
        enrollment_data=ENROLLMENT_DATA,
        course_completion=COURSE_COMPLETION,
        license_utilization=LICENSE_UTILIZATION,
        daily_hours=DAILY_LEARNING_HOURS,
        at_risk=AT_RISK,
        recent_enrollments=RECENT_ENROLLMENTS,
    )


@app.route("/admin/enrollment")
def admin_enrollment():
    annual_drill = get_drill("annual", None)

    course_rows = []
    for course in COURSES:
        enrolled = int(course["students"] * 1.35)
        active = course["students"]
        dropped = max(3, int(enrolled * 0.11))
        waitlist = int(enrolled * 0.07)
        active_rate = round((active / enrolled) * 100, 1)
        drop_rate = round((dropped / enrolled) * 100, 1)
        course_rows.append(
            {
                "name": course["name"],
                "enrolled": enrolled,
                "active": active,
                "dropped": dropped,
                "waitlist": waitlist,
                "active_rate": active_rate,
                "drop_rate": drop_rate,
            }
        )

    return render_template(
        "admin/enrollment.html",
        **role_context("admin"),
        initial_drill=annual_drill,
        enrollment_funnel=ENROLLMENT_FUNNEL,
        course_rows=course_rows,
        dropout_reasons=DROPOUT_REASONS,
        pending_invitations=PENDING_INVITATIONS,
    )


@app.route("/admin/utilization")
def admin_utilization():
    total_monthly = sum(item["monthly_cost"] for item in LICENSE_PLANS)
    return render_template(
        "admin/utilization.html",
        **role_context("admin"),
        roi=LICENSE_ROI,
        seat_usage=SEAT_USAGE_OVER_TIME,
        storage_breakdown=STORAGE_BREAKDOWN,
        feature_adoption=FEATURE_ADOPTION,
        license_plans=LICENSE_PLANS,
        total_monthly=total_monthly,
    )


@app.route("/admin/alerts")
def admin_alerts():
    risk_groups = {
        "High": [x for x in AT_RISK if x["risk"] == "High"],
        "Medium": [x for x in AT_RISK if x["risk"] == "Medium"],
        "Low": [x for x in AT_RISK if x["risk"] == "Low"],
    }
    return render_template(
        "admin/alerts.html",
        **role_context("admin"),
        risk_groups=risk_groups,
        plagiarism_flags=PLAGIARISM_FLAGS,
        honor_code_violations=HONOR_CODE_VIOLATIONS,
    )


@app.route("/admin/students")
def admin_students():
    summary = {"total": 847, "active": 784, "at_risk": 42, "inactive": 21}
    return render_template(
        "admin/students.html",
        **role_context("admin"),
        summary=summary,
        students=STUDENTS,
    )


@app.route("/admin/courses")
def admin_courses():
    return render_template("admin/courses.html", **role_context("admin"), courses=COURSES)


@app.route("/instructor")
def instructor_dashboard():
    default_course = next(iter(GRADEBOOK))
    return render_template(
        "instructor/dashboard.html",
        **role_context("instructor"),
        kpis=INSTRUCTOR_KPIS,
        course_cards=INSTRUCTOR_COURSE_CARDS,
        gradebook=GRADEBOOK[default_course],
        assessments=ASSESSMENTS,
        intervention_queue=[x for x in AT_RISK if x["risk"] in {"High", "Medium"}],
    )


@app.route("/instructor/gradebook")
def instructor_gradebook():
    return render_template(
        "instructor/gradebook.html",
        **role_context("instructor"),
        courses=COURSES,
        gradebook=GRADEBOOK,
    )


@app.route("/learner")
def learner_dashboard():
    learner = {
        "name": "Noah Iyer",
        "course": "Hip Hop I",
        "streak": 12,
        "progress": 68,
        "hours": 24.5,
        "rank": 7,
    }
    return render_template(
        "learner/dashboard.html",
        **role_context("learner"),
        learner=learner,
        weekly_plan=WEEKLY_PLAN,
        deadlines=UPCOMING_DEADLINES,
        skill_mastery=SKILL_MASTERY,
        leaderboard=LEADERBOARD,
        activity=ACTIVITY_VS_CLASS_AVG,
    )


@app.route("/learner/skills")
def learner_skills():
    return render_template(
        "learner/skills.html",
        **role_context("learner"),
        skill_mastery=SKILL_MASTERY,
    )


@app.get("/api/enrollment/drill")
def enrollment_drill_api():
    level = request.args.get("level", "annual")
    period = request.args.get("period")
    return jsonify(get_drill(level, period))


@app.get("/api/students")
def students_api():
    return jsonify(STUDENTS)


@app.get("/api/course/<course_id>")
def course_api(course_id: str):
    course = get_course_by_id(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify(course)


@app.get("/api/assessment/<name>")
def assessment_api(name: str):
    detail = get_assessment_detail(name)
    if not detail:
        return jsonify({"error": "Assessment not found"}), 404
    return jsonify(detail)


@app.get("/api/student/<student_id>")
def student_api(student_id: str):
    student = get_student_by_id(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)


if __name__ == "__main__":
    app.run(debug=True)