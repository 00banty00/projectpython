Q2.Consider the following two tables:

"Customers" table:
Columns: customer_id (integer), customer_name (varchar), city (varchar)

"Orders" table:
Columns: order_id (integer), customer_id (integer), order_date (date), order_amount (numeric)

Write an SQL query to find the total order amount for each customer who has placed more than 3 orders and is from a city with at least two customers who have placed an order.

Your query should return the following columns:

customer_id
customer_name
city
total_order_amount
with cte1 as (

    select * 
    from Orders ord
    left join Customers cust
    on ord.customer_id = cust.

) 

customer_df = spark.read.format("csv") \
                        .options("header","true")\
                        .options("inferschema","true")\
                        .load(path)


order_df = spark.read.format("csv") \
                        .options("header","true")\
                        .options("inferschema","true")\
                        .load(path)


cust_join_ordr = order_df.join(customer_df,on[customer_id],how="left")

win_specs_city = window.PartionedBy("city")
# win_specs_cust = window.PartionedBy("customer_id")
cust_join_ordr = cust_join_ordr.withcolumn("cust_more_than_2",over(win_specs_city))\
                                
                                .filter(col("cust_more_than_2") >= 2)

cust_placed_more_than_3 = cust_join_ordr.groupBy("customer_id").agg(count("order_id"))

cust_placed_more_than_3 = cust_placed_more_than_3.filter(col("count")>=3)


cust_join_ordr = cust_join_ordr.join(cust_placed_more_than_3,cust_join_ordr.customer_id == cust_placed_more_than_3.customer_id, "left")


cust_join_ordr = cust_join_ordr.filter(col("count").isNotnull())



def maxProfit(prices):
    initial_profit = 1

    for i in range(len(prices)):
        for j in range(1,len(prices)):
            if prices[j] - prices[i] > initial_profit:
                initial_profit = prices[j] - prices[i]

    return initial_profit


maxProfit(prices)
