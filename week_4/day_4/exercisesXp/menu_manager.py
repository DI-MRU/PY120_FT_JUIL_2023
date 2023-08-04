from database import DatabaseManager

class MenuManager:
    
    @classmethod
    def get_by_name(cls, name):
        select_query = "SELECT * FROM Menu_Items WHERE item_name = %s"
        dataManage = DatabaseManager("your_host","your_database","your_name","your_pass")
        return dataManage.execute_query(select_query,(name,))
    @classmethod
    def all_items(cls):
        select_query = 'SELECT * FROM Menu_items'
        dataManage = DatabaseManager("your_host","your_database","your_name","your_pass")
        return dataManage.execute_query(select_query)