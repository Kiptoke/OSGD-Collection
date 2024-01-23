// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    meta: {
        title: 'Open Source Game Dev',
    },
    modules: [
        '@inkline/plugin/nuxt',
        '@nuxtjs/supabase',
        'nuxt-api-party'
    ],
    devtools: { enabled: true },
    supabase: {
        redirect: false
    },
    inkline: {
        /**
         * @inkline/inkline
         * @description provides configuration file specific options
         */

        globals: {
            color: '',
            colorMode: 'system',
            colorModeStrategy: 'localStorage',
            componentOptions: {},
            locale: 'en',
            size: '',
            validateOn: ['input', 'blur']
        },

        /**
         * @inkline/plugin
         * @description provides import specific options
         */

        import: {
            mode: 'auto',
            scripts: true,
            styles: true,
            utilities: true
        }
    },
    apiParty: {
        endpoints: {
            github: {
                url: "https://api.github.com",
                // Global headers sent with each request
                headers: {
                    Authorization: "Bearer " + process.env.GITHUB_PAT
                }
            }
        }
    }
});
