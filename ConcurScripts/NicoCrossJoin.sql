create table "GD_dataset_expenseinfo" (
	"citylocation" VARCHAR(255),
	"department" VARCHAR(255),
	"destination" VARCHAR(255),
	"expense_id" VARCHAR(255),
	"expensetype" VARCHAR(255),
	"industry" VARCHAR(255),
	"amountpaid" DECIMAL(12,2),
	"transactiondate" DATE,
	"expenseinfo__vendorname" VARCHAR(255)
);

create table "GD_dataset_vendor" (
	"vendorname" VARCHAR(255),
	"vendorname_vendornamemask" VARCHAR(255)
);

drop table GD_dataset_expenseinfo;

INSERT INTO vendor_table (Vendor_Name) Select distinct Vendor_Name from in_concur;

Create table vendor_cross as select md5(T1.Vendor_name||'secretkey') as id,T1.Vendor_name, T2.Vendor_name as Vendor_Cross
From vendor_table T1 cross join vendor_table T2;

select * from vendor_cross where Vendor_cross='Hertz';


select count(1) from in_concur;