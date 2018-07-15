CREATE TABLE messages (
    mid varchar(40) PRIMARY KEY,
    is_passport boolean NOT NULL,
    is_avia boolean NOT NULL,
    passport_extra_info json,
    avia_extra_info json
);
