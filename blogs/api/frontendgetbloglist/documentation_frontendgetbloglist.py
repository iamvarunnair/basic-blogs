# ---------------------- ALGORITHM ---------------------- #
# Step 1:   fetch all blogs.
# Step 2:   if no blogs found, return none found response else goto next step.
# Step 3:   start loop.
# Step 4:   from blogtoparagrapgmapping model joined with paragrapg model fetch first paragraph and paragrapg id mapped to each blog in looped to index in blog id list.
# Step 5:   if paragraph not found assign blog_body as none else goto next step.
# Step 6:   from paragraphtomediamapping model joined with media model fetch first image name.
# Step 7:   if image found assign it to blog_image else assign blog_image as None.
# Step 8:   end of loop.
# Step 9:   convert query set to list using list function and DjangoJSONEncoder.
# Step 10:  convert list to valid json string using json.dumps and assign to output_json['Payload'] var.
# Step 11:  return rendered template with output_json data.
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body ---------------------- #
# {
#     "Payload": {
#         "blog_list": [
#             {
#                 "blog_id": "1",
#                 "blog_title": "Test Tile 1",
#                 "blog_image": "images/test_image_1",
#             },
#             {
#                 "blog_id": "2",
#                 "blog_title": "Test Tile 2",
#                 "blog_image": "images/test_image_2",
#             },
#             {
#                 "blog_id": "3",
#                 "blog_title": "Test Tile 3",
#                 "blog_image": "images/test_image_3",
#             },
#             {
#                 "blog_id": "4",
#                 "blog_title": "Test Tile 4",
#                 "blog_image": "images/test_image_4",
#             },
#             {
#                 "blog_id": "5",
#                 "blog_title": "Test Tile 5",
#                 "blog_image": "images/test_image_5",
#             },
#             {
#                 "blog_id": "6",
#                 "blog_title": "Test Tile 6",
#                 "blog_image": "images/test_image_6",
#             },
#         ]
#     }
# }
# ---------------------- End ---------------------- #
