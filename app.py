from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from flask import Flask, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware

ROOT = Path(__file__).resolve().parent


def load_flask_app(module_name: str, app_dir: Path, file_path: Path):
    """Load a standalone Flask app module from a child folder without changing its internals."""
    if str(app_dir) not in sys.path:
        sys.path.insert(0, str(app_dir))

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load Flask app from {file_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    flask_app = getattr(module, "app", None)
    if flask_app is None:
        raise RuntimeError(f"Expected a Flask app instance in {file_path}")

    return flask_app


engagement_app = load_flask_app(
    "hisabdo_engagement_app",
    ROOT / "AI User Engagement Features",
    ROOT / "AI User Engagement Features" / "app.py",
)
help_app = load_flask_app(
    "hisabdo_help_app",
    ROOT / "AI-Powered Help",
    ROOT / "AI-Powered Help" / "app.py",
)
support_app = load_flask_app(
    "hisabdo_support_app",
    ROOT / "Improve AI POC",
    ROOT / "Improve AI POC" / "app.py",
)

# Keep the support app's template resolution working when the app is mounted from the repo root.
support_app.template_folder = str(ROOT / "Improve AI POC" / "templates")
support_app.static_folder = str(ROOT / "Improve AI POC")

app = Flask(__name__)


@app.route("/")
def root_index():
    return jsonify(
        {
            "status": "success",
            "message": "HisabDo AI services are running via the root deployment entry point.",
            "services": {
                "engagement": "/engagement/",
                "help": "/help/",
                "support": "/support/",
            },
        }
    )


@app.route("/health")
def root_health():
    return jsonify({
        "status": "ok",
        "app": "root-entry-point",
        "services": ["engagement", "help", "support"],
    })


app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {
        "/engagement": engagement_app.wsgi_app,
        "/help": help_app.wsgi_app,
        "/support": support_app.wsgi_app,
    },
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
