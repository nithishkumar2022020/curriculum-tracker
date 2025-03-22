/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: '/curriculum-tracker',
  assetPrefix: '/curriculum-tracker/',
  trailingSlash: true,
  distDir: 'out',
}

module.exports = nextConfig 