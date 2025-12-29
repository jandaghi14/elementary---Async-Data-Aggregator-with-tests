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
- Comprehensive error handling (timeouts, network errors, API failures)
- Full test suite with mocked API responses
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
- **aioresponses**: For mocking async HTTP requests in tests

## 📁 Project Structure

```
async-data-aggregator/
├── fetchers.py          # Async API fetching logic
├── database.py          # Context manager for DB operations
├── processor.py         # Generator for batch processing
├── tests/
│   ├── test_fetchers.py
│   ├── test_database.py
│   └── test_processor.py
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
python processor.py
```

### Run tests
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_fetchers.py -v
```

## 📝 Code Examples

### Async API Fetching with Error Handling
```python
async def fetch_random_user(session, timeout=10):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
            if response.status != 200:
                return None
            data = await response.json()
            return data
    except asyncio.TimeoutError:
        print(f"Timeout: API took longer than {timeout} seconds")
        return None
    except aiohttp.ClientError as e:
        print(f"Network error: {e}")
        return None
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

## ⚠️ Error Handling

The application handles:
- **Network timeouts**: Default 10 seconds per request
- **API errors**: Non-200 status codes (404, 500, etc.)
- **Connection failures**: Network unavailability
- **Invalid responses**: Malformed API data
- **Database errors**: Connection and transaction failures

All errors are logged and handled gracefully without crashing the application.

## 🧪 Testing

The project includes comprehensive tests covering:
- ✅ Successful API responses with mocked data
- ✅ Timeout scenarios
- ✅ Bad status codes (404, 500)
- ✅ Network errors
- ✅ Database connection lifecycle
- ✅ Generator behavior and lazy evaluation
- ✅ Edge cases and error conditions

**Total tests**: 9+ covering all critical paths

## 🎓 Learning Outcomes

This project demonstrates:
- **Concurrent Programming**: Using `asyncio.gather()` to improve performance
- **Resource Management**: Safe handling of connections with context managers
- **Memory Efficiency**: Processing large datasets with generators
- **Error Handling**: Robust timeout and exception handling
- **Test-Driven Development**: Comprehensive mocking and async testing
- **Professional Code Structure**: Separation of concerns across modules

## 🔍 Performance Benefits

**Sequential execution**: APIs called one after another
```python
user = await fetch_random_user(session)
joke = await fetch_random_joke(session)
# Both wait for each other
```

**Concurrent execution**: Both APIs called simultaneously
```python
results = await asyncio.gather(
    fetch_random_user(session),
    fetch_random_joke(session)
)
# Both run at the same time - faster!
```

Concurrent execution significantly reduces total wait time when fetching from multiple APIs.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Built as part of a 180-day Python learning journey (Day 66-67)
- Demonstrates skills applicable to real-world backend development
- APIs used: randomuser.me, api.chucknorris.io