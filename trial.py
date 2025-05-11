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


# Example usage
expert_system = MedicalExpertSystem()
expert_system.start()
expert_system.diagnose()
expert_system.show_diagnosis()