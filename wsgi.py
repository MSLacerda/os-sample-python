# -*- coding: utf-8 -*-

from routes import routers 
import os

application = routers.application;


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)