Question no -1: 
Identify the primary keys and foreign keys in maven movies db. Discuss the differences
 Primary Keys:

actor: PK is actor_id.
actor_award: PK is actor_award_id.
address: PK is address_id.
advisor: PK is advisor_id.
category: PK is category_id.
city: PK is city_id.
country: PK is country_id.
customer: PK is customer_id.
film: PK is film_id.
film_actor: Composite PK is (actor_id, film_id).
film_category: Composite PK is (film_id, category_id).
film_text: PK is film_id.
inventory: PK is inventory_id.
investor: PK is investor_id.
language: PK is language_id.
payment: PK is payment_id.
rental: PK is rental_id.
staff: PK is staff_id.
store: PK is store_id.

Foreign Keys:

address: FK city_id references city(city_id).
city: FK country_id references country(country_id).
customer: FK address_id references address(address_id). FK store_id references store(store_id).
film: FK language_id references language(language_id). FK original_language_id references language(language_id).
film_actor: FK actor_id references actor(actor_id). FK film_id references film(film_id).
film_category: FK film_id references film(film_id). FK category_id references category(category_id).
film_text: FK film_id references film(film_id).
inventory: FK store_id references store(store_id). FK film_id references film(film_id).
payment: FK rental_id references rental(rental_id). FK customer_id references customer(customer_id). FK staff_id references staff(staff_id).
rental: FK inventory_id references inventory(inventory_id). FK customer_id references customer(customer_id). FK staff_id references staff(staff_id).
staff: FK store_id references store(store_id). FK address_id references address(address_id).
store: FK manager_staff_id references staff(staff_id). FK address_id references address(address_id).
These are the primary keys and foreign keys identified based on the provided MySQL script for the mavenmovies database.

Question no:2
List all details of actors
select * from actor;

Question no:3
List all customer information from DB.
Select * from customer;

Question no:4
List different countries.
select * from Country;

Question no :5
Display all active customers.
select first_name,last_name, active from customer;

Question no: 6
List of all rental IDs for customer with ID 1.
SELECT rental_id
FROM rental
WHERE customer_id = 1;

Question no: 7
Display all the films whose rental duration is greater than 5 .
select * from film where rental_duration >5;

Question no: 8

Select sum(film_id) from film where replacement_cost >15 and replacement_cost<20;

Question no: 9
Display the count of unique first names of actors.
select count(distinct(first_name)) from actor;

Question no: 10

Select * from customer limit 10;

Question no: 11

Select * from customer  where first_name like "%a" limit 3;

Question no: 12

select * from customer where first_name like 'b%' limit 3;

Question no: 13

select * from customer where first_name like "%a";

Question no: 14

select * from customer where first_name like "a%";

Question no: 15

Select * from city where city like "a%a" limit 4;

Question no: 16

select * from customer where first_name like '%NI%';

Question no : 17

select * from customer where first_name like '_R%';

Question no : 18

select * from customer where first_name like 'a%' and length(first_name)>=5;

Question no : 19

select * from customer where first_name like 'a%o';

Question no : 20

SELECT
    *
FROM
    film
WHERE
    rating IN ('PG', 'PG-13');
    
Question no : 21

select * from film where length between 50 and 100;

 Question no : 22
 
 select * from actor limit 50;
 
 Question no : 23
 
 select distinct(film_id) from inventory;
 
    



