declare @id int = 0;
declare @date datetime = getdate();
declare @product int = 0;
declare @sales_person  int = 0;
declare @order_type int = 0;
declare @weight int = 0;

declare @i int = 1

while (@i <= 10)
begin 
waitfor delay'00:00:01'
set @id = abs(checksum(newid()) %999999)
set @date = getdate();
set @product = abs(checksum(newid())%10) +10;
set @sales_person = (abs(checksum(newid())%5)+1)+10;
set @order_type = abs(checksum(newid())%3)+1;
set @weight = abs(checksum(newid())%10)+1;
insert into Orders values(@id, @date, @product, @sales_person, @order_type, @weight);
set @i = @i +1;

end