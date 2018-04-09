import json
from flask import Flask, render_template, request
from pyMap import process_latlng

app = Flask(__name__)

DICT = {
    "高德影像": "gaode.sat",
    "天地图影像": "tianditu.sat",
    "esri影像": "esri.sat",
    "谷歌影像": "google.sat",
    "高德路网": "gaode.road",
    "高德标准": "gaode.stand",
    "谷歌标准": "google.stand"
}

@app.route('/')
def index():
    app.logger.debug("index")
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    form = request.form
    name = str(form.get('name'))
    mtype = str(form.get('type'))
    bound = str(form.get('bound'))
    zoom = int(form.get('zoom'))
    bounds = bound.split(',')
    bounds = list(map(float, bounds))
    print(DICT[mtype])
    # process_latlng(bounds[0], bounds[1], bounds[2], bounds[3], zoom, name, DICT[mtype])

    # special for download 18 level
    process_latlng(23.86323358998692, 112.7691650390625, 22.411038440074023, 114.15343165397644, 18, name, DICT[mtype])
    # def process_latlng(north, west, south, east, zoom, output='mosaic', maptype="gaode.image"):
    # top left to lnglat result: { lng: 112.7691650390625, lat: 23.86323358998692 }
    # bottom right to lnglat result: { lng: 114.15343165397644, lat: 22.411038440074023 }
    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
