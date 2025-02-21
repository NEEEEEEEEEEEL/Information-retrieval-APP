from setuptools import find_packages, setup

setup(
    name='info-retrieval-app',
    version='1.0.0',
    author='Neel',
    author_email='debnilsarkar72300@gmail.com',
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "google-generativeai",
        "langchain",
        "pyPDF2",
        "faiss-cpu",
        "streamlit"
    ]
)
