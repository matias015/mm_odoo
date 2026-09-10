from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    mm_timesheet_time_ids = fields.One2many(
        'timesheet.time',
        'task_id',
        string="Registro de horas"
    )
