# Curriculum Tracker Frontend

The frontend for the Curriculum Progress Tracker application built with Next.js.

## Local Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

## Deployment to Render

### Option 1: Deploy via Render UI

1. Push your code to GitHub
2. Log in to [Render](https://app.render.com/)
3. Click "Add new site" > "Import an existing project"
4. Select your GitHub repository
5. Configure the build settings:
   - Base directory: `frontend`
   - Build Command: `rm -rf node_modules && npm install && npm run build`
   - Publish directory: `.next`
6. Click "Deploy site"

### Option 2: Deploy via Render CLI

1. Install Render CLI:
   ```bash
   npm install -g render-cli
   ```

2. Login to Render:
   ```bash
   render login
   ```

3. Initialize Render in your project:
   ```bash
   cd frontend
   render init
   ```

4. Follow the prompts to create a new site or connect to an existing one

5. Deploy your site:
   ```bash
   render deploy
   ```

## Environment Variables

The following environment variables need to be set in Render:

- `NEXT_PUBLIC_API_URL` - URL of the backend API

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
