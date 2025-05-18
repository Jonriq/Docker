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
    table_html = df.head(5).to_html(
        classes='data-table',
        index=False,
        border=0
    )

    # 3) compute survivors AND non-survivors by sex
    survival_counts = pd.crosstab(df['sex'], df['survived'])
    survival_counts.columns = ['Did not survive', 'Survived']

    # 4) generate grouped bar chart
    img_path = os.path.join(
        app.root_path, 'static', 'images', 'titanic_survival.png'
    )
    plt.figure(figsize=(6,4))
    ax = survival_counts.plot(
        kind='bar',
        rot=0,
        figsize=(6,4),
        edgecolor='black'
    )
    ax.set_title('Survival by Sex')
    ax.set_xlabel('Sex')
    ax.set_ylabel('Number of Passengers')
    ax.legend(title='')
    plt.tight_layout()
    plt.savefig(img_path, dpi=100)
    plt.close()

    # 5) render template, passing table_html as "tables"
    return render_template(
        'titanic.html',
        tables=table_html,
        chart_url=url_for('static', filename='images/titanic_survival.png')
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
