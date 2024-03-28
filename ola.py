# import random
# import requests
# from pprint import pprint

# class LangChain:
#     @staticmethod
#     def generate_text(text):
#         # Replace 'YOUR_API_KEY' with your actual API key
#         api_key = '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'
#         endpoint = 'https://en.wikipedia.org/wiki/Ola_Cabs'

#         # Make a POST request to the LangChain API
#         response = requests.post(endpoint, json={'text': text, 'api_key': api_key})

#         # Check if the request was successful
#         if response.status_code == 200:
#             try:
#                 return response.json()['generated_text']
#             except ValueError as e:
#                 print(f"Error decoding JSON: {e}")
#                 #pprint(f"Response content: {response.content}")
#                 return None
#         else:
#             # Handle errors
#             print(f"Error: {response.status_code} - {response.text}")
#             return None

       

# class CabService:
#     def __init__(self, name, base_fare):
#         self.name = name
#         self.base_fare = base_fare

#     def calculate_price(self, distance):
#         # Calculate price using a random number generator for demonstration
#         return self.base_fare * distance * random.uniform(0.8, 1.2)

# class CabApp:
#     def __init__(self):
#         self.cab_services = {
#             "Mini": CabService("Mini", 10),
#             "Sedan": CabService("Sedan", 15),
#             "SUV": CabService("SUV", 20)
#         }

#     def get_price_estimate(self, service, distance):
#         if service in self.cab_services:
#             return self.cab_services[service].calculate_price(distance)
#         else:
#             return None

#     def change_details(self):
#         pickup = input("Enter pickup location: ")
#         destination = input("Enter destination: ")

#         print("\nPrice Estimates:")
#         for service in self.cab_services:
#             price = self.get_price_estimate(service, random.randrange(20))
#             if price is not None:
#                 print(f"{service}: {price} INR")

# if __name__ == "__main__":
#     lang_chain = LangChain()
#     cab_app = CabApp()

#     print(lang_chain.generate_text("Welcome to Cab Booking App"))

#     while True:
#         cab_app.change_details()
#         choice = input("\nDo you want to change details? (yes/no): ").lower()
#         if choice != 'yes':
#             break

#     print("Thank you for using our Cab Booking App!")



from langchain import PromptTemplate, LLMChain
from langchain_openai import OpenAI
import openai
import random

# from langchain_community.chat_models import ChatOpenAI
# openai = ChatOpenAI(model_name="gpt-3.5-turbo")

# Define cab services and base fares
cab_services = {
    "Mini": 50,
    "Sedan": 80,
    "SUV": 120
}

# Define a function to generate a random distance
def generate_random_distance():
    return random.randint(1, 50)

# Set up LangChain for generating welcoming messages
welcome_prompt = PromptTemplate(
    input_variables=["user_name"],
    template="Hello {user_name}, welcome to our awesome cab booking app! How can I assist you today?"
)
# Verify the welcome_prompt's template and input variables
#print("Welcome Prompt Template:", welcome_prompt.template)
#print("Welcome Prompt Input Variables:", welcome_prompt.input_variables)

llm = OpenAI(openai_api_key="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", temperature=0.7)

# Initialize the LLMChain with the LangChain model and the prompt
welcome_chain = LLMChain(llm=llm, prompt=welcome_prompt)

# Get user's name and generate a welcoming message
# user_name = input("Please enter your name: ")
welcome_message = welcome_chain.invoke(input="Ajay")
print(welcome_message)

# Get user's pickup and destination locations
pickup_location = input("Please enter your pickup location: ")
destination_location = input("Please enter your destination location: ")

# Generate a random distance
distance = generate_random_distance()
print(f"The estimated distance from {pickup_location} to {destination_location} is {distance} km.")

# Calculate estimated prices for each cab service
print("\nEstimated prices for your trip:")
for service, base_fare in cab_services.items():
    price = base_fare + (distance * 10)  # Assuming a rate of $10 per km
    print(f"{service} cab: ${price}")
