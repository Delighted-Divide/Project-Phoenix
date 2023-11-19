import random
import uuid
from datetime import datetime, timedelta, time
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Q
from backbone.models import Surgery, Doctor, InpatientVisit, ICU

class Command(BaseCommand):
    help = 'Generate random surgeries'

    def add_arguments(self, parser):
        parser.add_argument('--num_surgeries', type=int, default=100, help='Number of surgeries to generate')

    def handle(self, *args, **kwargs):
        num_surgeries = kwargs['num_surgeries']
        self.stdout.write(f"Generating {num_surgeries} surgeries")

        for _ in range(num_surgeries):
            self.generate_surgery()

    def generate_surgery(self):
        # Random selection of inpatient visit
        inpatient_visit = random.choice(InpatientVisit.objects.all())
        admission_date = inpatient_visit.admission_date
        discharge_date = inpatient_visit.discharge_date or timezone.make_aware(datetime.now() + timedelta(days=15))

        # Random date within inpatient visit duration
        start_date = admission_date
        end_date = discharge_date
        if start_date >= end_date:
            return  # No suitable date range

        surgery_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        # surgery_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        surgery_time = time(hour, minute)
        scheduled_time = datetime.combine(surgery_date, surgery_time)

        # Select a random ICU that is available at this time
        available_icus = [icu for icu in ICU.objects.all() if not self.is_icu_occupied(icu, scheduled_time)]
        if not available_icus:
            return  # No available ICU at this time
        operating_room = random.choice(available_icus)

        # Duration between 1 and 4 hours
        duration = timedelta(hours=random.randint(1, 4))

        # Success rate and emergency status
        if datetime.now() < scheduled_time <= (datetime.now() + timedelta(days=15)):
            status = 'PLANNED'
        else:
            status = 'SUCCESS' if random.random() < 0.6 else 'FAILURE'
        was_emergency = random.random() < 0.1  # 10% chance

        # Create surgery with lead doctor
        lead_doctor = self.select_doctor(scheduled_time, duration,is_lead_doctor=True)
        if not lead_doctor:
            return  # No available doctor
        
        surgeries = [
            "Appendectomy", "Cholecystectomy", "Hernia Repair", "Colectomy", "Gastrectomy",
            "Hemorrhoidectomy", "Mastectomy", "Hysterectomy", "Cesarean Section", "Laparotomy",
            "Thyroidectomy", "Parathyroidectomy", "Adrenalectomy", "Pancreatectomy", "Splenectomy",
            "Liver Resection", "Bariatric Surgery", "Fundoplication", "Bowel Resection", "Varicose Vein Surgery",
            "Tonsillectomy", "Adenoidectomy", "Myringotomy", "Rhinoplasty", "Blepharoplasty",
            "Facelift", "Otoplasty", "Septoplasty", "Sinus Surgery", "Tracheostomy",
            "Cataract Surgery", "Glaucoma Surgery", "Corneal Transplant", "Retinal Detachment Repair", "Vitrectomy",
            "Pacemaker Insertion", "Coronary Artery Bypass", "Heart Valve Surgery", "Angioplasty", "Aortic Aneurysm Repair",
            "Varicocele Surgery", "Vasectomy", "Prostatectomy", "Cystoscopy", "Ureteroscopy",
            "Nephrectomy", "Bladder Repair", "Urethral Stricture Surgery", "Penile Implant", "Circumcision",
            "Knee Replacement", "Hip Replacement", "Shoulder Arthroscopy", "ACL Reconstruction", "Carpal Tunnel Release",
            "Spinal Fusion", "Laminectomy", "Discectomy", "Kyphoplasty", "Bone Fracture Repair",
            "Skull Base Surgery", "Craniotomy", "Brain Tumor Removal", "Ventriculoperitoneal Shunt", "Stereotactic Radiosurgery",
            "Breast Augmentation", "Breast Reduction", "Liposuction", "Tummy Tuck", "Arm Lift",
            "Thigh Lift", "Buttock Augmentation", "Hair Transplant", "Scar Revision", "Mohs Surgery",
            "Skin Grafting", "Burn Repair Surgery", "Hand Reconstruction", "Microsurgery", "Replantation Surgery",
            "Cleft Lip and Palate Repair", "Maxillofacial Surgery", "Dental Implant", "Orthognathic Surgery", "Palate Expansion",
            "Gastric Bypass", "Gastric Sleeve", "Gastric Banding", "Lipoma Removal", "Lymph Node Biopsy",
            "Port-a-Cath Insertion", "Chemotherapy Port Placement", "Bone Marrow Biopsy", "Fistula Surgery", "Abscess Drainage",
            "Ganglion Cyst Removal", "Trigger Finger Release", "Dupuytren's Contracture Release", "Knee Arthroscopy", "Ankle Repair",
            "Bunion Surgery", "Hammer Toe Correction", "Achilles Tendon Repair", "Rotator Cuff Repair", "Labrum Repair",
            "Hip Arthroscopy", "Elbow Arthroscopy", "Wrist Arthroscopy", "Gallbladder Removal", "Lung Biopsy",
            "Lobectomy", "Pneumonectomy", "Bronchoscopy", "Esophageal Surgery", "Gastric Band Adjustment",
            "Endoscopy", "Colonoscopy", "Polypectomy", "Endoscopic Sinus Surgery", "Tympanoplasty",
            "Stapedectomy", "Cochlear Implant", "Laryngectomy", "Voice Box Surgery", "Dental Extraction",
            "Root Canal", "Gum Surgery", "Oral Biopsy", "Wisdom Teeth Removal", "Braces Installation",
            "Orthopedic Surgery", "Neurosurgery", "Cardiac Surgery", "Thoracic Surgery", "Vascular Surgery",
            "Pediatric Surgery", "Oncological Surgery", "Transplant Surgery", "Plastic Surgery", "Reconstructive Surgery",
            "Robotic Surgery", "Laparoscopic Surgery", "Minimally Invasive Surgery", "Endovascular Surgery", "Microvascular Surgery",
            "Cystectomy", "Orchiectomy", "Epididymectomy", "Spermatocelectomy", "Hydrocelectomy",
            "Ovarian Cyst Removal", "Salpingectomy", "Tubal Ligation", "Endometrial Ablation", "Myomectomy"
        ]


        surgery = Surgery.objects.create(
            surgery_type=random.choice(surgeries),
            lead_doctor=lead_doctor,
            inpatient_visit=inpatient_visit,
            operating_room=operating_room,
            scheduled_time=scheduled_time,
            duration=duration,
            was_emergency=was_emergency,
            status=status
        )

        # Assign assisting doctors
        for _ in range(random.randint(0, 3)):  # 0-2 assisting doctors
            assisting_doctor = self.select_doctor(scheduled_time, duration, exclude_doctor=lead_doctor)
            if assisting_doctor:
                surgery.assisting_doctors.add(assisting_doctor)

    def is_doctor_available(self, doctor, start_time, end_time):
        # Check for overlapping surgeries
        if Surgery.objects.filter(
            Q(lead_doctor=doctor) | Q(assisting_doctors=doctor),
            scheduled_time__lt=end_time,
            scheduled_time__gte=start_time - timedelta(hours=4)
        ).exists():
            return False

        # Check work shift
        day_of_week = start_time.strftime('%A')
        work_shifts = doctor.work_shifts.filter(day_of_week=day_of_week)
        for shift in work_shifts:
            if shift.shift_start_time <= start_time.time() <= shift.shift_end_time:
                return False

        return True

    def select_doctor(self, scheduled_time, duration, exclude_doctor=None,is_lead_doctor=False):
        end_time = scheduled_time + duration
        # available_doctors = [doctor for doctor in Doctor.objects.exclude(id=exclude_doctor.id) if self.is_doctor_available(doctor, scheduled_time, end_time) if exclude_doctor else Doctor.objects.all()]
        doctors = Doctor.objects.all()

        if exclude_doctor:
            doctors = doctors.exclude(id=exclude_doctor.id)
        
        if is_lead_doctor:
        # Filtering lead doctors who have 'surgeon' in their specialty or subspeciality
            doctors = doctors.filter(
                Q(speciality__name__icontains='surgeon') | 
                Q(subspecialities__name__icontains='surgeon')
            )
        available_doctors = [doctor for doctor in doctors if self.is_doctor_available(doctor, scheduled_time, end_time)]

        return random.choice(available_doctors) if available_doctors else None

    def is_icu_occupied(self, icu, scheduled_time):
        # Check for overlapping surgeries in ICU
        return Surgery.objects.filter(
            operating_room=icu,
            scheduled_time__lte=scheduled_time + timedelta(hours=4),  # Considering max duration
            scheduled_time__gte=scheduled_time - timedelta(hours=4)  # Considering max duration
        ).exists()
