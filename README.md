# Ola LangChain & OpenAI Integration (Experimental)

This repository contains experimental code for integrating Ola cab booking functionality using LangChain and OpenAI. The implementation is currently in progress and not yet complete.

## Installation

Ensure you have Python 3.11 installed. You can install the required dependencies using the following commands:

```sh
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
```

## Current Program Flow

The program currently follows this interaction sequence:

1. **User Initiates Booking**
   ```json
   {'user_name': 'Ajay', 'text': '\n\n"Hello Ajay, thank you for choosing our cab service. May I know your pick-up location and drop-off location, please? Our drivers will be happy to take you to your destination."'}
   ```

2. **User Provides Pickup Location**
   ```json
   {'pickup': 'T-Nagar', 'text': '\n\n"Thank you for providing the pick-up location as T-Nagar. May I know the drop-off location for the cab booking?"'}
   ```

3. **User Provides Destination**
   ```json
   {'destination': 'Adyar', 'text': '\n\n"Acknowledged. All cab services will be displayed based on the price slabs for Adyar. Thank you for your query."'}
   ```

4. **Estimated Trip Details**
   - Distance: **38 km**
   - Price Estimates:
     - Mini Cab: **$430**
     - Sedan Cab: **$460**
     - SUV Cab: **$500**

5. **Final Response**
   ```json
   {'pickup': 'T-Nagar', 'destination': 'Adyar', 'ideal_price': 430, 'text': '\n\n"Explore T-Nagar and Adyar with our cab service! Book now for a hassle-free ride to the 430 area. See you soon!"'}
   ```

## Upcoming Enhancements

- **Implementing a Sequential Chain** for a smoother conversational flow.
- **Enhancing User Interaction** by confirming changes in user details before proceeding.
- **Integrating API Calls** to fetch real-time pricing and availability.

Stay tuned for updates!

---

### Contributing

Contributions are welcome! Please feel free to open issues and submit pull requests.

### License

This project is under the MIT License.

