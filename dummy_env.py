# Remove the comment from the import statement below:

# import os

# Application secret key

os.environ.setdefault(
    "SECRET_KEY", "")

# Stripe

os.environ.setdefault(
    "STRIPE_PUBLIC_KEY", "")

os.environ.setdefault(
    "STRIPE_SECRET_KEY", "")

os.environ.setdefault("STRIPE_WH_SECRET",
                      "")

# Gmail user and password

os.environ.setdefault(
    "EMAIL_HOST_PASS", "")

os.environ.setdefault("EMAIL_HOST_USER", "")

# Google social

os.environ.setdefault(
    "SOCIAL_CLIENT_ID", "")

os.environ.setdefault("SOCIAL_SECRET_KEY", "")

os.environ.setdefault(
    "SOCIAL_KEY", "")

# Posgres database

os.environ.setdefault(
    "DATABASE_URL", "")
