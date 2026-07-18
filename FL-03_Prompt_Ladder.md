# FL-03: Prompt Ladder & Iteration
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 3)  
**Date:** July 18, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Introduction

This prompt ladder documents the iterative improvement of an AI prompt to write a backend Express.js route handler for the **Farmer Trade System** (a digital marketplace). Each iteration adds exactly **one layer** of context, constraints, or formatting. By isolating each change, we determine which specific prompt engineering ingredients yield a better code output.

---

## 2. The Prompt Ladder

### Baseline Prompt: The Weak Draft
> **Prompt**: *"Help me write a backend API endpoint for my farmer marketplace app."*

#### Representative Output Excerpt
```javascript
const express = require('express');
const app = express();
app.use(express.json());

// In-memory products array
let products = [
  { id: 1, name: 'Apples', price: 2.5 }
];

app.get('/products', (req, res) => {
  res.json(products);
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

#### Iteration Notes (Baseline)
* **What changed in the prompt**: N/A (Initial baseline).
* **What actually improved in the output**: N/A.
* **What still failed**: The output is generic. It assumes a `GET /products` endpoint using dummy in-memory variables. It lacks a database connection, authentication, input validation, and business logic.
* **What to try next**: Define a clear, concrete goal for the endpoint (creating a trade record).

---

### Version 1: Adding a Clearer Goal (Layer 1)
> **Prompt**: *"Help me write a backend Express.js POST endpoint at `/api/trades` to create a new agricultural trade transaction in the database."*

#### Representative Output Excerpt
```javascript
const express = require('express');
const router = express.Router();
const { Trade } = require('../models'); // Sequelize model assumption

router.post('/api/trades', async (req, res) => {
  try {
    const newTrade = await Trade.create(req.body);
    return res.status(201).json(newTrade);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

module.exports = router;
```

#### Iteration Notes (Version 1)
* **What changed in the prompt**: Added a specific HTTP method (`POST`), endpoint path (`/api/trades`), and goal (creating a new trade database entry).
* **What actually improved in the output**: The handler structure correctly shifted from a generic mockup to a database write operation that parses request bodies.
* **What still failed**: The model assumed a Sequelize ORM and a generic database structure, which does not match our specific Node.js stack. There is also zero input validation.
* **What to try next**: Add real database context (SQLite/raw SQL) to align with our project stack.

---

### Version 2: Adding Real Context (Layer 2)
> **Prompt**: *"Help me write a backend Express.js POST endpoint at `/api/trades` to create a new agricultural trade transaction. We are using Node.js and raw SQL queries (using the `sqlite3` library). The database schema has a `trades` table with columns: `id`, `product_id`, `buyer_id`, `seller_id`, `quantity`, `price`, `status`, and `created_at`."*

#### Representative Output Excerpt
```javascript
const express = require('express');
const router = express.Router();
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./database.db');

router.post('/api/trades', (req, res) => {
  const { product_id, buyer_id, seller_id, quantity, price } = req.body;
  const sql = `INSERT INTO trades (product_id, buyer_id, seller_id, quantity, price, status, created_at) 
               VALUES (?, ?, ?, ?, ?, 'pending', datetime('now'))`;

  db.run(sql, [product_id, buyer_id, seller_id, quantity, price], function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    res.status(201).json({ id: this.lastID, message: 'Trade created successfully' });
  });
});

module.exports = router;
```

#### Iteration Notes (Version 2)
* **What changed in the prompt**: Specified the database dialect (SQLite), library (`sqlite3`), and the database schema fields.
* **What actually improved in the output**: The database interaction code updated to use raw SQL syntax and `db.run` parameters, matching our technical stack.
* **What still failed**: It accepts any user input. Empty values, negative quantities, or strings instead of prices will cause database corruption or runtime issues.
* **What to try next**: Enforce input validation constraints on quantity and price.

---

### Version 3: Adding Constraints (Layer 3)
> **Prompt**: *"Help me write a backend Express.js POST endpoint at `/api/trades` to create a new agricultural trade transaction. We are using Node.js and raw SQL queries (using the `sqlite3` library). The database schema has a `trades` table with columns: `id`, `product_id`, `buyer_id`, `seller_id`, `quantity`, `price`, `status`, and `created_at`.  
> **Constraints**:  
> 1. All input fields must be validated: `product_id`, `buyer_id`, `seller_id`, `quantity`, and `price` are required.  
> 2. `quantity` must be a positive integer > 0.  
> 3. `price` must be a positive float > 0.0.  
> 4. If validation fails, return a 400 Bad Request with a JSON array of errors."*

#### Representative Output Excerpt
```javascript
router.post('/api/trades', (req, res) => {
  const { product_id, buyer_id, seller_id, quantity, price } = req.body;
  const errors = [];

  if (!product_id) errors.push('product_id is required');
  if (!buyer_id) errors.push('buyer_id is required');
  if (!seller_id) errors.push('seller_id is required');
  if (quantity === undefined || !Number.isInteger(quantity) || quantity <= 0) {
    errors.push('quantity must be a positive integer > 0');
  }
  if (price === undefined || typeof price !== 'number' || price <= 0.0) {
    errors.push('price must be a positive float > 0.0');
  }

  if (errors.length > 0) {
    return res.status(400).json({ errors });
  }

  // Database insert logic follows...
```

#### Iteration Notes (Version 3)
* **What changed in the prompt**: Specified validation logic constraints (types, ranges, null-checks) and error response structure (400 Bad Request with a list of errors).
* **What actually improved in the output**: The handler now blocks invalid writes (e.g., negative prices or text quantities), protecting database integrity.
* **What still failed**:  
  > [!CAUTION]
  > **This made the code layout worse.** Adding raw logic constraints without structure resulted in a single, monolithic, 60-line controller file. The validation code is tightly coupled with database code, making it difficult to read and test.
* **What to try next**: Define a strict output format to enforce modularity and separate validation from execution logic.

---

### Version 4: Specifying Output Format (Layer 4)
> **Prompt**: *"Help me write a backend Express.js POST endpoint at `/api/trades` to create a new agricultural trade transaction. We are using Node.js and raw SQL queries (using the `sqlite3` library). The database schema has a `trades` table with columns: `id`, `product_id`, `buyer_id`, `seller_id`, `quantity`, `price`, `status`, and `created_at`.  
> **Constraints**:  
> 1. All input fields must be validated: `product_id`, `buyer_id`, `seller_id`, `quantity`, and `price` are required.  
> 2. `quantity` must be a positive integer > 0.  
> 3. `price` must be a positive float > 0.0.  
> 4. If validation fails, return a 400 Bad Request with a JSON array of errors.  
> **Output Format**:  
> Provide the code divided into two separate files:  
> 1. `validators.js`: Contains a reusable validation function `validateTradeInput(req, res, next)` behaving as Express middleware.  
> 2. `tradeController.js`: Contains the route handler function `createTrade` that assumes validation has already passed and focuses on the database transaction."*

#### Representative Output Excerpt
```javascript
// validators.js
exports.validateTradeInput = (req, res, next) => {
  const { product_id, buyer_id, seller_id, quantity, price } = req.body;
  const errors = [];
  // validation logic checks...
  if (errors.length > 0) return res.status(400).json({ errors });
  next();
};

// tradeController.js
const db = require('./db');
exports.createTrade = (req, res) => {
  const { product_id, buyer_id, seller_id, quantity, price } = req.body;
  // SQLite INSERT statement...
};
```

#### Iteration Notes (Version 4)
* **What changed in the prompt**: Commanded a modular file separation output format, establishing a clear line of division between validation middleware and controller routes.
* **What actually improved in the output**: The codebase layout is now organized. Route handling is clean because request checking is isolated in a middleware script.
* **What still failed**: There is no automated verification. We cannot prove that the database transaction error path handles errors (like db locked or constraints) correctly.
* **What to try next**: Stating verification requirements (unit tests) to cover test paths.

---

### Version 5: Adding Verification Requirements & Quality Criteria (Layer 5)
> **Prompt**: *"Help me write a backend Express.js POST endpoint at `/api/trades` to create a new agricultural trade transaction. We are using Node.js and raw SQL queries (using the `sqlite3` library). The database schema has a `trades` table with columns: `id`, `product_id`, `buyer_id`, `seller_id`, `quantity`, `price`, `status`, and `created_at`.  
> **Constraints**:  
> 1. All input fields must be validated: `product_id`, `buyer_id`, `seller_id`, `quantity`, and `price` are required.  
> 2. `quantity` must be a positive integer > 0.  
> 3. `price` must be a positive float > 0.0.  
> 4. If validation fails, return a 400 Bad Request with a JSON array of errors.  
> **Output Format**:  
> Provide the code divided into two separate files:  
> 1. `validators.js`: Contains a reusable validation function `validateTradeInput(req, res, next)` behaving as Express middleware.  
> 2. `tradeController.js`: Contains the route handler function `createTrade` that assumes validation has already passed and focuses on the database transaction.  
> **Verification Requirements**:  
> Include a third file `tradeController.test.js` using Jest containing two unit tests:  
> 1. A test verifying the happy path (successful insertion, returning 201 Created and the created trade object, asserting mock sqlite response).  
> 2. A test verifying error handling if the database query fails (returning 500 Internal Server Error)."*

#### Representative Output Excerpt
```javascript
// tradeController.test.js
const { createTrade } = require('./tradeController');
const db = require('./db');
jest.mock('./db');

describe('createTrade Controller', () => {
  it('should return 201 and the new trade details on success', () => {
    db.run.mockImplementation((sql, params, callback) => callback.call({ lastID: 42 }, null));
    // Test execution and asserts...
  });
  
  it('should return 500 if database query fails', () => {
    db.run.mockImplementation((sql, params, callback) => callback(new Error('DB Error')));
    // Test execution and asserts...
  });
});
```

#### Iteration Notes (Version 5)
* **What changed in the prompt**: Added strict verification parameters (Jest unit tests for both happy and database error paths).
* **What actually improved in the output**: The generated code now features comprehensive database mocks. The tests explicitly cover the error handling branch, ensuring the 500 error catch block has test coverage.
* **What still failed**: N/A (The output is production-ready, modular, and fully tested).
* **What to try next**: Clean up this prompt into a reusable template for any endpoint.

---

## 3. Final Reusable Prompt

This final, cleaned prompt can be used by any developer to build robust, modular, and fully tested Node.js API endpoints:

```markdown
You are a senior full-stack engineer. Build a modular backend Express.js route handler.

# Technology Stack
- Node.js, Express.js
- Database: SQLite (using raw SQL statements with the `sqlite3` library)

# Target Endpoint
- Route: POST `/api/trades`
- Goal: Create a new trade record in the `trades` table.
- Database Columns: `id`, `product_id`, `buyer_id`, `seller_id`, `quantity`, `price`, `status` (default: 'pending'), `created_at` (default: current timestamp).

# Input Validation Constraints
Verify the request body before running any query:
1. `product_id` (string), `buyer_id` (string), and `seller_id` (string) are required and must not be empty.
2. `quantity` (integer) is required and must be greater than 0.
3. `price` (float) is required and must be greater than 0.00.
4. If validation fails, return 400 Bad Request with a JSON body: `{ "errors": ["description of failure"] }`.

# Architecture Output Format
Organize the code into three files:
1. `validators.js`: An Express middleware function `validateTradeInput` that validates constraints and sends a 400 response if invalid.
2. `tradeController.js`: A controller function `createTrade` that performs the SQLite `INSERT` query. It assumes data is valid, and catches database errors (returning a 500 response).
3. `tradeController.test.js`: Jest unit tests with mocked database connections testing:
   - Happy path: returns 201 Created and the new trade ID.
   - Error path: database write failure returns 500 Internal Server Error.
```

---
*End of Report*
