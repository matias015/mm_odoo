from odoo import fields, models


class TimesheetTime(models.Model):
    _name = 'timesheet.time'
    _description = "Registro de horas"
    _order = 'date desc'

    name = fields.Char(string="Descripción")
    date = fields.Date(string="Fecha", required=True, default=fields.Date.context_today)
    time = fields.Float(string="Tiempo (horas)", required=True)
    employee_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    company_id = fields.Many2one('res.company', string="Empresa", default=lambda self: self.env.company)
