import React, { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { Toaster } from 'react-hot-toast'

// Simple Button Component (inline for now)
interface ButtonProps {
  children: React.ReactNode
  onClick?: () => void
  variant?: 'primary' | 'secondary' | 'outline'
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

function Button({ 
  children, 
  onClick, 
  variant = 'primary', 
  size = 'md', 
  className = '' 
}: ButtonProps) {
  const baseClasses = 'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 disabled:pointer-events-none disabled:opacity-50'
  
  const variantClasses = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700',
    secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200',
    outline: 'border border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
  }
  
  const sizeClasses = {
    sm: 'h-9 px-3 text-sm',
    md: 'h-10 px-4 py-2',
    lg: 'h-11 px-8 text-lg'
  }
  
  return (
    <button
      onClick={onClick}
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`}
    >
      {children}
    </button>
  )
}

// Landing Page Component
function LandingPage() {
  const [ideas, setIdeas] = useState<string[]>([])

  const handleCreateIdea = () => {
    const newIdea = `Idea ${ideas.length + 1}: AI-powered solution`
    setIdeas([...ideas, newIdea])
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <div className="flex items-center">
              <div className="text-2xl font-bold text-blue-600">
                💡 IdeaArchitect
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Button variant="outline">Login</Button>
              <Button>Get Started</Button>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center">
          <h1 className="text-4xl sm:text-6xl font-extrabold text-gray-900 mb-6">
            <span className="block">From Spontaneous Ideas</span>
            <span className="block text-blue-600">to Structured Success</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Transform your startup ideas into structured mind maps and actionable Jira-style task breakdowns with AI-powered insights.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button onClick={handleCreateIdea} size="lg">
              🚀 Create Your First Idea
            </Button>
            <Button variant="outline" size="lg">
              📖 View Demo
            </Button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="bg-white rounded-lg p-6 shadow-md">
            <div className="text-3xl mb-4">🤖</div>
            <h3 className="text-xl font-semibold mb-2">AI-Powered Analysis</h3>
            <p className="text-gray-600">
              Get instant insights on problem analysis, market validation, and revenue models.
            </p>
          </div>
          
          <div className="bg-white rounded-lg p-6 shadow-md">
            <div className="text-3xl mb-4">🗺️</div>
            <h3 className="text-xl font-semibold mb-2">Visual Mind Maps</h3>
            <p className="text-gray-600">
              Transform ideas into interactive mind maps for better visualization and structure.
            </p>
          </div>
          
          <div className="bg-white rounded-lg p-6 shadow-md">
            <div className="text-3xl mb-4">📋</div>
            <h3 className="text-xl font-semibold mb-2">Jira-Style Tasks</h3>
            <p className="text-gray-600">
              Automatically generate epics, stories, and tasks for actionable execution.
            </p>
          </div>
        </div>
      </section>

      {/* Ideas Demo Section */}
      {ideas.length > 0 && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-6">Your Ideas</h2>
            <div className="space-y-4">
              {ideas.map((idea, index) => (
                <div key={index} className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                  <div className="flex items-center justify-between">
                    <span className="font-medium">{idea}</span>
                    <div className="flex space-x-2">
                      <span className="px-2 py-1 bg-green-100 text-green-800 rounded text-sm">
                        Ready for Analysis
                      </span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <p className="text-lg font-semibold mb-4">IdeaArchitect</p>
            <p className="text-gray-400">
              Built with ❤️ for entrepreneurs and innovators worldwide
            </p>
            <div className="mt-4 text-sm text-gray-500">
              Backend: Node.js + PostgreSQL + OpenAI | Frontend: React + TypeScript + Tailwind
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}

// Create React Query client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
})

// Main App Component
function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/auth/*" element={<div>Auth Pages Coming Soon</div>} />
          <Route path="/dashboard/*" element={<div>Dashboard Coming Soon</div>} />
          <Route path="/ideas/*" element={<div>Ideas Management Coming Soon</div>} />
          <Route path="/mindmap/*" element={<div>Mind Mapping Coming Soon</div>} />
        </Routes>
        <Toaster position="top-right" />
      </Router>
    </QueryClientProvider>
  )
}

export default App