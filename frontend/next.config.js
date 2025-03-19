/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  reactStrictMode: true,
  basePath: '/curriculum-tracker',
  images: {
    unoptimized: true,
  },
}

module.exports = nextConfig 