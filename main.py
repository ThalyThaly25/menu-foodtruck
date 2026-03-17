from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles




app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")



# DATABASE SIMPLE DE PLATOS
dishes = {
    "cuban": {
        "name": "Cuban Sandwich",
        "category": "Sandwiches",
        "price": "$10",
        "badge": "Fan Fave",
        "emoji": "/static/images/pan.png",
        "desc": "A massive stack featuring your choice of Chicken, Pork, or Beef, plus seared ham, melted cheese, lettuce, and tomato on a toasted bun. No frills, just pure Cuban-inspired flavor",
        "inspo": "The Cuban Sandwich is more than just a meal—it’s a legacy. At Uncle Moro, we respect the tradition of the grill.We take premium cuts of pork, chicken, or beef and sear them directly on the grill to lock in every drop of juice and smoky aroma. No butter is needed when you have the authentic crunch of a perfectly dry-toasted bun and the richness of our flame-kissed meats.",
        "ingredients": [
            {"text":"Roasted Pork","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Roasted Chicken","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Roasted Beef","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Ham","bg_color":"#ffd6d6","text_color":"#7a0000"},
            {"text":"Cheese","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Lettuce","bg_color":"#d3f9d8","text_color":"#1b5e20"},
            {"text":"Tomato","bg_color":"#d3f9d8","text_color":"#1b5e20"},
        ]
    },

    "tacos": {
        "name": "Tacos ×2",
        "category": "Mexican Style",
        "price": "$15",
        "badge": "Popular",
        "emoji": "/static/images/tacos2.png",
        "desc": "Two oversized tacos filled with charcoal-grilled meat, sautéed peppers, and melted cheese. Topped with crisp garden veggies and fresh scallions. Messy, hearty, and full of island flavor",
        "inspo": "A Mexican soul with a Cuban heartbeat. We’ve taken the street-food classic and given it a Varadero twist. Your choice of flame-grilled pork, chicken, or beef, seasoned with our secret island rub, served on warm tortillas with sautéed peppers, melted cheese, and fresh pico de gallo.",
        "ingredients": [
            {"text":"Tortilla","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Beef","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Chicken","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Pork","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Cilantro","bg_color":"#d3f9d8","text_color":"#1b5e20"},
            {"text":"Lettuce","bg_color":"#d3f9d8","text_color":"#1b5e20"},
            {"text":"Tomato","bg_color":"#f1f3f5","text_color":"#343a40"},
            {"text":"Pepper","bg_color":"#f1f3f5","text_color":"#343a40"},
        ]
    },

    "quesadilla": {
        "name": "Kidsadilla",
        "category": "Mexican Style",
        "price": "$10",
        "badge": "Kid Friendly ✓",
        "emoji": "/static/images/kid2.png",
        "desc": "The perfect choice for our youngest foodies. We take a soft flour tortilla and fill it with a generous layer of melted cheese and premium seared ham, grilling it until it's golden and crispy on the outside. It’s simple, delicious, and exactly what they need for a quick, mess-free meal. Served warm and ready to enjoy!",
        "inspo": "A golden-brown tortilla filled with a mountain of melty cheese and tender ham. Designed specifically for our youngest guests who want a delicious, warm meal that’s easy to eat on the go. It’s the cheesy hug they’ve been waiting for!",
        "ingredients": [
            {"text":"Tortilla","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Cheese","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Ham","bg_color":"#fff3bf","text_color":"#665c00"},
        ]
    },

    "tacofries": {
        "name": "Taco Fries",
        "category": "Street Food",
        "price": "$15",
        "badge": "Must Try",
        "emoji": "/static/images/fries2.JPG",
        "desc": "A tropical twist on your favorite comfort food. Golden crispy fries topped with savory Cuban-style seasoned ground beef, sautéed red bell peppers, and a generous layer of shredded melted cheese. Finished with fresh chives for that perfect Caribbean pop of color.",
        "inspo": "Imagine taking the heart-warming comfort of the Great White North and seasoning it with the sun-drenched soul of Varadero's white sands. This isn't just a poutine; it's a journey. We took the crispy foundation of a Canadian classic and topped it with our authentic, slow-simmered Cuban Picadillo, vibrant roasted peppers, and a mountain of melted cheese. It’s cold-weather comfort meets Caribbean heat.",
        "ingredients": [
            {"text":"Fries","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Cheese","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Groundbeef","bg_color":"#d3f9d8","text_color":"#1b5e20"},
            {"text":"Cilantro","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Pepper","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Green Onion","bg_color":"#d3f9d8","text_color":"#1b5e20"},
        ]
    },

    "rice": {
        "name": "Rice & Meat",
        "category": "Cuban Tradition",
        "price": "$15",
        "badge": "Authentic",
        "emoji": "/static/images/rice.png",
        "desc": "Classic Cuban Congrí (black bean rice) with flame-seared grilled meat. Authentic and delicious.",
        "inspo": "Experience the deep flavors of the Caribbean. We simmer our rice and black beans together to create the perfect Congrí, infusing every grain with savory spices and smoky notes. Paired with our tender, grilled meat, this bowl is the ultimate tropical comfort dish.",
        "ingredients": [
            {"text":"Rice","bg_color":"#fff3bf","text_color":"#665c00"},
            {"text":"Black Beans","bg_color":"#e5dbff","text_color":"#3b2e7e"},
            {"text":"Chicken","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Pork","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Beef","bg_color":"#ffe8cc","text_color":"#8a4b00"},
            {"text":"Pepper","bg_color":"#ffe8cc","text_color":"#8a4b00"},
        ]
    }
}


@app.get("/")
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/plates")
def read_plate(request: Request, plate: str):
    dish = dishes.get(plate)
    return templates.TemplateResponse(
        "plates.html",
        {
            "request": request,
            "dish": dish
        }
    )