class MedicalExpertSystem:
    def __init__(self):
        self.symptoms = {}
        self.diagnosis = ""
        self.issue_type = ""

    def start(self):
        print("Welcome to the Medical Expert System.")
        print("Please choose the type of issue you're facing:")
        print("1. Physical pain")
        print("2. Mental health issues")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            self.issue_type = "physical"
            self.ask_physical_symptoms()
        elif choice == "2":
            self.issue_type = "mental"
            self.ask_mental_symptoms()
        else:
            print("Invalid choice. Exiting system.")
            exit()

    def ask_physical_symptoms(self):
        print("\nAnswer the following questions about physical symptoms:")
        self.symptoms["fever"] = input("Do you have a fever? (yes/no): ").strip().lower() == "yes"
        self.symptoms["cough"] = input("Do you have a cough? (yes/no): ").strip().lower() == "yes"
        self.symptoms["body_aches"] = input("Do you have body aches? (yes/no): ").strip().lower() == "yes"
        self.symptoms["sore_throat"] = input("Do you have a sore throat? (yes/no): ").strip().lower() == "yes"

    def ask_mental_symptoms(self):
        print("\nAnswer the following questions about your mental state:")
        self.symptoms["sadness"] = input("Have you been feeling sad or low? (yes/no): ").strip().lower() == "yes"
        self.symptoms["anxiety"] = input("Do you feel anxious or worried often? (yes/no): ").strip().lower() == "yes"
        self.symptoms["sleep_issues"] = input("Are you having trouble sleeping? (yes/no): ").strip().lower() == "yes"

    def diagnose(self):
        if self.issue_type == "physical":
            f = self.symptoms["fever"]
            c = self.symptoms["cough"]
            ba = self.symptoms["body_aches"]
            st = self.symptoms["sore_throat"]

            if f and c and ba:
                self.diagnosis = "You may have the flu. Please consult a doctor."
            elif f and st:
                self.diagnosis = "Possibly a throat infection with fever."
            elif c and st:
                self.diagnosis = "Common cold likely. Rest and hydrate."
            elif ba:
                self.diagnosis = "Body aches could indicate viral fatigue or exertion."
            else:
                self.diagnosis = "Symptoms unclear. Monitor your condition or see a doctor."

        elif self.issue_type == "mental":
            s = self.symptoms["sadness"]
            a = self.symptoms["anxiety"]
            si = self.symptoms["sleep_issues"]

            if s and si:
                self.diagnosis = "You may be facing signs of depression. Consider talking to a professional."
            elif a and si:
                self.diagnosis = "Possible anxiety disorder. Relaxation techniques or therapy might help."
            elif s or a:
                self.diagnosis = "Mild emotional distress. Talk to someone you trust or take time to relax."
            else:
                self.diagnosis = "Mental state seems stable. Stay mindful and balanced."

    def show_diagnosis(self):
        print("\nDiagnosis: ", self.diagnosis)


expert_system = MedicalExpertSystem()
expert_system.start()
expert_system.diagnose()
expert_system.show_diagnosis()





























'''
# Theory Answers for MedicalExpertSystem:

# 1. What is an expert system? How does this program simulate one?
# Ans: An expert system is a computer program that mimics the decision-making ability of a human expert. 
# This program simulates one by using a rule-based approach to ask symptom-related questions and provide diagnosis accordingly.

# 2. How are rule-based systems implemented in Python?
# Ans: Rule-based systems use conditional statements (if-elif-else) to apply logical rules based on user input. 
# In this program, rules are coded to match specific symptom combinations to diagnoses.

# 3. What is the difference between physical and mental symptoms in diagnosis?
# Ans: Physical symptoms are bodily discomforts like fever or pain, while mental symptoms relate to emotional or psychological conditions like sadness or anxiety. 
# The system separates them to ask more relevant questions and improve accuracy.

# 4. How does conditional logic help in medical decision-making?
# Ans: Conditional logic allows mapping certain symptoms to specific conditions. 
# This helps in providing preliminary diagnoses based on known symptom patterns.

# 5. Can this system be extended using machine learning? If yes, how?
# Ans: Yes. We can collect labeled symptom-diagnosis data and train a classifier (like Decision Tree or Naive Bayes) 
# to predict diagnoses automatically rather than using fixed rules.

# 6. How can user input validation be improved in such expert systems?
# Ans: By ensuring that the user can only enter valid inputs (e.g., using menus, dropdowns, or input sanitization), 
# we reduce errors and improve the system’s reliability.

# 7. What are the limitations of using only yes/no questions in diagnosis?
# Ans: Yes/no questions limit the detail and context of user input. 
# They may not capture symptom severity, duration, or additional symptoms, which can lead to incorrect or vague diagnoses.

# 8. Explain the concept of forward chaining and how it could be used here.
# Ans: Forward chaining is a reasoning method that starts with known facts (symptoms) and applies rules to infer conclusions (diagnosis). 
# This system already uses a simple form of forward chaining with if-else rules based on user input.

# 9. How would you store and manage symptoms and diagnoses for a large-scale system?
# Ans: For large-scale systems, symptoms and diagnoses should be stored in a database. 
# We can also use JSON/XML or ontology-based representations for structured and scalable knowledge bases.

# 10. What ethical considerations should be kept in mind while designing medical expert systems?
# Ans: The system must clarify that it's not a substitute for professional medical advice. 
# User data privacy, accuracy of diagnosis, and handling of sensitive mental health data must be carefully managed.

'''