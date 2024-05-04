class Database:
  def __init__(self,reset = True):
    if os.path.exist('house'):
      os.remove('order db')
      self.conn = sqlite3
      
  def create_tables(self): (ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NUL, CUSTOMER_ID INTEGER NOT NULL, PRODUCT_CODE INTEGER NOT NULL<)
    
  def query_data(self):
    cursor = self.comn.cursor()
    query = "SELECT * FROM Products"
    
    db.query_data()