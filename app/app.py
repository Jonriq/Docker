import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, url_for

app = Flask(__name__)

# simple in-memory counter
count = 0

@app.route('/')
def hello():
    global count
    count += 1
    return render_template(
        'hello.html',
        count=count,
        name="BIPM Visitor"
    )

@app.route('/titanic')
def titanic():
    # 1) load CSV
    csv_path = os.path.join(app.root_path, 'titanic.csv')
    df = pd.read_csv(csv_path)

    # 2) prepare first 5 rows HTML
    table_html = df.head(3).to_html(classes='data', index=False)

    # 3) compute survivors by sex
    survivors = df[df['survived'] == 1]['sex'].value_counts()

    # 4) generate bar chart
    img_path = os.path.join(app.root_path, 'static', 'images', 'titanic_survival.png')
    plt.figure()
    survivors.plot(kind='bar', title='Survivors by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(img_path)
    plt.close()

    # 5) render
    return render_template(
      'titanic.html',
      tables=table_html,
      chart_url=url_for('static', filename='images/titanic_survival.png')
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
