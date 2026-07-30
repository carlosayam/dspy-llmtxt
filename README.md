## A simple DSPy processing

This was modified from the original DSPy [tutorial](https://dspy.ai/tutorials/llms_txt_generation/)
to handle folders and oriented towards using local models (e.g. ollama, unsloth, etc).

### Installation

It assumes you have `uv` to manage Python projects

- clone the repo
- run `uv sync` to install dependencies


### Usage

To run, define environment variables

```bash
export API_MODEL=<model-id to use>
export API_BASE=<url>
export API_KEY=<api-key>
```

and execute to scan a folder in your machine like

```bash
uv run python src/llmtxt/main.py <folder>
```

it generates a `llms.txt` file in your current folder.
