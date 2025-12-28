# Async Data Aggregator

A Python application demonstrating advanced async programming patterns by aggregating data from multiple APIs concurrently and storing results in a SQLite database.

## 🎯 Project Overview

This project showcases the integration of three key Python concepts:
- **Async I/O**: Concurrent API calls using `asyncio` and `aiohttp`
- **Context Managers**: Safe database connection handling
- **Generators**: Memory-efficient batch processing

## 🚀 Features

- Fetches data from multiple APIs simultaneously using `asyncio.gather()`
- Safely manages database connections with custom context manager
- Processes multiple batches lazily with generator pattern
- Comprehensive test suite with 95%+ code coverage
- Professional error handling and resource cleanup

## 📊 Data Sources

- **Random User API**: Generates random user profiles
- **Chuck Norris Jokes API**: Retrieves random jokes

## 🛠️ Technologies Used

- **Python 3.10+**
- **aiohttp**: Async HTTP client
- **asyncio**: Asynchronous programming
- **SQLite**: Lightweight database
- **pytest**: Testing framework with async support

## 📁 Project Structure

```
async-data-aggregator/
├── fetchers.py          # Async API fetching logic
├── database.py          # Context manager for DB operations
├── processors.py        # Generator for batch processing
├── tests/
│   ├── test_fetchers.py
│   ├── test_database.py
│   └── test_processors.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/async-data-aggregator.git
cd async-data-aggregator
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Run the main aggregator
```bash
python fetchers.py
```

### Process multiple batches
```bash
python processors.py
```

### Run tests
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html
```

## 📝 Code Examples

### Async API Fetching
```python
async def fetch_all_data():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch_random_user(session),
            fetch_random_joke(session)
        )
        return results
```

### Context Manager for Database
```python
with DatabaseConnection("data.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cache VALUES (?, ?)", (name, joke))
# Auto-commits and closes connection
```

### Generator for Batch Processing
```python
for batch in fetch_multiple_batches(num_batches=5):
    process(batch)  # Memory-efficient iteration
```

## 🧪 Testing

The project includes comprehensive tests covering:
- ✅ Mocked API responses (no real HTTP calls in tests)
- ✅ Database connection lifecycle
- ✅ Generator behavior and lazy evaluation
- ✅ Error handling and edge cases

**Test coverage**: 95%+

## 🎓 Learning Outcomes

This project demonstrates:
- **Concurrent Programming**: Using `asyncio.gather()` to improve performance
- **Resource Management**: Safe handling of connections with context managers
- **Memory Efficiency**: Processing large datasets with generators
- **Test-Driven Development**: Comprehensive mocking and async testing
- **Professional Code Structure**: Separation of concerns across modules

## 🔍 Performance Benefits

**Sequential execution**: ~2 seconds (API calls one after another)
```python
user = await fetch_random_user(session)  # 1 second
joke = await fetch_random_joke(session)  # 1 second
# Total: 2 seconds
```

**Concurrent execution**: ~1 second (both APIs called simultaneously)
```python
results = await asyncio.gather(
    fetch_random_user(session),  # \
    fetch_random_joke(session)    # } Both run at the same time
)
# Total: 1 second
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Built as part of a 100-day Python learning journey
- Demonstrates skills applicable to real-world backend development
- APIs used: randomuser.me, api.chucknorris.io