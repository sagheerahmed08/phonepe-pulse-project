-- Create agg_transaction table
CREATE TABLE agg_transaction (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Transaction_type VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Create agg_insurance table
CREATE TABLE agg_insurance (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Transaction_type VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Create agg_user table
CREATE TABLE agg_user (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Brand VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_percentage DOUBLE
);

-- Create map_insurance table
CREATE TABLE map_insurance (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    District VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Create map_transaction table
CREATE TABLE map_transaction (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    District VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Create map_user table
CREATE TABLE map_user (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    District VARCHAR(100),
    RegisteredUser BIGINT,
    AppOpens BIGINT
);

-- Create top_insurance table
CREATE TABLE top_insurance (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Pincodes VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Create top_transaction table
CREATE TABLE top_transaction (
    States VARCHAR(100),
    Years INT,
    Quarter INT,
    Pincodes VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DOUBLE
);

-- Create top_user table
CREATE TABLE top_user (
    States VARCHAR(50),
    Years INT,
    Quarter INT,
    Pincodes INT,
    RegisteredUser BIGINT
);

-- Create top_district table
CREATE TABLE top_district (
    States VARCHAR(50),
    Years INT,
    Quarter INT,
    Districts VARCHAR(100),
    Transaction_count BIGINT,
    Transaction_amount DECIMAL(18,2)
);
