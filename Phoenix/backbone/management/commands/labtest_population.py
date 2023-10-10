from django.core.management.base import BaseCommand, CommandError
from backbone.models import LabTest, Lab


class Command(BaseCommand):
    help = 'Populate the database with initial scan data'

    def handle(self, *args, **kwargs):
        ltest = [{
            "Biochemistry Lab": {
                'SGOT Test': '$50',
                'SGPT Test': '$50',
                'Sodium Test': '$40',
                'Sperm DNA Fragmentation': '$200',
                'T3 (Triiodothyronine) Test': '$60',
                'T4 (Thyroxine) Test': '$60',
                'Testosterone Test': '$70',
                'Thyroglobulin Test': '$80',
                'Thyroid Test': '$90',
                'Total Protein Test': '$40',
                'Toxoplasma Test': '$100',
                'Transferrin Test': '$50',
                'Triglycerides Test': '$40',
                'TSH (Thyroid Stimulating Hormone) Test': '$60',
                'Urea Test': '$30',
                'Uric Acid Test': '$30',
                'Valproic Acid': '$75',
                'Vitamin A Test': '$80',
                'Vitamin B12 Test': '$80',
                'Vitamin C Test': '$80',
                'Vitamin D Test': '$90',
                'Vitamin E Test': '$90',
                'VLDL Test': '$40'
            },
            "Microbiology Lab": {
                'Sputum Culture': '$100',
                'Sputum Routine Test': '$30',
                'Stool Culture': '$100',
                'Stool Routine': '$30',
                'TB Test': '$50',
                'TORCH Test': '$150',
                'Typhidot Test': '$50',
                'Urine Culture': '$100',
                'Urine Routine': '$30',
                'VDRL Test': '$40',
                'Widal Test': '$40'
            },
            "Pathology Lab": {
                'Sickling Test': '$70',
                'Synovial Fluid Analysis': '$150',
                'Triple Marker Test': '$250'
            }
        },
            {
            "Biochemistry Lab": {
                'DHEA Test': '$60',
                'Electrolytes Test': '$50',
                'ESR (Erythrocyte Sedimentation Rate) Test': '$30',
                'Estradiol (E2) Test': '$70',
                'Ferritin Test': '$50',
                'Folic Acid Test': '$40',
                'FSH (Follicle Stimulating Hormone) Test': '$70',
                'G6PD Test': '$50',
                'Gamma GT (GGTP) Test': '$60',
                'Globulin / AG Ratio': '$40',
                'Globulin Test': '$40',
                'Glucose Tolerance Test (GTT)': '$50',
                'HbA1C Test': '$50',
                'HDL Cholesterol': '$40',
                'Hemoglobin (Hb) Test': '$40',
                'HGH Test': '$100',
                'Homocysteine Test': '$60',
                'Insulin Test': '$80',
                'Iron Test': '$40',
                'LDH (Lactate Dehydrogenase) Test': '$50',
                'LDL Cholesterol': '$40',
                'LH (Luteinizing Hormone) Test': '$70',
                'Lipase Test': '$60',
                'Lipid Profile': '$80',
                'Lipoprotein A / LP(a) Test': '$60',
                'Lithium Test': '$70',
                'Liver Function Test (LFT)': '$90',
                'Magnesium Test': '$40',
                'Microalbumin Test': '$50',
                'Phosphorus Test': '$40',
                'Plasma Lactate (Lactic Acid) Test': '$60',
                'Platelet Count': '$40',
                'Potassium Test': '$40',
                'Pregnancy Test': '$20',
                'Progesterone Test': '$70',
                'Prolactin Test': '$70',
                'Protein Test': '$40',
                'Protein/Creatinine Ratio': '$50',
                'PSA (Prostate Specific Antigen) Test': '$90',
                'PTH (Parathyroid Hormone) Test': '$90',
                'Renal Profile': '$100',
                'Reticulocyte Count Test': '$50',
                'Sex Hormone Test': '$90'
            },
            "Microbiology Lab": {
                'Fungal Culture Test': '$100',
                'Helicobacter Pylori Test': '$80',
                'Hepatitis A Test': '$60',
                'Hepatitis E Test': '$60',
                'Herpes Simplex Virus (HSV) Test': '$80',
                'Malaria (Malarial Parasite) Test': '$50',
                'Mantoux Test': '$40',
                'Microfilaria Parasite Test': '$70',
                'PAP Smear': '$70',
                'Paratyphi Test': '$60',
                'Rubella Test': '$60',
                'Semen Analysis Test': '$100'
            },
            "Pathology Lab": {
                'Double Marker Test': '$200',
                'Factor V Leiden Test': '$100',
                'FNAC Test': '$150',
                'HBeAb (Hepatitis B Antibody)': '$60',
                'HBsAg Test': '$60',
                'HCV Antibody Test': '$70',
                'HLA B27 Test': '$100',
                'HSG Test': '$250',
                'Peripheral Blood Smear Test': '$50',
                'PT (Prothrombin Time) Test': '$50',
                'Pulmonary Function Test (PFT)': '$100',
                'Rheumatoid Arthritis (RA) Factor Test': '$70'
            }
        },
            {
            "Biochemistry Lab": {
                'ACTH (Adreno Corticotropic Hormone) Test': '$100',
                'Adenosine Deaminase Test': '$80',
                'Albumin Test': '$40',
                'Alkaline Phosphatase (ALP) Test': '$50',
                'Ammonia Test': '$60',
                'Amylase Test': '$50',
                'Bicarbonate Test': '$40',
                'Bilirubin Test': '$40',
                'Blood Sugar Test': '$30',
                'Blood Urea Nitrogen Test': '$40',
                'C-Peptide Test': '$90',
                'Calcium Test': '$40',
                'Carbamazepine (Tegretol) Test': '$90',
                'Chloride Test': '$40',
                'Cholesterol Test': '$40',
                'CK-MB Test': '$70',
                'Complement C3': '$60',
                'Complement C4': '$60',
                'Cortisol Test': '$80',
                'CPK (Creatine Phosphokinase) Test': '$70',
                'Creatinine Clearance Test': '$60',
                'Creatinine Test': '$40',
                'CRP (C-Reactive Protein) Test': '$50',
                'D Dimer Test': '$90'
            },
            "Microbiology Lab": {
                'AFB (Acid Fast Bacilli) Culture Test': '$100',
                'Allergy Test': '$150',
                'Blood Culture Test': '$100',
                'Chikungunya Test': '$80',
                'Chlamydia Test': '$90',
                'Cryptococcal Antigen Test': '$110',
                'Cytomegalovirus (CMV) Test': '$90'
            },
            "Hematology Lab": {
                'AEC (Absolute Eosinophil Count) Test': '$50',
                'ANA (Antinuclear Antibody) Test': '$80',
                'ANC Profile': '$100',
                'ANCA Profile': '$100',
                'APTT (Activated Partial Thromboplastin Time) Test': '$60',
                'Arterial Blood Gas (ABG)': '$70',
                'ASO Test': '$60',
                'Beta Thalassemia Test': '$100',
                'Bleeding / Clotting Time Test': '$50',
                'Blood Group Test': '$30',
                'CBC / Hemogram Test': '$50',
                'CD Test': '$80',
                'Coombs Test': '$60',
                'Cerebral Spinal Fluid (CSF) Test': '$120'
            },
            "Cytology Lab": {
                'AFP (Alpha Feto Protein) Test': '$100',
                'Anti CCP (ACCP) Test': '$90',
                'Anti Phospholipid (APL) Test': '$90',
                'Anti TPO Test': '$80',
                'Anti-Mullerian Hormone (AMH) Test': '$110',
                'Antithyroglobulin Antibody Test': '$80',
                'Antithyroid Microsomal Antibody (AMA) Test': '$80',
                'Beta HCG Test': '$90',
                'CA 15.3 Test': '$110',
                'CA 19.9 Test': '$110',
                'CA  27.29Test': '$110',
                'CA- 125(Tumor Marker) Test': '$120',
                'Cardiolipin Antibodies (ACL)': '$90',
                'CEA (Carcinoembryonic Antigen) Test': '$110'
            },
            "Toxicology Lab": {
                'Ascitic Fluid Test': '$90',
                'Pleural Fluid Analysis': '$90'
            },
            "Genetics Lab": {
                'DNA Test': '$150'
            },
            "Neurology Lab": {
                'Karyotype Test': '$200',
                'L. E. Cells Test': '$60',
                'Nerve Conduction Velocity (NCV)': '$150'
            }
        }
        ]

        try:
            lt = [LabTest(name=test, price=int(price.replace("$", ""))*15, lab=Lab.objects.get(name=lab))
                  for part in ltest for lab, tests in part.items() for test, price in tests.items()]
            # for part in ltest:
            #     for lab, tests in part.items():
            #         for test, price in tests.items():
            #             self.stdout.write(self.style.ERROR(
            #                 f'{lab}'))
            #             LabTest(name=test, price=int(price.replace(
            #                 "$", ""))*15, lab=Lab.objects.get(name=lab))
            LabTest.objects.bulk_create(lt)
        except Exception as e:
            raise CommandError(f"Error occured: {e}")
        self.stdout.write(self.style.SUCCESS(
            f'Successfully added {LabTest.objects.count()} tests!'))
