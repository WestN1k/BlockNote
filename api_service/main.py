import os

from app import create_app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('SERVER_PORT', 5000), debug=os.environ.get('DEBUG', False))
