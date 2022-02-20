from flask import jsonify
from flask.views import MethodView
from flask import request
from app import app, db
from models import Advertisements as Ads
from models import User
from validators import validate_user_post, validate_adv_post


class AdvertisementsView(MethodView):

    def get(self, ads_id=None):
        if ads_id:
            query_set = Ads.query.get(ads_id)
            return jsonify(query_set.to_dict())
        else:
            query_set = Ads.query.all()
            data = [ads.to_dict() for ads in query_set]
            return jsonify(data)

    def post(self):
        validate_adv_post(request)
        data = request.json
        ads = Ads(title=data['title'], description=data.get('description'), owner_id=data['owner_id'])
        db.session.add(ads)
        db.session.commit()

        response = {
            'title': data['title'],
            'description': data.get('description'),
            'owner_id': data['owner_id'],
            'message': 'Advertisement successfully created'
        }
        return jsonify(response)

    def delete(self, ads_id):
        query_set = Ads.query.get(ads_id)
        response = query_set.to_dict()
        response['message'] = 'Advertisement successfully deleted'
        db.session.delete(query_set)
        db.session.commit()
        return jsonify(response)


class UserView(MethodView):

    def post(self):
        validate_user_post(request)
        data = request.json
        user = User(name=data.get('name'), email=data.get('email'), password=data.get('password'))
        db.session.add(user)
        db.session.commit()

        response = {
            'name': data.get('name'),
            'email': data.get('email'),
            'message': 'User successfully created'
        }
        return jsonify(response)


ads_api = AdvertisementsView.as_view('ads_api')
app.add_url_rule('/ads/', view_func=ads_api, methods=['GET', 'POST'])
app.add_url_rule('/ads/<int:ads_id>', view_func=ads_api, methods=['GET', 'DELETE'])

app.add_url_rule('/user/', view_func=UserView.as_view('post'), methods=['POST'])
