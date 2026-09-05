# Defect Report Examples

These are portfolio sample defects. They must be reproduced and confirmed in the actual application before being reported as real production defects.

## BUG-001 — Cart subtotal does not update after quantity change
- Severity: Medium
- Priority: High
- Module: Cart
- Steps: Add a product → open cart → increase quantity.
- Expected: Quantity and subtotal update immediately.
- Actual: Subtotal remains unchanged until refresh.
- Status: Sample / To Verify

## BUG-002 — Invalid email accepted during registration
- Severity: High
- Priority: High
- Module: Registration
- Steps: Open registration → enter malformed email → submit.
- Expected: Email validation blocks submission.
- Actual: Form proceeds without a valid email.
- Status: Sample / To Verify

## BUG-003 — Protected checkout page accessible without authentication
- Severity: Critical
- Priority: Critical
- Module: Authorization
- Steps: Sign out → directly open checkout URL.
- Expected: User is redirected to login.
- Actual: Checkout page is accessible.
- Status: Sample / To Verify

## Defect Workflow
New → Assigned → In Progress → Fixed → Retest → Closed / Reopened
