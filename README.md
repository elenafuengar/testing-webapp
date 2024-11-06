# testing-webapp

Trying to deply a simple web application using python and Okd (Kubernetes)

### Worktree provided by ChatGPT
```
lab-inventory-app/
│
├── app/                     # Main application folder
│   ├── __init__.py          # Initialize Flask app and load configurations
│   ├── inventory_model.py   # Database models (SQLAlchemy classes)
│   ├── routes.py            # Flask route definitions for API endpoints
│   ├── templates/           # HTML files (frontend)
│   │   └── inventory.html   # Main inventory page
│   └── static/              # Static files (CSS, JS, images)
│       ├── style.css        # CSS file for styling
│       └── app.js           # JavaScript file for frontend logic
│
├── migrations/              # Database migration files (if using Flask-Migrate)
│
├── tests/                   # Tests for your application
│   └── test_inventory.py    # Unit tests for inventory routes and logic
│
├── .flaskenv                # Flask environment variables for local development
├── Dockerfile               # Docker configuration file
├── requirements.txt         # Python dependencies
├── config.py                # Configuration settings for different environments
├── app.py                   # Entry point to run the Flask app
├── deployment.yaml          # Kubernetes deployment and service configuration
└── README.md                # Project documentation
```