![image](https://github.com/mariaegarciab/La-H-AI/assets/138514984/b6110948-f5f9-4e2d-bd5c-c002501ed03e)

# La H AI

## Project Overview
La H Hamburgueseria is a Burger Company in Colombia and with AI i desing an innovative chatbot to make dining decisions easy and personalized. Leveraging the power of AI via the OpenAI API, La H AI suggests menu items based on users' dietary preferences, allergies, caloric goals, and specific dietary regimes like keto. Whether you're dining out or ordering in, La H AI helps align your food choices with your dietary needs.

## Features
**Personalized Recommendations:** Users can input their dietary preferences (e.g., vegan, gluten-free), allergies, and nutritional goals.

**Menu integration:** Seamlessly integrates with restaurant menus to filter and suggest items that meet user criteria.

**Interactive Experience:** Engages users through a conversational interface, providing both recommendations and nutritional information.

## Technology Stack
**Python:** For backend logic and integration with the OpenAI API.

**Flask:** A lightweight WSGI web application framework to handle requests and serve our API.

**OpenAI API:** Powers the conversational AI capabilities of the chatbot.


## Installation
Before starting, ensure you have Python installed on your machine. This project was developed using Python 3.9.

### Clone the Repository
```
git clone https://github.com/yourusername/La-H-AI-Chatbot.git
cd La-H-AI-Chatbot
```

### Set Up a Virtual Environment (Optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```
pip install -r requirements.txt
```

## Usage
To start the chatbot server:
```
python app.py
```
After running the server, the API will be accessible via http://localhost:5000. Use tools like Postman or cURL to interact with the API.


Example Request
```
curl -X POST http://localhost:5000/recommend -d '{"preferences": {"diet": "keto", "allergies": "nuts", "calories": 1200}}' -H "Content-Type: application/json"
```
This request sends user dietary preferences to the chatbot, which then returns appropriate menu item recommendations.


## Contributing
Interested in contributing to the La H AI project? Great! Start by reviewing the CONTRIBUTING.md in this repository. If you have suggestions or improvements, feel free to fork this repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Support
If you encounter any problems, please file an issue along with a detailed description at GitHub Issues.

## Acknowledgments
Thanks to OpenAI for the API that powers our chatbot's intelligence.
Special thanks to all contributors and testers who helped improve this chatbot.
