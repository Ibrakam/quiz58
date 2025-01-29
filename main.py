
"""
class Table():
....
Добавление данных в бд
1. Подключение к базе данных через db = next(get_db())
2. new_table = Table(id=id, name=name)
3. db.add(new_table)
4. db.commit()

Получние всех данных или определенных
1. Подключение к базе данных через db = next(get_db())
2. all_table = db.query(Table).all()
3. all_level_table = db.query(Table).filter_by(level=level).all()
4. exact_table = db.query(Table).filter_by(id=id).first()

Изменение данных из бд
1. Подключение к базе данных через db = next(get_db())
2. to_update_table = db.query(Table).filter_by(id=id).first()
3. to_update_table.level = "hard"
4. db.commit()

Удаление данных из бд
1. Подключение к базе данных через db = next(get_db())
2. to_delete_table = db.query(Table).filter_by(id=id).first().delete()
3. db.delete(to_delete_table)
4. db.commit()
"""
