# Example Ralph Loop Prompt

This is a complete, working example of a well-structured Ralph Loop prompt.

## Task: Add User Authentication System

### Objective
Implement a complete user authentication system with login, logout, and session management for a web application.

### Success Criteria
- [ ] Users can register with email and password
- [ ] Users can log in and receive a session token
- [ ] Users can log out and invalidate their session
- [ ] Password hashing is implemented securely (bcrypt)
- [ ] All authentication endpoints have tests
- [ ] Integration tests pass for complete auth flow

### Scope

#### In Scope
✅ User registration endpoint
✅ Login endpoint with JWT token generation
✅ Logout endpoint
✅ Password hashing with bcrypt
✅ Session management
✅ Basic input validation
✅ Unit and integration tests

#### Out of Scope
❌ OAuth/social login
❌ Two-factor authentication
❌ Password reset functionality
❌ Email verification
❌ Role-based access control
❌ Frontend UI components

### Priority

#### P0 (Must Complete)
- User registration with password hashing
- Login with JWT token generation
- Logout functionality
- Basic tests for all endpoints

#### P1 (Important)
- Input validation (email format, password strength)
- Error handling and meaningful error messages
- Integration tests for complete flow

#### P2 (Optional)
- Rate limiting for login attempts
- Logging for security events
- API documentation

### Implementation Steps

1. **Set up authentication infrastructure**
   - Install required packages (bcrypt, jsonwebtoken)
   - Create User model with email and hashed password
   - Set up database schema

2. **Implement registration**
   - Create POST /api/auth/register endpoint
   - Validate email format and password strength
   - Hash password with bcrypt
   - Store user in database

3. **Implement login**
   - Create POST /api/auth/login endpoint
   - Verify email and password
   - Generate JWT token
   - Return token to client

4. **Implement logout**
   - Create POST /api/auth/logout endpoint
   - Invalidate session/token
   - Clear client-side storage

5. **Add tests**
   - Unit tests for password hashing
   - Unit tests for token generation
   - Integration tests for register → login → logout flow

### Validation

#### After Each Iteration
1. **Run tests**: `npm test` or `pytest`
2. **Check code quality**: `npm run lint` or `flake8`
3. **Manual testing**:
   - Register a new user
   - Log in with credentials
   - Verify token is received
   - Log out and verify token is invalidated
4. **Check logs**: Review application logs for errors

#### Success Indicators
- All tests pass (100% of auth tests)
- No security warnings from linter
- Manual test flow works end-to-end
- Code coverage >80% for auth module

### Iteration Phases
- **Phase 1 (iterations 1-2)**: Set up infrastructure, implement registration
- **Phase 2 (iterations 3-4)**: Implement login and logout
- **Phase 3 (iterations 5-6)**: Add tests and validation
- **Phase 4 (iterations 7-8)**: Error handling and edge cases

### Completion Condition
When all success criteria are met and all tests pass, output:
<promise>AUTH_COMPLETE</promise>

Conditions:
- All 6 success criteria checked off
- Test suite passes with >80% coverage
- Manual testing confirms all flows work
- No security vulnerabilities detected

### Execution Command

**Option 1: Using file**
```bash
/ralph-wiggum:ralph-loop "$(cat auth_prompt.md)" --max-iterations 8 --completion-promise "AUTH_COMPLETE"
```

**Option 2: Single-line format**
```bash
/ralph-wiggum:ralph-loop """Task: Add User Authentication System. Objective: Implement complete user authentication with login, logout, and session management. Success Criteria: Users can register with email/password, log in and receive session token, log out and invalidate session, password hashing with bcrypt, all endpoints have tests, integration tests pass. In Scope: registration endpoint, login with JWT, logout, password hashing, session management, validation, tests. Out of Scope: OAuth, 2FA, password reset, email verification, RBAC, frontend UI. Priority P0: registration with hashing, login with JWT, logout, basic tests. P1: validation, error handling, integration tests. P2: rate limiting, logging, docs. Implementation: 1) Set up auth infrastructure 2) Implement registration 3) Implement login 4) Implement logout 5) Add tests. Validation: Run tests, check linting, manual test flow, review logs. Success indicators: all tests pass, no security warnings, manual flow works, coverage >80%. Completion: When all criteria met output <promise>AUTH_COMPLETE</promise>""" --max-iterations 8 --completion-promise "AUTH_COMPLETE"
```

## Why This Prompt Works

### ✅ Clear Goal
"Add User Authentication System" - immediately understandable

### ✅ Testable Success Criteria
Each criterion can be objectively verified:
- "Users can register" → Test by calling registration endpoint
- "All endpoints have tests" → Check test files exist and pass
- "Integration tests pass" → Run test suite

### ✅ Defined Scope
Explicitly states what's included and excluded, preventing scope creep

### ✅ Concrete Validation
Specific commands to run (`npm test`, `npm run lint`) and manual steps to verify

### ✅ Completion Promise
Clear marker (`<promise>AUTH_COMPLETE</promise>`) with specific conditions

### ✅ Reasonable Iterations
8 iterations for a medium-complexity feature is realistic

### ✅ Priority Levels
P0/P1/P2 helps Claude focus on what matters most

## Common Mistakes to Avoid

❌ **Vague**: "Make authentication better"
✅ **Specific**: "Implement registration, login, and logout with JWT"

❌ **No validation**: "Check if it works"
✅ **Concrete**: "Run `npm test`, manual test: register → login → logout"

❌ **Subjective**: "Make it secure"
✅ **Measurable**: "Use bcrypt for password hashing, no security warnings from linter"

❌ **Too broad**: "Build entire auth system with OAuth, 2FA, roles, etc."
✅ **Focused**: "Basic auth only, OAuth out of scope"

## Adapting This Template

To use this for your own task:

1. **Change the task**: Replace "User Authentication" with your feature
2. **Update success criteria**: What can you test to verify it works?
3. **Define scope**: What's in and out?
4. **Set validation**: What commands will you run?
5. **Choose promise**: Pick a meaningful completion marker
6. **Estimate iterations**: Simple=5, Medium=10, Complex=20

## Next Steps

1. Save this as `my_prompt.md`
2. Customize for your task
3. Run: `/ralph-wiggum:ralph-loop "$(cat my_prompt.md)" --max-iterations N --completion-promise "YOUR_PROMISE"`
4. Watch Claude iterate and improve!
