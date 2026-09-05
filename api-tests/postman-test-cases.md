# API Testing Checklist

Use these checks with the target e-commerce REST API.

| API | Method | Checks |
|---|---|---|
| /login | POST | 200/4xx status, token, error validation, response schema |
| /products | GET | 200 status, JSON schema, pagination, response time |
| /products/{id} | GET | Valid ID, invalid ID, 404 handling |
| /cart | POST | Auth, required fields, created item |
| /cart/{id} | DELETE | Auth, deletion confirmation, invalid ID |
| /orders | POST | Auth, required fields, total validation |
| /orders | GET | Auth, response schema, user-specific data |

## Postman Assertions
- Verify status code
- Verify required JSON fields
- Verify data types
- Verify authentication behavior
- Verify invalid input handling
- Verify reasonable response time
- Add collection variables for base URL and token

## Example Test Script
```javascript
pm.test("Status code is successful", function () {
  pm.expect(pm.response.code).to.be.oneOf([200, 201]);
});

pm.test("Response is JSON", function () {
  pm.response.to.be.json;
});
```
