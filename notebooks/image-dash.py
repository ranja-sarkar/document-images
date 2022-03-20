
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import glob
import os

image_directory = 'C:/Users/Ranja.Sarkar/images'
#list_of_images = [os.path.abspath(x) for x in glob.glob('*.jpg'.format(image_directory))]
os.chdir(image_directory)
list_of_images = [x for x in glob.glob('*.jpg') and glob.glob('*.png')]
static_image_route = '/static/'
#print(list_of_images)
app = dash.Dash(__name__)
app.title = 'Directory Image Files'

app.layout = html.Div([
    dcc.Dropdown( 
        id = 'image-dropdown',
        options = [{'label': i, 'value': i} for i in list_of_images],
        value = list_of_images[0]
    ),
    html.Img(id = 'image')
])

@app.callback(
    dash.dependencies.Output('image', 'src'),
    [dash.dependencies.Input('image-dropdown', 'value')])
def update_image_src(value):
    return static_image_route + value

# Add a static image route that serves images from desktop

@app.server.route('{}<image_path>.jpg'.format(static_image_route) and '{}<image_path>.png'.format(static_image_route))
def serve_image(image_path):
    image_name = '{}.jpg'.format(image_path) + '{}.png'.format(image_path)
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory, image_name)

if __name__ == '__main__':
    app.run_server(debug = True)