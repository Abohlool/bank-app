from connection import Connection


# * ------------------ Users ------------------
def create_user(full_name: str, birthday: str, pin_hash: str):
    """Insert a new user into the `users` table."""
    with Connection() as conn:
        conn.execute(
            "INSERT INTO `users` (`full_name`, `birthday`, `pin_hash`) VALUES (?, ?, ?)",
            (full_name, birthday, pin_hash),
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
            (full_name, pin_hash, user_id),
        )


def delete_user(user_id: int, full_name: str, pin_hash: str):
    """Delete a user record after verifying `id`, `full_name`, and `pin_hash`."""
    with Connection() as conn:
        conn.execute(
            "DELETE FROM `users` WHERE `id` = ? AND `full_name` = ? AND `pin_hash` = ?",
            (user_id, full_name, pin_hash),
        )


# * ------------------ Accounts ------------------
def create_account(user_id: int, acc_number: str, acc_type: str):
    """Insert a new account into the `accounts` table."""
    with Connection() as conn:
        conn.execute(
            "INSERT INTO `accounts` (`user_id`, `account_number`, `account_type`) VALUES (?, ?, ?)",
            (user_id, acc_number, acc_type),
        )


def get_account_by_number(acc_number: str):
    """Return a account record by `account_number`."""
    with Connection() as conn:
        cursor = conn.execute(
            "SELCET * FROM `accounts` WHERE `account_number` = ?", (acc_number,)
        )
        return cursor.fetchone()


def get_all_accounts_for_user(user_id: int):
    """Return every account record for a `user_id`."""
    with Connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM `accounts` WHERE `user_id` = ?", (user_id,)
        )
        return cursor.fetchall()


def delete_account(user_id: int, acc_number: str):
    """Delete a account after transfering funds to another account if exists."""

    def check(idx, l):
        if idx + 1 > l:
            return 1
        elif idx - 1 > 0:
            return -1
        else:
            return 0

    def delete(conn, acc_number):
        conn.execute("DELETE FROM `accounts` WHERE `account_number` = ?", (acc_number,))

    with Connection() as conn:
        accounts = get_all_accounts_for_user(user_id)

        target, idx = [(a, i) for i, a in enumerate(accounts) if a[2] == acc_number][0]

        if target[4] == 0:
            delete(conn, acc_number)
            return

        res = check(idx, len(accounts))
        if res != 0:
            conn.execute(
                "UPDATE `accounts` SET `balance` = `balance` + ? WHERE `id` = ?",
                (target[4], accounts[idx + res][0]),
            )

            delete(conn, acc_number)
            return
        else:
            raise


def change_account_type(acc_number: str, acc_type: str):
    """Update `account_type`."""
    with Connection() as conn:
        conn.execute(
            "UPDATE `accounts` SET `account_type` = ? WHERE `account_number` = ?",
            (acc_type, acc_number),
        )


# * ------------------ Transaction ------------------
def add_transaction(
    acc_id: int, ttype: str, amount: float, target_account: str | None = None
):
    with Connection() as conn:
        conn.execute(
            "INSERT INTO `transactions` (`account_id`, `type`, `amount`, `target_account`) VALUES (?, ?, ?, ?)",
            (acc_id, ttype, amount, target_account),
        )


def get_transaction_by_id(trans_id: int):
    with Connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM `transactions` WHERE `id` = ?", (trans_id,)
        )
        return cursor.fetchone()


def get_all_transactions_for_account(acc_id: int, ttype: str | None = None):
    with Connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM `transactions` WHERE `account_id` = ? AND (? IS NULL OR `type` = ?)",
            (acc_id, ttype, ttype),
        )
        return cursor.fetchall()


# * ------------------ Utils ------------------
def update_balance():
    pass


def check_account_balance():
    pass


def find_user():
    pass


def find_account_number():
    pass
