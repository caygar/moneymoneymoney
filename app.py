from flask import Flask, request, render_template_string

app = Flask(__name__)

total = 0
random_number = 12345
contributors = []

@app.route('/', methods=['GET', 'POST'])
def sum_contributions():
    global total, contributors
    message = ""

    if request.method == 'POST':
        try:
            contribution = int(request.form['contribution'])
            name = request.form['name']

            if name not in contributors:
                total += contribution
                contributors.append(name)
                message = f"Contribution from {name} added successfully!"
            else:
                message = "You've already contributed!"
        except ValueError:
            message = "Please enter a valid number."

    form_html = '''
        <h2>Enter Your Contribution</h2>
        <form method="POST">
            Your Name: <input type="text" name="name" required><br>
            Your Contribution: <input type="number" name="contribution" required><br><br>
            <input type="submit" value="Submit">
        </form>
        <p>{message}</p>
        <h3>People who have contributed so far:</h3>
        <ul>
        {contributors_list}
        </ul>
    '''
    contributors_list = ''.join([f"<li>{contributor}</li>" for contributor in contributors])
    return render_template_string(form_html, message=message, contributors_list=contributors_list)


@app.route('/final_total')
def final_total():
    global total
    return f"The final total (including the random number) is {total}"


@app.route('/reveal_sum')
def reveal_sum():
    global total, random_number
    actual_sum = total - random_number
    return f"The total sum of contributions (excluding the random number) is {actual_sum}"

if __name__ == '__main__':
    app.run(debug=True)
