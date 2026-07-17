#email slicer

email=input("Enter your email:\n")
email_parts=email.split('@')
username=email_parts[0]
domain=email_parts[1]

print(f'Your username {username} and domain {domain}')
