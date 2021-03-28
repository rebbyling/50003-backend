from django.test import SimpleTestCase
from accounts.forms import AuditForm, CreateUserForm #checklistForm

""" class TestForms(SimpleTestCase):
    def test_checklist_is_valid(self):
        form = checklistForm(data = {
            'health1' : True ,
            'health2' : True ,
            'health3' : True ,
            'safety1' : True ,
            'safety2' : True
        })
        self.assertTrue(form.is_valid())
    
    def test_checklist_no_data(self):
        # the form allow empty data as each checkbox is not compulsory checked
        form = checklistForm(data = {})

        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors),0) """