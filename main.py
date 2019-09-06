from app import app

if __name__ == '__main__':
    app.run(host=app.config.get("APP_IP"), port=app.config.get("APP_PORT"), debug=app.config.get("APP_IS_DEBUG"))
