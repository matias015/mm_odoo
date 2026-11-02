from odoo import fields, models


class TimesheetTime(models.Model):
    _inherit = 'timesheet.time'
    
    task_id = fields.Many2one('project.task', string="Tarea", ondelete='cascade')

    def create(self, values):
        
        if type(values) is dict:
            if not values.get('name', '') and values.get('task_id', False):
                task = self.env['project.task'].browse(int(values.get('task_id')))
                values['name'] = task.name
        elif type(values) is list:
            if len(values) == 1 and not values[0].get('name', '') and values[0].get('task_id', False):
                task = self.env['project.task'].browse(int(values[0].get('task_id')))
                values[0]['name'] = task.name
        
        result = super().create(values)
        
        return result