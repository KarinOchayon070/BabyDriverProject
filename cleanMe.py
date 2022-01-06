import sqlite3
import statistics
con = sqlite3.connect('crawlerData.db')
con.row_factory = lambda cursor, row: row[0]
c = con.cursor()

# con.execute('UPDATE main SET hoops=1 WHERE hoops IS NULL')
# con.execute('UPDATE main SET hoops=2 WHERE hoops=0')
# con.execute('UPDATE main SET hoops=3 WHERE hoops IS "סגסוגת כרום"')
# con.execute('UPDATE main SET head_light="הלוגן" WHERE head_light IS NULL')

# c.execute(
#     'SELECT next_test FROM main')

# rows = c.fetchall()
# if(rows):
#     result = list(map(int, rows))
#     j2 = [x for x in result if x <= 36]
#     su = statistics.mean(j2)
#     print(j2)
#     print(su)
#     print(len(j2))

c.execute(
    'UPDATE main SET next_test=5.241139680333565 WHERE next_test="1604" OR next_test="4731" OR next_test="985" OR next_test="1102" OR next_test="1424" OR next_test="3357" OR next_test="2130" OR next_test="2563" OR next_test="1693" OR next_test="3366" OR next_test="1811" OR next_test="2019" OR next_test="1835" OR next_test="1205" OR next_test="1353" OR next_test="880" OR next_test="1074" OR next_test="1584" OR next_test="1235" OR next_test="1529" OR next_test="1427" OR next_test="2417" OR next_test="1508" OR next_test="1262" OR next_test="1726" OR next_test="1962" OR next_test="2397"')
# 5.241139680333565


# con.execute(
#     'UPDATE main SET original_ownership=1 WHERE original_ownership IS "1"')
# con.execute(
#     'UPDATE main SET original_ownership=2 WHERE original_ownership IS "0"')
# con.execute(
#     'UPDATE main SET original_ownership=3 WHERE original_ownership IS "השכרה"')
# con.execute(
#     'UPDATE main SET original_ownership=4 WHERE original_ownership IS "חברה"')
# con.execute(
#     'UPDATE main SET original_ownership=5 WHERE original_ownership IS "מונית"')
# con.execute(
#     'UPDATE main SET original_ownership=6 WHERE original_ownership IS "ייבוא אישי"')

# con.execute('UPDATE main SET turbo=0 WHERE turbo IS NULL')
# con.execute('UPDATE main SET tire_type="R" WHERE tire_type IS NULL')
# c.execute(
#     'DELETE FROM main WHERE height_ratio is NULL AND horsepower is NULL and max_speed is NULL AND max_torque is NULL AND number_of_seats is NULL')
# c.execute(
#     'DELETE FROM main WHERE new_car_price IS NULL')
# c.execute('SELECT tire_width FROM main WHERE tire_width IS NOT NULL')
# c.execute(
#     'UPDATE main SET tire_width=209.49968132568515 WHERE tire_width IS NULL')
# c.execute(
#     'SELECT height_ratio FROM main WHERE height_ratio IS NOT NULL')
# c.execute(
#     'UPDATE main SET height_ratio=57.26896112173359 WHERE height_ratio IS NULL')
# c.execute(
#     'SELECT wheel_diameter FROM main WHERE wheel_diameter IS NOT NULL')
# c.execute(
#     'UPDATE main SET wheel_diameter=16.384321223709367 WHERE wheel_diameter IS NULL')
# c.execute(
#     'SELECT finish_level FROM main WHERE finish_level IS NULL')
# c.execute(
#     'DELETE FROM main WHERE finish_level is NULL')
# c.execute(
#     'SELECT number_of_doors FROM main WHERE number_of_doors IS NULL')
# c.execute(
#     'SELECT avrage_fuel_consumption FROM main WHERE avrage_fuel_consumption IS NOT NULL')
# c.execute(
#     'UPDATE main SET avrage_fuel_consumption=17.745368492224475 WHERE avrage_fuel_consumption IS NULL')
# c.execute(
#     'SELECT avrage_fuel_consumption_city FROM main WHERE avrage_fuel_consumption_city IS NOT NULL')
# c.execute(
#     'UPDATE main SET avrage_fuel_consumption_city=20.386326530612244 WHERE avrage_fuel_consumption_city IS NULL')
# c.execute(
#     'SELECT avrage_fuel_consumption_highway FROM main WHERE avrage_fuel_consumption_highway IS NOT NULL')
# c.execute(
#     'UPDATE main SET avrage_fuel_consumption_highway=14.626915113871636 WHERE avrage_fuel_consumption_highway IS NULL')
# c.execute(
#     'SELECT horsepower FROM main WHERE horsepower IS NOT NULL')
# c.execute(
#     'UPDATE main SET horsepower=140.21616656460503 WHERE horsepower IS NULL')
# c.execute(
#     'SELECT max_speed FROM main WHERE max_speed IS NOT NULL')
# c.execute(
#     'UPDATE main SET max_speed=189.11954331766287 WHERE max_speed IS NULL')

# rows = c.fetchall()
# print(rows)
# if(rows):
#     su = statistics.mean(rows)
#     print(su)
#     print(len(rows))

# col_names = [  # 'max_torque',
#  'number_of_cylinders',
#  'number_of_gears',
#  'rounds_per_minute_for_max_power',
#  'rounds_per_minute_for_max_torque',
#  'zero_to_100_km_in_seconds',
#  'number_of_airbags',
#  'trunk_volume_in_liters',
#  'trunk_volume_in_seat_folding',
#  'front_seat_headroom_in_cm',
#  'rear_seat_headroom_in_cm',
#  'height_in_cm',
#  'front_seat_waist_in_cm',
#  'rear_seat_waist_in_cm',
#  'front_legroom_in_cm',
#  'rear_legroom_in_cm',
#  'length_in_cm',
#  'front_seat_shoulder_in_cm',
#  'rear_seat_shoulder_in_cm',
#  'width_in_cm',
#  'full_tank_volume_in_liters',
#  'minimal_weight_in_kg',
#  'maximal_weight_in_kg',
#  'wheelbase_in_cm',
#  'electric_windows',
#  'year',
#  'engine',
#  'current_km',
#  'hand',
#  'annual_licensing_fee',
# 'number_of_air_conditioning_locations']

# for col_name in col_names:

#     c.execute(
#         f'SELECT {col_name} FROM main WHERE {col_name} IS NOT NULL')
#     rows = c.fetchall()

#     if(rows):
#         try:
#             average = statistics.mean(rows)
#             c.execute(
#                 f'UPDATE main SET {col_name}={average} WHERE {col_name} IS NULL')
#         except:
#             print("error in:", col_name)

# col_names = [
#     'automatic_high_beam',
#     'dead_vehicle_monitoring_system',
#     'independent_emergency_break',
#     'abs',
#     'turn_tracking_headlights',
#     'cancel_airbag',
#     'isofix',
#     'lane_departure_warning_system',
#     'seat_belt_warning_system',
#     'airpressure_sensors',
#     'road_sign_recognition',
#     'subwoofer',
#     'bluetooth',
#     'rear_control_air_conditioning',
#     'air_conditioning',
#     'cruise_control',
#     'driver_heated_seat',
#     'fog_lights',
#     'heated_front_passenger_seat',
#     'rain_sensors',
#     'heated_rear_passenger_seat',
#     'roof_window',
#     'dark_windows',
# ]

# for col_name in col_names:
#     try:
#         c.execute(
#             f'UPDATE main SET {col_name}=0 WHERE {col_name} IS NULL')
#     except:
#         print("error in:", col_name)

con.commit()
con.close()
