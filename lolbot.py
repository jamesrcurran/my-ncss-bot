from flask import Flask, request, jsonify

# Create the web server
app = Flask(__name__)

# You can message lol_bot via <your website>/lol
@app.route('/lol', methods=['GET', 'POST'])
def lol_bot():
  # Get the value of the 'text' query parameter
  # request.values is a dictionary (cool!)
  text = request.values.get('text')

  # This bot lols at every command it gets sent!
  return jsonify({
    'response_type': 'in_channel',
    'text': f'lol {text}',
  })

# Start the web server!
if __name__ == '__main__':
  app.run()
