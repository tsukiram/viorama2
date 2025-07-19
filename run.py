# run.py
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Railway biasanya pakai 8080
    app.run(host='0.0.0.0', port=port, debug=os.environ.get("FLASK_DEBUG") == "1")
