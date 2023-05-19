try:

    from flask import Flask
    from dotenv import load_dotenv
    import jpype

    # Rutas
    from app_Api_Registro_Automotor.apisucerp import automotor_api

except Exception as e:
    print(f'Falta algun modulo {e}')


# Genero una instancia de Flask
app = Flask('__name__')
app.config["DEBUG"] = False

# Registro una ruta
app.register_blueprint(automotor_api)

# Iniciamos el servidor
#if __name__ == '__main__':
#    load_dotenv()
app.run(port=5100)
