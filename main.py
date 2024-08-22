# when starting the web server

from website import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)

# 1:56:00