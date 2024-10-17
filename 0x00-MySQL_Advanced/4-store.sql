-- Task: Create a trigger that decreases the quantity of an item in the 'items' table after a new order is added.
-- The quantity in the 'items' table can be negative.

-- Create the triggeer
CREATE TRIGGER decrease_items_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
