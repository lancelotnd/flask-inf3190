ingredients  = {
                                                "Purée de patates": {
                                                    "Pommes de terre": None,
                                                    "Eau": None,
                                                    "Huile de soya": None,
                                                    "Poudre de lait entier": None,
                                                    "Sel": None,
                                                    "Fromage à la crème": {
                                                        "Lait et crème": None,
                                                        "Culture bactérienne": None,
                                                        "Sel, Gomme de caroube": None,
                                                        "Lactosérum": None,
                                                        "Concentré de protéine de lactosérum": None
                                                        },
                                                    "Pyrophosphate acide de sodium": None,
                                                    "Cellulose modifiée": None,
                                                    "Épices": None,
                                                    "Colorant": None
                                                    },
                                                "Carottes": None,
                                                "Galette de boeuf cuite": {
                                                    "Boeuf": None,
                                                    "Eau": None,
                                                    "Chapelure de blé grillé": None,
                                                    "Farine de blé": None,
                                                    "Sel": None,
                                                    "Gluten de blé": None,
                                                    "Vinaigre": None,
                                                    "Poudre d'oignon": None,
                                                    "Épices": None
                                                    },
                                                "Sauce brune": {
                                                    "Eau": None,
                                                    "Amidon de maïs modifié": None,
                                                    "Protéine végétale hydrolisée": {
                                                        "Soya": None,
                                                        "Maïs": None
                                                        },
                                                    "Levure Torula": None,
                                                    "Extrait de levure": None,
                                                    "Extraits secs de glucose": None,
                                                    "Farine de blé": None,
                                                    "Amidon de maïs": None,
                                                    "Sel": None,
                                                    "Huile de canola": None,
                                                    "Caramel en poudre": None,
                                                    "Saveurs naturelles": None,
                                                    "Farine de soya": None
                                                    },
                                                "Oignons blancs": None
                                                }


def print_recursive(d):
    to_return = ""
    for key in d:
        to_return+="<li>"+key
        if d[key]:
            to_return +="<ul>"
            to_return += print_recursive(d[key])
            to_return += "</ul>"
        to_return+= "</li>"
    return to_return



print(print_recursive(ingredients))