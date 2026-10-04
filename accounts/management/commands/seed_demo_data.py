"""
Management command to seed sample branches, courses, and batches
near Indore for demo purposes.

Run with: python manage.py seed_demo_data
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, time, timedelta

from branches.models import Branch
from courses.models import Course
from batches.models import Batch


BRANCHES = [
    {
        "name": "Nritya Shilp | Nanda Nagar",
        "city": "Indore",
        "address": "195/3 Nanda Nagar, Indore, MP 452011",
        "phone": "0731-4001111",
        "email": "nandanagar@nrityashilp.in",
    },
    {
        "name": "Nritya Shilp | Vijay Nagar",
        "city": "Indore",
        "address": "12, Scheme No. 54, Vijay Nagar, Indore, MP 452010",
        "phone": "0731-4002222",
        "email": "vijaynagar@nrityashilp.in",
    },
    {
        "name": "Nritya Shilp | Palasia",
        "city": "Indore",
        "address": "3rd Floor, City Centre Mall, Palasia Chowk, Indore, MP 452001",
        "phone": "0731-4003333",
        "email": "palasia@nrityashilp.in",
    },
    {
        "name": "Nritya Shilp | Bhopal",
        "city": "Bhopal",
        "address": "Plot 22, MP Nagar Zone-II, Bhopal, MP 462011",
        "phone": "0755-4004444",
        "email": "bhopal@nrityashilp.in",
    },
    {
        "name": "Nritya Shilp | Ujjain",
        "city": "Ujjain",
        "address": "Freeganj Road, Near Clock Tower, Ujjain, MP 456010",
        "phone": "0734-4005555",
        "email": "ujjain@nrityashilp.in",
    },
]

COURSES = [
    {
        "name": "Bharatanatyam — Beginners",
        "dance_style": "bharatanatyam",
        "level": "beginner",
        "description": "Foundation Adavus, Mudras, and Navarasas.",
        "duration_months": 3,
        "fee": 5000.00,
    },
    {
        "name": "Bharatanatyam — Intermediate",
        "dance_style": "bharatanatyam",
        "level": "intermediate",
        "description": "Advanced Adavus, Varnam, and Abhinaya.",
        "duration_months": 6,
        "fee": 8500.00,
    },
    {
        "name": "Kathak — Beginners",
        "dance_style": "kathak",
        "level": "beginner",
        "description": "Tatkaar, Chakkar, and basic Taal.",
        "duration_months": 3,
        "fee": 5000.00,
    },
    {
        "name": "Kathak — Advanced",
        "dance_style": "kathak",
        "level": "advanced",
        "description": "Jugalbandi, Bandish Thumri, and solo performance.",
        "duration_months": 9,
        "fee": 12000.00,
    },
    {
        "name": "Bollywood Fusion",
        "dance_style": "bollywood",
        "level": "beginner",
        "description": "High-energy Bollywood choreography blending folk and film.",
        "duration_months": 2,
        "fee": 3500.00,
    },
    {
        "name": "Contemporary Dance",
        "dance_style": "contemporary",
        "level": "intermediate",
        "description": "Modern technique combining classical and free-form movement.",
        "duration_months": 4,
        "fee": 6000.00,
    },
    {
        "name": "Folk Dance Ensemble",
        "dance_style": "folk_dance",
        "level": "beginner",
        "description": "Malwi Matki, Lavani, and Garba styles.",
        "duration_months": 3,
        "fee": 4000.00,
    },
    {
        "name": "Odissi — Classical",
        "dance_style": "odissi",
        "level": "intermediate",
        "description": "Mangalacharan, Pallavi, and Abhinaya.",
        "duration_months": 6,
        "fee": 9000.00,
    },
]

BATCHES_DATA = [
    # Branch index, Course index, batch name, start_time, end_time, days, max
    (0, 0, "Bharatanatyam Morning Batch A", time(7, 0), time(8, 0), ["mon", "wed", "fri"], 20),
    (0, 2, "Kathak Evening Batch",          time(18, 0), time(19, 0), ["tue", "thu", "sat"], 18),
    (0, 4, "Bollywood Weekend Batch",       time(10, 0), time(11, 30), ["sat", "sun"], 25),

    (1, 0, "Bharatanatyam Juniors",         time(16, 30), time(17, 30), ["mon", "wed", "fri"], 15),
    (1, 1, "Bharatanatyam Advanced",        time(18, 0),  time(19, 30), ["tue", "thu"], 12),
    (1, 5, "Contemporary — Batch A",        time(7, 30),  time(8, 30), ["mon", "wed", "fri"], 16),

    (2, 2, "Kathak Beginners — Morning",   time(9, 0),  time(10, 0), ["mon", "wed", "fri"], 20),
    (2, 3, "Kathak Masters Programme",     time(17, 0), time(19, 0), ["tue", "thu", "sat"], 10),
    (2, 7, "Odissi Classical Batch",       time(6, 30), time(7, 30), ["mon", "wed", "fri"], 14),

    (3, 0, "Bharatanatyam Bhopal — AM",    time(8, 0),  time(9, 0), ["mon", "wed", "fri"], 20),
    (3, 6, "Folk Dance — Bhopal",          time(17, 30), time(18, 30), ["tue", "thu", "sat"], 22),

    (4, 0, "Bharatanatyam Ujjain",         time(7, 0),  time(8, 0), ["mon", "wed", "fri"], 18),
    (4, 2, "Kathak Ujjain Batch",          time(17, 0), time(18, 0), ["tue", "thu", "sat"], 15),
]


class Command(BaseCommand):
    help = "Seed demo branches, courses, and batches for Heritage Dance Academy"

    def handle(self, *args, **options):
        self.stdout.write("🌱 Seeding demo data...")

        # ── Courses ──────────────────────────────────────────
        course_objs = []
        for c in COURSES:
            obj, created = Course.objects.get_or_create(
                name=c["name"],
                defaults=c,
            )
            course_objs.append(obj)
            action = "Created" if created else "Exists "
            self.stdout.write(f"  {action} course: {obj.name}")

        # ── Branches ─────────────────────────────────────────
        branch_objs = []
        for b in BRANCHES:
            obj, created = Branch.objects.get_or_create(
                name=b["name"],
                defaults=b,
            )
            branch_objs.append(obj)
            action = "Created" if created else "Exists "
            self.stdout.write(f"  {action} branch: {obj.name}")

        # ── Batches ───────────────────────────────────────────
        today = date.today()
        for (bi, ci, bname, st, et, days, mx) in BATCHES_DATA:
            branch = branch_objs[bi]
            course = course_objs[ci]
            obj, created = Batch.objects.get_or_create(
                name=bname,
                branch=branch,
                course=course,
                defaults={
                    "start_date": today,
                    "end_date": today + timedelta(days=course.duration_months * 30),
                    "start_time": st,
                    "end_time": et,
                    "days": days,
                    "max_students": mx,
                    "is_active": True,
                },
            )
            action = "Created" if created else "Exists "
            self.stdout.write(f"  {action} batch:  {obj.name} @ {branch.name}")

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Done! {len(branch_objs)} branches, {len(course_objs)} courses, "
            f"{len(BATCHES_DATA)} batches seeded."
        ))
