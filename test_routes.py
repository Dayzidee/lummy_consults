#!/usr/bin/env python3
"""
Test script to verify all routes are working properly
"""

import os
import sys
from app import create_app, db
from config import config

def test_routes():
    """Test all application routes"""
    
    # Create app with testing configuration
    app = create_app(config['testing'])
    
    with app.test_client() as client:
        print("Testing Lummy Consults Application Routes...")
        print("=" * 50)
        
        # Test main routes
        routes_to_test = [
            ('/', 'Homepage'),
            ('/auth/login', 'Login Page'),
            ('/auth/register', 'Registration Page'),
            ('/tutors/tutors', 'Tutors List'),
            ('/recruitment/jobs', 'Jobs List'),
            ('/library/library', 'Library List'),
            ('/admin/dashboard', 'Admin Dashboard'),
        ]
        
        for route, description in routes_to_test:
            try:
                response = client.get(route)
                status = "✅ PASS" if response.status_code in [200, 302] else f"❌ FAIL ({response.status_code})"
                print(f"{description:20} | {route:25} | {status}")
            except Exception as e:
                print(f"{description:20} | {route:25} | ❌ ERROR: {str(e)}")
        
        print("=" * 50)
        print("Route testing completed!")

if __name__ == '__main__':
    test_routes()
