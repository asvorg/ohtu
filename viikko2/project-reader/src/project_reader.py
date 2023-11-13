from urllib import request
from project import Project
import tomlkit

class ProjectReader:
    def __init__(self, url):
        self._url = url


    def get_project(self):
        # Tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("File Content:")
        #print(content)

        # Deserialisoi TOML-formaatissa oleva merkkijono
        toml_data = tomlkit.loads(content)
        #print("Deserialized Data:")
        #print(toml_data)

        # Extract information from the deserialized data
        poetry_data = toml_data.get("tool", {}).get("poetry", {})
        dependencies = poetry_data.get("dependencies", {})
        dev_dependencies = poetry_data.get("group", {}).get("dev", {}).get("dependencies", {})

        # Muodosta Project-olio sen tietojen perusteella
        project = Project(
            name=poetry_data.get("name", "Default Name"),
            description=poetry_data.get("description", "Default Description"),
            license=poetry_data.get("license", "Default License"),
            authors=poetry_data.get("authors", []),
            dependencies=list(dependencies.keys()),
            development_dependencies=list(dev_dependencies.keys())
        )



        return project
