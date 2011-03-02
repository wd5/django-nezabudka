# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group
from piston.handler import AnonymousBaseHandler
import models
import re

class TicketResource(AnonymousBaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        project = 1
        tickets = models.Ticket.objects.filter(project=project)
        out = [{'id': o.id, 'title': o.title} for o in tickets]
        return out

class CommentResource(AnonymousBaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, ticket_id):
        out = {}
        ticket = models.Ticket.objects.get(id=int(ticket_id))
        out['ticket'] = {'id': ticket.id,
                         'title': ticket.title,
                         'assigned_to_id': ticket.assigned_to.id,
                         'assigned_to_username': ticket.assigned_to.username,
                         'status_id': ticket.status.id,
                         'status_title': ticket.status.title,
                         'component_id': ticket.component.id,
                         'component_title': ticket.component.title,
                         'priority_id': ticket.priority.id,
                         'priority_title': ticket.priority.title,
                         'severity_id': ticket.severity.id,
                         'severity_title': ticket.severity.title,
                         }
        comments = models.Comment.objects.filter(ticket=ticket)
        out['comments'] = [{'id': o.id, 'text': o.text, 'user': o.user.username,
                            'date': o.reg_datetime} for o in comments]
        return out

class MediaResource(AnonymousBaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, ticket_id):
        pass

class StatusResource(AnonymousBaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        statuses = models.Status.objects.all()
        out = [{'id': o.id, 'title': o.title} for o in statuses]
        return out

