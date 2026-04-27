import psycopg2
from psycopg2 import sql


def connect_db():
    conn = psycopg2.connect(
        dbname="clothes_database",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )
    return conn


def initialize_db(conn):
    with conn.cursor() as cur:
        query = """ 
               CREATE TABLE IF NOT EXISTS users (
                   id SERIAL PRIMARY KEY,
                   tg_id BIGINT NOT NULL UNIQUE,
                   username TEXT,
                   currency TEXT NOT NULL DEFAULT 'BYN'
                   );
                        
               CREATE TABLE IF NOT EXISTS category (
                   id SERIAL PRIMARY KEY,
                   name TEXT NOT NULL UNIQUE
                   );
           
               CREATE TABLE IF NOT EXISTS item (
                   id SERIAL PRIMARY KEY,
                   user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
                   category_id INTEGER REFERENCES category(id),
                   brand TEXT,
                   price NUMERIC(10,2) NOT NULL,
                   photo_id TEXT,
                   purchase_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                   usage_count INTEGER DEFAULT 0
                   );
           """
        cur.execute(query)
        conn.commit()

        categories = ['Верхняя одежда', 'Обувь', 'Брюки/Джинсы', 'Аксессуары', 'Футболки/Рубашки/Блузки', 'Платья',
                      'Юбки',
                      'Жакеты и пиджаки', 'Шорты', 'Леггинсы', 'Джемперы/Свитеры']
        for cat in categories:
            cur.execute("INSERT INTO category (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (cat,))

        conn.commit()


# регистрация/проверка пользователя
def register_user(conn, tg_id, username):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO users (tg_id, username) 
            VALUES (%s, %s) ON CONFLICT (tg_id) DO NOTHING
        """, (tg_id, username))
        conn.commit()


# Получить список всех категорий для кнопок
def get_categories(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, name FROM category")
        return cur.fetchall()  # Вернет список кортежей


def add_item(conn, tg_id, category_id, brand, price, photo_id):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users WHERE tg_id = %s", (tg_id,))
        user_db_record = cur.fetchone()

        if user_db_record:
            user_id = user_db_record[0]

            insert_query = """
                            INSERT INTO item (user_id, category_id, brand, price, photo_id)
                            VALUES (%s, %s, %s, %s, %s)
                """
            cur.execute(insert_query, (user_id, category_id, brand, price, photo_id))
            conn.commit()
            print("Вещь успешно добавлена!")
        else:
            print("Пользователь не найден.")


def get_monthly_spending(conn, tg_id):
    with conn.cursor() as cur:
        query = """
            SELECT SUM(price) FROM item 
            JOIN users ON item.user_id = users.id 
            WHERE users.tg_id = %s 
            AND purchase_date > NOW() - INTERVAL '1 month'
        """
        cur.execute(query, (tg_id,))
        return cur.fetchone()[0] or 0


# Получить общую сумму трат пользователя
def get_total_spent(conn, tg_id):
    with conn.cursor() as cur:
        query = """
            SELECT SUM(price) FROM item 
            JOIN users ON item.user_id = users.id 
            WHERE users.tg_id = %s
        """
        cur.execute(query, (tg_id,))
        result = cur.fetchone()
        return result[0] if result[0] else 0


def get_wardrobe(conn, tg_id):
    with conn.cursor() as cur:
        query = """
            SELECT item.id, item.brand, item.price, category.name, item.purchase_date, item.photo_id, item.usage_count 
            FROM item
            JOIN users ON item.user_id = users.id
            JOIN category ON item.category_id = category.id
            WHERE users.tg_id = %s
            ORDER BY item.purchase_date DESC
        """
        cur.execute(query, (tg_id,))
        return cur.fetchall()


def delete_user_item(conn, tg_id, item_id):
    with conn.cursor() as cur:
        query = """
            DELETE FROM item 
            WHERE id = %s AND user_id = (SELECT id FROM users WHERE tg_id = %s)
        """
        cur.execute(query, (item_id, tg_id))
        conn.commit()
        if cur.rowcount > 0:
            print("Вещь удалена.")
            return True
        else:
            print("Вещь не найдена или не принадлежит пользователю.")
            return False


# +1 носка какой-либо вещи
def add_usage(conn, item_id):
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE item 
            SET usage_count = usage_count + 1 
            WHERE id = %s
        """, (item_id,))
        conn.commit()


#  стоимость одной носки
def get_cost_per_wear(conn, item_id):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT price, usage_count 
            FROM item 
            WHERE id = %s
        """, (item_id,))
        result = cur.fetchone()

        if result:
            price, usage_count = result
            if usage_count > 0:
                return round(price / usage_count, 2)
            return price  # Если еще ни разу не надевали, цена за носку равна цене покупки
        return 0


def get_random_item_from_category(conn, tg_id, category_name):
    with conn.cursor() as cur:
        query = """
            SELECT item.brand, item.photo_id, category.name
            FROM item
            JOIN users ON item.user_id = users.id
            JOIN category ON item.category_id = category.id
            WHERE users.tg_id = %s AND category.name = ANY (%s)
            ORDER BY RANDOM()
            LIMIT 1
        """
        cur.execute(query, (tg_id, list(category_name)))
        return cur.fetchone()


def get_wardrobe_stats(conn, tg_id):
    with conn.cursor() as cur:
        query = """
            SELECT 
                COUNT(item.id), 
                SUM(item.price), 
                MIN(item.price), 
                MAX(item.price),
                AVG(item.price)
            FROM item
            JOIN users ON item.user_id = users.id
            WHERE users.tg_id = %s
        """
        cur.execute(query, (tg_id,))
        result = cur.fetchone()

        if result and result[0] > 0:
            return {
                'total_count': result[0],
                'total_sum': result[1],
                'min_price': result[2],
                'max_price': result[3],
                'avg_price': round(result[4], 2)
            }
        return None


def main():
    with connect_db() as conn:
        print("Connected to database successfully!")
        initialize_db(conn)
        print("Initialized database successfully!")


main()
