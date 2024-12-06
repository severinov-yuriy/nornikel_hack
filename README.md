# nornikel_hack

    nornikel_hack/
    ├── .github/
    │   └── workflows/
    │       └── deploy.yml
    ├── .vscode/
    │   └── settings.json/
    ├── client/                 # Фронт
    │   ├── public
    |   |   ├── favicon.ico
    |   |   └── robots.txt
    │   ├── server
    |   |   └── tsconfig.json
    │   ├── src/
    |   |   ├── app
    |   |   |   ├── assets
    |   |   |   |   └── scss
    |   |   |   |       └── main.scss
    |   |   |   ├── layouts
    |   |   |   |       └── default.vue
    |   |   |   ├── routes
    |   |   |   |       └── index.vue
    |   |   ├── features
    |   |   |   ├── theme-toggle
    |   |   |   |   ├── index.ts
    |   |   |   |   └── ui
    |   |   |   |       └── ThemeToggle.vue
    |   |   ├── pages
    |   |   |   ├── home
    |   |   |   |   ├── index.ts
    |   |   |   |   └── ui
    |   |   |   |       └── HomePage.vue
    |   |   └── widgets
    |   |       └── header
    |   |           ├── index.ts
    |   |           └── ui
    |   |               └── VHeader.vue
    |   ├── tailwind.config
    |   ├── .dockerignore
    |   ├── .gitignore
    |   ├── .prettierrc.json
    |   ├── app.config.ts
    |   ├── eslint.config.js
    |   ├── nuxt.config.ts
    |   ├── package-lock.json
    |   ├── package.json
    |   ├── tailwind.config.js
    |   ├── tsconfig.json
    |   ├── Dockerfile
    |   └── README.md               # Документация
    ├── app/                    # Бэк
    │   ├── app/
    |   │   │   ├── main.py              # Запуск API
    |   │   │   ├── config.py            # Конфигурация API
    |   │   │   └── routes/
    |   │   │       ├── upload.py        # Эндпоинт загрузки данных
    |   │   │       └── query.py         # Эндпоинт обработки запроса
    |   ├── src/
    |   ├── requirements.txt        # Зависимости
    |   ├── Dockerfile
    |   └── README.md               # Документация
    ├── docker-compose.yml
    └── README.md               # Документация

