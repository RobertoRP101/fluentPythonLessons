# Example: Comprehensive list of tasks for a project

tasks = [
    {
        "task_id": 1,
        "title": "Project Initialization",
        "description": "Set up project repository and initial documentation.",
        "status": "Completed",
        "priority": "High",
        "due_date": "2024-08-15"
    },
    {
        "task_id": 2,
        "title": "Database Schema Design",
        "description": "Design the initial database schema for the application.",
        "status": "In Progress",
        "priority": "Medium",
        "due_date": "2024-08-20"
    },
    {
        "task_id": 3,
        "title": "API Development",
        "description": "Develop RESTful APIs for user authentication and data retrieval.",
        "status": "Not Started",
        "priority": "High",
        "due_date": "2024-08-25"
    },
    {
        "task_id": 4,
        "title": "Frontend Development",
        "description": "Create the user interface using React and Bootstrap.",
        "status": "Not Started",
        "priority": "Medium",
        "due_date": "2024-08-30"
    },
    {
        "task_id": 5,
        "title": "Testing and QA",
        "description": "Perform unit testing and end-to-end testing of the application.",
        "status": "Not Started",
        "priority": "High",
        "due_date": "2024-09-05"
    },
    {
        "task_id": 6,
        "title": "Deployment",
        "description": "Deploy the application to the production server.",
        "status": "Not Started",
        "priority": "High",
        "due_date": "2024-09-10"
    }
]

# Print out the list in a readable format
for task in tasks:
    print(f"Task ID: {task['task_id']}")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Status: {task['status']}")
    print(f"Priority: {task['priority']}")
    print(f"Due Date: {task['due_date']}\n")
