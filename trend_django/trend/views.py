from datetime import date
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic import ListView


# Create your views here.
from trend.models import TodayTrend


class TodayTrendListView(ListView):
    model = TodayTrend
    paginate_by = 25


    def get_context_data(self, **kwargs):
        context = super(TodayTrendListView, self).get_context_data(**kwargs)
        start_idx = context['page_obj'].end_index()
        end_idx = start_idx + self.paginate_by
        yesterday_trend = TodayTrend.objects.all()[start_idx:end_idx]

        for object in context['object_list']:
            for yesterday in yesterday_trend:
                if object.url == yesterday.url:
                    object.diff = object.rank - yesterday.rank
                    break

        return context


class OneItemListView(ListView):
    template_name = 'trend/oneitem_list.html'
    model = TodayTrend

    def get_queryset(self):
        item = get_object_or_404(TodayTrend, pk=self.kwargs['pk'])
        today = date.today()
        return TodayTrend.objects.filter(url=item.url).order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super(OneItemListView, self).get_context_data(**kwargs)

        rank_list = []
        today_star_list = []
        star_list = []
        fork_list = []

        for object in self.object_list:
            rank_list.append(object.rank)
            today_star_list.append(object.today_star_count)
            star_list.append(object.star_count)
            fork_list.append(object.fork_count)

        context['rank_list'] = rank_list
        context['today_star_list'] = today_star_list
        context['star_list'] = star_list
        context['fork_list'] = fork_list

        date_list = []
        for object in self.object_list:
            date_list.append(str(object.created_at.month) + ' / ' + str(object.created_at.day))
        context['date_list'] = date_list

        context['rank_before'] = int(self.kwargs['pk']) - 1
        context['rank_next'] = int(self.kwargs['pk']) + 1

        return context
