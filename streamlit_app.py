import streamlit as st
from google.cloud import vision
from google.cloud.vision_v1 import types
from groq import Groq

client = vision.ImageAnnotatorClient.from_service_account_json(r'C:\Users\Lenovo\app-starter-kit\myenv\poised-tenure-428115-s9-2948be56ea26.json')

# Function to extract text from an image using Google Vision API
def extract_text_from_image(image_bytes):
    image = types.Image(content=image_bytes)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if texts:
        return texts[0].description
    return None

# Function to get the response back from GroqCloud
def getLLMResponse(form_input, email_sender, email_recipient, email_style, language, groq_api, model_id, temperature, top_p, max_length):
    # Template for building the PROMPT
    template = """
    Write an email in {language} with {style} style includes topic: {email_topic}.\n\nSender: {sender}\nRecipient: {recipient}\n\nEmail Text:
    """

    # Creating the final PROMPT
    prompt = template.format(email_topic=form_input, sender=email_sender, recipient=email_recipient, style=email_style, language=language)

    client = Groq(
        api_key=groq_api,
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=model_id,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_length
        )

        if chat_completion:
            generated_response = chat_completion.choices[0].message.content
            return generated_response
        else:
            return 'Error in API response!'
    except Exception as e:
        return f'Exception occurred: {str(e)}'

# Email generator function
def email_generator():
    # Streamlit app configuration
   # st.set_page_config(page_title="Generate Emails",
    #                   page_icon='📧',
      #                 layout='centered',
      #                 initial_sidebar_state='collapsed')

    st.image('C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg', width=100)
    st.markdown("<h2 style='text-align: center; color: #FFA500;'>Email Generator 📧</h2>", unsafe_allow_html=True)

    # Add a horizontal line separator
    st.markdown("<hr style='border:2px solid #FFA500'>", unsafe_allow_html=True)

    # Add a description
    st.markdown("""
        <p style='text-align: center;'>
        Welcome to the Forge de Bazas Email Generator. This tool helps you create professional emails effortlessly. 
        Fill in the details below and click "Generate" to get started.
        </p>
        """, unsafe_allow_html=True)

    # Sidebar for user input
    with st.sidebar:
        st.title('💬 Email Generator')
        
        if 'GROQ_CLOUD_API_TOKEN' in st.secrets:
            st.success('API key already provided!', icon='✅')
            groq_api = st.secrets['GROQ_CLOUD_API_TOKEN']
        else:
            groq_api = st.text_input('Enter Groq Cloud API token:', type='password')
            if not groq_api:
                st.warning('Please enter your credentials!', icon='⚠️')
            else:
                st.success('Proceed to entering your prompt message!', icon='👉')
        
        st.subheader('Models and parameters')
        selected_model = st.selectbox(
            'Choose a model',
            [ 
                'Llama3-8B', 
                'Llama3-70B', 
                'Mixtral-8x7B', 
                'Gemma-7B', 
                'Gemma2-9B',
            ],
            key='selected_model'
        )
        model_id = {
            'Llama3-8B': 'llama3-8b-8192',
            'Llama3-70B': 'llama3-70b-8192',
            'Mixtral-8x7B': 'mixtral-8x7b-32768',
            'Gemma-7B': 'gemma-7b-it',
            'Gemma2-9B': 'gemma2-9b-it',
        }[selected_model]
        max_tokens_dict = {
            'Llama3-8B': 8192,
            'Llama3-70B': 8192,
            'Mixtral-8x7B': 32768,
            'Gemma-7B': 2048,
            'Gemma2-9B': 4096,
        }

        max_tokens = max_tokens_dict[selected_model]
        
        temperature = st.slider('Temperature', min_value=0.01, max_value=2.0, value=0.1, step=0.01)
        top_p = st.slider('Top P', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
        max_length = st.slider('Max Length', min_value=32, max_value=max_tokens, value=min(30, max_tokens), step=8)

    # Use session state to keep track of form input
    if 'form_input' not in st.session_state:
        st.session_state.form_input = ''

    # Text area for entering email topic
    st.session_state.form_input = st.text_area('Enter the email topic', value=st.session_state.form_input, height=50)

    # Columns for sender, recipient, email style, and language
    col1, col2, col3, col4 = st.columns([8, 8, 5, 5])
    with col1:
        email_sender = st.text_input('Sender Name')
    with col2:
        email_recipient = st.text_input('Recipient Name')
    with col3:
        email_style = st.selectbox('Writing Style',
                                   ('Formal', 'Appreciating', 'Not Satisfied', 'Neutral'),
                                   index=0)
    with col4:
        language = st.selectbox('Choose the language', ('English', 'French', 'Arabic'))

    # File uploader for images
    uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Process the uploaded image to extract text
        if st.button('Extract Text'):
            # Read image bytes
            image_bytes = uploaded_file.read()

            # Extract text from image using Google Vision API
            extracted_text = extract_text_from_image(image_bytes)

            # Display extracted text
            if extracted_text:
                st.write("Extracted Text:")
                st.write(extracted_text)
                # Set extracted text as email topic
                st.session_state.form_input = extracted_text
                st.experimental_rerun()
            else:
                st.write("No text found in the uploaded image.")

    # Generate button to execute email generation
    submit = st.button("Generate")

    if submit:
        if groq_api:
            st.write(getLLMResponse(st.session_state.form_input, email_sender, email_recipient, email_style, language, groq_api, model_id, temperature, top_p, max_length))
        else:
            st.warning('API key is missing! Please provide your Groq Cloud API token.')

    # Footer
    st.markdown("<hr style='border:2px solid #FFA500'>", unsafe_allow_html=True)
    st.markdown("""
        <footer style='text-align: center;'>
            <p>&copy; 2024 FORGES DE BAZAS. All rights reserved.</p>
        </footer>
        """, unsafe_allow_html=True)
