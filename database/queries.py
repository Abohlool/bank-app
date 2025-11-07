from database.connection import Connection


# * ------------------ Users ------------------
def create_user(full_name: str, birthday: str, pin_hash: str):
    """Insert a new user into the `users` table."""
    with Connection() as conn:
        conn.execute(
            "INSERT INTO `users` (`full_name`, `birthday`, `pin_hash`) VALUES (?, ?, ?)",
            (full_name, birthday, pin_hash)
        )


def get_user_by_id(user_id: int):
    """Return a user record by `id`."""
    with Connection() as conn:
        cursor = conn.execute("SELECT * FROM `users` WHERE `id` = ?", (user_id,))
        return cursor.fetchone()


def get_user_by_name(name: str):
    """Return all users with `full_name` matching the input name."""
    with Connection() as conn:
        cursor = conn.execute("SELECT * FROM `users` WHERE `full_name` LIKE ?", (name,))
        return cursor.fetchall()


def update_user_info(user_id: int, full_name: str, pin_hash: str):
    """Update users `full_name` and `pin_hash` by their `id`."""
    with Connection() as conn:
        conn.execute(
            "UPDATE  `users` SET `full_name` = ?, `pin_hash` = ? WHERE `id` = ?",
            (full_name, pin_hash, user_id)
        )


def delete_user(user_id: int, full_name: str, pin_hash: str):
    """Delete a user record after verifying `id`, `full_name`, and `pin_hash`."""
    with Connection() as conn:
        conn.execute(
            "DELETE FROM `users` WHERE `id` = ? AND `full_name` = ? AND `pin_hash` = ?",
            (user_id, full_name, pin_hash)
        )


# * ------------------ Accounts ------------------
def create_account():
    pass


def get_account_by_number():
    pass


def get_all_accounts_for_user():
    pass


def delete_account():
    pass


def update_account_info():
    pass


# * ------------------ Transaction ------------------
def add_transaction():
    pass


def get_transaction_by_id():
    pass


def get_all_transactions_for_account():
    pass


# * ------------------ Utils ------------------
def update_balance():
    pass


def check_account_balance():
    pass


def find_user():
    pass


def find_account_number():
    pass
