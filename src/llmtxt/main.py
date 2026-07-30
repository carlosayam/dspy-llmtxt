import os

import click
import dspy

from llmtxt.analyzer import RepositoryAnalyzer
from llmtxt.helpers import gather_repository_info

def generate_llms_txt_for_dspy(api_base, api_key, model, folder):
    # Configure DSPy (use your preferred LM)
    lm = dspy.LM(
        api_base=api_base,
        api_key=api_key,
        model=f"openai/{model}",
    )
    dspy.configure(lm=lm)

    # Initialize our analyzer
    analyzer = RepositoryAnalyzer()

    # Gather DSPy repository information
    file_tree, readme_content, package_files = gather_repository_info(folder)

    # Generate llms.txt
    result = analyzer(
        repo_folder=folder,
        file_tree=file_tree,
        readme_content=readme_content,
        package_files=package_files
    )

    return result


@click.command()
@click.argument('folder', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.argument('api_base', envvar='API_BASE')
@click.argument('api_key', envvar='API_KEY')
@click.argument('model', envvar='API_MODEL')
def main(
    folder,
    api_base,
    api_key,
    model,
):
    result = generate_llms_txt_for_dspy(api_base, api_key, model, folder)

    # Save the generated llms.txt
    with open("llms.txt", "w") as f:
        f.write(result.llms_txt_content)

    print("Generated llms.txt file!")
    print("\nPreview:")
    print(result.llms_txt_content[:500] + "...")

# Run the generation
if __name__ == "__main__":
    main()
