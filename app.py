from flask import Flask, jsonify, request
from algorithms import bubble_sort, dfs

app = Flask(__name__)

@app.route('/api/sort', methods=['POST'])
def sort_algorithm():
    data = request.json
    array = data['array']
    sorted_array = bubble_sort(array)
    return jsonify({'sortedArray': sorted_array})

@app.route('/api/graph-traversal', methods=['POST'])
def graph_traversal():
    data = request.json
    graph = data['graph']
    start_node = data['startNode']
    traversal_result = dfs(graph, start_node)
    return jsonify({'result': traversal_result})

if __name__ == '__main__':
    app.run(debug=True)
