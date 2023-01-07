import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import { VitePWA } from "vite-plugin-pwa"

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        VitePWA({
            includeAssets: ['favicon.ico'],
            workbox: {
                globPatterns: ['**\/*.{js,css,html,svg,mp4}'],
                // navigateFallback: '/index.html',
                cleanupOutdatedCaches: true,
                cacheId: 'bigboxgas',
                runtimeCaching: [
                    {
                        urlPattern: /^http:\/\/.*\/api\/.*/,
                        handler: 'NetworkOnly',
                    },
                    {
                        urlPattern: /\/api\/.*/,
                        handler: 'NetworkOnly'
                    },
                    {
                        urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,
                        handler: 'CacheFirst',
                        options: {
                          cacheName: 'google-fonts-cache',
                          expiration: {
                            maxEntries: 10,
                            maxAgeSeconds: 60 * 60 * 24 * 365 // <== 365 days
                          },
                          cacheableResponse: {
                            statuses: [0, 200]
                          }
                        }
                      },
                      {
                        urlPattern: /^https:\/\/fonts\.gstatic\.com\/.*/i,
                        handler: 'CacheFirst',
                        options: {
                          cacheName: 'gstatic-fonts-cache',
                          expiration: {
                            maxEntries: 10,
                            maxAgeSeconds: 60 * 60 * 24 * 365 // <== 365 days
                          },
                          cacheableResponse: {
                            statuses: [0, 200]
                          },
                        }
                      }
                ],
                // mode: 'development',
                navigateFallbackDenylist: [
                    /\/api\/.*/,
                    /\/privacy/,
                    /\/.well-known\/.*/
                ]
            },
            manifest: {
                name: 'Big Box Gas',
                short_name: 'Big Box Gas',
                description: 'Gas is expensive, less so at big box retailers.',
                start_url: '/',
                background_color: '#d5d5d5',
                theme_color: '#d5d5d5',
                scope: '/',
                display: 'standalone',
                icons: [
                    {
                        src: '/any-192x192.png',
                        sizes: '192x192',
                        type: 'image/png',
                        purpose: 'any'
                    },
                    {
                        src: '/any-512x512.png',
                        sizes: '512x512',
                        type: 'image/png',
                        purpose: 'any'
                    },
                    {
                        src: '/masked-192x192.png',
                        sizes: '192x192',
                        type: 'image/png',
                        purpose: 'maskable'
                    },
                    {
                        src: '/masked-512x512.png',
                        sizes: '512x512',
                        type: 'image/png',
                        purpose: 'maskable'
                    }
                ]

            },
            manifestFilename: 'manifest.json'
        })
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})
