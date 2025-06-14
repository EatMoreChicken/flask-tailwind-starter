from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    features = [
        {
            "title": "Flask + Tailwind Integration",
            "description": "Seamlessly combine Python's Flask framework with Tailwind's utility-first CSS."
        },
        {
            "title": "Responsive Design",
            "description": "Fully responsive layouts that work beautifully on any device or screen size."
        },
        {
            "title": "Modern Development",
            "description": "Hot reloading, on-demand CSS generation, and a streamlined development workflow."
        },
        {
            "title": "Production Ready",
            "description": "Optimized build process that minimizes CSS size for production deployment."
        }
    ]
    
    return render_template('index.html', features=features)

if __name__ == '__main__':
    app.run(debug=True)
