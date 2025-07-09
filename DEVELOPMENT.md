# 🔧 Development Guide - IdeaArchitect

## Quick Start Commands

### Installation & Setup
```bash
# Install root dependencies  
npm install

# Install backend dependencies
cd backend && npm install

# Generate Prisma client
npm run db:generate

# Copy environment file
cp .env.example .env
# Edit .env with your database URL and OpenAI API key
```

### Database Setup
```bash
# Make sure PostgreSQL is running, then:
npm run db:push       # Push schema to database
npm run db:migrate    # Run migrations (alternative)
```

### Development Server
```bash
# Start backend development server
npm run dev:backend   # Runs on http://localhost:3001

# Health check
curl http://localhost:3001/health
```

## 🧪 Testing the API

### 1. Health Check
```bash
curl http://localhost:3001/health
```

### 2. Register User
```bash
curl -X POST http://localhost:3001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpassword123",
    "name": "Test User"
  }'
```

### 3. Login User
```bash
curl -X POST http://localhost:3001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpassword123"
  }'
```

### 4. Create Idea (replace JWT_TOKEN)
```bash
curl -X POST http://localhost:3001/api/ideas \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer JWT_TOKEN_HERE" \
  -d '{
    "title": "AI Recipe Generator",
    "description": "An app that generates personalized recipes based on dietary preferences, available ingredients, and cooking time constraints using AI.",
    "category": "Food & Tech",
    "tags": ["AI", "Food", "Recipes", "Personalization"]
  }'
```

### 5. Get Ideas
```bash
curl -H "Authorization: Bearer JWT_TOKEN_HERE" \
  http://localhost:3001/api/ideas
```

## 📊 Database Management

### View Database
```bash
# Start Prisma Studio
npx prisma studio
# Opens at http://localhost:5555
```

### Reset Database
```bash
npm run db:push --force-reset
```

### Migrations
```bash
npm run db:migrate
```

## 🔍 Debugging

### Check Logs
The server logs will show:
- Incoming requests
- AI analysis results
- Error messages
- Database operations

### Common Issues

1. **Database Connection**: Make sure PostgreSQL is running and DATABASE_URL is correct
2. **OpenAI API**: Verify your API key is valid and has credits
3. **JWT Errors**: Check that JWT_SECRET is set
4. **CORS Issues**: Verify CORS_ORIGINS includes your frontend URL

## 🏗️ Project Structure Overview

```
backend/src/
├── controllers/     # HTTP request handlers
├── middleware/      # Express middleware
├── routes/          # API route definitions  
├── services/        # Business logic (AI, etc.)
├── utils/           # Helper functions
├── prisma/          # Database schema
└── server.ts        # Main server file
```

## ⚡ Quick Development Tips

1. **Auto-restart**: The dev server uses nodemon for automatic restarts
2. **Type Safety**: Full TypeScript support with strict typing
3. **Validation**: All inputs validated with Zod schemas
4. **Error Handling**: Comprehensive error responses
5. **AI Fallbacks**: Graceful degradation if OpenAI is unavailable

## 🚀 Next Steps

1. Set up database and test endpoints
2. Verify AI integration works
3. Start frontend development
4. Implement mind mapping
5. Add task generation
6. Deploy to production

## 📝 Environment Variables Checklist

- [ ] `DATABASE_URL` - PostgreSQL connection string
- [ ] `JWT_SECRET` - Secure random string for JWT signing
- [ ] `OPENAI_API_KEY` - Your OpenAI API key
- [ ] `PORT` - Server port (default: 3001)
- [ ] `NODE_ENV` - Environment (development/production)

**Happy coding! 🎉**