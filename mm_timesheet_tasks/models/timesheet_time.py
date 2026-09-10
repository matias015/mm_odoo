from odoo import fields, models


class TimesheetTime(models.Model):
    _inherit = 'timesheet.time'
    
    task_id = fields.Many2one('project.task', string="Tarea")