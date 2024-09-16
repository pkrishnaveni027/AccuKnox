# Django Signals and Custom Classes in Python

## 1. Django Signals Example

This project contains a demonstration of how Django signals work, including:

- Synchronous signal execution
- Running signals in the same thread as the caller
- Running signals within the same database transaction

### Files
- `signals/signal_handlers.py`: Contains signal handler implementations.

### Usage
Ensure that `Django` is installed and set up in your project. Then you can test signal execution by triggering model events (e.g., `post_save` signal from `MyModel`).

---

## 2. Custom Rectangle Class

This project includes a custom `Rectangle` class that:
- Requires `length` and `width` attributes.
- Can be iterated over, returning a dictionary with length and width.

### Files
- `rectangle_example/rectangle.py`: Contains the `Rectangle` class implementation.

### Usage
You can run the `rectangle.py` file to see the iteration output:
```bash
python rectangle_example/rectangle.py
