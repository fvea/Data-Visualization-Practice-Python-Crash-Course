from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name:str)->str:
    """ Return the 2-digit Pygal country code for the given country.""" 
    for code,name in COUNTRIES.items(): 
        if name == country_name: 
            return code 
    return None 


if __name__ == "__main__":
    print(get_country_code('Andorra'))
    print(get_country_code('United Arab Emirates'))
    print(get_country_code('Afghanistan'))
    print(get_country_code('Philippines'))