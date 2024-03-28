Experimental code for Ola for Lang chain and Open AI - Not completed

PACKAGE LIST -

pip install pydantic==1.10.11

pip install pydantic -U 

pip install typing-inspect==0.8.0 typing_extensions==4.5.0

pip install langchain-openai  

pip install langchain

brew install python@3.11

brew install python3.11 python3.11-distutils

pip install 'langchain[all]' 

pip install -U pip setuptools    

brew install qtbase5-dev  

-------------------------
Current Program flow example -

{'user_name': 'Ajay', 'text': '\n\n"Hello Ajay, thank you for choosing our cab service. May I know your pick up location and drop off location, please? Our drivers will be happy to take you to your destination."'}

Please enter your pickup location: T-Nagar

{'pickup': 'T-Nagar', 'text': '\n\n"Thank you for providing the pick-up location as T-Nagar. May I know the drop-off location for the cab booking?"'}

Please enter your destination location: Adyar

{'destination': 'Adyar', 'text': '\n\nAcknowledged. All cab services will be displayed based on the price slabs for Adyar. Thank you for your query.'}

The estimated distance from T-Nagar to Adyar is 38 km.


Estimated prices for your trip:

Mini cab: $430

Sedan cab: $460

SUV cab: $500

{'pickup': 'T-Nagar', 'destination': 'Adyar', 'ideal_price': 430, 'text': '\n\n"Explore T-Nagar and Adyar with our cab service! Book now for a hassle-free ride to the 430 area. See you soon!"'}


---------------------------

Things to do -

1. I have to do a Sequentail Chain for better flow

2. Then only I can ask if any changes in the App or user details

3. After that I have to integrate with an api call function
