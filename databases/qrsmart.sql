CREATE TABLE `QR_codes` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`short_code` varchar(255) NOT NULL UNIQUE,
	`qrcode_state` enum NOT NULL DEFAULT 'static',
	`qrcode_type` enum NOT NULL,
	`filename` TEXT NOT NULL UNIQUE,
	`qrcode_link` TEXT NOT NULL,
	`design` json NOT NULL,
	`user_id` int NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `url_links` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`link` varchar(255) NOT NULL,
	`qr_code_id` INT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
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

CREATE TABLE `virtual_card` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`website` TEXT,
	`company_name` varchar(255),
	`company_position` TEXT,
	`contact_mobile_phone` TEXT,
	`contact_mobile_phone_work` TEXT,
	`contact_email` varchar(255) NOT NULL,
	`address_country` TEXT,
	`address_state` TEXT,
	`address_city` TEXT,
	`address_street` TEXT,
	`address_zipcode` tinytext,
	`personal_description` TEXT,
	`photo_file` TEXT,
	`social_media` json,
	`additional_info` json,
	`qr_code_id` int NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `social_media` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`social_media` json NOT NULL,
	`customization` json NOT NULL,
	`additionnal_info` json NOT NULL,
	`qr_code_id` INT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `menu` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`menu_filename` TEXT NOT NULL,
	`qr_code_id` INT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `events` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` varchar(255) NOT NULL,
	`location` TEXT NOT NULL,
	`start_time` DATETIME NOT NULL,
	`end_time` DATETIME NOT NULL,
	`qr_code_id` int NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `connected_account` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`qr_code_id` INT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

CREATE TABLE `chatbot` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`chatbot_name` TEXT NOT NULL,
	`chatbot_data` json NOT NULL,
	`qr_code_id` INT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`update_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
);

ALTER TABLE `QR_codes` ADD CONSTRAINT `QR_codes_fk0` FOREIGN KEY (`user_id`) REFERENCES `users`(`id`);

ALTER TABLE `url_links` ADD CONSTRAINT `url_links_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);

ALTER TABLE `virtual_card` ADD CONSTRAINT `virtual_card_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);

ALTER TABLE `social_media` ADD CONSTRAINT `social_media_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);

ALTER TABLE `menu` ADD CONSTRAINT `menu_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);

ALTER TABLE `events` ADD CONSTRAINT `events_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);

ALTER TABLE `connected_account` ADD CONSTRAINT `connected_account_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);

ALTER TABLE `chatbot` ADD CONSTRAINT `chatbot_fk0` FOREIGN KEY (`qr_code_id`) REFERENCES `QR_codes`(`id`);










