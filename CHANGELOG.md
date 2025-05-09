# CHANGELOG


## v0.1.2 (2025-05-09)

### Documentation

- Update footer in README file
  ([`005111f`](https://github.com/labtst-online/fast-auth_service/commit/005111fbfd621adf859ad16410dc31849fa1a98a))

- Update README file. Use organization name.
  ([`96cc295`](https://github.com/labtst-online/fast-auth_service/commit/96cc295644486b68059a4360b917969f0d238f57))

### Refactoring

- Change description in pyproject.toml.
  ([`14b7328`](https://github.com/labtst-online/fast-auth_service/commit/14b732877513fd3db475c9387e72e6885e66bce4))


## v0.1.1 (2025-05-09)

### Bug Fixes

- Add permissions for contents and packages in CD workflow
  ([`c608d33`](https://github.com/labtst-online/fast-auth_service/commit/c608d3329a7a0b74d0ebce375379e756e9568dde))

- Make rebranding
  ([`a915da6`](https://github.com/labtst-online/fast-auth_service/commit/a915da6662fb4bf4d0079c6437f56b7fed511f6b))

- Refactor CD workflow to use workflow_run for CI success confirmation and streamline release
  process
  ([`c68cb74`](https://github.com/labtst-online/fast-auth_service/commit/c68cb74bd67dfce8a0c16c2a58044ae35c0f9ece))

- Update Dockerfile and .dockerignore for improved dependency management and build efficiency
  ([`8926865`](https://github.com/labtst-online/fast-auth_service/commit/892686569e78ad6574501f1f5c56960a88819510))

- Update semantic release configuration for release management in pyproject.toml
  ([`e0b6a5c`](https://github.com/labtst-online/fast-auth_service/commit/e0b6a5c80abc9b83ecd9f36221bcb7880eb7afd8))

### Chores

- Update README to format GitHub Actions section as a list
  ([`160416a`](https://github.com/labtst-online/fast-auth_service/commit/160416a582905efca49e3ba05c9d8c9e4fb1dd9e))


## v0.1.0 (2025-05-07)

### Bug Fixes

- Correct service name formatting in CD workflow
  ([`d4c0b41`](https://github.com/labtst-online/fast-auth_service/commit/d4c0b41b99f212f0409158b0fe948779c67a1f26))

- Remove feature branch trigger from CD workflow
  ([`f9b3937`](https://github.com/labtst-online/fast-auth_service/commit/f9b3937ca44452b3abf34dcee9ec6d7e2512f01c))

- Remove UV installation step and streamline python-semantic-release setup
  ([`afefd1a`](https://github.com/labtst-online/fast-auth_service/commit/afefd1a69b8e74d0de9234bdd1a4d1ac3120268a))

- **auth**: Change exposed port from 8001 to 8000 in Dockerfile
  ([`f0b4952`](https://github.com/labtst-online/fast-auth_service/commit/f0b4952ab857935f02dff5755c264eab2a3e9c63))

### Code Style

- Code styling using ruff formater
  ([`aa0e648`](https://github.com/labtst-online/fast-auth_service/commit/aa0e648b24112e7382dfcad242e58a2f2b8ef74f))

### Features

- Add CD workflows for continuous delivery. Update CI.
  ([`3c8f400`](https://github.com/labtst-online/fast-auth_service/commit/3c8f400b426a48ee17b6acf01a20bbb16950374d))

- Add initial implementation of Auth Service with FastAPI and database configuration
  ([`965b26a`](https://github.com/labtst-online/fast-auth_service/commit/965b26a7a1771a8051cdf3db70f011c171e175b0))

- Add python-semantic-release package. Update main.py.
  ([`7aa3221`](https://github.com/labtst-online/fast-auth_service/commit/7aa32216ceea5fbd60bad4376195e965255010b7))

- Update python version to 3.13. Add dockerignore
  ([`6a0ecfc`](https://github.com/labtst-online/fast-auth_service/commit/6a0ecfce52cbd6b1a9e2f6d8004697a3e37d7440))

- **auth**: Add alembic migrations and make some code refactors
  ([`9321e2e`](https://github.com/labtst-online/fast-auth_service/commit/9321e2ed183149b514d07f079c0ac9072c3ad6d4))

- **auth**: Add Dockerfile and entrypoint script for auth service
  ([`a5bb0bc`](https://github.com/labtst-online/fast-auth_service/commit/a5bb0bc3760b3419da11623fb266c480eb3cfc02))

- **auth**: Add FastAPI Users schemas, UserManager and make some refactors
  ([`38ec9e7`](https://github.com/labtst-online/fast-auth_service/commit/38ec9e706e25a5022f6f0a1080b338f4fcec2293))

- **auth**: Add SECRET_KEY config for FastAPI Users
  ([`f91bbf4`](https://github.com/labtst-online/fast-auth_service/commit/f91bbf43cd4a25bc4030233ac63cca33f1420bbd))

- **auth**: Adjust project root path and clean import statements in alembic env
  ([`7413ae6`](https://github.com/labtst-online/fast-auth_service/commit/7413ae663bd182ef19244b551b28d14239e0daec))

- **auth**: Configure JWT authentication backend
  ([`46fcfa8`](https://github.com/labtst-online/fast-auth_service/commit/46fcfa8a5cab6b61b303d172aa812a3ca67a0d36))

- **auth**: Implement async database connection
  ([`501b127`](https://github.com/labtst-online/fast-auth_service/commit/501b12735ea264cd6852d7ae69209376efe64408))

- **auth**: Initial setup, config loading, and dependencies
  ([`27a0fbf`](https://github.com/labtst-online/fast-auth_service/commit/27a0fbfa87fdc3fa0c1f5658eb860381903eb398))

- **auth**: Integrate FastAPI Users routers into main app
  ([`7170c57`](https://github.com/labtst-online/fast-auth_service/commit/7170c57bcc2e1c5e4463fc0d73a516eac01974b1))

- **auth**: Refactor code and devide routes
  ([`b806239`](https://github.com/labtst-online/fast-auth_service/commit/b806239d5b876cc60fd8b578a7149805bf9c8567))

- **auth**: Rename packages
  ([`1efa25b`](https://github.com/labtst-online/fast-auth_service/commit/1efa25b4b4b428a843fb518bce36dd12eee7edc6))

- **auth**: Setting up security file
  ([`33f1317`](https://github.com/labtst-online/fast-auth_service/commit/33f1317ccd0ab30f33d40f3e975d5f7905b40fc6))
