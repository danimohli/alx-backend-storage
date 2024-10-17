-- Task: Create a trigger that decreases the quantity of an item in the 'items' table after a new order is added.
-- The quantity in the 'items' table can be negative.

-- Create the trigger
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE id = NEW.item_id;
END;
