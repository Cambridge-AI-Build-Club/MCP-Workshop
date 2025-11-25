# Common Anti-Patterns by Language

## Python

### Resource Management
```python
# Bad: Resource leak
file = open("data.txt")
content = file.read()
# file never closed

# Good: Context manager
with open("data.txt") as file:
    content = file.read()
```

### Mutable Default Arguments
```python
# Bad: Shared mutable state
def add_item(item, items=[]):
    items.append(item)
    return items

# Good: None default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Exception Handling
```python
# Bad: Bare except
try:
    risky_operation()
except:
    pass

# Good: Specific exceptions
try:
    risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise
```

## JavaScript/TypeScript

### Equality Checks
```javascript
// Bad: Type coercion
if (value == null) { }
if (value == '') { }

// Good: Strict equality
if (value === null || value === undefined) { }
if (value === '') { }
```

### Async/Await Errors
```javascript
// Bad: Unhandled promise
async function getData() {
    const data = await fetch(url);
    return data.json();
}

// Good: Error handling
async function getData() {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Fetch failed:', error);
        throw error;
    }
}
```

### Memory Leaks
```javascript
// Bad: Event listener leak
element.addEventListener('click', handler);
// Never removed

// Good: Cleanup
const handler = () => { /* ... */ };
element.addEventListener('click', handler);
// Later:
element.removeEventListener('click', handler);
```

## Java

### Resource Management
```java
// Bad: Resource leak
InputStream stream = new FileInputStream("file.txt");
// stream never closed

// Good: Try-with-resources
try (InputStream stream = new FileInputStream("file.txt")) {
    // use stream
}
```

### Null Handling
```java
// Bad: NPE risk
String value = map.get(key).toString();

// Good: Null check or Optional
String value = Optional.ofNullable(map.get(key))
    .map(Object::toString)
    .orElse("");
```

## Go

### Error Handling
```go
// Bad: Ignored error
result, _ := riskyOperation()

// Good: Handle errors
result, err := riskyOperation()
if err != nil {
    return fmt.Errorf("operation failed: %w", err)
}
```

### Goroutine Leaks
```go
// Bad: Unbounded goroutine
for item := range items {
    go process(item) // No control
}

// Good: Worker pool
sem := make(chan struct{}, maxWorkers)
for item := range items {
    sem <- struct{}{}
    go func(item Item) {
        defer func() { <-sem }()
        process(item)
    }(item)
}
```

## General Anti-Patterns

| Pattern | Problem | Solution |
|---------|---------|----------|
| Magic numbers | Hard to understand | Named constants |
| Deep nesting | Hard to follow | Early returns |
| God functions | Too many responsibilities | Extract methods |
| Copy-paste | Maintenance burden | DRY principle |
| No validation | Security/stability risk | Validate inputs |
