# Corrected Requirements - Online Learning System

## Functional Requirements (Updated)

### FR1: Course Management
- FR1.1: Admin can create new courses with title, description, and lesson count
- FR1.2: Admin can edit existing course information
- FR1.3: Admin can delete courses (only if no students enrolled)
- FR1.4: System displays list of all available courses with enrollment count

### FR2: Student Management
- FR2.1: Students can register with email, password, and full name
- FR2.2: Students can enroll in unlimited courses
- FR2.3: Students can view their enrolled courses with progress
- FR2.4: Students can unenroll from courses (progress will be lost)

### FR3: Progress Tracking
- FR3.1: System automatically calculates progress using formula:
  - Progress = (Completed Lessons / Total Lessons) × 70% + (Best Test Score / 100) × 30%
- FR3.2: Students can view their current progress (read-only)
- FR3.3: Progress is displayed as percentage (0-100%)
- FR3.4: Progress updates in real-time after lesson completion or test submission

### FR4: Testing and Assessment
- FR4.1: Each course has one final test
- FR4.2: Students can take tests maximum 3 times
- FR4.3: 24-hour cooldown between test attempts
- FR4.4: Best score counts toward progress
- FR4.5: Test results are displayed immediately after submission

### FR5: Authentication (NEW)
- FR5.1: Users must login with email and password
- FR5.2: Password must be minimum 8 characters
- FR5.3: System provides password recovery via email
- FR5.4: Session expires after 24 hours of inactivity
- FR5.5: Users can logout manually

## Non-Functional Requirements (Updated)

### NFR1: Platform
- NFR1.1: System must work on modern web browsers (Chrome 90+, Firefox 88+, Safari 14+)
- NFR1.2: System must be responsive for devices 320px width and above
- NFR1.3: Backend must use Python 3.10+ with Flask/Django

### NFR2: Performance
- NFR2.1: Page load time must not exceed 3 seconds on 3G connection
- NFR2.2: Phase 1: Support 100 concurrent users (current)
- NFR2.3: Phase 2: Scale to 500 concurrent users (6 months)
- NFR2.4: Phase 3: Support 1000 concurrent users (12 months)
- NFR2.5: Database queries must complete within 1 second

### NFR3: Security
- NFR3.1: Passwords must be hashed using bcrypt
- NFR3.2: HTTPS must be used for all connections
- NFR3.3: Student data must comply with GDPR
- NFR3.4: Only authenticated admins can modify course content
- NFR3.5: SQL injection protection must be implemented

### NFR4: Usability
- NFR4.1: Interface must follow Material Design guidelines
- NFR4.2: Error messages must be clear and actionable
- NFR4.3: Maximum 3 clicks to reach any feature
- NFR4.4: System must provide tooltips for complex features

---

## Changes Summary

### Added:
- FR5: Complete authentication requirements
- Progress calculation formula
- Test attempt limits and cooldown
- Specific browser versions
- Phased performance targets
- Security standards (bcrypt, HTTPS, GDPR)

### Modified:
- FR1.3: Added condition for course deletion
- FR1.4: Added enrollment count display
- FR2.4: Added unenrollment option
- FR3.1: Defined exact progress formula
- FR4.2: Limited test attempts to 3
- NFR2.1: Adjusted page load time to realistic 3 seconds
- NFR2.2-2.4: Split into phased targets

### Removed:
- Ambiguous "automatic" progress updates without definition
- Unrealistic single-phase 1000 user target

---

## Validation Result:  PASSED

All requirements are now:
- Complete (all scenarios covered)
- Clear (no ambiguities)
- Consistent (no contradictions)
- Feasible (realistic targets)
