import arcade

arcade.open_window(700,400, "Nellie Leaverton")
arcade.start_render()
###############
arcade.draw_lrtb_rectangle_filled(0,700,400,240, arcade.color.BOSTON_UNIVERSITY_RED) #TOP RED
arcade.draw_lrtb_rectangle_filled(0, 700, 240, 0, arcade.color.BLUEBONNET) #BOTTOM BLUE
### #1 YELLOW
a = 279
b = 303
c = 270
d = 249

my_list=()
###### for the loop
# for i in range(2):
#     my_list = (
#         (0,a),
#         (120, b),
#         (120, c),
#         (0, d)
#         )
#     arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
#     a = a - 20
#     b = b - 20
#     c = c - 20
#     d = d - 20
############

my_list = (
    (0,a),
    (120, b),
    (120, c),
    (0, d)
    )
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
### #2
my_list = (
    (120, 270),
    (350, 200),
    (350, 233),
    (120, 303)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
### #3
my_list = (
    (350, 233),
    (580, 303),
    (580, 270),
    (350, 200)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
### #4
my_list = (
    (580, 304),
    (700, 280),
    (700, 249),
    (580, 270)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
################
arcade.finish_render()

arcade.run()