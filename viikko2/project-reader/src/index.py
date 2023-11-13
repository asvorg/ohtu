from project_reader import ProjectReader


def main():
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy/tehtavat/main/viikko2/test-project/pyproject.toml"
    reader = ProjectReader(url)
    project = reader.get_project()

    print(f"Name: {project.name}")
    print(f"Description: {project.description}")
    print(f"License: {project.license}")
    print("Authors:")
    for author in project.authors:
        print(f"- {author}")
    
    print("Dependencies:")
    for dep in project.dependencies:
        print(f"- {dep}")

    print("Development Dependencies:")
    for dev_dep in project.dev_dependencies:
        print(f"- {dev_dep}")

if __name__ == "__main__":
    main()
