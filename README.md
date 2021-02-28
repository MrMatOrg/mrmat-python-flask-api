# MrMat :: Python :: Flask API

Boilerplate code for a Python Flask API

This variant of a Python Flask API is spec-first and using [Connexion](https://github.com/zalando/connexion) to 
implement that capability. Also see [Connexion Documentation](https://connexion.readthedocs.io/en/latest/)

Features:

* Spec-first
* Multiple API versions
* Configurability via command line
* No TLS, because this is intended to run behind a reverse proxy
* Healthz
* No OAuth 2, there are still some [issues](https://github.com/zalando/connexion/issues/549) with Connexion to support that
