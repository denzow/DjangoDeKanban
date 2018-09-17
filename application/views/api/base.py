from django.views.generic import View


class BaseApiView(View):
    """
    API系Viewの基底クラス
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login_member = None

    def dispatch(self, request, *args, **kwargs):
        self.login_member = request.user
        return super().dispatch(request, *args, **kwargs)
