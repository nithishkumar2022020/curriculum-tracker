/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  reactStrictMode: true,
  experimental: {
    outputFileTracingRoot: undefined,
    outputFileTracingIncludes: {
      '/**/*': ['./public/**/*'],
    },
  },
  server: {
    port: process.env.PORT || 1000,
    hostname: '0.0.0.0',
  },
}

module.exports = nextConfig 