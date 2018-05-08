from django.db import migrations

def seed(apps, schema_editor):
    Company = apps.get_model('seekr', 'Company')
    Job = apps.get_model('seekr', 'Job')
    TodoItem = apps.get_model('seekr', 'TodoItem')

    apple = Company(name='Apple', industry='Information Technology', address='Cupertino, CA', url='https://www.apple.com/', glassdoor_link='https://www.glassdoor.com/Overview/Working-at-Apple-EI_IE1138.11,16.htm')
    microsoft = Company(name='Microsoft', industry='Information Technology', address='Redmond, WA', url='https://www.microsoft.com/en-us/', glassdoor_link='https://www.glassdoor.com/Overview/Working-at-Microsoft-EI_IE1651.11,20.htm')
    
    apple.save()
    microsoft.save()

    todo1 = TodoItem(status=False, name='Set up app')
    todo2 = TodoItem(status=False, name='Name')
    todo3 = TodoItem(status=False, name='Test')
    todo4 = TodoItem(status=False, name='Thing')

    todo1.save()
    todo2.save()
    todo3.save()
    todo4.save()

    job1 = Job(company = apple, title='Technical Specialist', description='You help new owners get started and current ones get quick, efficient support — developing strong, positive relationships with Apple. ', requirements='Ability to assess customers\’ support needs when they arrive, then provide solutions or refer them to other team members. ', salary_range_start=36000, salary_range_end=50000, source='glassdoor', notes='yes', date_posted='2018-02-12', job_status='Applied')
    job2 = Job(company = apple, title='Solution Engineer', description='You\'re part of a team that helps customers introduce Apple technology within their businesses. ', requirements='Extensive experience in mixed-technology environments, including enterprise-level infrastructure. ', salary_range_start=121000, salary_range_end=181000, source='glassdoor', notes='mhm', date_posted='2018-02-12', job_status='First Contact')
    
    job3 = Job(company = microsoft, title='Executive Assistant to the Corporate Vice President', description='You will work with a dynamic and diverse group of people responsible for the company\’s government affairs outreach in Washington, DC. ', requirements='Solid project-management and problem-solving skills. ', salary_range_start=56000, salary_range_end=100000, source='', notes='HOT', date_posted='2018-02-12', job_status='Interview')
    job4 = Job(company = microsoft, title='Solution Sales Manager- Intelligent Cloud (SLG)', description='Senior leader within our enterprise sales organization. ', requirements='Strong experience in leadership and executing on Technology visions preferred', salary_range_start=99000, salary_range_end=180000, source='glassdoor', notes='master\'s degree preferred', date_posted='2018-02-12', job_status='Offer')
    
    job1.save()
    job2.save()
    job3.save()
    job4.save()
    
    job1.todo_list.add(todo1)
    job2.todo_list.add(todo2)
    job3.todo_list.add(todo3)
    job4.todo_list.add(todo4)
    
    job1.save()
    job2.save()
    job3.save()
    job4.save()


class Migration(migrations.Migration):

    dependencies = [
        ('seekr', '0002_auto_20180507_2116'),
    ]

    operations = [
        migrations.RunPython(seed)
    ]
