from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:110692@localhost:5432/postgres"

engine = create_engine(DB_URL)


def test_add_item():
    with engine.connect() as connection:
        query_insert = text(
            "INSERT INTO subject (subject_title) VALUES ('QA Testing')")
        connection.execute(query_insert)
        connection.commit()
        query_select = text(
            "SELECT * FROM subject WHERE subject_title = 'QA Testing'")
        result = connection.execute(query_select).fetchone()
        assert result is not None, "Item was not added to the database"
        query_delete = text(
            "DELETE FROM subject WHERE subject_title = 'QA Testing'")
        connection.execute(query_delete)
        connection.commit()


def test_update_item():
    with engine.connect() as connection:
        query_prep = text(
            "INSERT INTO subject (subject_title) VALUES ('Old subject_title')")
        connection.execute(query_prep)
        connection.commit()
        query_upd = text(
            "UPDATE subject SET subject_title = "
            "'New subject_title' WHERE subject_title = 'Old subject_title'"
        )
        connection.execute(query_upd)
        connection.commit()
        query_select = text(
            "SELECT * FROM subject WHERE subject_title = 'New subject_title'")
        result = connection.execute(query_select).fetchone()
        assert result is not None, "Item was not updated"
        query_del = text(
            "DELETE FROM subject WHERE subject_title = 'New subject_title'")
        connection.execute(query_del)
        connection.commit()


def test_delete_item():
    with engine.connect() as connection:
        query_prep = text(
            "INSERT INTO subject (subject_title) VALUES ('To delete')")
        connection.execute(query_prep)
        connection.commit()
        query_del = text(
            "DELETE FROM subject WHERE subject_title = 'To delete'")
        connection.execute(query_del)
        connection.commit()
        query_select = text(
            "SELECT * FROM subject WHERE subject_title = 'To delete'")
        result = connection.execute(query_select).fetchone()
        assert result is None, "Item was not deleted"
