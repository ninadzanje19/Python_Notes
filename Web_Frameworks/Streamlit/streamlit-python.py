import streamlit as st
import streamlit.components.v1 as com

"""
To run the streamlit file run the following command
streamlit run app.py
"""
st.write("Hello World")
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.markdown("Markdown")
st.caption("Caption")

code = """
def hello(name):
    return 'Hello ' + name
"""
st.code(code, language="python")
st.divider()

with st.echo():
    print("Hello Wolrd")
    a = 3 + 5
    print(a)

form_values  = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
}

with st.form(key="user_info_form"):
    #text box
    form_values["name"] = st.text_input("Enter your name")

    #numeric text box
    form_values["height"] = st.number_input("Enter your height")

    #select box, second argument is the nlist of options
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])

    #select from calender
    form_values["dob"] = st.date_input("Enter your birthdate")

    #create a submit button
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all the data")
        else:
            st.balloons()
            for (key, value) in form_values.items():
                st.write(f"{key}         {value}")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increement Counter"):
    st.session_state.counter += 1
    st.write(f"Counter increemented to {st.session_state.counter}")

if st.button("Reset Counter"):
    st.session_state.counter = 0
    st.write(f"Counter value {st.session_state.counter}")

#Sidebar
st.sidebar.title("This is the Sidebar")
st.sidebar.write("You can palce element here")
sidebar_input = st.sidebar.text_input("Enter in the sidebar")

#Tabs
tab1, tab2 = st.tabs(["Tab1", "Tab2"])
with tab1:
    st.write("This is Tab1")
with tab2:
    st.write("This is Tab2")

#Columns
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
with col2:
    st.header("Column 2")

#Container
with st.container(border=True):
    st.write("This is inside of the container.")
    st.write("################################")
    st.write("###########Sample Text##########")

#Expander
with st.expander("Expand for more details"):
    st.write("This is additional information")
    st.write("More additional information")

#Popover
st.write("Hover over this button for tooltips")
st.button("Button with Tooltip", help="This is tooltip")

#Sidebar input handling
if sidebar_input:
    st.write(f"You entered in teh sidebar: {sidebar_input}")


#Placeholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful")
if st.button("Update Placeholder"):
    placeholder.write("This is the content of the placeholder")

st.image("IMG_1371.PNG")
st.audio("Start Living.mp3")
#st.video("")

def change():
    print(st.session_state.checker)
#value is the default value given
state = st.checkbox("Checkbox", value=False,  key="checker")

#Sclect a single option
st.selectbox("Select an option", options=("A", "B", "C"))

#Select multiple options
st.multiselect("Select multiple options", options=("A", "B", "C"))

#upload files
st.file_uploader("Upload a file", type=["png, jpg"], accept_multiple_files=True)

#create a slider
#value represents the default value when the page is loaded
st.slider("Slider", min_value=0, max_value=100, value=50)

#create a select slider
#select from a given set of values
st.select_slider("Select Slider", options=["A", "B", "C"], value="B")

#get single line text from user
st.text_input("Enter your text", max_chars=60)

#get multiple line text from user
st.text_area("Enter your text", max_chars=60)

#select date
st.date_input("Enter the date")

#get time
st.time_input("Set Timer")

#clour picker
st.color_picker("Pick a colour", value="#FF7400")

#Warning message
st.warning("This is a Warning")
#Success message
st.success("This is a Success message")


def demo_message(input):
    print(f"Hello {input}")
input = st.text_input("Enter your name")
btn = st.button("Submit")
if btn:
    st.checkbox("Want to get a hello message?", on_change=demo_message(input))
#The above on change arg is given as a function. This is given for a function to happen once some change is done in the widget
#For changes using clicks use on click = <some function>
"""We use this since when any change in the widget takes place in Streamlit app the entire webpage is reloaded again and all the values are set to default"""

"""
Widgets experience changes, These changes are stored as states in an dict called as session_state
For widgets that can have multiple values, we use non boolean value for the session_state
For widgets that can have multiple values, we use boolean value for the session_state
Based upon the value we can decide the display of other things
"""

"""
For a function whose value which is calculated and returned, the calculation takes time hence on every reload the calculation takes place and time is wasted to display the value.
To avoid this a value when first calculated is stored in the cache(cached). SO on the next reloads it is retrieved quickly.
Useful for ML models and Neural Networks.
Use the decorator above the function whose value is to be cached
@st.cache(supress_st_warning=True)"""

with open("design.css") as source:
    style = source.read()

com.html(f"""
<h1 class= heading>Hello World</h1>
<style>
{style}
</style>
<p>Inline and internal CSS can be used like any html document</p>
""")