rutas_transcaribe = {
    "T100E": {
        "horarios": {
            "lunes_viernes": "6 AM - 8 PM",
            "sabados": "6 AM - 1 PM"
        },
        "estaciones": [
            "La Bodeguita", "Centro", "María Auxiliadora", 
            "Cuatro Vientos", "La Castellana", "Madre Bernarda", "Portal"
        ]
    },
    "T101": {
        "horarios": {
            "lunes_viernes": "5 AM - 9:30 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM",
        },
        "estaciones": [
            "La Bodeguita", "Centro", "Chambacú", 
            "La popa", "Bazurto", "El prado", "España",
            "Cuatro vientos","Los ejecutivos","La castellana","Madre bernarda","Portal"
        ]
    },
    "T102": {
        "horarios": {
            "lunes_viernes": "5 AM - 9:00 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM"
        },
        "estaciones": [
            "Portal", "Madre bernarda", "Los Angeles",
            "Villa Olimpica", "Rep. del Líbano", "María Auxiliadora",
            "El Prado","Bazurto","Chambacú","Centro"
        ]
    },
    "X101": {
        "horarios": {
            "lunes_viernes": "5 AM - 9 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM",
        },
        "estaciones": [
            "La Bodeguita", "Centro", "Chambacù", 
            "Bazurto", "María Auxiliadora", "España", "República del Líbano",
            "Cuatro Vientos","Villa Olímpica","Los Ejecutivos"
        ]
    },
    "X102": {
        "horarios": {
            "lunes_viernes": "5 AM - 9 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM",
        },
        "estaciones": [
            "La Bodeguita", "Centro", "Lo Amador", 
            "Delicias", "Bazurto", "Madre Bernarda", "Portal"
        ]
    },
    "X104": {
        "horarios": {
            "lunes_viernes": "5 AM - 9 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM",
          },
        "estaciones": [
            "La Bodeguita", "Centro", "Chambacú", 
            "La Popa", "Bazurto",
         ]
    },
    "T103": {
        "horarios": {
            "lunes_viernes": "5 AM - 9:00 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM"
        },
        "estaciones": [
            "Portal", "Madre bernarda", "La Castellana",
            "Los Ejecutivos", "Cuatro Vientos", "España",
            "Bazurto","La Popa","Chambacú","La Bodeguita"
        ]
    },
    "X103": {
        "horarios": {
            "lunes_viernes": "5 AM - 9:00 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM"
        },
        "estaciones": [
            "Patio Porta", "Madre bernarda", "El Prado",
            "Bazurto", "Delicias", "Centro",
            "La Bodeguita"
        ]
    },
    "X105": {
        "horarios": {
            "lunes_viernes": "5 AM - 9:00 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM",
        },
        "estaciones": [
            "Bazurto","Delicias","Lo amador","Centro",
            "Bodeguita"
        ]
    },     
    "X106": {
        "horarios": {
            "lunes_viernes": "5 AM - 9:00 PM",
            "sabados": "5:30 AM - 8:30 PM",
            "domingos": "6 AM - 8 PM",
        },
        "estaciones": [

            "La Bodeguita", "Centro", "Chambacú", 
            "La Popa", "Bazurto",
            "La Castellana","Los Ejecutivos","República del Líbano",
            "María Auxiliadora","Delicias","La Popa","Lo Amador","Centro",
            "La Bodeguita"
        ]
    },
}

def obtener_info_ruta(ruta):
    if ruta in rutas_transcaribe:
        detalles = rutas_transcaribe[ruta]
        resultado = f"Ruta: {ruta}\n"
        resultado += f"  Horarios:\n"
        resultado += f"    - Lunes a Viernes: {detalles['horarios']['lunes_viernes']}\n"
        resultado += f"    - Sábados: {detalles['horarios'].get('sabados', 'No disponible')}\n"
        resultado += f"    - Domingos: {detalles['horarios'].get('domingos', 'No disponible')}\n"
        resultado += f"  Estaciones: {', '.join(detalles['estaciones'])}\n"
        return resultado
    else:
        return "Ruta no encontrada"