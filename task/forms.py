from django import  forms

from task.models import Task

class new_task(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'


        labels={

       ' Title':'Title',
      
      'TaskDescription' : 'Task Description'
              }

        widgets={
       'Date':forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})
                }