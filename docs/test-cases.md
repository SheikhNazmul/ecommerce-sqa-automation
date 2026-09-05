# Test Cases

| ID | Module | Scenario | Expected Result | Priority |
|---|---|---|---|---|
| TC-001 | Auth | Register with valid data | Account is created | High |
| TC-002 | Auth | Register with existing email | Duplicate-email validation appears | High |
| TC-003 | Auth | Register with missing required field | Field validation appears | High |
| TC-004 | Auth | Login with valid credentials | User reaches account/dashboard | Critical |
| TC-005 | Auth | Login with invalid password | Error message appears | High |
| TC-006 | Auth | Login with blank fields | Validation appears | Medium |
| TC-007 | Auth | Logout | Session ends | High |
| TC-008 | Search | Search existing product | Relevant products appear | High |
| TC-009 | Search | Search unknown product | Empty-state message appears | Medium |
| TC-010 | Search | Apply category filter | Matching products only | High |
| TC-011 | Product | Open product details | Correct details are shown | High |
| TC-012 | Product | Select unavailable variant | Unavailable state is shown | Medium |
| TC-013 | Cart | Add product | Product appears in cart | Critical |
| TC-014 | Cart | Increase quantity | Quantity and subtotal update | High |
| TC-015 | Cart | Decrease quantity | Quantity and subtotal update | High |
| TC-016 | Cart | Remove product | Product is removed | High |
| TC-017 | Cart | Cart persists after refresh | Items remain when expected | Medium |
| TC-018 | Checkout | Checkout with valid address | Order review opens | Critical |
| TC-019 | Checkout | Missing address | Validation prevents checkout | High |
| TC-020 | Checkout | Empty cart checkout | Checkout is blocked | High |
| TC-021 | Order | Place valid order | Order confirmation appears | Critical |
| TC-022 | Order | Verify order history | New order is listed | High |
| TC-023 | Regression | Login after logout | Login still works | High |
| TC-024 | Regression | Search after cart update | Search remains functional | Medium |
| TC-025 | Regression | Refresh checkout | State behaves correctly | Medium |
| TC-026 | Negative | Invalid email format | Validation appears | Medium |
| TC-027 | Negative | Extremely long input | Input is safely handled | Medium |
| TC-028 | Negative | Invalid quantity | Invalid value is rejected | High |
| TC-029 | Negative | Direct access to protected page | Unauthorized user is redirected | Critical |
| TC-030 | Smoke | Homepage loads | Page loads without blocking error | Critical |

## Execution Status
Initial portfolio test design. Status should be updated to Pass/Fail/Blocked after execution against a real test environment.
