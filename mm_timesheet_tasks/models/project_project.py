from odoo import fields, models, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    mm_total_estimated_time = fields.Float(string="Tiempo estimado", default=0)

    def _update_project_estimated_time(self):
        tareas = self.task_ids

        cantidad_total = 0

        for tarea in tareas:
            cantidad_total += tarea.mm_estimated_time
        
        self.write({'mm_total_estimated_time':cantidad_total})


    