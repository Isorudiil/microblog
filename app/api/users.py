from app.api import bp

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass

@bp.route('/users', methods=['GET'])
def get_user():
    pass

@bp.route('/users/<int:id>/followers', methods=['GET'])
def get_user(id):
    pass

@bp.route('/users/<int:id>/following', methods=['GET'])
def get_user(id):
    pass

@bp.route('/users', methods=['POST'])
def get_user():
    pass

@bp.route('/users/<int:id>', methods=['PUT'])
def get_user(id):
    pass