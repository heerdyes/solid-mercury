create table grocery_items (
  itemname   text,
  quantity   number,
  unitprice  number
)

create table purchase (
  itemname    text,
  unitprice   number,
  quantity    number,
  bill        integer
)

create table customer (
  name        text,
  phnum       text
)

create table purchasebill (
  created_date  text,
  
)

insert into grocery_items 
  (itemname, quantity, unitprice) values
  ('potato', 10.0, 30.0),
  ('tomato', 10.0, 30.0),
  ('onion', 10.0, 30.0),
  ('dal kanpur', 10.0, 30.0),
  ('dal urad', 10.0, 30.0);
