from flask import Flask, request, jsonify
from db import get_connection  # This should return a MySQL connection object

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query_mysql():
    try:
        data = request.get_json()
        sql_query = data.get("query")  # ✅ Fix is here

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)

        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]

        return jsonify({"success": True, "data": results})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
