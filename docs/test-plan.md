# Test Plan

## Objective
Verify that critical e-commerce workflows behave correctly, consistently, and safely before release.

## In Scope
- Registration, login and logout
- Product search/filtering
- Product details
- Cart operations
- Checkout and order placement
- REST API validation
- UI regression automation

## Out of Scope
- Production payment processing with real money
- Load/stress testing
- Security penetration testing

## Test Types
- Functional testing
- Smoke testing
- Regression testing
- Negative testing
- API testing
- UI automation

## Entry Criteria
- Test environment is accessible
- Build is deployable
- Test data is available
- Major blocking defects are resolved

## Exit Criteria
- Critical workflows pass
- No open blocker/critical defects
- Regression suite completes successfully
- Test report is prepared

## Risks
- Environment instability
- Changing UI selectors
- Third-party API availability
- Incomplete test data

## Deliverables
Test cases, defect reports, execution report, API test documentation, automation suite, and CI configuration.
