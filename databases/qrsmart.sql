CREATE TABLE `QR_codes` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`short_code` varchar(255) NOT NULL UNIQUE,
	`type` ENUM('static','dynamic')  NOT NULL DEFAULT 'static',
	`filename` TEXT NOT NULL UNIQUE,
	`user_id` int NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `url_links` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`link` varchar(255) NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`qr_code_id` bigint NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `users` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`firstname` varchar(255),
	`lastname` varchar(255),
	`email` varchar(255) UNIQUE,
	`session_id` varchar(255) NOT NULL UNIQUE,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

ALTER TABLE `QR_codes` ADD CONSTRAINT `QR_codes_fk0` FOREIGN KEY (`user_id`) REFERENCES `users`(`id`);

ALTER TABLE `url_links` ADD CONSTRAINT `url_links_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);




