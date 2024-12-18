// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2024-11-01',
    devtools: { enabled: false },
    modules: ['@nuxt/ui', '@pinia/nuxt', 'nuxt-mdi'],
    css: ['./src/app/assets/scss/main.scss'],
    alias: {
        '@': '../src',
    },
    dir: {
        pages: './src/app/routes',
        layouts: './src/app/layouts',
    },
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    ssr: false,
})