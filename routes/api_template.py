from flask import jsonify, request, abort
from flask.views import MethodView
import jwt
from flask import current_app as app
import datetime
from helpers.validations import token_required, validate_json
from models import ma
from models.Login import LoginSchema


class MethodsApi(MethodView):
    def __init__(self, table, table_schema, customize_login: dict = None):
        if customize_login is None:
            customize_login = {}
        self.customize_login = customize_login
        self.Table = table
        self.Result: ma.Schema = table_schema()
        self.Results: ma.Schema = table_schema(many=True)
        self.login = validate_json(customize_login.get("schema", LoginSchema)())(self.login)
        self.put = validate_json(self.Result)(self.put)
        self.add = validate_json(self.Result)(self.add)

    @token_required()
    def get(self, current_user, id=None):
        print(current_user)
        if id:
            one_registry = self.Table.query.get_or_404(id)
            return self.Result.jsonify(one_registry)

        if 'page' in request.args.keys():
            page = int(request.args.get('page'))
            per_page = int(request.args.get('size', 10))
            paginar = self.Table.query.paginate(page, per_page, False)
            if not paginar.items:
                abort(404)
            return jsonify(
                {"Result": self.Results.dump(paginar.items),
                 "total-pages": paginar.pages})

        all_registrys = self.Table.query.all()
        if not all_registrys:
            abort(404)
        return self.Results.jsonify(all_registrys)

    def post(self):
        rute = str(request.url_rule)
        if rute.find('login') != -1:
            return self.login()
        return self.add()

    def login(self):
        auth = request.json
        search = {
            self.customize_login.get('field_search', "email"): auth[
                self.customize_login.get('field_search', "email")
            ]}

        user = self.Table.query.filter_by(**search).first()

        if not user:
            abort(401)

        if user.compare_passwords(auth[self.customize_login.get('password_field_name', "password")]):
            token = jwt.encode({
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            }, self.customize_login.get('key_encrypt', app.config['SECRET_KEY']))
            action = self.customize_login.get('post_action', False)
            if action:
                exec(f'action[0]({action[1]})')
            return jsonify({'token': token.decode('UTF-8')})
        abort(401)

    @token_required()
    def add(self, current_user):
        new_registry = self.Table(request.json, current_user)
        insert_correct_data = new_registry.save()
        if not insert_correct_data:
            return self.databse_err()
        return self.Result.jsonify(new_registry), 201

    @token_required()
    def put(self, current_user, id):
        registry_update = self.Table.query.get_or_404(id)
        registry_update.changes(request.json, current_user)
        update_correct_data = registry_update.save()
        if not update_correct_data:
            return self.databse_err("update")
        return self.Result.jsonify(registry_update)

    @token_required()
    def delete(self, current_user, id):
        registry_delete = self.Table.query.get_or_404(id)
        deleted_data = registry_delete.delete(current_user)
        if not deleted_data:
            return self.databse_err("delete")
        return self.Result.jsonify(registry_delete)

    @staticmethod
    def databse_err(action: str = "insert") -> jsonify:
        return jsonify(
            {"Err": f"Error trying to {action} data"}), 409
