class MedicalExpertSystem:
    def __init__(self):
        self.symptoms = []
        self.diagnosis = ""

    def ask_symptoms(self):
        print("Please answer with 'yes' or 'no' for the following questions.")

        # Ask for symptoms
        self.symptoms.append(input("Do you have a fever? ").lower() == "yes")
        self.symptoms.append(input("Do you have a cough? ").lower() == "yes")
        self.symptoms.append(input("Are you feeling fatigued? ").lower() == "yes")
        self.symptoms.append(input("Do you have body aches? ").lower() == "yes")
        self.symptoms.append(input("Do you have a sore throat? ").lower() == "yes")

    def diagnose(self):
        # Rule-based diagnosis
        if self.symptoms[0] and self.symptoms[1] and self.symptoms[2]:
            self.diagnosis = "You may have the flu. Please consult a doctor."
        elif self.symptoms[0] and self.symptoms[1] and not self.symptoms[2]:
            self.diagnosis = "You may have a common cold. Please rest and hydrate."
        elif self.symptoms[0] and not self.symptoms[1]:
            self.diagnosis = "You might have a fever. Check your temperature and rest."
        elif self.symptoms[4]:
            self.diagnosis = "Sore throat detected. It could be a viral infection or strep throat."
        else:
            self.diagnosis = "It’s hard to determine the illness with the current symptoms. Please visit a doctor."

    def show_diagnosis(self):
        print("\nDiagnosis: ", self.diagnosis)

# Example usage
expert_system = MedicalExpertSystem()
expert_system.ask_symptoms()
expert_system.diagnose()
expert_system.show_diagnosis()
