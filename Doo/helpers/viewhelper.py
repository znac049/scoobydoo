class ViewHelper():
    menu = []

    def get_side_menu(self):
        return self.menu

    def is_ajax(self, request):
       return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' 

