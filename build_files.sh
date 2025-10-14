#!/bin/bash
echo "🔧 Starting Vercel build process..."

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🧹 Collecting static files..."
export DJANGO_SETTINGS_MODULE=storefront.settings.prod
python3 manage.py collectstatic --noinput --clear

echo "✅ Build process complete."
