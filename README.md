# 🚀 IdeaArchitect

**"From Spontaneous Ideas to Structured Success"**

Transform your spontaneous startup ideas into structured mind maps and actionable Jira-style task breakdowns with AI-powered insights.

## 🌟 Overview

IdeaArchitect is a full-stack web application that helps entrepreneurs and innovators capture, structure, and execute their startup ideas through:

- **Intelligent Idea Management**: Quick capture with AI-powered analysis
- **Visual Mind Mapping**: Interactive mind maps to visualize idea structures  
- **Jira-Style Task Generation**: Automatic breakdown into epics, stories, and tasks
- **AI-Enhanced Features**: Problem analysis, solution validation, and expansion suggestions

## 🛠️ Tech Stack

### Backend (Completed)
- **Node.js** + **Express.js** + **TypeScript**
- **PostgreSQL** with **Prisma ORM** 
- **JWT Authentication** with secure session management
- **OpenAI API** integration for AI-powered features
- **Zod** validation schemas
- **bcryptjs** for password hashing
- **Security**: Helmet, CORS, Rate limiting

### Frontend (Coming Next)
- **React.js** + **TypeScript** + **Vite**
- **Tailwind CSS** + **ShadCN/UI** components
- **React Flow** for interactive mind mapping
- **React Query** for server state management

## 📊 Database Schema

Our robust database design supports the complete idea-to-execution workflow:

```sql
Users -> Ideas -> MindMaps
              -> Tasks (hierarchical: Epic > Story > Task)
              -> AI Analysis (JSON insights)
```

### Key Models:
- **User**: Authentication and profile management
- **Idea**: Core idea storage with status tracking
- **MindMap**: Visual representation with nodes/edges
- **Task**: Jira-style task hierarchy with full metadata
- **Session**: Secure JWT session management

## 🔥 Core Features Implemented

### ✅ Authentication System
- User registration with validation
- Secure login/logout with JWT tokens
- Session management with expiration
- Password hashing with bcrypt
- Token refresh capabilities

### ✅ Idea Management 
- **CRUD Operations**: Create, read, update, delete ideas
- **Smart Search**: Full-text search with filters
- **Categorization**: Organize ideas by category and tags
- **Status Tracking**: Draft → Analyzing → Structured → Planned → Archived

### ✅ AI-Powered Analysis
- **Automated Analysis**: Extract problem, solution, target audience, revenue model
- **Market Intelligence**: Competitors, market size, key features identification
- **Risk Assessment**: Potential risks and opportunities analysis
- **Idea Expansion**: AI-generated related concepts and features
- **Confidence Scoring**: AI confidence metrics for reliability

### ✅ Advanced API Features
- **Pagination**: Efficient data loading with limits
- **Filtering**: By category, status, date ranges
- **Sorting**: Multiple sort options with order control
- **Validation**: Comprehensive input validation with Zod
- **Error Handling**: Structured error responses
- **Rate Limiting**: API protection against abuse

## 🌐 API Endpoints

### Authentication
```
POST   /api/auth/register     # Register new user
POST   /api/auth/login        # User login  
POST   /api/auth/logout       # User logout
GET    /api/auth/me           # Get current user
POST   /api/auth/refresh      # Refresh token
```

### Ideas Management
```
POST   /api/ideas             # Create new idea
GET    /api/ideas             # Get all user ideas (paginated)
GET    /api/ideas/:id         # Get specific idea
PUT    /api/ideas/:id         # Update idea
DELETE /api/ideas/:id         # Delete idea
POST   /api/ideas/:id/analyze # Trigger AI analysis
POST   /api/ideas/:id/expand  # Get expansion suggestions
```

### Mind Maps & Tasks (Ready for Implementation)
```
PUT    /api/mindmaps/:ideaId  # Update mind map
POST   /api/tasks             # Create tasks from mind map
```

## 🤖 AI Integration Features

### Idea Analysis Pipeline
1. **Problem Identification**: What problem does this solve?
2. **Solution Validation**: How does it provide value?
3. **Market Analysis**: Target audience and market size
4. **Business Model**: Revenue streams and monetization
5. **Competitive Landscape**: Similar solutions and differentiators
6. **Feature Extraction**: Core features and capabilities
7. **Risk Assessment**: Potential challenges and mitigation

### AI-Generated Insights
```typescript
interface AIAnalysis {
  problem: string;           // Core problem being solved
  solution: string;          // Proposed solution approach  
  targetAudience: string;    // Primary user segments
  revenueModel: string;      // Monetization strategy
  marketSize?: string;       // Total addressable market
  competitors?: string[];    // Competitive analysis
  keyFeatures?: string[];    // Essential product features
  risks?: string[];          // Potential challenges
  opportunities?: string[];  // Growth opportunities
  confidence: number;        // AI confidence score (0-1)
}
```

## 🏗️ Project Structure

```
ideaarchitect/
├── backend/                    # Node.js API Server
│   ├── src/
│   │   ├── controllers/        # Request handlers
│   │   │   ├── auth.controller.ts     # Authentication logic
│   │   │   ├── ideas.controller.ts    # Idea management
│   │   │   └── ...
│   │   ├── middleware/         # Express middleware
│   │   │   ├── auth.middleware.ts     # JWT authentication  
│   │   │   ├── error.middleware.ts    # Error handling
│   │   │   └── notFound.middleware.ts # 404 handling
│   │   ├── routes/             # API route definitions
│   │   ├── services/           # Business logic
│   │   │   ├── ai.service.ts          # OpenAI integration
│   │   │   └── ...
│   │   ├── utils/              # Helper functions
│   │   │   ├── database.ts            # Prisma client
│   │   │   ├── validation.ts          # Zod schemas
│   │   │   └── ...
│   │   ├── prisma/             # Database management
│   │   │   └── schema.prisma          # Database schema
│   │   └── server.ts           # Express app setup
│   ├── package.json
│   └── .env.example           # Environment variables template
├── shared/                     # Shared TypeScript types
│   └── types/index.ts         # Common interfaces
├── frontend/                   # React app (next phase)
└── docs/                      # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ and npm
- PostgreSQL database
- OpenAI API key

### 1. Environment Setup
```bash
# Clone the repository
git clone <repository-url>
cd ideaarchitect

# Install dependencies
npm run install:all
```

### 2. Environment Configuration
```bash
# Copy environment template
cp backend/.env.example backend/.env

# Configure your environment variables:
DATABASE_URL="postgresql://username:password@localhost:5432/ideaarchitect_db"
JWT_SECRET="your-super-secret-jwt-key-here"
OPENAI_API_KEY="your-openai-api-key-here"
```

### 3. Database Setup
```bash
cd backend
npm run db:generate    # Generate Prisma client
npm run db:push        # Create database schema
```

### 4. Start Development Server
```bash
# Start backend server
npm run dev:backend    # Runs on http://localhost:3001

# Health check
curl http://localhost:3001/health
```

## 📝 API Usage Examples

### Register User
```bash
curl -X POST http://localhost:3001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepassword123",
    "name": "John Doe"
  }'
```

### Create Idea (with AI Analysis)
```bash
curl -X POST http://localhost:3001/api/ideas \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "AI-Powered Fitness Coach",
    "description": "A mobile app that uses AI to create personalized workout plans based on user goals, available equipment, and real-time form feedback using computer vision.",
    "category": "Health & Fitness",
    "tags": ["AI", "Fitness", "Mobile", "Computer Vision"]
  }'
```

### Get Ideas with Filtering
```bash
curl "http://localhost:3001/api/ideas?page=1&limit=10&category=Health&search=AI&sortBy=createdAt&sortOrder=desc" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: bcrypt with salt rounds for secure storage
- **Session Management**: Automatic session expiration and cleanup
- **Rate Limiting**: Protect against API abuse (100 requests/15min)
- **Input Validation**: Comprehensive validation with Zod schemas
- **CORS Protection**: Configured for specific origins
- **Helmet Security**: Standard security headers

## 🎯 Next Development Phase: Frontend

The backend foundation is complete! Next steps include:

1. **React Frontend Setup**: Component library with ShadCN/UI
2. **Authentication Flow**: Login/register forms with JWT handling
3. **Idea Dashboard**: Create, edit, view ideas with rich interface
4. **Interactive Mind Maps**: React Flow integration for visual mapping
5. **Task Management**: Jira-style task boards and hierarchy
6. **AI Integration UI**: Analysis results display and interaction
7. **Responsive Design**: Mobile-first approach with Tailwind CSS

## 🛡️ Environment Variables

Required environment variables for deployment:

```env
# Database
DATABASE_URL="postgresql://..."

# Authentication
JWT_SECRET="your-256-bit-secret"
JWT_EXPIRES_IN="7d"

# AI Services  
OPENAI_API_KEY="sk-..."

# Server Configuration
PORT=3001
NODE_ENV="production"
CORS_ORIGINS="https://yourdomain.com"

# Security
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
```

## 📊 Performance & Scalability

- **Database Indexing**: Optimized queries with proper indexes
- **Pagination**: Efficient data loading for large datasets
- **Caching Strategy**: Ready for Redis integration
- **Error Handling**: Graceful degradation for AI service failures
- **Rate Limiting**: Built-in API protection
- **Session Management**: Automatic cleanup of expired sessions

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT API integration
- Prisma team for excellent ORM
- Express.js community for robust framework
- All contributors and testers

---

**Built with ❤️ for entrepreneurs and innovators worldwide**

*Ready to turn your next big idea into structured success? Start with IdeaArchitect!*