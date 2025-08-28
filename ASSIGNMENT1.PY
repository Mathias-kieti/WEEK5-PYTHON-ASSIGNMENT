class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")

# Derived class: AndroidPhone
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, android_version):
        super().__init__(brand, model, storage)
        self.android_version = android_version

    def use_google_assistant(self):
        print("How can I help you?")

# Testing the class
android = AndroidPhone("Samsung", "Galaxy S23", 128, "Android 13")

android.info()
android.call("0719688799")
android.use_google_assistant()
