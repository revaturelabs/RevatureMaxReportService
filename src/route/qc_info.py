from src.config.flask_config import app
from src.service import qa_service as service


@app.route("/qa/notes/trainee/<associate_id>", methods=["GET"])
def get_qc_notes_on_trainne(associate_id):
    # localhost:5000/qa/notes/trainee/SF-2274
    return service.get_qc_info_trainee(associate_id)

@app.route("/qa/notes/batch/<batch_id>", methods=["GET"])
def get_qc_notes_on_batch(batch_id):
    # localhost:5000/qa/notes/batch/TR-1145
    return service.get_qc_info_batch(batch_id)
