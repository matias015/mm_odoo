from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    mm_timesheet_time_ids = fields.One2many(
        'timesheet.time',
        'task_id',
        string="Registro de horas"
    )

    mm_estimated_time = fields.Float(string="Tiempo estimado (en horas)", required=False)
    mm_real_time = fields.Float(string="Tiempo consumido (en horas)", compute='_compute_real_time')

    @api.depends('mm_timesheet_time_ids', 'mm_timesheet_time_ids.time')
    def compute_real_time(self):
        for task in self:
            task._compute_real_time()
    
    def _compute_real_time(self):
        timesheets = self.mm_timesheet_time_ids
        real_time = 0
        
        for timesheet in timesheets:
            real_time += timesheet.time
        
        self.mm_real_time = real_time

    