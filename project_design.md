# Minimal features
**Author: Arturo Regalado**

1. Demand and supply balances
2. Forecasts
   1. EIA
   2. ARIMA
   3. XGBoost
3. Spot prices and futures
4. Availability for per country analysis
5. Check against past STEO to see the change per month

# TODO: Pending work
1. Store api calls for all desired data points from EIA.
2. Make the storage to database program. Remeber one core functionality is to be able to compare STEOs between each month to see how forecasts change.
3. Make retriever function from database. Make sure the STEO data series clearly outline which years are historicals and which ones are forecasts. 
4. Make dashboard