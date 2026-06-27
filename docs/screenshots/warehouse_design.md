# Customer Analytics Data Warehouse

## Star Schema

### Fact Table

Fact_Sales

Columns

- Order ID
- Customer ID
- Product ID
- Location ID
- Sales
- Quantity
- Discount
- Profit

---

### Dimension Table

Dim_Customer

Columns

- Customer ID
- Customer Name
- Segment

---

### Dimension Table

Dim_Product

Columns

- Product ID
- Category
- Sub-Category
- Product Name

---

### Dimension Table

Dim_Location

Columns

- Location ID
- Country
- State
- City
- Region