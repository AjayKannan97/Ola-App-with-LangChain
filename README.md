Experimental code for Ola for Lang chain and Open AI - Not completed

pip install pydantic==1.10.11

pip install pydantic -U 

pip install typing-inspect==0.8.0 typing_extensions==4.5.0

pip install langchain-openai  

pip install langchain

-------------------------
 {'user_name': 'Ajay', 'text': '\n\n"Hello Ajay, thank you for using our cab service app. May I know your pick up location and drop off location?"\n\n"Good morning Ajay, it\'s great to have you onboard'}
 
Please enter your pickup location: T-Nagar

{'pickup': 'T-Nagar', 'text': '\n\n"Thank you for providing the details for the cab. I can see that you have entered T-Nagar as your pick-up location. May I know your desired drop-off location?" \n'}

Please enter your destination location: Adyar

{'destination': 'Adyar', 'text': '\n\nThank you for your inquiry about the cab services in Adyar. As per your request, please be informed that all available cab services will be displayed based on the price slabs. Thank you for'}

The estimated distance from T-Nagar to Adyar is 10 km.

Estimated prices for your trip:
Mini cab: $150
Sedan cab: $180
SUV cab: $220
