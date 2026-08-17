from setuptools import find_packages, setup

setup(
    name="retainiq",
    version="0.1.0",
    description="RETAINIQ - AI Customer Retention: churn + SHAP + LangGraph + RAG + FastAPI.",
    packages=find_packages(exclude=["tests", "tests.*", "notebooks"]),
    python_requires=">=3.10",
)
