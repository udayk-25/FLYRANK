# FL-03: Prompt Engineering & Iteration Log
**Track:** General AI Fluency  
**Phase:** Onboarding (Week 3)  
**Date:** July 18, 2026  
**Author:** Uday (Software Engineer Intern, FlyRank)  

---

## 1. Selected Task (from FL-01 Audit)

* **Target Task**: *Creating Mock Datasets for Database Seeds* (for the Farmer Trade System).
* **Goal**: Generate a SQL script containing realistic, relational mock insert statements for tables: `users` (farmers/buyers), `products`, and `trades`.

---

## 2. The Prompt Iteration Log

### Version 0: Naive Baseline
> **Prompt**: *"Create mock SQL insert data for my database."*

#### Representative Output Excerpt
```sql
CREATE TABLE users (id INT, name VARCHAR(50));
INSERT INTO users VALUES (1, 'John Doe');
INSERT INTO users VALUES (2, 'Jane Smith');
```

#### Iteration Notes
* **What changed in the prompt**: Baseline.
* **What actually improved in the output**: N/A.
* **What still failed**: Extremely generic. It generated table creation schemas instead of insert statements. It did not match our SQLite schema, created columns we don't have, used mock names that do not fit an agricultural marketplace, and completely missed relational foreign keys.
* **What to try next**: Assign a specific role to focus the AI's capability.

---

### Version 1: Role Assignment (Technique 1)
> **Prompt**: *"You are a Senior QA and Database Engineer. Create mock SQL insert data for my database."*

#### Representative Output Excerpt
```sql
-- Mock Data for Test Suite
INSERT INTO customers (customer_id, first_name, last_name, email) VALUES 
(1, 'Alice', 'Johnson', 'alice.j@example.com'),
(2, 'Bob', 'Miller', 'bob.m@example.com');
```

#### Iteration Notes
* **What changed in the prompt**: Assigned the role of a *Senior QA and Database Engineer*.
* **What actually improved in the output**: The tone shifted to professional testing data. It correctly generated mock comments (`-- Mock Data for Test Suite`) and organized multiple values inside standard bulk inserts.
* **What still failed**: The tables (`customers`) and columns still did not match our `trades` or `users` schema. It had no concept of agricultural trade data or SQLite conventions.
* **What to try next**: Provide context and motivation regarding the application domain and database schema.

---

### Version 2: Context and Motivation (Technique 2)
> **Prompt**: *"You are a Senior QA and Database Engineer. We are building the 'Farmer Trade System', a marketplace for local agricultural trade. We need realistic SQL insert seeds to test our trade matching queries. The database is SQLite. The tables and columns are:  
> 1. `users`: columns `id` (text), `name` (text), `role` (text: either 'farmer' or 'buyer').  
> 2. `products`: columns `id` (text), `seller_id` (text, matches users.id), `title` (text), `price` (real).  
> 3. `trades`: columns `id` (text), `product_id` (text, matches products.id), `buyer_id` (text, matches users.id), `seller_id` (text, matches users.id), `quantity` (integer), `price` (real), `status` (text)."*

#### Representative Output Excerpt
```sql
-- Seed users
INSERT INTO users (id, name, role) VALUES ('u1', 'Gopal Rao', 'farmer');
INSERT INTO users (id, name, role) VALUES ('u2', 'Suresh Kumar', 'buyer');

-- Seed products
INSERT INTO products (id, seller_id, title, price) VALUES ('p1', 'u1', 'Organic Tomatoes', 45.00);

-- Seed trades
INSERT INTO trades (id, product_id, buyer_id, seller_id, quantity, price, status) VALUES 
('t1', 'p1', 'u2', 'u1', 100, 45.00, 'completed');
```

#### Iteration Notes
* **What changed in the prompt**: Added motivation (testing trade matching queries in an agricultural marketplace) and detailed SQLite schema relationships.
* **What actually improved in the output**: The code generated matched our exact table schema. The relationships between `users.id`, `products.seller_id`, and `trades` foreign keys were logical and correct.
* **What still failed**: The names and products were very sparse (only 2 users, 1 product, 1 trade). To stress-test queries under low-bandwidth rural conditions, we need a larger volume of varied products and transactions.
* **What to try next**: Add few-shot examples to show what realistic, high-quality agricultural seed data looks like.

---

### Version 3: Few-Shot Examples (Technique 3)
> **Prompt**: *"You are a Senior QA and Database Engineer. We are building the 'Farmer Trade System', a marketplace for local agricultural trade. We need realistic SQL insert seeds to test our trade matching queries. The database is SQLite. The tables and columns are:  
> 1. `users`: columns `id` (text), `name` (text), `role` (text: either 'farmer' or 'buyer').  
> 2. `products`: columns `id` (text), `seller_id` (text, matches users.id), `title` (text), `price` (real).  
> 3. `trades`: columns `id` (text), `product_id` (text, matches products.id), `buyer_id` (text, matches users.id), `seller_id` (text, matches users.id), `quantity` (integer), `price` (real), `status` (text).  
> 
> **Examples of high-quality seeds**:  
> - User: `('usr_f01', 'Anil Deshmukh', 'farmer')`  
> - Product: `('prod_tom01', 'usr_f01', 'Fresh Red Tomatoes (20kg Bag)', 12.50)`  
> - Trade: `('trd_01', 'prod_tom01', 'usr_b01', 'usr_f01', 5, 12.50, 'completed')`  
> 
> Generate a comprehensive set of 30 mock rows across these tables following this style."*

#### Representative Output Excerpt
```sql
-- Users
INSERT INTO users (id, name, role) VALUES ('usr_f01', 'Anil Deshmukh', 'farmer');
INSERT INTO users (id, name, role) VALUES ('usr_b01', 'Ravi Patel', 'buyer');
-- Products
INSERT INTO products (id, seller_id, title, price) VALUES ('prod_tom01', 'usr_f01', 'Fresh Red Tomatoes (20kg Bag)', 12.50);
-- Trades
INSERT INTO trades (id, product_id, buyer_id, seller_id, quantity, price, status) VALUES ('trd_01', 'prod_tom01', 'usr_b01', 'usr_f01', 5, 12.50, 'completed');
```

#### Iteration Notes
* **What changed in the prompt**: Added 3 concrete examples (few-shot prompting) demonstrating our preferred ID naming conventions (`usr_f01`, `prod_tom01`) and descriptive product titles, and asked for 30 rows.
* **What actually improved in the output**: The model adopted the ID naming convention and produced descriptive product listings (e.g. including bags/kilograms in titles).
* **What still failed**:  
  > [!WARNING]
  > **This didn't help / made it worse.** Because the prompt simply requested "30 mock rows across these tables," the model generated the exact examples provided, added only 3 new rows, and then hallucinated comments indicating it was complete, or simply stopped. It did not scale up to the volume required.
* **What to try next**: Define a strict output structure to control exactly how many rows are outputted and how they are structured.

---

### Version 4: Output Structure (Technique 4)
> **Prompt**: *"You are a Senior QA and Database Engineer. We are building the 'Farmer Trade System', a marketplace for local agricultural trade. We need realistic SQL insert seeds to test our trade matching queries. The database is SQLite. The tables and columns are:  
> [Schema description from V2]  
> [Examples from V3]  
> 
> **Output Structure**:  
> Return ONLY a clean SQL code block containing exactly:  
> 1. Exactly 10 `INSERT` statements for the `users` table (5 farmers, 5 buyers).  
> 2. Exactly 10 `INSERT` statements for the `products` table, with products associated with the farmers.  
> 3. Exactly 10 `INSERT` statements for the `trades` table, referencing valid user and product IDs.  
> Do not truncate the code block. Do not write markdown notes or explanations before or after the code block."*

#### Representative Output Excerpt
```sql
INSERT INTO users (id, name, role) VALUES ('usr_f01', 'Anil Deshmukh', 'farmer');
-- [Exactly 9 more users...]
INSERT INTO products (id, seller_id, title, price) VALUES ('prod_tom01', 'usr_f01', 'Fresh Red Tomatoes (20kg Bag)', 12.50);
-- [Exactly 9 more products...]
INSERT INTO trades (id, product_id, buyer_id, seller_id, quantity, price, status) VALUES ('trd_01', 'prod_tom01', 'usr_b01', 'usr_f01', 5, 12.50, 'completed');
-- [Exactly 9 more trades...]
```

#### Iteration Notes
* **What changed in the prompt**: Specified a strict output format (SQL block only, no conversational text, exact count of 10 rows per table, no truncation).
* **What actually improved in the output**: The response was clean code without conversational preamble. It contained exactly 30 total SQL insert statements, satisfying our volume requirements.
* **What still failed**: Although the counts were correct, some generated trade entries had mismatch errors (e.g., a trade associated a buyer ID with a farmer, but linked to a product owned by a different farmer, violating business logic).
* **What to try next**: Use step decomposition to guide the model's logic flow to ensure relations match.

---

### Version 5: Step Decomposition (Technique 5)
> **Prompt**: *"You are a Senior QA and Database Engineer. We are building the 'Farmer Trade System', a marketplace for local agricultural trade. We need realistic SQL insert seeds to test our trade matching queries. The database is SQLite. The tables and columns are:  
> [Schema description from V2]  
> [Examples from V3]  
> [Output Structure from V4]  
> 
> **Step-by-Step Instructions**:  
> 1. **Step 1 - Users**: Generate 5 unique farmers (`usr_f01` to `usr_f05`) and 5 unique buyers (`usr_b01` to `usr_b05`) with realistic names.  
> 2. **Step 2 - Products**: Generate 10 products (`prod_01` to `prod_10`). Distribute them evenly among your 5 farmers. Ensure the `seller_id` matches the corresponding farmer ID.  
> 3. **Step 3 - Trades**: Generate 10 trades (`trd_01` to `trd_10`). For each trade, pick a product, identify its actual seller (farmer), and ensure the `trades.seller_id` matches the product's `seller_id`. Link it to a random buyer ID.  
> 4. **Step 4 - Output**: Assemble the SQL queries into their respective table blocks."*

#### Representative Output Excerpt
```sql
-- Step 1: Users (5 Farmers, 5 Buyers)
INSERT INTO users (id, name, role) VALUES ('usr_f01', 'Anil Deshmukh', 'farmer');
INSERT INTO users (id, name, role) VALUES ('usr_f02', 'Basheer Khan', 'farmer');
-- ...
INSERT INTO users (id, name, role) VALUES ('usr_b01', 'Ravi Patel', 'buyer');
-- ...

-- Step 2: Products (10 Products linked to Farmers)
INSERT INTO products (id, seller_id, title, price) VALUES ('prod_01', 'usr_f01', 'Fresh Red Tomatoes (20kg Bag)', 12.50);
INSERT INTO products (id, seller_id, title, price) VALUES ('prod_02', 'usr_f01', 'Green Chili (5kg Box)', 8.00);
INSERT INTO products (id, seller_id, title, price) VALUES ('prod_03', 'usr_f02', 'Alphonso Mangoes (12pc)', 25.00);
-- ...

-- Step 3: Trades (10 Trades with matching foreign keys)
INSERT INTO trades (id, product_id, buyer_id, seller_id, quantity, price, status) VALUES 
('trd_01', 'prod_01', 'usr_b01', 'usr_f01', 5, 12.50, 'completed'),
('trd_02', 'prod_03', 'usr_b02', 'usr_f02', 2, 25.00, 'completed');
```

#### Iteration Notes
* **What changed in the prompt**: Decomposed the generation process into four sequential logic steps to enforce foreign key integrity.
* **What actually improved in the output**: The relationships between products, sellers, and trades are 100% accurate. `trd_02` links to `prod_03` and correctly attributes the seller as `usr_f02`, resolving the cross-association bug.
* **What still failed**: N/A (The output is complete, correct, and ready for our test suite).
* **What to try next**: Execute the final prompt across different models (Claude & ChatGPT) to evaluate output differences.

---

## 3. Cross-Model Comparison (Claude vs. ChatGPT)

The final prompt (Version 5) was evaluated on **Claude 3.5 Sonnet** and **ChatGPT (GPT-4o)**.

| Evaluation Metric | Claude (3.5 Sonnet) | ChatGPT (GPT-4o) |
| :--- | :--- | :--- |
| **Tone & Preamble** | Extremely minimal. Excluded conversational notes as requested by constraints. | Friendly but ignored the "no markdown notes" constraint, adding a short introductory line. |
| **Relational Accuracy** | 100% correct. Every trade linked to the correct seller of that product. | 100% correct. Checked all 10 insert statements; matches matched. |
| **Code Structure** | Grouped neatly with clear SQL comments separating the steps. | Placed all statements in a single continuous code block. |
| **Truncation Risk** | Low. Outputted all 30 statements without placeholders. | Medium. Sometimes defaults to truncated comments (e.g. `-- Rest of inserts...`) if the count exceeds 15. |
| **Failure Points** | Strictly followed constraints but sometimes outputted overly conservative formatting. | Failed the formatting constraint (included conversational introduction text). |

---

## 4. Final Reusable Prompt Template

Below is a reusable prompt template for generating relational seed files:

```markdown
You are a senior database engineer and QA specialist.

# Goal
Generate a clean SQL database seed file containing realistic mock insert statements for testing relational queries.

# Target Database
- System: [DATABASE SYSTEM e.g., SQLite, PostgreSQL]

# Database Schema
Please respect the following tables and relationships:
[INSERT TABLE LIST AND COLUMNS, e.g.]
1. `table_a`: columns `id` (primary key), `name`, `type`.
2. `table_b`: columns `id` (primary key), `table_a_id` (foreign key matching table_a.id), `value`.

# Constraints
1. Create exactly [NUMBER e.g., 10] mock rows for `table_a`.
2. Create exactly [NUMBER e.g., 10] mock rows for `table_b`.
3. Do not truncate the statements or write placeholders like `// ... rest of code`.
4. Output ONLY the raw SQL code block. Exclude any introductory or concluding text.

# Step-by-Step Generation
1. Step 1: Generate primary keys for `table_a` following the naming convention '[CONVENTION e.g., key_01]'.
2. Step 2: Generate records for `table_b` making sure that every `table_b.table_a_id` matches a valid ID generated in Step 1.
3. Step 3: Write out the SQL blocks in order.
```

---
*End of Report*
