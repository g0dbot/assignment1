from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from App.models import db

from App.controllers import create_admin

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

