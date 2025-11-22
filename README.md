# Trip Planner AI

A CrewAI-powered travel planning application that generates detailed itineraries using AI agents and Groq's fast language models.

## 🚀 Features

- **Multi-Agent Collaboration**: Uses specialized AI agents (Travel Expert, City Selection Expert, Local Tour Guide) to create comprehensive travel plans
- **Detailed Itineraries**: Generates 7-day travel plans with daily activities, budgets, and packing suggestions
- **Smart City Selection**: Analyzes multiple cities based on weather, seasonal events, and travel costs to recommend the best destination
- **Web Search Integration**: Leverages internet search to provide up-to-date travel information
- **Cost Calculation**: Includes budget planning and cost calculations for your trip
- **Free & Fast**: Powered by Groq's API for fast, cost-effective AI responses

## 🛠️ Tech Stack

- **CrewAI**: Multi-agent framework for orchestrating AI tasks
- **LangChain**: LLM development framework
- **Groq**: Fast language model inference (replaces OpenAI)
- **LangChain-Groq**: Integration between LangChain and Groq
- **Python**: Core programming language

## 📋 Prerequisites

- Python 3.8+
- Groq API Key (free tier available)
- Serper API Key (for web search functionality)

## How It Works

The application uses three specialized AI agents working together:
1. City Selection Expert: Analyzes multiple cities based on weather, seasonal events, prices, and your interests to recommend the best destination
2. Expert Travel Agent: Creates a detailed 7-day itinerary with daily plans, budget breakdown, packing suggestions, and safety tips
3. Local Tour Guide: Provides insights about the selected city's attractions, customs, and special events

The system performs these tasks:
1. Compares multiple cities for optimal travel experience
2. Gathers detailed city information and local insights
3. Creates comprehensive day-by-day travel plans
4. Provides budget breakdowns and practical travel advice


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
