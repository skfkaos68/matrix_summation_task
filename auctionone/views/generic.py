from django.views.generic import TemplateView, ListView
from django.urls import reverse


# Welcoming page
class HomeView(TemplateView):
    template_name = 'auctionone/admin/Home.html'
    url_name = 'geg_home'
    url_pattern = r'^export/gift_exchange$'
    display_name = 'Gift Exchange game - export data'
    navbar_active_tag = 'home'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['nbar'] = self.navbar_active_tag
        return c


class PaginatedListView(ListView):
    navbar_active_tag = None
    export_link_name = None
    export_activated = None
    title = ''
    paginate_by = 50

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['title'] = self.title
        c['nbar'] = self.navbar_active_tag
        curpage_num = c['page_obj'].number
        paginator = c['paginator']
        epsilon = 3
        c['allowed_range'] = range(max(1, curpage_num - epsilon), min(curpage_num + epsilon, paginator.num_pages) + 1)
        if self.export_link_name:
            c['export_link'] = self.export_link_name
        c['export_activated'] = self.export_activated or False
        return c
