-- Sample data for Serene Family Boutique
-- Run this after creating the schema to populate with sample records

-- ============================================================
-- Collections
-- ============================================================
INSERT INTO collections (name, description) VALUES
('Spring Collection', 'Fresh and vibrant pieces for the spring season'),
('Summer Essentials', 'Light and breezy items perfect for warm weather'),
('Autumn Warmth', 'Cozy and comfortable selections for fall'),
('Winter Elegance', 'Sophisticated pieces for the holiday season'),
('Timeless Classics', 'Enduring styles that never go out of fashion');

-- ============================================================
-- Products
-- ============================================================
INSERT INTO products (name, description, price, sku, quantity, is_active, collection_id) VALUES
('Linen Blouse', 'Breathable linen blouse in natural cream', 89.99, 'SPR-LB-001', 25, TRUE, 1),
('Floral Midi Dress', 'Elegant floral print midi dress', 145.00, 'SPR-FD-002', 15, TRUE, 1),
('Cotton Cardigan', 'Lightweight cotton cardigan in sage green', 75.00, 'SPR-CC-003', 30, TRUE, 1),
('Silk Scarf', 'Hand-painted silk scarf with botanical motifs', 65.00, 'SPR-SS-004', 20, TRUE, 1),

('Linen Trousers', 'Wide-leg linen trousers in natural', 95.00, 'SUM-LT-001', 18, TRUE, 2),
('Straw Tote', 'Handwoven straw tote with leather handles', 120.00, 'SUM-ST-002', 12, TRUE, 2),
('Cotton Sundress', 'Airy cotton sundress in terracotta', 110.00, 'SUM-CS-003', 22, TRUE, 2),
('Raffia Hat', 'Wide-brim raffia sun hat', 55.00, 'SUM-RH-004', 8, TRUE, 2),

('Wool Wrap', 'Luxurious merino wool wrap in dusty rose', 185.00, 'AUT-WW-001', 10, TRUE, 3),
('Cashmere Sweater', 'Soft cashmere sweater in forest green', 225.00, 'AUT-CS-002', 14, TRUE, 3),
('Corduroy Skirt', 'A-line corduroy skirt in camel', 95.00, 'AUT-CK-003', 16, TRUE, 3),

('Velvet Blazer', 'Tailored velvet blazer in deep burgundy', 275.00, 'WIN-VB-001', 8, TRUE, 4),
('Silk Camisole', 'Elegant silk camisole in champagne', 85.00, 'WIN-SC-002', 20, TRUE, 4),
('Pearl Earrings', 'Freshwater pearl drop earrings', 145.00, 'WIN-PE-003', 25, TRUE, 4),

('Leather Handbag', 'Classic leather handbag in cognac', 295.00, 'TML-LH-001', 6, TRUE, 5),
('Gold Necklace', 'Delicate gold chain necklace', 175.00, 'TML-GN-002', 15, TRUE, 5),
('Cashmere Throw', 'Luxurious cashmere throw blanket', 350.00, 'TML-CT-003', 5, TRUE, 5);

-- ============================================================
-- Orders
-- ============================================================
INSERT INTO orders (customer_name, customer_email, customer_phone, shipping_address, order_total, status) VALUES
('Eleanor Vance', 'eleanor.vance@email.com', '555-0101', '123 Maple Street, Portland, OR 97201', 234.99, 'delivered'),
('Margaret Chen', 'margaret.chen@email.com', '555-0102', '456 Oak Avenue, Seattle, WA 98101', 420.00, 'shipped'),
('Isabella Romano', 'isabella.r@email.com', '555-0103', '789 Pine Lane, San Francisco, CA 94102', 185.00, 'processing'),
('Charlotte Webb', 'c.webb@email.com', '555-0104', '321 Cedar Road, Denver, CO 80202', 540.00, 'pending'),
('Olivia Hart', 'olivia.hart@email.com', '555-0105', '654 Birch Street, Austin, TX 78701', 295.00, 'delivered'),
('Sophia Laurent', 'sophia.l@email.com', '555-0106', '987 Willow Way, Nashville, TN 37201', 175.00, 'cancelled');

-- ============================================================
-- Order Items (linking orders to products)
-- ============================================================
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 89.99),
(1, 4, 1, 65.00),
(1, 8, 1, 55.00),
(2, 9, 1, 185.00),
(2, 10, 1, 225.00),
(3, 9, 1, 185.00),
(4, 12, 1, 275.00),
(4, 15, 1, 295.00),
(5, 15, 1, 295.00),
(6, 16, 1, 175.00);
