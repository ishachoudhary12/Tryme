import numpy as np
import pickle
import streamlit as st
import time
import pandas as pd
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import hydralit_components as hc
import sqlite3

conn = sqlite3.connect('record.db', check_same_thread=False)
cur = conn.cursor()
#from PIL import Image2
#from filekanaam import functionkanaam


def pred(data):
  loaded_model = pickle.load(open('calories_model.sav','rb'))
  p = loaded_model.predict(data)
  return p

def Home():
  menu_data = [
    {'label':"Left End"},
    {'label':"Book"},
    {'label':"Component"},
    {'label':"Dashboard"},
    {'label':"Right End"},
  ]

  menu_id = hc.nav_bar(menu_definition=menu_data)

  #st.info(f"{menu_id=}")
  st.title('This is a title')
  st.header('This is a header')
  txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
  col1, col2, col3 = st.columns(3)

  with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

  with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

  with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


  

def show_something():
  """components.html(
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link href="myst.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    <title>Diet page</title>
    </head>
    <body>
    <div class="card text-center">
      <div class="card-header">
        <strong>DIET CHART</strong>
      </div>
      <div class="card-body">
        <h5 class="card-title">HEALTH IS WEALTH</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="https://www.who.int/initiatives/behealthy/healthy-diet" class="btn btn-success">Why To stay FIT?</a>
      </div>
    </div>
      <br/>
      <br/>
    <div class="container">
        <div class="row">
            <div class="col">
        <div class="card bg-danger" style="width: 18rem;">
            <img src="https://media.istockphoto.com/photos/raw-salmon-meat-and-chicken-breasts-near-green-vegetables-isolated-on-picture-id1169647832?b=1&k=20&m=1169647832&s=170667a&w=0&h=FqAvK3sZ_x4ydhT09_xr8eJpyq-rLrrbNiQjBR8cKJU=" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Protein Rich Foods</h5>
              <p class="card-text">Protein is an important macronutrient that every cell in the body needs.</p>
              <a href="https://www.piedmont.org/living-better/why-is-protein-important-in-your-diet" class="btn btn-primary">Why Protein Rich food is important in diet?</a>
            </div>
          </div>
          </div>
          <div class="col">
          <div class="card bg-danger" style="width: 18rem;">
            <img src="https://media.istockphoto.com/photos/selection-of-healthy-food-picture-id1069330620?b=1&k=20&m=1069330620&s=170667a&w=0&h=zYS35n9bF2yAGWK24VdHgVqzxiyOigsh3BMph1OcjPM=" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Vitamin Rich Foods</h5>
              <p class="card-text">A vitamin is an organic molecule that is an essential micronutrient which an organism needs small quantity.</p>
              <a href="https://www.centrum.com/learn/why-are-vitamins-important/" class="btn btn-primary">Why Vitamin is important in diet?</a>
            </div>
          </div>
          </div>
          <div class="col">
          <div class="card bg-danger" style="width: 18rem;">
            <img src="https://media.istockphoto.com/photos/healthy-high-fibre-food-picture-id903819438?b=1&k=20&m=903819438&s=170667a&w=0&h=HmYeJfcny7uoUmj3mgkxjA4LaIvmqbmaG6TBeCyF6G4=" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Carbohydrated Food</h5>
              <p class="card-text">Carbohydrates, or carbs, are sugar molecules. Along with proteins and fats, carbohydrates are main diet source.</p>
              <a href="https://www.everydayhealth.com/weight/why-carbohydrates-are-important-for-your-diet.aspx" class="btn btn-primary">Why Carbohydrates is important in diet?</a>
            </div>
          </div>
          </div>
    </div>
    <div class="row mt-2">
        <div class="col">
            <div class="card bg-danger" style="width: 18rem;">
              <img src="https://media.istockphoto.com/photos/unhealthy-food-picture-id1157591821?b=1&k=20&m=1157591821&s=170667a&w=0&h=g5ripr3khD7-5XryBWngtfLJVnu_9QgABVAQKlDy2AY=" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Junk Food</h5>
                <p class="card-text">Junk food is food that contains little or no nutritional value, but harmful amounts of salt.</p>
                <a href="https://southgatemedical.com.au/the-bad-effects-of-eating-junk-food/" class="btn btn-primary">Why Junk Food is unhealthy for body?</a>
              </div>
            </div>
            </div>
            <div class="col">
                <div class="card bg-danger" style="width: 18rem;">
                  <img src="https://media.istockphoto.com/photos/healthy-lifestyle-african-american-curly-young-woman-drinks-with-a-picture-id1334901593?b=1&k=20&m=1334901593&s=170667a&w=0&h=GAZRac0lkIsNL68_h6uIDAIpRkFJpM4hlIfCQYqXlbc=" class="card-img-top" alt="...">
                  <div class="card-body">
                    <h5 class="card-title">Water</h5>
                    <p class="card-text">Water is the main source of energy that provide hydration to our body and save us from dehydration.</p>
                    <a href="https://www.hartmanndirect.co.uk/information-centre/why-water-is-important/" class="btn btn-primary">Why Water is so important for body?</a>
                  </div>
                </div>
                </div>
                <div class="col">
                    <div class="card bg-danger" style="width: 18rem;">
                      <img src="https://media.istockphoto.com/photos/grilled-chicken-meat-and-fresh-vegetable-salad-of-tomato-avocado-and-picture-id1295633127?b=1&k=20&m=1295633127&s=170667a&w=0&h=VDkBqjm0RShberDPMJ_L-LHX1rZ5v8yNvq0I0UxXquM=" class="card-img-top" alt="...">
                      <div class="card-body">
                        <h5 class="card-title">Low Fat Foods</h5>
                        <p class="card-text">Low fat foods are those that have 30% of their calories or less from fats.Low fat food maintain our diet.</p>
                        <a href="https://www.webmd.com/women/reducing-dietary-fat" class="btn btn-primary">Why we need low fat food in diet?</a>
                      </div>
                    </div>
                    </div>

    </div>
        <div class="row mt-3">
            <div class="col">
                <div class="card bg-danger" style="width: 18rem;">
                  <img src="https://media.istockphoto.com/photos/various-piles-of-nuts-and-seeds-picture-id179751167?b=1&k=20&m=179751167&s=170667a&w=0&h=LoXkI6Uuqqow6MwThDnLNwJ7Kem_E1nH3TprWdfs8Ko=" alt="...">
                  <div class="card-body">
                    <h5 class="card-title">Rich Mineral Foods</h5>
                    <p class="card-text">Minerals are those elements on the earth and in foods that our bodies need to develop.</p>
                    <a href="https://medlineplus.gov/minerals.html" class="btn btn-primary">Why Minerals are must in our diet?</a>
                  </div>
                </div>
                </div>
                <div class="col">
                    <div class="card bg-danger" style="width: 18rem;">
                      <img src="https://media.istockphoto.com/photos/homemade-breakfast-fried-egg-vegetable-and-jam-yogurt-picture-id1215252023?b=1&k=20&m=1215252023&s=170667a&w=0&h=96yyolSskk2YnU8QkFcwHNcGS0ie9T2wzsMJxG0UfJA=" class="card-img-top" alt="...">
                      <div class="card-body">
                        <h5 class="card-title">Low Calorie Food</h5>
                        <p class="card-text"> A low-calorie diet is a structured eating plan that restricts caloric intake,weight loss.</p>
                        <a href="https://www.livestrong.com/article/266566-the-effects-of-a-high-calorie-diet/" class="btn btn-primary">How high Calorie can affect our diet?</a>
                      </div>
                    </div>
                    </div>
                    <div class="col">
                        <div class="card bg-danger" style="width: 18rem;">
                          <img src="https://media.istockphoto.com/photos/young-woman-drinking-milk-picture-id1171812310?b=1&k=20&m=1171812310&s=170667a&w=0&h=S8T3wtNyoziLREIeUjm5R6y6eZUidaODqJA2Y7JTB3A=" class="card-img-top" alt="...">
                          <div class="card-body">
                            <h5 class="card-title">Milk</h5>
                            <p class="card-text">Milk is essentially an emulsion of fat and protein in water, along with dissolved sugar.</p>
                            <a href="https://www.idfa.org/importance-of-milk-in-diet" class="btn btn-primary">How Milk play a mojor role in diet?</a>
                          </div>
                        </div>
                        </div>
                        <br>
                        <br>
                        <div class="card">
                          <iframe src="https://www.youtube.com/embed/pWahNIMRxR0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"></iframe>
                          <div class="card-body">
                            <h5 class="card-title">YOGA</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            <a href="https://yogalifeuk.com/" class="btn btn-primary">Go somewhere</a>
                          </div>
                        </div>
        </div>
    </div>
    <!-- Footer -->
<footer class="page-footer font-small cyan darken-3">
    <!-- Copyright -->
    <div class="footer-copyright text-center py-3">© 2020 Copyright:
      <a href="/"> Health.com</a>
    </div>
    <!-- Copyright -->
  
  </footer>
  <!-- Footer -->
    
</body>
</html>,
   scrolling = True,
   width= auto ,
   height= auto,
  )"""


def cal():


  with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

  st.title('Creating My First App.')
  # st.header('This is a header')
  # st.subheader('This is a subheader')
  # st.caption('This is a string that explains something above.')
  # st.text('This is some text.')

  title = st.text_input('Enter your Name:', )
  st.write('Hello', title)

  gender = st.radio(
      "Choose your gender:",
      ('Male', 'Female'))

  if gender == 'Male':
    gender = int(0)
  else:
    gender = int(1)

  st.write(gender)

  age = st.slider('How old are you?', 0, 100, 22)
  st.write("I'm ", age, 'years old')

  col1, col2, col3 = st.columns(3)

  with col1:
    height = st.number_input('Enter your height:')

  with col2:
    Weight = st.number_input('Enter your weight:')

  with col3:
    duration = st.number_input('Enter your Duration of Excercise:')

  col11, col12 = st.columns(2)

  with col11:
    heart_rate = st.number_input('Enter your Heart Rate:')
  with col12:
    Temp = st.number_input('Enter your Body Temperature:')

  if st.button('SUBMIT'):
      st.write('Submited data')
      data = [[gender,age,height,Weight,duration,heart_rate,Temp]]
      ans = pred(data)
      st.success(f'Calorie burned: {ans[0]}')
      st.balloons()
      addData(title,age,height,Weight,heart_rate,Temp)

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings','cal','show_something', 'Magic','extra','Excercise'], 
        icons=['house', 'gear','bi-activity','bi-hourglass-split','bi-magic','bi-bar-chart','bi-stopwatch'], menu_icon="cast", default_index=2)
    selected

def addData(a,b,c,d,e,f):
  cur.execute("CREATE TABLE IF NOT EXISTS myrec(NAME TEXT(50),AGE INT,HEIGHT INT, WEIGHT INT,HEARTRATE INT, TEMP INT);")
  cur.execute("INSERT INTO myrec VALUES (?,?,?,?,?,?)",(a,b,c,d,e,f))
  conn.commit()
  conn.close()

# option = st.sidebar.selectbox(
#      'How would you like to be contacted?',
#      ('cal','show_something', 'Magic','extra'))

if selected == "cal":
  cal()

elif selected == "show_something":
  show_something()

elif selected == "Home":
  Home()

elif selected == "Magic":
  magic()

elif selected == "extra":
  extra()

elif selected == "Excercise":
  Excercise()