
francais_anglais = {
    "vrai": "true",
    "faux": "false",
    "integer": "entier"
}


def switch_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key

    return new_dict


anglais_francais = switch_dict(francais_anglais)

print(anglais_francais)