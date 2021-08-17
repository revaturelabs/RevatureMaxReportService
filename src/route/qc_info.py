from config.flask_config import app
from service import qc_service as service


@app.route("/qa/notes/trainee/<associate_id>", methods=["GET"])
def get_qc_notes_on_trainne(associate_id):
    # localhost:5000/qa/notes/trainee/SF-2274
    return service.get_qc_info_trainee(associate_id)
