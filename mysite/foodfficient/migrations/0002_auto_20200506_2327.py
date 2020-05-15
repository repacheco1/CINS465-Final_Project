# Generated by Django 3.0.6 on 2020-05-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfficient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.IntegerField(choices=[(1, 'Ainu'), (2, 'Albanian'), (3, 'Argentine'), (4, 'Andhra'), (5, 'American'), (6, 'Arab'), (7, 'Armenian'), (8, 'Assyrian'), (9, 'Awadhi'), (10, 'Azerbaijani'), (11, 'Balochi'), (12, 'Belarusian'), (13, 'Bangladeshi'), (14, 'Bengali'), (15, 'Berber'), (16, 'Brazilian'), (17, 'Buddhist'), (18, 'Bulgarian'), (19, 'Cajun'), (20, 'Cantonese'), (21, 'Caribbean'), (22, 'Chechen'), (23, 'Chinese'), (24, 'ChineseIslamic'), (25, 'Circassian'), (26, 'Crimean Tatar'), (27, 'Cypriot'), (28, 'Danish'), (29, 'English'), (30, 'Estonian'), (31, 'French'), (32, 'Filipino'), (33, 'Georgian'), (34, 'German'), (35, 'Goan'), (36, 'Goan Catholic'), (37, 'Greek'), (38, 'Gujarati'), (39, 'Hyderabad'), (40, 'Indian'), (41, 'Indian Chinese'), (42, 'Indian Singaporean'), (43, 'Indonesian'), (44, 'Inuit'), (45, 'Irish'), (46, 'Italian-American'), (47, 'Italian'), (48, 'Jamaican'), (49, 'Japanese'), (50, 'Jewish'), (51, 'Karnataka'), (52, 'Kazakh'), (53, 'Keralite'), (54, 'Korean'), (55, 'Kurdish'), (56, 'Laotian'), (57, 'Lebanese'), (58, 'Latvian'), (59, 'Lithuanian'), (60, 'Louisiana Creole'), (61, 'Maharashtrian'), (62, 'Mangalorean'), (63, 'Malay'), (64, 'Malaysian Chinese'), (65, 'Malaysian Indian'), (66, 'Mediterranean'), (67, 'Mexican'), (68, 'Mordovian'), (69, 'Mughal'), (70, 'Native American'), (71, 'Nepalese'), (72, 'New Mexican'), (73, 'Odia'), (74, 'Parsi'), (75, 'Pashtun'), (76, 'Polish'), (77, 'Pennsylvania Dutch'), (78, 'Pakistani'), (79, 'Peranakan'), (80, 'Persian'), (81, 'Peruvian'), (82, 'Portuguese'), (83, 'Punjabi'), (84, 'Rajasthani'), (85, 'Romanian'), (86, 'Russian'), (87, 'Sami'), (88, 'Serbian'), (89, 'Sindhi'), (90, 'Slovak'), (91, 'Slovenian'), (92, 'Somali'), (93, 'SouthIndian'), (94, 'Soviet'), (95, 'Spanish'), (96, 'SriLankan'), (97, 'Taiwanese'), (98, 'Tatar'), (99, 'Thai'), (100, 'Turkish'), (101, 'Tamil'), (102, 'Udupi'), (103, 'Ukrainian'), (104, 'Vietnamese'), (105, 'Yamal'), (106, 'Zambian'), (107, 'Zanzibari')]),
        ),
    ]
