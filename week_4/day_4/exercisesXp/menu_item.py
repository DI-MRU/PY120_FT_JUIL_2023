from database import DatabaseManager

class MenuItem:

    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
        self.dataManage = DatabaseManager("your_host","your_database","your_name","your_pass")
    
    def save(self):
        insert_query = 'INSERT INTO Menu_items (item_name,item_price) VALUES (%s,%s)'
        return self.dataManage.execute_query(insert_query,(self.name,self.price))
    
    def delete(self):
        delete_query = 'DELETE FROM Menu_items WHERE item_name = %s'
        return self.dataManage.execute_query(delete_query,(self.name,))
    
    def update(self, new_name, new_price):
         update_query = "UPDATE Menu_items SET item_name = %s, item_price = %s WHERE item_name = %s"
         return self.dataManage.execute_query(update_query, (new_name, new_price, self.name))