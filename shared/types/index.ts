// Shared types for IdeaArchitect application
export interface User {
  id: string;
  email: string;
  name: string;
  avatar?: string;
  createdAt: string;
  updatedAt: string;
}

export interface AuthResponse {
  user: User;
  token: string;
  expiresAt: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  password: string;
  name: string;
}

// Idea Types
export enum IdeaStatus {
  DRAFT = 'DRAFT',
  ANALYZING = 'ANALYZING',
  STRUCTURED = 'STRUCTURED',
  PLANNED = 'PLANNED',
  ARCHIVED = 'ARCHIVED'
}

export interface Idea {
  id: string;
  title: string;
  description: string;
  category?: string;
  tags: string[];
  status: IdeaStatus;
  aiAnalysis?: AIAnalysis;
  createdAt: string;
  updatedAt: string;
  userId: string;
  mindMap?: MindMap;
  tasks: Task[];
}

export interface CreateIdeaRequest {
  title: string;
  description: string;
  category?: string;
  tags?: string[];
}

export interface UpdateIdeaRequest {
  title?: string;
  description?: string;
  category?: string;
  tags?: string[];
  status?: IdeaStatus;
}

// AI Analysis Types
export interface AIAnalysis {
  problem: string;
  solution: string;
  targetAudience: string;
  revenueModel: string;
  marketSize?: string;
  competitors?: string[];
  keyFeatures?: string[];
  risks?: string[];
  opportunities?: string[];
  suggestedCategories?: string[];
  confidence: number; // 0-1 score
}

// Mind Map Types
export interface MindMapNode {
  id: string;
  type: string;
  position: { x: number; y: number };
  data: {
    label: string;
    description?: string;
    category?: string;
    color?: string;
  };
}

export interface MindMapEdge {
  id: string;
  source: string;
  target: string;
  type?: string;
  animated?: boolean;
  label?: string;
}

export interface MindMap {
  id: string;
  nodes: MindMapNode[];
  edges: MindMapEdge[];
  layout?: Record<string, any>;
  createdAt: string;
  updatedAt: string;
  ideaId: string;
}

// Task Types
export enum TaskType {
  EPIC = 'EPIC',
  STORY = 'STORY',
  TASK = 'TASK',
  BUG = 'BUG',
  SUBTASK = 'SUBTASK'
}

export enum Priority {
  LOW = 'LOW',
  MEDIUM = 'MEDIUM',
  HIGH = 'HIGH',
  URGENT = 'URGENT'
}

export enum TaskStatus {
  TODO = 'TODO',
  IN_PROGRESS = 'IN_PROGRESS',
  IN_REVIEW = 'IN_REVIEW',
  DONE = 'DONE',
  BLOCKED = 'BLOCKED'
}

export interface Task {
  id: string;
  title: string;
  description?: string;
  type: TaskType;
  priority: Priority;
  status: TaskStatus;
  storyPoints?: number;
  acceptanceCriteria: string[];
  parentId?: string;
  order: number;
  createdAt: string;
  updatedAt: string;
  ideaId: string;
  children?: Task[];
}

export interface CreateTaskRequest {
  title: string;
  description?: string;
  type?: TaskType;
  priority?: Priority;
  storyPoints?: number;
  acceptanceCriteria?: string[];
  parentId?: string;
}

// API Response Types
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface PaginatedResponse<T> {
  success: boolean;
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

// Error Types
export interface ApiError {
  message: string;
  code: string;
  details?: Record<string, any>;
}