import random
from django.core.management.base import BaseCommand
from app.models import Course, Programme, AcademicYear, Level

class Command(BaseCommand):
    help = 'Generate 100 random unique Course records'

    def handle(self, *args, **options):
        # Retrieve all lookup records as lists
        programmes = list(Programme.objects.all())
        academic_years = list(AcademicYear.objects.all())
        levels = list(Level.objects.all())

        if not all([programmes, academic_years, levels]):
            self.stdout.write(self.style.ERROR("Please ensure all lookup tables have at least one record."))
            return

        # Define a list of courses with their corresponding programme ids
        course_data = [
            (1, 'History'),
            (1, 'Geography'),
            (1, 'Maths'),
            (1, 'Civics'),
            (1, 'Bookkeeping'),
            (1, 'Commerce'),
            (1, 'Economics'),
            (1, 'Management'),
            (1, 'Leadership'),
            (2, 'Maths'),
            (2, 'Physics'),
            (2, 'Biology'),
            (2, 'Electronics'),
            (2, 'Geography'),
            (2, 'Programming'),
            (2, 'Web Development'),
            (2, 'Networking'),
            (3, 'Biology'),
            (3, 'Chemistry'),
            (3, 'Physics'),
            (3, 'Maths'),
            (3, 'General Studies'),
            (3, 'Anatomy'),
            (3, 'Physiology'),
            (3, 'Biostatistics'),
            (3, 'Pharmacology'),
            (4, 'Maths'),
            (4, 'Physics'),
            (4, 'Chemistry'),
            (4, 'Technical Drawing'),
            (4, 'Electronics'),
            (4, 'Mechanics'),
            (4, 'Material Science'),
            (4, 'Design'),
            (5, 'History'),
            (5, 'Civics'),
            (5, 'English Literature'),
            (5, 'General Studies'),
            (5, 'Geography'),
            (5, 'Constitutional Law'),
            (5, 'Criminal Law'),
            (5, 'Ethics'),
            (40, 'Operations Management'),
            # Add more courses here to make it 100
            (2, 'Software Engineering'),
            (2, 'Artificial Intelligence'),
            (3, 'Neuroscience'),
            (3, 'Genetics'),
            (3, 'Medical Terminology'),
            (4, 'Thermodynamics'),
            (4, 'Structural Engineering'),
            (4, 'Robotics'),
            (5, 'Public Speaking'),
            (1, 'Philosophy'),
            (1, 'Linguistics'),
            (1, 'International Relations'),
            (2, 'Database Management'),
            (2, 'Operating Systems'),
            (3, 'Pharmacology'),
            (3, 'Biomedical Engineering'),
            (3, 'Microbiology'),
            (4, 'Mathematical Modelling'),
            (4, 'Fluid Mechanics'),
            (5, 'Political Science'),
            (5, 'Sociology'),
            (5, 'Anthropology'),
            (2, 'Network Security'),
            (3, 'Bioinformatics'),
            (3, 'Epidemiology'),
            (4, 'Geotechnical Engineering'),
            (4, 'Material Engineering'),
            (5, 'Criminal Justice'),
            (5, 'Human Rights'),
            (1, 'History of Art'),
            (1, 'Cultural Studies'),
            (2, 'Computer Graphics'),
            (2, 'Machine Learning'),
            (3, 'Forensic Science'),
            (3, 'Medical Imaging'),
            (4, 'Control Systems'),
            (4, 'Environmental Engineering'),
            (5, 'Public Administration'),
            (5, 'Global Economics'),
            (1, 'Political Philosophy'),
            (2, 'Cloud Computing'),
            (3, 'Clinical Psychology'),
            (4, 'Renewable Energy'),
            (5, 'International Trade'),
            (1, 'Rhetoric'),
            (1, 'Modern Languages'),
            (2, 'Data Science'),
            (3, 'Pathology'),
            (4, 'Civil Engineering'),
            (4, 'Electrical Engineering'),
            (5, 'Education Theory'),
            (5, 'International Development'),
            (2, 'Quantum Computing'),
            (3, 'Neuropsychology'),
            (3, 'Toxicology'),
            (4, 'Systems Engineering'),
            (5, 'Corporate Finance'),
            (1, 'Ancient History'),
            (1, 'Archaeology'),
            (2, 'Mobile Development'),
            (3, 'Public Health'),
            (4, 'Production Engineering'),
            (5, 'Corporate Social Responsibility'),
            (2, 'DevOps'),
            (2, 'Front-End Development'),
            (3, 'Environmental Science'),
            (4, 'Machine Vision'),
            (5, 'Social Work'),
            (1, 'Medieval History'),
            (1, 'Modern History'),
            (2, 'Computer Vision'),
            (3, 'Nanotechnology'),
            (4, 'Mechanical Engineering'),
            (5, 'Logistics Management'),
            (1, 'Psychology'),
            (1, 'Sociology'),
            (3, 'Genetic Engineering'),
            (4, 'Thermal Engineering'),
            (5, 'International Marketing'),
            # Add more until 100
        ]

        # Generate unique courses based on the course data
        courses = []
        for i in range(100):
            # Randomly select data for each course
            programme_id, course_name = course_data[i]
            programme = random.choice([programme for programme in programmes if programme.id == programme_id])
            academic_year = random.choice(academic_years)
            level = random.choice(levels)
            code = f"{programme.code}-{random.randint(100, 999)}"

            course = Course(
                name=course_name,
                code=code,
                programme=programme,
                academic_year=academic_year,
                level=level
            )
            courses.append(course)

        # Bulk create for performance
        Course.objects.bulk_create(courses)
        self.stdout.write(self.style.SUCCESS("Successfully generated 100 unique Course records"))
