import requests

'''response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

filterData = [item for item in data if len(item["title"].split()) <= 6]
print(f"Filtered results for GET  6 words:",filterData)

filterData = [item for item in filterData if len(item["body"].split("\n")) <= 3]
print(f"Filtered results for GET  3 lines:",filterData)
print("--------------------------------------------------------------")

data={"title": "New Post Title", "body": "New Post Body"}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(f"Response from POST call to posts endpoint:",response.json())

data = {"id": 1, "title": "Updated Post Title", "body": "Updated Post Body"}
id=1
response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{id}", json=data)
print(f"Response from PUT call to posts endpoint:",response.json())

response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{id}")
print(f"Response from DELETE call to posts endpoint:",response.status_code)'''

# Get posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

# Filter posts with titles containing more than 6 words
filtered_posts = [post for post in posts if len(post['title'].split()) <= 6]
print('Posts with titles containing more than 6 words filtered out:')
print(filtered_posts)

# Get comments
response = requests.get('https://jsonplaceholder.typicode.com/comments')
comments = response.json()

# Filter comments with descriptions containing more than 3 lines
filtered_comments = [comment for comment in comments if len(comment['body'].split('\n')) <= 3]
print('Comments with descriptions containing more than 3 lines filtered out:')
print(filtered_comments)

# POST requests

# Create a new post
new_post = {
    'title': 'New Post Title',
    'body': 'New Post Body',
    'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
if response.status_code == 201:
    print('Post created successfully:')
    print(response.json())
else:
    print('Error creating post:', response.status_code)

# Create a new comment
new_comment = {
    'postId': 1,
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'body': 'New Comment Body'
}

response = requests.post('https://jsonplaceholder.typicode.com/comments', json=new_comment)
if response.status_code == 201:
    print('Comment created successfully:')
    print(response.json())
else:
    print('Error creating comment:', response.status_code)

# PUT requests

# Update an existing post
existing_post_id = 1
updated_post = {
    'id': existing_post_id,
    'title': 'Updated Post Title',
    'body': 'Updated Post Body'
}

response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{existing_post_id}', json=updated_post)
if response.status_code == 200:
    print('Post updated successfully:')
    print(response.json())
else:
    print('Error updating post:', response.status_code)

# Update an existing comment
existing_comment_id = 1
updated_comment = {
    'id': existing_comment_id,
    'email': 'updated@example.com',
    'body': 'Updated Comment Body'
}

response = requests.put(f'https://jsonplaceholder.typicode.com/comments/{existing_comment_id}', json=updated_comment)
if response.status_code == 200:
    print('Comment updated successfully:')
    print(response.json())
else:
    print('Error updating comment:', response.status_code)

# DELETE requests

# Delete an existing post
existing_post_id = 1

response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{existing_post_id}')
if response.status_code == 200:
    print('Post deleted successfully')
else:
    print('Error deleting post:', response.status_code)

# Delete an existing comment
existing_comment_id = 1

response = requests.delete(f'https://jsonplaceholder.typicode.com/comments/{existing_comment_id}')
if response.status_code == 200:
    print('Comment deleted successfully')
else:
    print('Error deleting comment:', response.status_code)