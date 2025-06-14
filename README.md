# Python Flask and Tailwind CSS Starter Template

A streamlined starter template for building web applications using Python Flask and Tailwind CSS.

## Prerequisites
- Python 3.x
- Node.js and npm

## Setup Instructions

### 1. Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd flask-tailwind-starter
```

Install Tailwind CSS and its dependencies:

```bash
npm install -D tailwindcss@3 postcss autoprefixer
```
> The `-D` flag installs the packages as development dependencies, which won't be included in the production build.

Create the Tailwind CSS configuration files:

```bash
npx tailwindcss init -p
```
> This command creates two files: `tailwind.config.js` and `postcss.config.js`.

### 2. Tailwind Configuration

The template includes pre-configured Tailwind files:

**tailwind.config.js**:
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
> This configuration tells Tailwind CSS where to look for class names in your Flask templates and JavaScript files.

**postcss.config.js** sets up PostCSS to use Tailwind CSS and Autoprefixer:
> PostCSS is a tool that processes CSS using JavaScript plugins, transforming your raw CSS into production-ready CSS.

**static/src/styles.css** includes the necessary Tailwind directives:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

> Here's what each directive does:
> - `@tailwind base`: Resets and normalizes styles (like `normalize.css`)
> - `@tailwind components`: Injects pre-built component classes
> - `@tailwind utilities`: Loads all the utility classes (like `p-4`, `text-center`, etc.)

### 3. Flask Setup

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

Install Flask and dependencies:

```bash
pip install Flask
pip freeze > requirements.txt
```
> The requirements.txt file helps track dependencies, making it easy to reinstall them in a new environment.

### 4. Building and Running

Build the CSS file:

```bash
npx tailwindcss -i ./static/src/styles.css -o ./static/dist/styles.css --watch
```
> The `--watch` flag keeps the process running, automatically compiling changes to your CSS.

Run the Flask application:

```bash
flask run
```

The application will be available at `http://localhost:5000`.

## Project Structure

```
flask-tailwind-starter/
├── app.py                 # Flask application
├── static/
│   ├── dist/
│   │   └── styles.css     # Generated Tailwind CSS
│   └── src/
│       └── styles.css     # Source CSS with Tailwind directives
├── templates/
│   ├── base.html         # Base template
│   └── index.html        # Home page template
├── tailwind.config.js    # Tailwind configuration
├── postcss.config.js     # PostCSS configuration
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file
└── README.md
```

## Version Control

The template includes a `.gitignore` file configured for Python, Flask, and Node.js projects. This helps keep your repository clean by excluding:

- Python cache files and virtual environments
- Node.js dependencies (node_modules)
- Generated CSS files
- Environment variables and local settings
- IDE/editor specific files
- Database files

## Contributing

Feel free to open issues or submit pull requests with improvements or bug fixes!