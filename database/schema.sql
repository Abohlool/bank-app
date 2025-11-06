CREATE TABLE IF NOT EXISTS `users` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `full_name` TEXT NOT NULL,
    `birthday` TEXT NOT NULL,
    `pin_hash` TEXT NOT NULL,
    `created_at` TEXT DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS `accounts` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `user_id` INTEGER NOT NULL,
    `account_number` TEXT UNIQUE NOT NULL,
    `account_type` TEXT CHECK(`account_type` IN ('Checking', 'Savings')) NOT NULL,
    `balance` NUMERIC DEFAULT 0,
    `created_at` TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);


CREATE TABLE IF NOT EXISTS `transactions` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `account_id` INTEGER NOT NULL,
    `type` TEXT CHECK(`type` IN ('deposit', 'withdrawal', 'transfer_out', 'transfer_in')) NOT NULL,
    `amount` NUMERIC CHECK(`amount` > 0) NOT NULL,
    `timestamp` TEXT DEFAULT CURRENT_TIMESTAMP,
    `target_account` TEXT,
    FOREIGN KEY (`account_id`) REFERENCES `accounts`(`id`)
);


CREATE INDEX IF NOT EXISTS `idx_acc_usr_id` ON `accounts`(`user_id`);
CREATE INDEX IF NOT EXISTS `idx_trans_acc_id` ON `transactions`(`account_id`)
