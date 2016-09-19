# Concur-Benchmarking-Project

The project uses a python script from the ConcurScripts folder with dummy expense data that matches the data available from the Concur expensing software. The data is then loaded into a graph in Cloud Connect where a two database tables are created and then cross joined based on the Vendor Name in order to Hash the Vendors other than the one who has access to the project. The graph then uploads the data to the GoodData server where project admins can now generate reports and metrics based on the data available.
