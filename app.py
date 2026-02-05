import streamlit as st

st.set_page_config(page_title="My App")

st.title("Welcome to My Website")
st.write("This webpage is made using Python")

if st.button("Click Me"):
    st.success("Hello Div!")


html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>My First Webpage</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f2f2f2;
            text-align: center;
            margin-top: 100px;
        }

        h1 {
            color: blue;
        }

        p {
            font-size: 18px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
</head>

<body>

    <h1>Welcome to My Website</h1>
    <p>This webpage is made using Python Flask</p>

    <button onclick="alert('Hello Div!')">Click Me</button>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

