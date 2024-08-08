import subprocess

result = subprocess.run(['python', 'generate_blog_post.py'], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)