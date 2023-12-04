import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion_percentage, completed):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion_percentage = int(completion_percentage)
        self.completed = completed

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.estimate:,.2f}, completion: {self.completion_percentage}%"

    def is_completed(self):
        return self.completed

    def filter_by_date(self, filter_date):
        return self.start_date > filter_date

    def update_completion(self, new_percentage):
        self.completion_percentage = new_percentage

    def update_priority(self, new_priority):
        self.priority = new_priority

def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split('\t')
                projects.append(Project(*data))
    except FileNotFoundError:
        print(f"File '{file_name}' not found. No projects loaded.")
    return projects

def save_projects(file_name, projects):
    with open(file_name, 'w', newline='') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion %\tCompleted\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"${project.estimate:,.2f}\t{project.completion_percentage}\t{project.completed}\n")

def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("\nIncomplete projects: ")
    display_group(incomplete_projects)

    print("Completed projects: ")
    display_group(completed_projects)

def display_group(group):
    group.sort(key=lambda x: x.priority)
    for project in group:
        print(f"  {project}")

def filter_projects_by_date(projects):
    try:
        filter_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.filter_by_date(filter_date)]
        display_group(filtered_projects)
    except ValueError:
        print("Invalid date format.")

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    completed = False  # New projects are not completed by default

    projects.append(Project(name, start_date, priority, estimate, completion_percentage, completed))
    print(f"{name} added successfully.")

def update_project(projects):
    try:
        project_index = int(input("Project choice: ")) - 1
        if 0 <= project_index < len(projects):
            project = projects[project_index]

            new_percentage = input(f"New Percentage (press Enter to keep existing value): ")
            new_priority = input(f"New Priority (press Enter to keep existing value): ")

            if new_percentage:
                project.update_completion(int(new_percentage))

            if new_priority:
                project.update_priority(int(new_priority))

            print(f"{project.name} updated successfully.")
        else:
            print("Invalid index. No project updated.")
    except ValueError:
        print("Invalid index. No project updated.")

def main():
    file_name = "projects.txt"
    all_projects = load_projects(file_name)

    while True:
        print("\nMenu:")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            all_projects = load_projects(input("Enter file name to load projects from: "))
        elif choice == 's':
            save_projects(input("Enter file name to save projects to: "), all_projects)
        elif choice == 'd':
            display_projects(all_projects)
        elif choice == 'f':
            filter_projects_by_date(all_projects)
        elif choice == 'a':
            add_new_project(all_projects)
        elif choice == 'u':
            update_project(all_projects)
        elif choice == 'q':
            save_projects(file_name, all_projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
