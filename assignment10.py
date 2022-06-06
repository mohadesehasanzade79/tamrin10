
import sqlite3

db = sqlite3.connect('Ali Assets.db')

cursor = db.cursor()

cursor.execute("CREATE TABLE  Assets (id INTEGER PRIMARY KEY, Name TEXT, Price INTEGER , Count INTEGER)")

#INSERT

id1 = '3'
Name1 = 'Apartment'
Price1= '800 M'
Count1 = '1'

cursor.execute(''' INSERT INTO Assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(id1, Name1,Price1,Count1)

db.commit()

#UPDATE

newprice1 = '1300 M'
newprice3 = '200 M'
assets_id1 = '1'
assets_id3 = '3'

cursor.execute('''UPDATE Assets SET Price = ? WHERE id = ?''',(newprice1 , assets_id1))

cursor.execute('''UPDATE Assets SET Price = ? WHERE id = ?''',(newprice3 , assets_id3))

#DELETE & INSERT

delete_assets_id = '3'
delete_assets_id = '2'

new_assets_id = '4'
new_assets_name = 'Cash'
new_assets_price = '8 K'
new_assets_count = '52 K'

cursor.execute('''DELETE FROM Assets WHERE id = ?''',(delete_assets_id = '3',))

cursor.execute('''DELETE FROM Assets WHERE id = ?''',(delete_assets_id = '2',))

cursor.execute(''' INSERT INTO Assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(new_assets_id , new_assets_name,new_assets_price,new_assets_count)

db.commit()

#INSERT & UPDATE

new_assets_id1 = '5'
new_assets_name1 = 'EOS'
new_assets_price1 = '40 K'
new_assets_count1 = '5 K'

new_assets_id2 = '6'
new_assets_name2 = 'ETH'
new_assets_price2 = '7'
new_assets_count2 = '60 M'

new_assets_count4 = '10 K'
assets_id4 = '4'

cursor.execute(''' INSERT INTO Assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(new_assets_id1 , new_assets_name1,new_assets_price1,new_assets_count1)

cursor.execute(''' INSERT INTO Assets(id,Name,Price,Count) VALUE(?,?,?,?) ''' ,(new_assets_id2 , new_assets_name2,new_assets_price2,new_assets_count2)

cursor.execute('''UPDATE Assets SET Count = ? WHERE id = ?''',(new_assets_count4 , assets_id4))

db.commit

query = "SELECT * FROM Assets;"

cursor.execute(query)
print(cursor.fetchall())
