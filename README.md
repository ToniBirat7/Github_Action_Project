# First GitHub Actions Project 🚀

A beginner-friendly "Hello World" project demonstrating GitHub Actions CI/CD pipeline implementation with Python. This project serves as a practical learning resource for understanding continuous integration and deployment workflows.

## 🎯 Project Overview

This project is designed to teach the fundamentals of GitHub Actions through a simple Python application with automated testing, linting, and deployment workflows. It's part of a larger ETL pipeline learning journey and serves as a submodule for understanding CI/CD concepts.

## 📁 Project Structure

```
First_Github_Action_Project/
├── .github/
│   └── workflows/
│       ├── ci.yml                 # Main CI/CD pipeline
│       ├── code-quality.yml       # Code quality checks
│       └── release.yml            # Release automation
├── src/
│   ├── __init__.py
│   ├── math_operations.py         # Core Python functions
│   └── utils.py                   # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_math_operations.py    # Unit tests
│   └── test_integration.py        # Integration tests
├── requirements.txt               # Python dependencies
├── requirements-dev.txt           # Development dependencies
├── .gitignore                     # Git ignore rules
├── Dockerfile                     # Container configuration
├── docker-compose.yml             # Multi-service setup
└── README.md                      # This file
```

## 🛠️ Technologies Used

- **Python 3.9+**: Core programming language
- **GitHub Actions**: CI/CD automation
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Type checking
- **Docker**: Containerization
- **Poetry/pip**: Dependency management

## 🚀 Features

### Core Functionality

- ✅ Basic mathematical operations (add, subtract, multiply, divide)
- ✅ Error handling and input validation
- ✅ Type hints for better code quality
- ✅ Comprehensive unit tests

### CI/CD Pipeline Features

- 🔄 **Automated Testing**: Run tests on every push and pull request
- 📝 **Code Quality**: Automated linting and formatting checks
- 🐳 **Docker Support**: Containerized application deployment
- 📦 **Multi-Platform**: Test across different Python versions and OS
- 🏷️ **Automated Releases**: Version tagging and release notes
- 📊 **Coverage Reports**: Test coverage tracking
- 🔒 **Security Scanning**: Dependency vulnerability checks

## 🔧 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- Git
- Docker (optional)

### Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/First_Github_Action_Project.git
   cd First_Github_Action_Project
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Run tests**

   ```bash
   pytest tests/ -v --cov=src
   ```

5. **Run the application**
   ```bash
   python -m src.math_operations
   ```

### Docker Setup

1. **Build and run with Docker**

   ```bash
   docker build -t github-actions-demo .
   docker run -it github-actions-demo
   ```

2. **Use Docker Compose**
   ```bash
   docker-compose up --build
   ```

## 🧪 Testing

### Running Tests Locally

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_math_operations.py -v

# Run with different verbosity
pytest -v -s
```

### Test Structure

- **Unit Tests**: Test individual functions in isolation
- **Integration Tests**: Test component interactions
- **Coverage Reports**: Ensure >90% code coverage
- **Performance Tests**: Basic performance benchmarks

## 📋 GitHub Actions Workflows

### 1. CI Pipeline (`.github/workflows/ci.yml`)

Triggered on every push and pull request:

- ✅ Code checkout
- 🐍 Python environment setup (multiple versions)
- 📦 Dependencies installation
- 🧪 Test execution
- 📊 Coverage reporting
- 🔍 Code quality checks

### 2. Code Quality (`.github/workflows/code-quality.yml`)

Automated code quality enforcement:

- 🎨 **Black**: Code formatting
- 📝 **Flake8**: PEP8 compliance
- 🔍 **MyPy**: Type checking
- 🔒 **Bandit**: Security scanning
- 📋 **isort**: Import sorting

### 3. Release Pipeline (`.github/workflows/release.yml`)

Automated release management:

- 🏷️ Version tagging
- 📝 Release notes generation
- 🐳 Docker image building
- 📦 Package publishing
- 🚀 Deployment automation

## 📚 Learning Objectives

This project teaches:

1. **GitHub Actions Fundamentals**

   - Workflow syntax and structure
   - Triggers and events
   - Jobs and steps configuration
   - Environment variables and secrets

2. **CI/CD Best Practices**

   - Automated testing strategies
   - Code quality enforcement
   - Multi-environment deployments
   - Security considerations

3. **Python Development Workflow**

   - Testing with pytest
   - Code formatting and linting
   - Type checking with mypy
   - Dependency management

4. **DevOps Concepts**
   - Containerization with Docker
   - Infrastructure as Code
   - Monitoring and alerting
   - Release management

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Run tests and quality checks**
   ```bash
   pytest
   black src/ tests/
   flake8 src/ tests/
   mypy src/
   ```
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

## 📈 Workflow Examples

### Basic CI Workflow

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.9, 3.10, 3.11]
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Run tests
        run: pytest --cov=src
```

### Code Quality Workflow

```yaml
name: Code Quality
on: [push, pull_request]
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install black flake8 mypy
      - name: Run Black
        run: black --check src/ tests/
      - name: Run Flake8
        run: flake8 src/ tests/
      - name: Run MyPy
        run: mypy src/
```

## 🔗 Related Projects

This project is part of a larger learning ecosystem:

- **[Airflow ETL Pipeline](../Airflow_ETL_Pipeline_Astro_Postgres)**: Main ETL pipeline with NASA APOD API
- **[Airflow Practice](../Airflow_Practice)**: Basic Airflow DAG examples
- **[ML Flow Complete](../)**: Complete machine learning and data engineering journey

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- GitHub Actions documentation and community
- Python testing best practices
- CI/CD pipeline design patterns
- Open source contributors and maintainers

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/First_Github_Action_Project/issues) page
2. Create a new issue with detailed information
3. Refer to the GitHub Actions documentation
4. Join the discussion in our learning community

---

**Happy Learning! 🎉**

_This project is designed for educational purposes and serves as a stepping stone to more complex CI/CD implementations._
