# Code Review Checklist

## File under review: course.py

### 1. Code Readability
- [ ] Variable names are meaningful
- [ ] Function names describe actions
- [ ] Code is easy to understand without comments

### 2. Style Compliance (PEP 8)
- [ ] 4 spaces indentation
- [ ] 2 blank lines between classes
- [ ] 1 blank line between methods
- [ ] Line length up to 79 characters

### 3. No Code Duplication
- [ ] No repeated code
- [ ] Common logic extracted to methods

### 4. No Magic Numbers
- [ ] Numbers replaced with constants
- [ ] Clear boundary values (0, 100)

### 5. No Commented Code
- [ ] No old code in comments
- [ ] Only relevant comments

## Found Issues:

1. **Missing docstrings** for classes and methods
2. **Magic numbers**: 0 and 100 in update_progress method
3. **No type validation**: can pass non-Student to add_student

## Improvement Suggestions:

1. Add docstrings
2. Create MIN_PROGRESS and MAX_PROGRESS constants
3. Add type checking

