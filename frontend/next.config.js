/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: process.env.NODE_ENV === 'production' ? '/curriculum-tracker' : '',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/curriculum-tracker' : '',
  trailingSlash: true,
  distDir: 'out',
}

module.exports = nextConfig 