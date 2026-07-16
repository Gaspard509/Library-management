from source.frameworks.web.flask_app import create_app

if __name__ == "__main__":
    app = create_app()
    print("\n clean architecture LIBRARY-MANAGEMENT-SYSTEM REST API")
    print(" running on http://localhost:5000\n")
    app.run(debug=True)