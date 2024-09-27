import os
import sys
import ast
import graphviz


class ClassAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.classes = {}

    def visit_ClassDef(self, node):
        self.classes[node.name] = {
            "bases": [base.id for base in node.bases],
            "methods": [n.name for n in node.body if isinstance(n, ast.FunctionDef)],
            "calls": self.analyze_function_calls(node),
        }

    def analyze_function_calls(self, node):
        calls = []
        for n in ast.walk(node):
            if isinstance(n, ast.Call):
                try:
                    func = next(
                        a.id for a in ast.walk(n.func) if isinstance(a, ast.Name)
                    )
                    calls.append(func)
                except StopIteration:
                    pass
        return calls


def generate_class_graph(directory):
    analyzer = ClassAnalyzer()
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            with open(os.path.join(directory, filename), "r") as f:
                try:
                    tree = ast.parse(f.read())
                    analyzer.visit(tree)
                except SyntaxError:
                    print(f"Skipping {filename} due to syntax error.")

    graph = graphviz.Digraph(comment="Class Relationships")

    for cls, data in analyzer.classes.items():
        graph.node(cls)
        for base in data["bases"]:
            if base in analyzer.classes:
                graph.edge(cls, base, label="inherits")
        for call in data["calls"]:
            if call in analyzer.classes and call != cls:
                graph.edge(cls, call, label="calls")

    graph.render("class_relationship_graph", view=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python class_graph.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    generate_class_graph(directory)
