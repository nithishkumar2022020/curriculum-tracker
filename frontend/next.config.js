/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: '/curriculum-tracker',
  assetPrefix: '/curriculum-tracker',
  trailingSlash: true,
}

module.exports = nextConfig 