from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ================= FULL MENU =================
MENU = {
    "full-meal": {
        "label": "Full Meal",
        "subs": {

            # ================= INDIAN =================
            "indian": {
                "label": "Indian",
                "cuisines": {
                    "gujarati": {
                        "label": "Gujarati Thali",
                        "items": ["Complete Gujarati Thali Set"]
                    },
                    "punjabi": {
                        "label": "Punjabi Thali",
                        "items": ["Complete Punjabi Thali Set"]
                    },
                    "kathiyawadi": {
                        "label": "Kathiyawadi Thali",
                        "items": ["Complete Kathiyawadi Thali Set"]
                    }
                }
            },

            # ================= ITALIAN =================
            "italian": {
                "label": "Italian",
                "subs": {
                    "pizza": {
                        "label": "Pizza",
                        "items": [
                            "Margherita Pizza",
                            "Cheese Burst Pizza",
                            "Veg Supreme Pizza"
                        ]
                    },
                    "pasta": {
                        "label": "Pasta",
                        "items": [
                            "White Sauce Pasta",
                            "Red Sauce Pasta",
                            "Pesto Pasta"
                        ]
                    },
                    "lasagna": {
                        "label": "Lasagna",
                        "items": [
                            "Veg Lasagna",
                            "Cheese Lasagna",
                            "Mushroom Lasagna"
                        ]
                    }
                }
            },

            # ================= CHINESE =================
            "chinese": {
                "label": "Chinese",
                "subs": {
                    "fried-rice": {
                        "label": "Fried Rice",
                        "items": [
                            "Veg Fried Rice",
                            "Schezwan Fried Rice",
                            "Egg Fried Rice"
                        ]
                    },
                    "manchurian": {
                        "label": "Manchurian",
                        "items": [
                            "Dry Manchurian",
                            "Gravy Manchurian",
                            "Paneer Manchurian"
                        ]
                    },
                    "spring-roll": {
                        "label": "Spring Roll",
                        "items": [
                            "Veg Spring Roll",
                            "Cheese Spring Roll",
                            "Paneer Spring Roll"
                        ]
                    }
                }
            },

            # ================= MEXICAN =================
            "mexican": {
                "label": "Mexican",
                "subs": {
                    "tacos": {
                        "label": "Tacos",
                        "items": [
                            "Veg Tacos",
                            "Chicken Tacos",
                            "Cheese Tacos"
                        ]
                    },
                    "burritos": {
                        "label": "Burritos",
                        "items": [
                            "Veg Burrito",
                            "Chicken Burrito",
                            "Bean Burrito"
                        ]
                    },
                    "quesadilla": {
                        "label": "Quesadilla",
                        "items": [
                            "Cheese Quesadilla",
                            "Veg Quesadilla",
                            "Chicken Quesadilla"
                        ]
                    }
                }
            }
        }
    },

    # ================= DIET MEAL =================
    "diet-meal": {
        "label": "Diet Meal",
        "subs": {

            "low-carb": {
                "label": "Low Carb",
                "items": ["Salad Bowl", "Grilled Veg", "Soup"]
            },

            "high-protein": {
                "label": "High Protein",
                "items": [
                    "Egg Bowl",
                    "Chicken Breast",
                    "Paneer Bowl"
                ]
            },

            "keto": {
                "label": "Keto",
                "items": [
                    "Avocado Salad",
                    "Keto Eggs",
                    "Butter Coffee"
                ]
            },

            # ================= FRUIT DIET =================
            "fruit-diet": {
                "label": "Fruit Diet",
                "subs": {
                    "fruit-bowl": {
                        "label": "Fruit Bowl",
                        "items": [
                            "Apple Banana Bowl",
                            "Tropical Mix",
                            "Berry Bowl"
                        ]
                    },
                    "smoothies": {
                        "label": "Smoothies",
                        "items": [
                            "Mango Smoothie",
                            "Strawberry Smoothie",
                            "Banana Smoothie"
                        ]
                    },
                    "fruit-salad": {
                        "label": "Fruit Salad",
                        "items": [
                            "Mixed Fruit Salad",
                            "Citrus Salad",
                            "Honey Fruit Salad"
                        ]
                    }
                }
            }
        }
    },

    # ================= SNACKS =================
    "snacks": {
        "label": "Snacks",
        "subs": {
            "healthy": {
                "label": "Healthy Snacks",
                "items": ["Nuts Mix", "Protein Bar", "Fruit Cups"]
            },
            "fried": {
                "label": "Fried Snacks",
                "items": ["Fries", "Samosa", "Pakora"]
            },
            "fast-food": {
                "label": "Fast Food",
                "items": ["Burger", "Pizza Slice", "Wrap"]
            }
        }
    }
}

# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("index.html", menu=MENU)

@app.route("/get_menu")
def get_menu():
    return jsonify(MENU)

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)