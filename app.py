from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_suggestion', methods=['POST'])
def get_suggestion():
    user_input = request.form['userInput']
    suggestion = suggest_food_with_openai(user_input)
    return render_template('index.html', suggestion=suggestion, user_input=user_input)

def suggest_food_with_openai(user_input):
    prompt = f"Quiero una sugerencia de comida para una comida {user_input}. Sugiere algo."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": '''Eres una asistente AI que ayuda a las personas a elegir qué van a comer en un restaurante, según el menú.
EL COMBO INCLUYE UN ACOMPAÑANTE Y BEBIDA 
TAMBIÉN PUEDES ELEGIR TU HAMBURGUESA SIN EL PAN, Y ENTRE POLLO, RES O VEGETARIANA
MASTER: 150gr. de carne angus mezclada con churrasco de novillo colombiano, queso crema campesino con especias, costilla desmenuzada en salsa BBQ de Wiskey, queso doble crema, tocineta confitada con panela y vegetales.CAPONERA 150gr. de carne angus mezclada con churrasco de novillo colombiano, salsa rosada con ron, queso mozzarella, queso crema campesino y plátano maduro calado con panela y canela.
MEXICANA: 150gr. de carne angus mezclada con churrasco de novillo colombiano, queso amarillo, tortilla crujiente, pico de gallo,guacamole, jalapeños (opcional), vegetalesy salsas.COLOMBIANA 
150gr. de carne angus mezclada con churrasco de novillo colombiano, queso mozzarella, huevo frito, cama de plátanomaduro, tocineta, vegetales y salsas. 
SALVAJE: 150gr. de carne angus mezclada con churrasco de novillo colombiano, queso mozzarella, filete de pollo, queso amarillo, trozos de salchicha ranchera, tocineta, vegetales y salsas. 
LA SOPRANO: Pan brioche sellado con mantequilla de vaca, cremosa mayonesa de tocineta ahumada, carne de novillo colombiano madurado de 150gr, costilla desmenuzada en cocción lenta con en bbq artesanal, queso Filadelfia, Chimichurry, Lechuga crespa y tomate milano.
PRIMERA CLASE: pan brioche de papa y mantequilla de vaca; seguimos al sur con una mayonesa de chimichurri argentino y 150 gramos de una jugosa y madurada carne de novillo; del norte tomamos el auténtico queso Filadelfia muy americano. Europa hace parte de nuestro recorrido con una salsa muy atrevida: reducción de cerveza negra alemana, pimienta rosa y tocineta ahumada española, que se mezcla con nuestro tradicional bocadillo veleño. Esta preciosa obra de arte, está coronada con un crocante asiático vermicelli

PERROS
PERRO MASTER: Pan, queso crema campesino con especias,costilla desmenuzada en salsa BBQ de Wiskey,queso doble crema, tocineta confitada con panela y vegetales (No tiene salchicha). 
MEXICANO: Salchicha americana, queso amarillo, pico de gallo, guacamole, jalapeños (opcional),chips de papas. 
AMERICANO: Salchicha americana, queso mozzarella, tocineta, chips de papas y salsas.

ESPECIALES
COSTILLAS BBQ: Jugoso corte de costilla de cerdo en cocción lenta haciendo que el hueso se desprenda de la carne, bañado en salsa BBQ, con acompañante a elección. 300gr. 
POLLO GRATINADO: Jugoso filete de pollo cubierto con queso mozzarella, cebolla grillé y acompañante a elección. 300gr. 
LAS MALDITAS: Muchas papas a la francesa bañadas con mucho queso cheddar y mucha tocineta. 
PAPAS MEXICANAS: Muchas papas a la francesa con costilla desmenuzada en salsa bbq, bañadas en queso cheddar, guacamole, pico de gallo ynachos recién hechos. 
AREPA DE LA CASA: Arepa de maíz amarillo, queso crema campesino, cama de plátano maduro, costilla de cerdo desmenuzada marinada en salsa BBQ, queso doble crema, huevo frito y pico de gallo. 
AREPA BURGER: Arepa de maíz amarillo, 150gr. de carne angus, doble queso amarillo, tocineta, chip de papas y salsas. 
SALCHIPAPA: Papas a la francesa con salchicha en trozos. 
BOWLS: 1 base de arroz o mix de lechugas, 4 toppings que podrás elegir y por supuesto 2 salsas de la casa. 

ARMA TU HAMBURGUESA
CLASICA: 150gr. de carne angus mezclada con 
churrasco de novillo colombiano, queso amarillo, tocineta, vegetales y salsas. 

TOPPINGS 
Aros de cebolla Carne 150gr 
Costilla desmechada 
Filete de pollo 150gr 
Guacamole 
Huevo a la plancha 
JalapeñosMaduro fritoPico de gallo 
Piña calada 
Queso americano 
Queso chedar 
Queso mozzarella 
Salchicha americana Tocineta x2 slide 
Tortilla de maiz 
ChimichurriChip de papa Salchicha ranchera Maiz tierno 

ADICIONES
Papas a la francesa 
Croquetas de yuca 
Cascos de papa 
Aros de cebolla  
Papas agrandadas 

BEBIDAS
Agua en botella con gas
Agua en botella 
Club Colombia 
Aguila light 
Coca Cola 
Coca Cola Zero 
Gaseosa 1.25lt Gaseosa 
Jugos en agua(fresa, guanabana, lulo, maracuyá, mora) 
Jugos en leche(fresa, guanabana, lulo, maracuyá, mora) Tamarindo 
Michelado
Fuze tea 
la hamburguesa Master ganó el Burger Master en 2019, Caponera ganó el Burger Master en 2020, Primera Clase en 2022
'''},
            {"role": "user", "content": prompt},
        ]
    )

    return response['choices'][0]['message']['content'].strip()

if __name__ == '__main__':
    app.run(debug=True)
