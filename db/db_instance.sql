.open stock_manager.db

-- Create 'product' table
CREATE TABLE IF NOT EXISTS product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(255) NOT NULL,
    price DOUBLE NOT NULL,
    stock INT(255) NOT NULL,
    unit VARCHAR(25) NOT NULL
);

-- Create 'operations' table
CREATE TABLE IF NOT EXISTS operation (
    operations_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    product_id INT(255) NOT NULL,
    operation_date DATE NOT NULL,
    units INT(255) NOT NULL,
    price DOUBLE NOT NULL,
    is_sale BOOLEAN NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id) 
);